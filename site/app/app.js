/* EasySwingPick app layer (web app / PWA). Loaded on every page by build_deploy.py.
   - registers the service worker (offline use, install to home screen)
   - on calculators: "save to my bag", "share result card", related guide link, full-set flow (driver → iron → wedge → putter)
   - remembers age / height / handicap so the next calculator is pre-filled
   Everything is stored only on the visitor's device (localStorage). Nothing here changes calculator results. */
(function () {
  "use strict";
  var LS = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  var SS = {
    get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) {} }
  };
  function L() {
    try { if (typeof lang !== "undefined" && (lang === "ko" || lang === "en")) return lang; } catch (e) {}
    try { return localStorage.getItem("esp_lang") || "en"; } catch (e) { return "en"; }
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* ---------- service worker (live site only, or when testing with ?sw=1) ---------- */
  var host = location.hostname;
  var swOK = /(^|\.)easyswingpick\.com$/.test(host) || /[?&]sw=1/.test(location.search);
  if ("serviceWorker" in navigator && swOK) {
    window.addEventListener("load", function () { navigator.serviceWorker.register("/sw.js").catch(function () {}); });
  }
  /* install prompt (Android/Chrome): kept so the app page can offer an "Install" button */
  window.addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); window.__espInstall = e; document.dispatchEvent(new Event("esp-install-ready")); });

  /* ---------- large text (setting on the app page) ---------- */
  if (LS.get("esp_big", false)) document.documentElement.classList.add("esp-big");
  var st = document.createElement("style");
  st.textContent =
    "html.esp-big body{zoom:1.12}" +
    ".esp-bar{max-width:760px;margin:16px auto 0;padding:0 16px}" +
    ".esp-bar .in{background:#fff;border:1px solid #e3e8ec;border-radius:16px;padding:16px;box-shadow:0 1px 2px rgba(15,42,61,.06),0 6px 20px rgba(15,42,61,.06)}" +
    ".esp-bar h3{margin:0 0 4px;font-size:1.05rem;color:#0f2a3d}.esp-bar p{margin:0 0 12px;color:#64727d;font-size:.9rem}" +
    ".esp-row{display:flex;gap:8px;flex-wrap:wrap}" +
    ".esp-b{flex:1 1 150px;min-height:48px;border-radius:12px;border:1.5px solid #0f2a3d;background:#fff;color:#0f2a3d;font:600 .95rem Inter,'Noto Sans KR',system-ui,sans-serif;cursor:pointer;padding:10px 12px;text-align:center;text-decoration:none;display:flex;align-items:center;justify-content:center;gap:6px}" +
    ".esp-b.pri{background:#0f2a3d;color:#fff}.esp-b.ok{background:#e6f4ee;border-color:#178a5b;color:#178a5b}" +
    ".esp-guide{display:block;margin-top:12px;font-size:.92rem;color:#173b55;font-weight:600}" +
    ".esp-set{margin:14px 0 4px}" +
    ".esp-set .in{background:rgba(255,255,255,.12);color:#fff;border-radius:14px;padding:12px 14px;display:flex;align-items:center;gap:12px;font-size:.92rem}" +
    ".esp-set .dots{display:flex;gap:5px;margin-left:auto}.esp-set .dots i{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.3)}.esp-set .dots i.on{background:#c89b3c}" +
    ".esp-set a{color:#c89b3c;font-weight:600;text-decoration:none}" +
    ".esp-toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:#15212b;color:#fff;padding:10px 16px;border-radius:999px;font:500 .9rem Inter,'Noto Sans KR',sans-serif;z-index:99;opacity:0;transition:opacity .2s}.esp-toast.on{opacity:1}";
  document.head.appendChild(st);

  var CALCS = ["driver", "iron", "wedge", "putter"];
  var T = {
    ko: {
      club: { driver: "드라이버", iron: "아이언", wedge: "웨지", putter: "퍼터" },
      barT: "이 결과로 무엇을 할까요?", barS: "저장한 결과는 이 휴대폰(브라우저)에만 보관됩니다.",
      save: "내 골프백에 저장", saved: "골프백에 저장됨 ✓", share: "결과 카드 공유", bag: "내 골프백 보기",
      guide: { driver: "관련 가이드: 2026 인기 드라이버 비교 →", iron: "관련 가이드: 2026 인기 아이언 비교 →", wedge: "관련 가이드: 2026 인기 웨지 비교 →", putter: "관련 가이드: 2026 인기 퍼터 비교 →" },
      setT: function (i) { return "전체 세트 추천 " + (i + 1) + "/4 · "; }, setQuit: "그만하기",
      next: function (c) { return "저장하고 다음: " + c + " →"; }, finish: "저장하고 내 골프백 보기 →",
      toastSaved: "내 골프백에 저장했습니다", cardT: "나의 골프백", cardS: "무료 클럽 피팅 계산기 추천 결과", cardFoot: "easyswingpick.com · 내 스윙에 맞는 골프채 찾기",
      shareText: "EasySwingPick 계산기로 받은 내 클럽 추천입니다.", dl: "이미지를 저장했습니다"
    },
    en: {
      club: { driver: "Driver", iron: "Irons", wedge: "Wedges", putter: "Putter" },
      barT: "What would you like to do with this result?", barS: "Saved results stay only on this phone (browser).",
      save: "Save to my bag", saved: "Saved to my bag ✓", share: "Share result card", bag: "View my bag",
      guide: { driver: "Related guide: 2026's hot drivers compared →", iron: "Related guide: 2026's hot irons compared →", wedge: "Related guide: 2026's hot wedges compared →", putter: "Related guide: 2026's hot putters compared →" },
      setT: function (i) { return "Full-set fitting " + (i + 1) + "/4 · "; }, setQuit: "Stop",
      next: function (c) { return "Save & next: " + c + " →"; }, finish: "Save & view my bag →",
      toastSaved: "Saved to your bag", cardT: "My Golf Bag", cardS: "Picks from free club-fitting calculators", cardFoot: "easyswingpick.com · Find clubs that fit your swing",
      shareText: "My club picks from the EasySwingPick calculators.", dl: "Image saved"
    }
  };
  var GUIDE = { driver: "/blog/hot-drivers-2026", iron: "/blog/hot-irons-2026", wedge: "/blog/hot-wedges-2026", putter: "/blog/hot-putters-2026" };

  function toast(msg) {
    var el = document.querySelector(".esp-toast");
    if (!el) { el = document.createElement("div"); el.className = "esp-toast"; document.body.appendChild(el); }
    el.textContent = msg; el.classList.add("on"); clearTimeout(el._t); el._t = setTimeout(function () { el.classList.remove("on"); }, 2200);
  }

  /* ---------- share card (canvas image) — used here and on /app/ ---------- */
  function wrapText(ctx, text, maxW) {
    var words = String(text).split(" "), lines = [], cur = "";
    words.forEach(function (w) { var t = cur ? cur + " " + w : w; if (ctx.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t; });
    if (cur) lines.push(cur); return lines;
  }
  function drawCard(items) {
    var t = T[L()], W = 1080, H = 1350, c = document.createElement("canvas"); c.width = W; c.height = H;
    var x = c.getContext("2d"), F = "Inter, 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', system-ui, sans-serif";
    x.fillStyle = "#0f2a3d"; x.fillRect(0, 0, W, H);
    x.fillStyle = "#c89b3c"; x.fillRect(80, 110, 90, 10);
    x.fillStyle = "#fff"; x.font = "700 76px " + F; x.fillText(t.cardT, 80, 220);
    x.fillStyle = "rgba(255,255,255,.65)"; x.font = "500 34px " + F; x.fillText(t.cardS, 80, 275);
    var y = 340, slot = Math.min(230, (H - 340 - 150) / Math.max(items.length, 1));
    items.forEach(function (it) {
      x.fillStyle = "rgba(255,255,255,.07)"; roundRect(x, 70, y, W - 140, slot - 24, 28); x.fill();
      x.fillStyle = "#c89b3c"; x.font = "700 30px " + F; x.fillText(t.club[it.calc].toUpperCase(), 110, y + 58);
      x.fillStyle = "#fff"; x.font = "700 50px " + F;
      var name = it.name || (it.brand + " " + it.model).trim(), ln = wrapText(x, name, W - 220);
      x.fillText(ln[0], 110, y + 122);
      x.fillStyle = "rgba(255,255,255,.72)"; x.font = "500 30px " + F;
      /* spec line: whole items only (never cut mid-item), head-type label skipped on the card */
      var parts = (it.specs || []).filter(function (s) { return s[0]; }).map(function (s) { return s[0] + " " + s[1]; }), spec = "";
      parts.forEach(function (q) { var tr = spec ? spec + "  ·  " + q : q; if (x.measureText(tr).width <= W - 220) spec = tr; });
      if (spec && slot > 200) x.fillText(spec, 110, y + 172);
      y += slot;
    });
    x.fillStyle = "rgba(255,255,255,.55)"; x.font = "500 30px " + F; x.fillText(t.cardFoot, 80, H - 80);
    return c;
  }
  function roundRect(x, l, tp, w, h, r) { x.beginPath(); x.moveTo(l + r, tp); x.arcTo(l + w, tp, l + w, tp + h, r); x.arcTo(l + w, tp + h, l, tp + h, r); x.arcTo(l, tp + h, l, tp, r); x.arcTo(l, tp, l + w, tp, r); x.closePath(); }
  function shareCard(items) {
    var t = T[L()], c = drawCard(items);
    c.toBlob(function (blob) {
      var file = null; try { file = new File([blob], "easyswingpick-my-bag.png", { type: "image/png" }); } catch (e) {}
      if (file && navigator.canShare && navigator.canShare({ files: [file] })) {
        navigator.share({ files: [file], title: t.cardT, text: t.shareText + " https://easyswingpick.com/app/" }).catch(function () {});
      } else {
        var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "easyswingpick-my-bag.png";
        document.body.appendChild(a); a.click(); a.remove(); toast(t.dl);
      }
    }, "image/png");
  }
  window.ESP = { drawCard: drawCard, shareCard: shareCard, T: T, LS: LS, SS: SS, CALCS: CALCS, toast: toast };

  /* ---------- calculator pages ---------- */
  var m = location.pathname.match(/^\/(driver|iron|wedge|putter)\/?/);
  if (!m) return;
  var calc = m[1], idx = CALCS.indexOf(calc);
  function $(id) { return document.getElementById(id); }

  if (/[?&]set=1/.test(location.search)) SS.set("esp_set", "1");
  var setMode = SS.get("esp_set") === "1";

  /* remember shared inputs and pre-fill empty ones */
  var SHARED = ["age", "hft", "hin", "hcp"];
  function prefill() {
    var p = LS.get("esp_profile", {});
    SHARED.forEach(function (k) {
      var e = $(k); if (!e || p[k] === undefined || p[k] === "") return;
      if (e.tagName === "INPUT") {
        if (e.value !== "") return;
        e.value = p[k]; e.dispatchEvent(new Event("input", { bubbles: true }));
      } else if (!e.querySelector("button.on")) {          /* chip group (handicap) */
        var b = e.querySelector('button[data-k="' + p[k] + '"]'); if (b) b.click();
      }
    });
  }
  function remember() {
    var p = LS.get("esp_profile", {});
    SHARED.forEach(function (k) {
      var e = $(k); if (!e) return;
      if (e.tagName === "INPUT") { if (e.value !== "") p[k] = e.value; }
      else { var on = e.querySelector("button.on"); if (on) p[k] = on.dataset.k; }
    });
    LS.set("esp_profile", p);
  }
  var form = $("f");
  if (form) form.addEventListener("submit", remember);

  function summary() {
    var r = $("result"); if (!r || r.style.display === "none") return null;
    var picks = r.querySelectorAll(".pick"), top = r.querySelector(".pick.top1") || picks[0];
    if (!top || !top.querySelector(".model")) return null;
    var specs = [].slice.call(r.querySelectorAll(".spec")).slice(0, 3).map(function (s) {
      return [s.querySelector("span").textContent.trim(), s.querySelector("b").textContent.trim()];
    });
    if (calc === "wedge") {
      var l = [].slice.call(r.querySelectorAll("#sp b")).map(function (x) { return x.textContent.trim(); });
      specs = l.length ? [[L() === "ko" ? "로프트" : "Lofts", l.join(" · ")]] : [];
    }
    var sc = top.querySelector(".score b");
    /* iron/putter cards show "Brand · head type": split it, and don't repeat the brand when the model already starts with it */
    function nm(card) {
      var raw = card.querySelector(".brand").textContent.trim().split(" · "), b = raw[0], mo = card.querySelector(".model").textContent.trim();
      return { brand: b, kind: raw.slice(1).join(" · "), model: mo, name: mo.toLowerCase().indexOf(b.toLowerCase()) === 0 ? mo : b + " " + mo };
    }
    var n = nm(top);
    if (n.kind) specs.unshift(["", n.kind]);
    return {
      calc: calc, brand: n.brand, model: n.model, name: n.name, fit: sc ? sc.textContent.trim() : "", specs: specs, lang: L(),
      date: new Date().toISOString().slice(0, 10),
      alts: [].slice.call(picks).filter(function (p) { return p !== top; }).map(function (p) { return nm(p).name; })
    };
  }
  function save() {
    var s = summary(); if (!s) return false;
    var bag = LS.get("esp_bag", {}); bag[calc] = s; LS.set("esp_bag", bag); return true;
  }
  function isSaved() {
    var s = summary(), b = LS.get("esp_bag", {})[calc];
    return !!(s && b && b.brand === s.brand && b.model === s.model);
  }

  function setBanner() {
    if (!setMode || document.querySelector(".esp-set")) return;
    var t = T[L()], hero = document.querySelector(".top-in .hero");
    var d = document.createElement("div"); d.className = "esp-set";
    d.innerHTML = '<div class="in"><span><b>' + esc(t.setT(idx)) + esc(t.club[calc]) + '</b></span><span class="dots">' +
      CALCS.map(function (c, i) { return '<i class="' + (i <= idx ? "on" : "") + '"></i>'; }).join("") +
      '</span><a href="/app/" data-quit>' + esc(t.setQuit) + "</a></div>";
    d.querySelector("[data-quit]").onclick = function () { SS.set("esp_set", null); };
    if (hero) hero.parentNode.insertBefore(d, hero); else document.body.prepend(d);
  }
  function refreshBanner() { var b = document.querySelector(".esp-set"); if (b) { b.remove(); setBanner(); } }

  function bar() {
    var r = $("result"), old = document.querySelector(".esp-bar");
    if (!summary()) { if (old) old.remove(); return; }
    var t = T[L()], saved = isSaved(), last = idx === CALCS.length - 1;
    var d = old || document.createElement("div"); d.className = "esp-bar";
    var nextBtn = setMode ? '<a class="esp-b pri" href="#" data-next>' + esc(last ? t.finish : t.next(t.club[CALCS[idx + 1]])) + "</a>" : "";
    d.innerHTML = '<div class="in"><h3>' + esc(t.barT) + "</h3><p>" + esc(t.barS) + '</p><div class="esp-row">' + nextBtn +
      '<button type="button" class="esp-b ' + (saved ? "ok" : setMode ? "" : "pri") + '" data-save>' + esc(saved ? t.saved : t.save) + "</button>" +
      '<button type="button" class="esp-b" data-share>' + esc(t.share) + "</button>" +
      (setMode ? "" : '<a class="esp-b" href="/app/#bag">' + esc(t.bag) + "</a>") +
      '</div><a class="esp-guide" href="' + GUIDE[calc] + '">' + esc(t.guide[calc]) + "</a></div>";
    if (!old) r.parentNode.insertBefore(d, r.nextSibling);
    d.querySelector("[data-save]").onclick = function () { if (save()) { toast(t.toastSaved); bar(); } };
    d.querySelector("[data-share]").onclick = function () { var s = summary(); if (s) shareCard([s]); };
    var n = d.querySelector("[data-next]");
    if (n) n.onclick = function (e) {
      e.preventDefault(); remember(); save();
      if (last) { SS.set("esp_set", null); location.href = "/app/#bag"; } else location.href = "/" + CALCS[idx + 1] + "/?set=1";
    };
  }

  function init() {
    prefill(); setBanner();
    var r = $("result");
    if (r) new MutationObserver(function () { setTimeout(bar, 0); }).observe(r, { childList: true });
    var lt = $("langT"); if (lt) lt.addEventListener("click", function () { setTimeout(function () { refreshBanner(); bar(); }, 30); });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
