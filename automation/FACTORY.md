# SHRYDER Digital Real Estate Factory

## Standing authorization
On 1 October 2026 Shaddow authorized setup and immediate operation of the previously proposed autonomous daily factory. Routine research, drafting, QA, commits to main and publishing pages within the existing city/lifestyle strategy are authorized without a separate per-page approval. This supersedes the earlier per-page approval requirement for this scope only.

Repository: shaddowmusic/shryder-search-empire
Public base: https://shaddowmusic.github.io/shryder-search-empire/
Scheduler: one enabled Work automation, SHRYDER Digital Real Estate Factory.
Deployment: existing GitHub Pages from main branch root.
No additional paid subscriptions, API keys, model spending or hosting services are authorized. Do not claim GitHub Actions generates researched content; the Work agent does research and editing through the connected GitHub app.

## Boundaries
Produce at most one new quality property per Asia/Bangkok calendar date. Finish qualified Pattaya properties, then Bangkok, then research aligned cities. Relevant themes: nightlife, jazz/live music, luxury travel, beaches, rooftops, night drives, car culture, digital nomad and focus-listening lifestyle. Useful visitor intent comes first; music and community follow naturally.
No mass templated city-name swaps, near-duplicates, keyword doorway pages, fabricated statistics, unverified search volumes, paid tools, unrelated expansion, sponsorship claims, investment/return promises or business commitments.
Raise only spending, material strategic deviation, legal/financial commitments, destructive changes, lost access or consequential unresolved problems. Routine choice of layout, factual edits and in-scope publication do not need approval.

## Persistent state
Read automation/queue.json and automation/runs.json on every run and reconcile against the current repository tree and live URLs. Repository contents prevail over stale queue state.
Runs have date_bangkok, city, target_query, path, url, research_sources with checked_at and supported facts, commit_sha, status, qa and error where applicable.
States: researching -> validated -> committed -> deployed; alternatively deferred or blocked. Never mark deployed until the public URL returns the expected new content.
Record a validated pending run with the page in the same commit; update commit/deployment evidence afterward. Before creating another page, resume any committed/deployment-pending run. If a page already exists, recover its state instead of creating a second copy.
Use non-force fast-forward writes. Read current main before committing; if main changes, rebuild atop current tree and revalidate. Preserve unrelated pages, verification file, assets, paths and prior records.

## Production
1. Reconcile state; recover interrupted runs; enforce one new property per local date.
2. Choose next queued qualified property. #18 JDM requires original coverage, actual organizers and query evidence; defer it if those gates fail. When Pattaya is complete, begin a researched Bangkok hub. Extend other cities with their own justified queue.
3. Research actual search intent with current free/connected resources. Verify hotels/venues/events with official operator, tourism or organizer sources. Keep source URLs and checked dates. Search-volume figures only when returned by a reliable source. Unsupported claims must be omitted or clearly scoped.
4. Reuse existing HTML/CSS and preserve URLs. Each guide needs genuinely distinct helpful content, one H1, unique title/description, canonical/OG URL, applicable accurate JSON-LD, mobile layout, readable comparison tables where useful, city hub link and 2–3 relevant published neighbors.
5. Include relevant verified Shaddow music/video and direct Telegram CTA https://t.me/SHRYDERNetwork. Use the existing Pattaya song module for Pattaya; verify artist assets before adding other cities. Never invent a Spotify link or substitute another artist. Preserve the page's artist voice without inventing firsthand visits, interviews or photos.
6. Update hub discovery links, appropriate neighbors and sitemap only for actual pages. Lastmod and last verified dates change only after corresponding edits/verification.
7. Run python3 scripts/validate_factory.py against the current complete checkout including edits. Review candidate HTML visually in a local browser when available; otherwise inspect full HTML and responsive CSS and report that limitation. Validate factual accuracy, distinct intent, working media and sources separately; a script passing is not proof of editorial quality.
8. Commit the validated page, linking/sitemap changes and state atomically through GitHub. Check Pages workflow/deployment status and the public page for title, canonical, content marker, music and Telegram CTA. Retry transient errors once and leave deployment_pending if not yet live; next run must verify it before building again. Never claim indexing/rankings from deployment.
9. Record outcomes. Report briefly: city/property, query, live URL, verified status and any real blocker. Continue automatically next run.

## Maintenance
At each run, check relevant dated events; past events must not be labeled upcoming. Archive dated entries while preserving durable URLs. Do not add year/spelling variants as separate properties. If research cannot support a page, record why and advance to a qualified queued page within the daily cap.
Pause publication for validation failures; repair safe reversible issues in scope. Do not repeatedly notify about already logged unchanged low-impact issues.
