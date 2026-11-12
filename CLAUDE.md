# EasySwingPick (easyswingpick.com)

Golf club fitting calculators + bilingual (KO/EN) blog for Korean-American and senior golfers.
Owner writes in Korean: **always reply to the owner in Korean.**

## Layout
- `site/index.html` – homepage source. `const POSTS=[...]` is the post registry (newest first). Blog index `/blog/` and the homepage "최신 가이드" read from it.
- `site/blog-<slug>.html` – built blog posts. Every `site/blog-*.html` is published automatically at `/blog/<slug>` and added to the sitemap.
- `site/posts/build.py` – shared post template (`page()`), CSS, calculator links. `build_adjust.py`, `build_hot.py`, `build_split.py` are worked examples of a post script.
- `driver-fit/ iron-fit/ wedge-fit/ putter-fit/` – calculators. `logo/` – logo SVGs (wordmark = header, c.svg = favicon). `site/img/` – licensed photos (Pixabay, no brand logos).
- `build_deploy.py` – builds everything into `deploy/` (needs google-chrome for PNG icons/OG image). **`deploy/` is committed**; Cloudflare Workers deploys it as static assets (`wrangler.jsonc`) whenever `main` changes.

## Affiliate links
- Awin publisher ID 3153241; joined 2nd Swing Golf (awinmid 95935). `build_deploy.py` turns every calculator pick and every blog `B.picks()` card ("구매처 보기") into an Awin deep link to a 2nd Swing search for that model (rel="sponsored"). New posts get this automatically — just use `B.picks()` for product cards.
- FlexOffers application submitted 2026-11-12 (pending). Do not add other merchants' links until the owner sends them.

## Calculator quality (trust rules)
- `python3 build_deploy.py` ends by running `qa/run.py`: ~1,700 fixed scenario runs (KO+EN, `qa/scenarios/*.json`) plus 600 fresh random cases ×2 languages, ~40 consistency rules (`qa/checks.py`) and owner-facing expected answers (`qa/golden.json`). **If it prints `BUILD FAILED`, do not commit or publish** — fix the calculator (or, if the rule itself is wrong, explain why to the owner before changing it).
- Each QA run also tests 600 **fresh random scenarios** (`qa/gen.py`, new seed every run, printed in the result) so it keeps searching for new problems, not just re-testing fixed sets. If a fresh case fails, reproduce with `python3 qa/run.py --seed N`, fix it, and add it to `qa/golden.json` so it stays covered.
- Rules only catch problem types they know. On every scheduled blog run, also read ~10 random fresh results yourself (one per calculator at least) like a fitter would; if something looks wrong that no rule caught, fix it, add a rule to `qa/checks.py`, and tell the owner.
- Every calculator has a `guard()` step after scoring that removes combinations that must never be recommended (e.g. draw-biased drivers for a hook, irons more than one head class away, putters with the opposite toe hang). Keep it when editing pick logic.
- Explanation lines must only describe adjustments that actually changed the result.
- When the owner reports an odd calculator result: reproduce it, add it to `qa/golden.json` (or a scenario + rule), fix, and ask for approval. (The owner chose not to add a user feedback button, 2026-11-12.)

## Publishing rule (important)
Never push to `main` without the owner's explicit approval ("승인") in chat. Drafts go to a branch `publish/YYYY-MM-DD`.

## New blog post workflow (scheduled runs)
1. **Collect 10 hot candidates** with web search (last 2–4 weeks): new club releases, GolfWRX/MyGolfSpy/Golf Digest tests, seasonal topics (holiday deals, new season, spring fitting), rising searches. Skip anything already in `POSTS`.
2. **Score each 1–5** on: fit for Korean-American & senior golfers, affiliate potential (2nd Swing, FlexOffers merchants, later Awin: Dunlop/Honma), current interest, link to one of our calculators, no overlap with existing posts. Pick the top one.
3. **Write the post** as `site/posts/build_<slug>.py` following `build_adjust.py`/`build_hot.py` (uses `B.page(P)`):
   - Korean and English versions, each ≥2,000 characters; comparison table; who it suits; pros/cons; US prices; link to the matching calculator; sources list with links.
   - Only facts from sources you actually read; cite them. No invented test numbers.
   - Photos: only from `site/img/` or none. Never images showing brand logos or identifiable people.
   - Run it to produce `site/blog-<slug>.html`.
4. **Register it**: add an entry at the top of `POSTS` in `site/index.html` with `u:"/blog/<slug>"`, `cat` (gear/jp/senior/buy/putter/setup), `ko`, `en`, `dko`, `den`, `c` (card color).
5. **Build & check**: `python3 build_deploy.py` (must end with `QA OK`), serve `deploy/` locally, screenshot the post at 1300px and 390px with headless chrome, fix layout issues.
6. **Ask for approval**: commit to `publish/YYYY-MM-DD`, push the branch, then send the owner (in Korean): the 10 candidates with scores, why the winner was chosen, the post title/summary, and the screenshots. Include the QA line (e.g. "계산기 자동 점검 1,714건 이상 없음"). Ask "승인하시면 사이트에 올리겠습니다."
7. **On "승인"**: `git checkout main && git merge --ff-only publish/YYYY-MM-DD && git push origin main`. Cloudflare redeploys in a few minutes; then confirm https://easyswingpick.com/blog/<slug> returns the new post. On "보류"/edits: revise on the branch and ask again.
