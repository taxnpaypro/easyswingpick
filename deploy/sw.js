/* EasySwingPick service worker: calculators and the app work offline.
   Pages: network first (always fresh when online), cached copy when offline.
   Files (scripts, images, icons): cached copy first, refreshed in the background. */
var VER = "ff6a15cb60";
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
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
      return res;
    }).catch(function () {
      return caches.match(req, { ignoreSearch: true }).then(function (r) { return r || caches.match("/app/"); });
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
