# Infracore Gallery — Local dev & Cloudflare Worker

This project serves the Infracore site and a Telegram-powered gallery. It supports:

- Local dev with `uvicorn src.test:app` (filesystem cache of images)
- Local dev of the Cloudflare-compatible entry with `uvicorn src.entry:app` (proxies Telegram files)
- Prepared `wrangler.toml` for Cloudflare deployment (fill account-specific fields)

Quick start (PowerShell):

1. Create and activate virtualenv:

```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Set your Telegram bot token (local):

```powershell
$env:TELEGRAM_TOKEN = "<your_bot_token>"
```

4a. Run the filesystem-backed gallery server (caches images to `src/data/images`):

```powershell
uvicorn src.test:app --reload --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000 — the gallery page is at `/` and the "Get Latest Images" button will download images from Telegram and cache them.

4b. Run the Cloudflare-compatible app (proxies Telegram files via `/media/{file_id}`):

```powershell
uvicorn src.entry:app --reload --host 127.0.0.1 --port 8000
```

This serves the `src/templates/infracore.html` template and exposes `/api/photos` and `/media/{file_id}` which the template uses to display the Telegram feed.

Cloudflare deploy notes:

- Install Wrangler: https://developers.cloudflare.com/workers/cli-wrangler/
- Configure `wrangler.toml` with your `account_id` and KV namespace id (optional). We've added a placeholder `wrangler.toml`.
- Store your `TELEGRAM_TOKEN` as a secret:

```bash
wrangler secret put TELEGRAM_TOKEN
```

- Publish:

```bash
wrangler publish
```

If you want, I can:
- Start the local `uvicorn src.entry:app` server here and confirm the page loads.
- Add Cloudflare KV/R2-backed caching logic into the worker code.
- Help configure `wrangler.toml` with your account details.

