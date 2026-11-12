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

## Publishing rule (important)
Never push to `main` without the owner's explicit approval ("승인") in chat. Drafts go to a branch `publish/YYYY-MM-DD`.

## Pending change to ship with the next post (owner request, 2026-11-12)
Branch `pending/disclosure` shortens the blog affiliate disclosure to one line under the title (with a "자세히 보기" link) and moves the full text to the end of each post, and makes English the default language on every page (the visitor's KO/EN choice is remembered in localStorage `esp_lang`). The owner asked to ship it together with the next blog post:
- After creating `publish/YYYY-MM-DD`, run `git merge --no-edit origin/pending/disclosure` into it before building, then rebuild with `python3 build_deploy.py`.
- Mention it in the approval message ("제휴 안내 문구 변경과 영어 기본 화면도 함께 반영됩니다") and include a screenshot of the top of the new post.
- When the owner approves and main is pushed, delete this section from CLAUDE.md (commit on main) and delete the remote branch: `git push origin --delete pending/disclosure`.

## New blog post workflow (scheduled runs)
1. **Collect 10 hot candidates** with web search (last 2–4 weeks): new club releases, GolfWRX/MyGolfSpy/Golf Digest tests, seasonal topics (holiday deals, new season, spring fitting), rising searches. Skip anything already in `POSTS`.
2. **Score each 1–5** on: fit for Korean-American & senior golfers, affiliate potential (2nd Swing, FlexOffers merchants, later Awin: Dunlop/Honma), current interest, link to one of our calculators, no overlap with existing posts. Pick the top one.
3. **Write the post** as `site/posts/build_<slug>.py` following `build_adjust.py`/`build_hot.py` (uses `B.page(P)`):
   - Korean and English versions, each ≥2,000 characters; comparison table; who it suits; pros/cons; US prices; link to the matching calculator; sources list with links.
   - Only facts from sources you actually read; cite them. No invented test numbers.
   - Photos: only from `site/img/` or none. Never images showing brand logos or identifiable people.
   - Run it to produce `site/blog-<slug>.html`.
4. **Register it**: add an entry at the top of `POSTS` in `site/index.html` with `u:"/blog/<slug>"`, `cat` (gear/jp/senior/buy/putter/setup), `ko`, `en`, `dko`, `den`, `c` (card color).
5. **Build & check**: `python3 build_deploy.py`, serve `deploy/` locally, screenshot the post at 1300px and 390px with headless chrome, fix layout issues.
6. **Ask for approval**: commit to `publish/YYYY-MM-DD`, push the branch, then send the owner (in Korean): the 10 candidates with scores, why the winner was chosen, the post title/summary, and the screenshots. Ask "승인하시면 사이트에 올리겠습니다."
7. **On "승인"**: `git checkout main && git merge --ff-only publish/YYYY-MM-DD && git push origin main`. Cloudflare redeploys in a few minutes; then confirm https://easyswingpick.com/blog/<slug> returns the new post. On "보류"/edits: revise on the branch and ask again.
