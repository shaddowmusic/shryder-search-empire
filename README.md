# SHRYDER Search Empire

Static, GitHub Pages-compatible source for SHRYDER-owned search and listening assets.

## Live routes

`/bitcoin-music/bitcoin-focus-music-late-night-trading/`

`/crypto-music/crypto-trading-music/`

`/focus-music/focus-music-for-work-trading/`

## Verified live media

- YouTube: https://www.youtube.com/watch?v=xzPycg1Q6gw
- Title: `1 Hour Bitcoin Focus Music for Late Night Trading`
- Runtime: `1:03:03` (`PT1H3M3S`)
- Channel: `Shaddowmusic`
- Chapters: 17, copied from the live description on 26 September 2026

BUILD #002:

- YouTube: https://www.youtube.com/watch?v=WGp1xire3sc
- Title: `80+ Minutes of Deep Electronic Music for Crypto Traders`
- Runtime displayed by the player: `1:22:11`
- Channel: `Shaddowmusic`
- Chapters: 20, copied from the live description on 26 September 2026

BUILD #003:

- YouTube: https://www.youtube.com/watch?v=g4mXXUefOMw
- Title: `Focus Music for Work & Trading | 1 Hour of Deep Electronic Music`
- Runtime displayed by the player: `1:04:21`
- Channel: `Shaddowmusic`
- Chapters: 22, copied from the live description on 28 September 2026

## Deployment

Published from the `main` branch root at `https://shaddowmusic.github.io/shryder-search-empire/`.

The canonical URL, Open Graph URL, sitemap and robots declaration use that approved GitHub Pages origin. GitHub Pages enforces HTTPS.

## Measurement

Outbound links carry source/campaign parameters where the destination supports them. `assets/app.js` emits a `shryder_outbound_click` event and pushes it to `dataLayer`, ready for a later approved analytics provider.

## Local preview

Serve this folder with any static HTTP server. No build step or runtime dependency is required.

## Autonomous city-property production

The SHRYDER Digital Real Estate Factory is governed by [automation/FACTORY.md](automation/FACTORY.md). Its durable queue and execution log are in `automation/queue.json` and `automation/runs.json`. One Work automation performs research, validation and authorized publication through the connected GitHub app; existing GitHub Pages publishes main. No paid generation API or extra hosting is configured.

Run `python3 scripts/validate_factory.py` in a complete checkout before committing city guides. Editorial research and public deployment verification are additional required checks.
