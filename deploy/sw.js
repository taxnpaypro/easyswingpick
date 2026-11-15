/* EasySwingPick service worker: calculators and the app work offline.
   Pages: network first (always fresh when online), cached copy when offline.
   Files (scripts, images, icons): cached copy first, refreshed in the background. */
var VER = "3961352fd9";
var CACHE = "esp-" + VER;
var CORE = ["/app/", "/driver/", "/iron/", "/wedge/", "/putter/", "/assets/app.js", "/assets/logo.svg", "/assets/favicon.svg",
            "/assets/wordmark.svg", "/assets/icon-192.png", "/assets/logo-512.png", "/manifest.webmanifest"];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.filter(function (k) { return k.indexOf("esp-") === 0 && k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener("fetch", function (e) {
  var req = e.request, url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== location.origin) return;   // affiliate links, fonts, analytics: browser as usual
  /* pages and scripts: network first (always the newest version online), saved copy offline */
  if (req.mode === "navigate" || /\.js$/.test(url.pathname)) {
    e.respondWith(fetch(req).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
      return res;
    }).catch(function () {
      return caches.match(req, { ignoreSearch: true }).then(function (r) { return r || (req.mode === "navigate" ? offlinePage() : r); });
    }));
    return;
  }
  e.respondWith(caches.match(req).then(function (hit) {
    var net = fetch(req).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
      return res;
    }).catch(function () { return hit; });
    return hit || net;
  }));
});

/* a page that was never opened before can't be shown offline: say so instead of a browser error */
function offlinePage() {
  var h = '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Offline</title>' +
    '<body style="margin:0;font-family:system-ui,sans-serif;background:#f3f5f7;color:#15212b;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;padding:24px">' +
    '<div><div style="font-size:42px">⛳</div><h2 style="color:#0f2a3d">인터넷 연결이 필요합니다<br><small style="font-weight:500">You\'re offline</small></h2>' +
    '<p>이 페이지는 연결된 뒤에 열 수 있습니다. 계산기와 내 골프백은 오프라인에서도 쓸 수 있습니다.<br>Calculators and My bag still work offline.</p>' +
    '<p><a href="/app/" style="display:inline-block;background:#0f2a3d;color:#fff;padding:12px 20px;border-radius:12px;text-decoration:none;font-weight:700">앱 홈 / App home</a></p></div></body>';
  return new Response(h, { headers: { "Content-Type": "text/html; charset=utf-8" } });
}
