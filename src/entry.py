import json
from urllib.parse import urlparse
from js import console, fetch, Uint8Array
from workers import WorkerEntrypoint, Response

from templates.site import TEMPLATE


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        url = urlparse(request.url)
        path = url.path.rstrip("/") or "/"

        if path == "/":
            return self._gallery()
        elif path == "/api/photos":
            return await self._api_photos()
        elif path.startswith("/media/"):
            file_id = path.split("/media/", 1)[-1]
            if not file_id:
                return Response("Missing file_id", status=400)
            return await self._media(file_id)

        return Response("Not Found", status=404)

    def _gallery(self):
        return Response(TEMPLATE, headers={"Content-Type": "text/html"})

    async def _api_photos(self):
        try:
            token = getattr(self.env, "TELEGRAM_TOKEN", None)
            if not token:
                return Response("Telegram token not configured", status=500)

            kv = getattr(self.env, "IMAGES_KV", None)

            index = {}
            if kv:
                try:
                    raw = await kv.get("index")
                    if raw:
                        index = json.loads(raw)
                except Exception:
                    index = {}

            tg_resp = await fetch(
                f"https://api.telegram.org/bot{token}/getUpdates"
            )
            data = json.loads(await tg_resp.text())

            file_ids = []
            for item in data.get("result", []):
                msg = item.get("channel_post") or item.get("message") or {}
                if "photo" in msg:
                    photos = msg["photo"]
                    file_ids.append(photos[-1]["file_id"])

            new = False
            for fid in file_ids:
                if fid not in index:
                    index[fid] = {"cached": False}
                    new = True

            if new and kv:
                await kv.put("index", json.dumps(index))

            urls = [f"/media/{fid}" for fid in file_ids]
            return Response(json.dumps({"photos": urls}), headers={"Content-Type": "application/json"})
        except Exception as e:
            console.log(f"Error in _api_photos: {e}")
            return Response(str(e), status=500)

    async def _media(self, file_id):
        try:
            token = getattr(self.env, "TELEGRAM_TOKEN", None)
            if not token:
                return Response("Telegram token not configured", status=500)

            info_resp = await fetch(
                f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}"
            )
            if info_resp.status != 200:
                return Response("Failed to get file info", status=502)

            info = json.loads(await info_resp.text())
            file_path = info.get("result", {}).get("file_path")
            if not file_path:
                return Response("File not found", status=404)

            dl_resp = await fetch(
                f"https://api.telegram.org/file/bot{token}/{file_path}"
            )
            if dl_resp.status != 200:
                return Response("Failed to download file", status=502)

            content_type = dl_resp.headers.get("content-type", "application/octet-stream")
            buffer = await dl_resp.arrayBuffer()
            body = bytes(Uint8Array.new(buffer))
            return Response(body, headers={"Content-Type": content_type})
        except Exception as e:
            console.log(f"Error in _media: {e}")
            return Response(str(e), status=500)
