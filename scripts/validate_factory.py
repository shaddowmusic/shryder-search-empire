#!/usr/bin/env python3
"""Deterministic local checks; factual/editorial and live deployment QA remain required."""
import json
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://shaddowmusic.github.io/shryder-search-empire"
PREFIX = "/shryder-search-empire"
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.canonical = []
        self.descriptions = []
        self.refs = []
        self.title = ""
        self.in_title = False
        self.schema = None
        self.schemas = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1": self.h1 += 1
        if tag == "title": self.in_title = True
        if tag == "link" and a.get("rel") == "canonical": self.canonical.append(a.get("href", ""))
        if tag == "meta" and a.get("name") == "description": self.descriptions.append(a.get("content", ""))
        if tag in ("a", "link", "script", "iframe", "img"):
            ref = a.get("href") if tag in ("a", "link") else a.get("src")
            if ref: self.refs.append(ref)
        if tag == "script" and a.get("type") == "application/ld+json": self.schema = ""
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.schema is not None: self.schema += data
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag == "script" and self.schema is not None:
            self.schemas.append(self.schema)
            self.schema = None

def fail(path, message):
    errors.append(str(path) + ": " + message)

sitemap = ET.parse(ROOT / "sitemap.xml")
urls = [x.text for x in sitemap.findall(".//{*}loc")]
if len(urls) != len(set(urls)): fail("sitemap.xml", "duplicate URLs")
for url in urls:
    if not url.startswith(BASE + "/"):
        fail("sitemap.xml", "unexpected origin: " + str(url))
        continue
    rel = url[len(BASE)+1:]
    target = ROOT / rel
    if url.endswith("/"): target = target / "index.html"
    if not target.is_file(): fail("sitemap.xml", "missing page: " + url)

seen_titles = {}
seen_canonical = {}
for path in sorted(ROOT.rglob("index.html")):
    if any(p.startswith(".") for p in path.relative_to(ROOT).parts): continue
    raw = path.read_text(encoding="utf-8")
    page = Page()
    page.feed(raw)
    rel = path.relative_to(ROOT)
    expected = BASE + "/" + (str(rel.parent) + "/" if str(rel.parent) != "." else "")
    if page.h1 != 1: fail(rel, "expected one H1")
    if page.canonical != [expected]: fail(rel, "canonical must be " + expected)
    if len(page.descriptions) != 1 or not page.descriptions[0].strip(): fail(rel, "missing unique meta description")
    if not page.title.strip(): fail(rel, "missing title")
    if page.title in seen_titles: fail(rel, "duplicate title with " + seen_titles[page.title])
    seen_titles[page.title] = str(rel)
    if expected in seen_canonical: fail(rel, "duplicate canonical")
    seen_canonical[expected] = str(rel)
    if expected not in urls: fail(rel, "missing from sitemap")
    for schema in page.schemas:
        try: json.loads(schema)
        except ValueError as exc: fail(rel, "invalid JSON-LD: " + str(exc))
    if str(rel).startswith("cities/"):
        if "https://t.me/SHRYDERNetwork" not in page.refs: fail(rel, "missing direct Telegram CTA")
        if not any("youtube" in r and "/embed/" in r for r in page.refs): fail(rel, "missing music embed")
        if not page.schemas: fail(rel, "missing JSON-LD")
    for ref in page.refs:
        u = urlsplit(ref)
        if u.scheme and not (u.scheme in ("http", "https") and u.netloc == "shaddowmusic.github.io"): continue
        if u.netloc and u.netloc != "shaddowmusic.github.io": continue
        p = unquote(u.path)
        if not p: continue
        if p.startswith("/"):
            if not (p == PREFIX or p.startswith(PREFIX + "/")): continue
            target = ROOT / p[len(PREFIX):].lstrip("/")
        else: target = path.parent / p
        target = target.resolve()
        if not target.is_relative_to(ROOT): fail(rel, "link outside checkout: " + ref); continue
        if target.is_dir() or p.endswith("/"): target = target / "index.html"
        if not target.is_file(): fail(rel, "broken local reference: " + ref)

queue = json.loads((ROOT / "automation/queue.json").read_text())
runs = json.loads((ROOT / "automation/runs.json").read_text())["runs"]
paths = [p["path"] for p in queue["properties"]]
if len(paths) != len(set(paths)): fail("queue.json", "duplicate property path")
for p in queue["properties"]:
    if p["status"] in ("published", "deployed") and not (ROOT / p["path"]).is_file():
        fail("queue.json", "published file missing: " + p["path"])
daily = {}
for run in runs:
    if run.get("status") not in ("committed", "deployment_pending", "deployed"): continue
    key = run["date_bangkok"]
    daily.setdefault(key, set()).add(run["path"])
for day, values in daily.items():
    if len(values) > 1: fail("runs.json", "more than one property on " + day)
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS: HTML metadata, JSON-LD, sitemap, local references, city media/CTA and factory state.")
