from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
import httpx
import os


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def gallery(request: Request, env=None):
    # Serve the site template so local uvicorn shows the full site with gallery.
    tpl_path = Path(__file__).parent / "templates" / "infracore.html"
    if tpl_path.exists():
        return HTMLResponse(tpl_path.read_text(encoding="utf-8"))

    # fallback
    html_content = """
    <html>
        <head><meta charset="utf-8"><title>Infracore</title></head>
        <body>
            <h1>Infracore — Worker</h1>
            <p>Template not found.</p>
        </body>
    </html>
    """
    return HTMLResponse(html_content)


@app.get("/api/photos")
async def api_photos(request: Request, env=None):
    # token from env (Cloudflare) or OS env for local dev
    token = None
    if env:
        token = getattr(env, "TELEGRAM_TOKEN", None)
    if not token:
        token = os.environ.get("TELEGRAM_TOKEN") or os.environ.get("TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="Telegram token not configured")

    # Try to read a KV index if available (binding name: IMAGES_KV)
    index = {}
    try:
        kv = getattr(env, "IMAGES_KV", None) if env else None
        if kv:
            raw = await kv.get("index")
            if raw:
                import json
                index = json.loads(raw)
    except Exception:
        index = {}

    async with httpx.AsyncClient() as client:
        tg_res = await client.get(f"https://api.telegram.org/bot{token}/getUpdates")
        data = tg_res.json()
        file_ids = []
        for item in data.get("result", []):
            msg = item.get("channel_post") or item.get("message") or {}
            if "photo" in msg:
                file_ids.append(msg["photo"][-1]["file_id"])

        # Update index in KV with any new file_ids (store minimal metadata)
        new = False
        for fid in file_ids:
            if fid not in index:
                index[fid] = {"cached": False}
                new = True

        if new and kv:
            import json
            await kv.put("index", json.dumps(index))

    # Return URLs that the client can fetch (worker will proxy via /media/{file_id})
    urls = [f"/media/{fid}" for fid in file_ids]
    return JSONResponse({"photos": urls})


@app.get('/media/{file_id}')
async def media(file_id: str, request: Request, env=None):
    token = None
    if env:
        token = getattr(env, "TELEGRAM_TOKEN", None)
    if not token:
        token = os.environ.get("TELEGRAM_TOKEN") or os.environ.get("TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="Telegram token not configured")

    async with httpx.AsyncClient() as client:
        info_res = await client.get(f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}")
        if info_res.status_code != 200:
            raise HTTPException(status_code=502, detail="Failed to get file info")
        info = info_res.json()
        file_path = info.get("result", {}).get("file_path")
        if not file_path:
            raise HTTPException(status_code=404, detail="File not found")

        download_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        resp = await client.get(download_url)
        if resp.status_code != 200:
            raise HTTPException(status_code=502, detail="Failed to download file")

        content_type = resp.headers.get("Content-Type", "application/octet-stream")
        return StreamingResponse(iter([resp.content]), media_type=content_type)

from workers import WorkerEntrypoint
class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(app, request, self.env)