import TEMPLATE from './templates_infracore_html.js';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Serve the HTML template at /
    if (path === "/") {
      // Try to fetch the bundled template; if that fails, fall back to the embedded TEMPLATE.
      try {
        const tplUrl = new URL('./templates/infracore.html', import.meta.url);
        const resp = await fetch(tplUrl);
        if (resp.ok) {
          const tpl = await resp.text();
          return new Response(tpl, { headers: { 'Content-Type': 'text/html; charset=utf-8' } });
        }
      } catch (e) {
        // ignore and use fallback
      }
      // fallback to embedded template
      return new Response(TEMPLATE, { headers: { 'Content-Type': 'text/html; charset=utf-8' } });
    }

    // API: list photos
    if (path === '/api/photos') {
      const token = env.TELEGRAM_TOKEN;
      if (!token) return new Response(JSON.stringify({ error: 'TELEGRAM_TOKEN not configured' }), { status: 500, headers: { 'Content-Type': 'application/json' } });
      const tg = await fetch(`https://api.telegram.org/bot${token}/getUpdates`);
      if (!tg.ok) return new Response('Failed to fetch updates', { status: 502 });
      const data = await tg.json();
      const file_ids = [];
      for (const item of data.result || []) {
        const msg = item.channel_post || item.message || {};
        if (msg.photo) file_ids.push(msg.photo[msg.photo.length - 1].file_id);
      }
      const urls = file_ids.map(fid => `/media/${fid}`);
      return new Response(JSON.stringify({ photos: urls }), { headers: { 'Content-Type': 'application/json' } });
    }

    // Proxy a Telegram file at /media/{file_id}
    if (path.startsWith('/media/')) {
      const token = env.TELEGRAM_TOKEN;
      if (!token) return new Response('TELEGRAM_TOKEN not configured', { status: 500 });
      const parts = path.split('/');
      const file_id = parts.slice(2).join('/');
      if (!file_id) return new Response('Missing file id', { status: 400 });

      // 1) getFile
      const info = await fetch(`https://api.telegram.org/bot${token}/getFile?file_id=${encodeURIComponent(file_id)}`);
      if (!info.ok) return new Response('Failed to get file info', { status: 502 });
      const infoJson = await info.json();
      const file_path = infoJson.result && infoJson.result.file_path;
      if (!file_path) return new Response('File path not found', { status: 404 });

      // 2) download file
      const downloadUrl = `https://api.telegram.org/file/bot${token}/${file_path}`;
      const fileRes = await fetch(downloadUrl);
      if (!fileRes.ok) return new Response('Failed to download file', { status: 502 });

      // stream response with content-type
      const headers = {};
      const ct = fileRes.headers.get('content-type');
      if (ct) headers['Content-Type'] = ct;
      return new Response(fileRes.body, { headers });
    }

    return new Response('Not found', { status: 404 });
  }
}
