# EasySwingPick

Source for https://easyswingpick.com — golf club fitting calculators and a bilingual (KO/EN) blog.

- Build: `python3 build_deploy.py` → writes `deploy/`
- Deploy: Cloudflare Workers Builds runs `npx wrangler deploy` on every push to `main` (static assets from `deploy/`).
- New posts are drafted on `publish/YYYY-MM-DD` branches and merged to `main` only after the owner approves. See `CLAUDE.md`.
