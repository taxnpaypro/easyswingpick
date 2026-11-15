/* EasySwingPick app layer (web app / PWA). Loaded on every page by build_deploy.py.
   - registers the service worker (offline use, install to home screen)
   - on calculators: "save to my bag" (saved in Korean AND English), "share result card", related guide link,
     full-set flow (driver → iron → wedge → putter, skip / resume), sticky action bar, app tab bar when installed
   - remembers age / height / handicap so the next calculator is pre-filled
   - in-app browsers (KakaoTalk, Pinterest, Instagram, Facebook…): tells the visitor to open Safari/Chrome
   Everything is stored only on the visitor's device (localStorage). Nothing here changes calculator results:
   it only reads the finished result and adds boxes *below/outside* #result (QA reads #result). */
(function () {
  "use strict";
  var LS = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return localStorage.getItem(k) === JSON.stringify(v); } catch (e) { return false; } },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
  };
  var SS = {
    get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) {} }
  };
  function defLang() { try { return localStorage.getItem("esp_lang") || (/^ko/i.test(navigator.language || "") ? "ko" : "en"); } catch (e) { return "en"; } }
  function L() {
    try { if (typeof lang !== "undefined" && (lang === "ko" || lang === "en")) return lang; } catch (e) {}
    var d = document.documentElement.lang; return d === "ko" || d === "en" ? d : defLang();
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var UA = navigator.userAgent || "";
  var IOS = /iphone|ipad|ipod/i.test(UA) || (/Macintosh/.test(UA) && navigator.maxTouchPoints > 1);
  var STANDALONE = (window.matchMedia && window.matchMedia("(display-mode: standalone)").matches) || navigator.standalone === true;
  var INAPP = /KAKAOTALK/i.test(UA) ? "kakao" : /Pinterest/i.test(UA) ? "pinterest" : /Instagram/i.test(UA) ? "instagram" :
              /FBAN|FBAV|FB_IAB/i.test(UA) ? "facebook" : /\bLine\//i.test(UA) ? "line" : /NAVER\(inapp/i.test(UA) ? "naver" : "";
  var DATA_DATE = { ko: "2026년 11월", en: "November 2026" };

  /* ---------- service worker (live site only, or when testing with ?sw=1) ---------- */
  var swOK = /(^|\.)easyswingpick\.com$/.test(location.hostname) || /[?&]sw=1/.test(location.search);
  if ("serviceWorker" in navigator && swOK) {
    window.addEventListener("load", function () { navigator.serviceWorker.register("/sw.js").catch(function () {}); });
  }
  window.addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); window.__espInstall = e; document.dispatchEvent(new Event("esp-install-ready")); });
  function persist() { try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist(); } catch (e) {} }

  /* ---------- styles ---------- */
  if (LS.get("esp_big", false)) document.documentElement.classList.add("esp-big");
  var F = "Inter,'Noto Sans KR',system-ui,sans-serif";
  var st = document.createElement("style");
  st.textContent =
    "html.esp-big body{zoom:1.12}" +
    ".esp-bar{max-width:760px;margin:16px auto 0;padding:0 16px}" +
    ".esp-bar .in{background:#fff;border:1px solid #e3e8ec;border-radius:16px;padding:16px;box-shadow:0 1px 2px rgba(15,42,61,.06),0 6px 20px rgba(15,42,61,.06)}" +
    ".esp-bar h3{margin:0 0 4px;font-size:1.05rem;color:#0f2a3d}.esp-bar p{margin:0 0 12px;color:#64727d;font-size:.9rem}" +
    ".esp-row{display:flex;gap:8px;flex-wrap:wrap}" +
    ".esp-b{flex:1 1 150px;min-height:48px;border-radius:12px;border:1.5px solid #0f2a3d;background:#fff;color:#0f2a3d;font:600 .95rem " + F + ";cursor:pointer;padding:10px 12px;text-align:center;text-decoration:none;display:flex;align-items:center;justify-content:center;gap:6px}" +
    ".esp-b.pri{background:#0f2a3d;color:#fff}.esp-b.ok{background:#e6f4ee;border-color:#178a5b;color:#178a5b}" +
    ".esp-guide{display:block;margin-top:12px;font-size:.92rem;color:#173b55;font-weight:600}" +
    ".esp-set{margin:14px 0 4px}" +
    ".esp-set .in{background:rgba(255,255,255,.12);color:#fff;border-radius:14px;padding:12px 14px;display:flex;align-items:center;gap:10px;font-size:.92rem;flex-wrap:wrap}" +
    ".esp-set .dots{display:flex;gap:5px;margin-left:auto}.esp-set .dots i{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.3)}.esp-set .dots i.on{background:#c89b3c}" +
    ".esp-set a{color:#c89b3c;font-weight:600;text-decoration:none}" +
    ".esp-toast{position:fixed;left:50%;top:calc(16px + env(safe-area-inset-top));transform:translateX(-50%);width:max-content;max-width:calc(100% - 32px);background:#178a5b;color:#fff;padding:14px 20px;border-radius:14px;font:600 1rem " + F + ";z-index:99;opacity:0;pointer-events:none;transition:opacity .2s;box-shadow:0 8px 24px rgba(0,0,0,.2);text-align:center}" +
    ".esp-toast.on{opacity:1;pointer-events:auto}.esp-toast.bad{background:#b3412e}.esp-toast a{color:#fff;display:block;margin-top:4px;font-weight:700}" +
    ".esp-stick{position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(255,255,255,.97);border-top:1px solid #e3e8ec;padding:10px 12px calc(10px + env(safe-area-inset-bottom));display:none;gap:8px;box-shadow:0 -6px 20px rgba(15,42,61,.08)}" +
    ".esp-stick.on{display:flex}.esp-stick .esp-b{flex:1 1 0;min-height:46px;font-size:.92rem}" +
    "html.esp-tabs .esp-stick{bottom:calc(62px + env(safe-area-inset-bottom));padding-bottom:10px}" +
    "html.esp-tabs body{padding-bottom:calc(140px + env(safe-area-inset-bottom))}" +
    ".esp-tabbar{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #e3e8ec;display:flex;padding-bottom:env(safe-area-inset-bottom);z-index:41}" +
    ".esp-tabbar a{flex:1;text-align:center;text-decoration:none;color:#64727d;font:600 .75rem " + F + ";padding:9px 0 10px}.esp-tabbar a b{display:block;font-size:1.15rem;line-height:1.3}.esp-tabbar a.on{color:#0f2a3d}" +
    ".esp-inapp{position:relative;z-index:50;background:#fbf4e4;border-bottom:1px solid #ecd9a8;color:#5a4410;font:500 .92rem/1.45 " + F + ";padding:12px 40px 12px 16px}" +
    ".esp-inapp b{color:#0f2a3d}.esp-inapp a.go{display:inline-block;margin-top:8px;background:#0f2a3d;color:#fff;border-radius:10px;padding:8px 14px;font-weight:700;text-decoration:none}" +
    ".esp-inapp button{position:absolute;right:8px;top:8px;border:0;background:none;font-size:1.3rem;color:#8a6d1f;cursor:pointer;width:32px;height:32px}" +
    ".esp-ov{position:fixed;inset:0;background:rgba(15,42,61,.85);z-index:100;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;gap:14px}" +
    ".esp-ov img{max-width:100%;max-height:70vh;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.4)}" +
    ".esp-ov p{color:#fff;font:600 1rem " + F + ";margin:0;text-align:center}.esp-ov .esp-b{max-width:320px;background:#fff}";
  document.head.appendChild(st);

  var CALCS = ["driver", "iron", "wedge", "putter"];
  var T = {
    ko: {
      club: { driver: "드라이버", iron: "아이언", wedge: "웨지", putter: "퍼터" },
      barT: "이 결과로 무엇을 할까요?", barS: "저장한 결과는 이 휴대폰(브라우저)에만 보관됩니다.",
      save: "내 골프백에 저장", saved: "✓ 저장됨 · 내 골프백 보기 →", savedShort: "✓ 저장됨 · 골프백 →", share: "결과 카드 공유", bag: "내 골프백 보기",
      guide: { driver: "관련 가이드: 2026 인기 드라이버 비교 →", iron: "관련 가이드: 2026 인기 아이언 비교 →", wedge: "관련 가이드: 2026 인기 웨지 비교 →", putter: "관련 가이드: 2026 인기 퍼터 비교 →" },
      setT: function (i) { return "전체 세트 추천 " + (i + 1) + "/4 · "; }, setQuit: "그만하기", setSkip: "이 클럽 건너뛰기 →",
      next: function (c) { return "저장하고 다음: " + c + " →"; }, nextShort: function (c) { return "저장·다음: " + c + " →"; },
      finish: "저장하고 내 골프백 보기 →", finishShort: "저장·골프백 보기 →",
      toastSaved: "✓ 내 골프백에 저장했습니다", toastSee: "내 골프백 보기 →",
      iosKeep: "iPhone에서는 홈 화면에 추가해야 오래 보관됩니다",
      noStore: "이 브라우저에서는 저장할 수 없습니다. 개인정보 보호(시크릿) 모드를 끄고 다시 해 주세요.",
      cardT: "나의 골프백", cardS: "무료 클럽 피팅 계산기 추천 결과", cardFoot: "나도 해 보기 → easyswingpick.com/app",
      shareText: "EasySwingPick 계산기로 받은 내 클럽 추천입니다.", dl: "이미지를 저장했습니다", hold: "이미지를 길게 눌러 저장하거나 공유하세요", close: "닫기",
      inp: { driver: "드라이버 ", iron: "7번 ", wedge: "7번 ", yd: "야드", age: "세" },
      offline: "인터넷에 연결되면 열 수 있습니다",
      inapp: { kakao: "카카오톡", pinterest: "Pinterest", instagram: "Instagram", facebook: "Facebook", line: "LINE", naver: "네이버" },
      inappT: function (a) { return "지금 <b>" + a + " 안의 브라우저</b>로 열려 있어 골프백 저장과 홈 화면 설치가 제대로 되지 않을 수 있습니다."; },
      inappHow: IOS ? "오른쪽 아래(또는 위) <b>⋯ / 공유</b> → <b>Safari로 열기</b>를 누르세요." : "오른쪽 위 <b>⋮</b> → <b>다른 브라우저로 열기</b>(Chrome)를 누르세요.",
      inappGo: "Safari/Chrome으로 열기"
    },
    en: {
      club: { driver: "Driver", iron: "Irons", wedge: "Wedges", putter: "Putter" },
      barT: "What would you like to do with this result?", barS: "Saved results stay only on this phone (browser).",
      save: "Save to my bag", saved: "✓ Saved · View my bag →", savedShort: "✓ Saved · My bag →", share: "Share result card", bag: "View my bag",
      guide: { driver: "Related guide: 2026's hot drivers compared →", iron: "Related guide: 2026's hot irons compared →", wedge: "Related guide: 2026's hot wedges compared →", putter: "Related guide: 2026's hot putters compared →" },
      setT: function (i) { return "Full-set fitting " + (i + 1) + "/4 · "; }, setQuit: "Stop", setSkip: "Skip this club →",
      next: function (c) { return "Save & next: " + c + " →"; }, nextShort: function (c) { return "Save & next: " + c + " →"; },
      finish: "Save & view my bag →", finishShort: "Save & view bag →",
      toastSaved: "✓ Saved to your bag", toastSee: "View my bag →",
      iosKeep: "On iPhone, add the app to your Home Screen to keep it long-term",
      noStore: "This browser can't save. Turn off private browsing and try again.",
      cardT: "My Golf Bag", cardS: "Picks from free club-fitting calculators", cardFoot: "Try it yourself → easyswingpick.com/app",
      shareText: "My club picks from the EasySwingPick calculators.", dl: "Image saved", hold: "Press and hold the image to save or share it", close: "Close",
      inp: { driver: "Driver ", iron: "7-iron ", wedge: "7-iron ", yd: " yd", age: "age " },
      offline: "Available once you're back online",
      inapp: { kakao: "KakaoTalk", pinterest: "Pinterest", instagram: "Instagram", facebook: "Facebook", line: "LINE", naver: "Naver" },
      inappT: function (a) { return "This page is open <b>inside " + a + "</b>, so saving your bag and installing the app may not work."; },
      inappHow: IOS ? "Tap <b>⋯ / Share</b> → <b>Open in Safari</b>." : "Tap <b>⋮</b> (top right) → <b>Open in Chrome</b> / another browser.",
      inappGo: "Open in Safari/Chrome"
    }
  };
  var GUIDE = { driver: "/blog/hot-drivers-2026", iron: "/blog/hot-irons-2026", wedge: "/blog/hot-wedges-2026", putter: "/blog/hot-putters-2026" };

  function toast(msg, link, bad, extra) {
    var el = document.querySelector(".esp-toast");
    if (!el) { el = document.createElement("div"); el.className = "esp-toast"; document.body.appendChild(el); }
    el.innerHTML = esc(msg) + (extra ? '<div style="font-weight:500;font-size:.85rem;margin-top:4px;opacity:.9">' + esc(extra) + "</div>" : "") +
      (link ? '<a href="' + link[1] + '">' + esc(link[0]) + "</a>" : "");
    el.classList.toggle("bad", !!bad); el.classList.add("on"); clearTimeout(el._t); el._t = setTimeout(function () { el.classList.remove("on"); }, link ? 4500 : 2500);
  }

  /* bag items: new format {calc, date, fit, inp, ko:{name,brand,model,specs,alts}, en:{…}}; old items had those fields at top level */
  function view(it, l) { return it[l] || it[l === "ko" ? "en" : "ko"] || it; }
  function itemName(v) { return v.name || ((v.brand || "") + " " + (v.model || "")).trim(); }
  function specLine(v, withKind) {
    return (v.specs || []).filter(function (s) { return withKind || s[0]; }).map(function (s) { return (s[0] + " " + s[1]).trim(); });
  }
  function inpLine(it, l) {
    var t = T[l].inp, i = it.inp || {}, out = [];
    if (i.d) out.push(t[it.calc] + i.d + t.yd);
    if (i.age) out.push(l === "ko" ? i.age + t.age : t.age + i.age);
    return out.join(" · ");
  }

  /* ---------- share card (canvas image) ---------- */
  function drawCard(items) {
    var l = L(), t = T[l], W = 1080, H = Math.min(1350, 340 + Math.max(items.length, 1) * 230 + 150), c = document.createElement("canvas"); c.width = W; c.height = H;
    var x = c.getContext("2d"), FF = "Inter, 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', system-ui, sans-serif";
    x.fillStyle = "#0f2a3d"; x.fillRect(0, 0, W, H);
    x.fillStyle = "#c89b3c"; x.fillRect(80, 110, 90, 10);
    x.fillStyle = "#fff"; x.font = "700 76px " + FF; x.fillText(t.cardT, 80, 220);
    x.fillStyle = "rgba(255,255,255,.65)"; x.font = "500 34px " + FF; x.fillText(t.cardS, 80, 275);
    var y = 340, slot = Math.min(230, (H - 340 - 150) / Math.max(items.length, 1));
    items.forEach(function (it) {
      var v = view(it, l);
      x.fillStyle = "rgba(255,255,255,.07)"; rr(x, 70, y, W - 140, slot - 24, 28); x.fill();
      x.fillStyle = "#c89b3c"; x.font = "700 30px " + FF; x.fillText(t.club[it.calc].toUpperCase(), 110, y + 58);
      x.fillStyle = "#fff"; x.font = "700 50px " + FF;
      var name = itemName(v); while (x.measureText(name).width > W - 220 && name.length > 4) name = name.slice(0, -2) + "…";
      x.fillText(name, 110, y + 122);
      x.fillStyle = "rgba(255,255,255,.72)"; x.font = "500 30px " + FF;
      var spec = ""; specLine(v, false).forEach(function (q) { var tr = spec ? spec + "  ·  " + q : q; if (x.measureText(tr).width <= W - 220) spec = tr; });
      if (spec && slot > 200) x.fillText(spec, 110, y + 172);
      y += slot;
    });
    x.fillStyle = "#c89b3c"; x.font = "700 34px " + FF; x.fillText(t.cardFoot, 80, H - 80);
    return c;
  }
  function rr(x, l, tp, w, h, r) { x.beginPath(); x.moveTo(l + r, tp); x.arcTo(l + w, tp, l + w, tp + h, r); x.arcTo(l + w, tp + h, l, tp + h, r); x.arcTo(l, tp + h, l, tp, r); x.arcTo(l, tp, l + w, tp, r); x.closePath(); }
  function overlay(html) {
    var o = document.createElement("div"); o.className = "esp-ov"; o.innerHTML = html;
    o.addEventListener("click", function (e) { if (e.target === o || e.target.hasAttribute("data-close")) o.remove(); });
    document.body.appendChild(o); return o;
  }
  function showImage(url) {
    var t = T[L()];
    overlay('<p>' + esc(t.hold) + '</p><img src="' + url + '" alt=""><a class="esp-b" download="easyswingpick-my-bag.png" href="' + url + '">PNG ↓</a><button class="esp-b" data-close>' + esc(t.close) + "</button>");
  }
  function shareCard(items) {
    var t = T[L()], c = drawCard(items);
    c.toBlob(function (blob) {
      var file = null; try { file = new File([blob], "easyswingpick-my-bag.png", { type: "image/png" }); } catch (e) {}
      if (file && navigator.canShare && navigator.canShare({ files: [file] })) {
        navigator.share({ files: [file], title: t.cardT, text: t.shareText + " https://easyswingpick.com/app/" }).catch(function () {});
      } else showImage(URL.createObjectURL(blob));   // older phones / desktop: show the image to press-and-hold or download
    }, "image/png");
  }

  /* ---------- in-app browsers (KakaoTalk, Pinterest, …) ---------- */
  function inAppNotice() {
    if (!INAPP || SS.get("esp_inapp_x") || document.querySelector(".esp-inapp")) return;
    var t = T[L()], name = t.inapp[INAPP], url = location.href.replace(/[?&]sw=1/, "");
    var go = INAPP === "kakao" ? '<br><a class="go" href="kakaotalk://web/openExternal?url=' + encodeURIComponent(url) + '">' + esc(t.inappGo) + "</a>" : "";
    var d = document.createElement("div"); d.className = "esp-inapp";
    d.innerHTML = t.inappT(esc(name)) + " " + t.inappHow + go + '<button aria-label="close">×</button>';
    d.querySelector("button").onclick = function () { SS.set("esp_inapp_x", "1"); d.remove(); };
    document.body.insertBefore(d, document.body.firstChild);
  }

  /* ---------- offline: external links can't open ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]"); if (!a || navigator.onLine !== false) return;
    try { if (new URL(a.href, location.href).origin !== location.origin) { e.preventDefault(); toast(T[L()].offline, null, true); } } catch (x) {}
  }, true);

  /* ---------- app tab bar on calculator pages when opened from the home screen ---------- */
  function tabBar(active) {
    if (!STANDALONE || document.querySelector(".esp-tabbar")) return;
    var l = L(), n = l === "ko" ? ["계산기", "내 골프백", "가이드", "설정"] : ["Fit", "My bag", "Guides", "Settings"];
    var d = document.createElement("nav"); d.className = "esp-tabbar";
    d.innerHTML = [["/app/#home", "◎"], ["/app/#bag", "▣"], ["/app/#guides", "▤"], ["/app/#settings", "⚙"]].map(function (x, i) {
      return '<a href="' + x[0] + '" class="' + (i === active ? "on" : "") + '"><b>' + x[1] + "</b>" + n[i] + "</a>"; }).join("");
    document.body.appendChild(d); document.documentElement.classList.add("esp-tabs");
  }

  /* backup / move link: the whole bag in the link itself (no server, no account) */
  function b64e(s) { return btoa(unescape(encodeURIComponent(s))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); }
  function b64d(s) { s = s.replace(/-/g, "+").replace(/_/g, "/"); while (s.length % 4) s += "="; return decodeURIComponent(escape(atob(s))); }

  window.ESP = { drawCard: drawCard, shareCard: shareCard, T: T, LS: LS, SS: SS, CALCS: CALCS, toast: toast, view: view, itemName: itemName,
                 specLine: specLine, inpLine: inpLine, IOS: IOS, STANDALONE: STANDALONE, INAPP: INAPP, DATA_DATE: DATA_DATE,
                 b64e: b64e, b64d: b64d, overlay: overlay, persist: persist, defLang: defLang, esc: esc };

  function ready(f) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", f); else f(); }
  ready(inAppNotice);

  /* ---------- calculator pages ---------- */
  var m = location.pathname.match(/^\/(driver|iron|wedge|putter)\/?/);
  if (!m) return;
  var calc = m[1], idx = CALCS.indexOf(calc);
  function $(id) { return document.getElementById(id); }

  if (/[?&]set=1/.test(location.search)) SS.set("esp_set", "1");
  var setMode = SS.get("esp_set") === "1";
  if (setMode) LS.set("esp_resume", { step: idx, ts: Date.now() });   // lets the app home offer "continue where you left off"

  /* remember shared inputs and pre-fill empty ones */
  var SHARED = ["age", "hft", "hin", "hcp"];
  function prefill() {
    var p = LS.get("esp_profile", {});
    SHARED.forEach(function (k) {
      var e = $(k); if (!e || p[k] === undefined || p[k] === "") return;
      if (e.tagName === "INPUT") { if (e.value !== "") return; e.value = p[k]; e.dispatchEvent(new Event("input", { bubbles: true })); }
      else if (!e.querySelector("button.on")) { var b = e.querySelector('button[data-k="' + p[k] + '"]'); if (b) b.click(); }
    });
    var i7 = $("i7");   /* wedge calculator: 7-iron carry already entered in the iron calculator */
    if (i7 && i7.value === "" && p.i7) { i7.value = p.i7; i7.dispatchEvent(new Event("input", { bubbles: true })); }
  }
  function remember() {
    var p = LS.get("esp_profile", {});
    SHARED.forEach(function (k) {
      var e = $(k); if (!e) return;
      if (e.tagName === "INPUT") { if (e.value !== "") p[k] = e.value; }
      else { var on = e.querySelector("button.on"); if (on) p[k] = on.dataset.k; }
    });
    var i7 = calc === "iron" ? $("dist") : $("i7"); if (i7 && i7.value !== "") p.i7 = i7.value;
    LS.set("esp_profile", p);
  }
  var form = $("f");
  if (form) form.addEventListener("submit", remember);

  /* read the finished result (in the language currently shown) */
  function read() {
    var r = $("result"); if (!r || r.style.display === "none") return null;
    var picks = r.querySelectorAll(".pick"), top = r.querySelector(".pick.top1") || picks[0];
    if (!top || !top.querySelector(".model")) return null;
    var specs = [].slice.call(r.querySelectorAll(".spec")).slice(0, 3).map(function (s) {
      return [s.querySelector("span").textContent.trim(), s.querySelector("b").textContent.trim()];
    });
    if (calc === "wedge") {
      var lo = [].slice.call(r.querySelectorAll("#sp b")).map(function (x) { return x.textContent.trim(); });
      specs = lo.length ? [[L() === "ko" ? "로프트" : "Lofts", lo.join(" · ")]] : [];
    }
    function nm(card) {   /* iron/putter cards show "Brand · head type"; don't repeat the brand when the model starts with it */
      var raw = card.querySelector(".brand").textContent.trim().split(" · "), b = raw[0], mo = card.querySelector(".model").textContent.trim();
      return { brand: b, kind: raw.slice(1).join(" · "), model: mo, name: mo.toLowerCase().indexOf(b.toLowerCase()) === 0 ? mo : b + " " + mo };
    }
    var n = nm(top); if (n.kind) specs.unshift(["", n.kind]);
    var sc = top.querySelector(".score b");
    return { brand: n.brand, model: n.model, name: n.name, specs: specs, fit: sc ? sc.textContent.trim() : "",
             alts: [].slice.call(picks).filter(function (p) { return p !== top; }).map(function (p) { return nm(p).name; }) };
  }
  /* full item in both languages: re-render the result in the other language for a moment, read it, switch back */
  function summary() {
    var cur = read(); if (!cur) return null;
    var l = L(), o = l === "ko" ? "en" : "ko", other = null;
    try {
      if (typeof render === "function" && typeof lang !== "undefined") {
        lang = o; render(); other = read(); lang = l; render();
      }
    } catch (e) { try { lang = l; render(); } catch (x) {} }
    var d = $("dist") || $("i7"), a = $("age"), item = { calc: calc, date: (function (d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); })(new Date()), fit: cur.fit,
      inp: { d: d && d.value ? d.value : "", age: a && a.value ? a.value : "" } };
    item[l] = cur; item[o] = other || cur;
    return item;
  }
  function save() {
    var s = summary(); if (!s) return false;
    var bag = LS.get("esp_bag", {}); bag[calc] = s; var ok = LS.set("esp_bag", bag); if (ok) persist(); return ok;
  }
  function isSaved() {
    var s = read(), b = LS.get("esp_bag", {})[calc]; if (!s || !b) return false;
    var v = view(b, L()); return v.brand === s.brand && v.model === s.model;
  }

  function setBanner() {
    if (!setMode || document.querySelector(".esp-set")) return;
    var t = T[L()], hero = document.querySelector(".top-in .hero"), last = idx === CALCS.length - 1;
    var d = document.createElement("div"); d.className = "esp-set";
    d.innerHTML = '<div class="in"><span><b>' + esc(t.setT(idx)) + esc(t.club[calc]) + '</b></span><span class="dots">' +
      CALCS.map(function (c, i) { return '<i class="' + (i <= idx ? "on" : "") + '"></i>'; }).join("") +
      '</span><a href="' + (last ? "/app/#bag" : "/" + CALCS[idx + 1] + "/?set=1") + '" data-skip>' + esc(t.setSkip) + '</a><a href="/app/" data-quit>' + esc(t.setQuit) + "</a></div>";
    d.querySelector("[data-quit]").onclick = function () { SS.set("esp_set", null); LS.del("esp_resume"); };
    d.querySelector("[data-skip]").onclick = function () { if (last) { SS.set("esp_set", null); LS.del("esp_resume"); } };
    if (hero) hero.parentNode.insertBefore(d, hero); else document.body.prepend(d);
  }
  function refreshBanner() { var b = document.querySelector(".esp-set"); if (b) { b.remove(); setBanner(); } }

  function goNext() {
    remember(); save();
    if (idx === CALCS.length - 1) { SS.set("esp_set", null); LS.del("esp_resume"); location.href = "/app/#bag"; }
    else location.href = "/" + CALCS[idx + 1] + "/?set=1";
  }
  function onSave() {
    var t = T[L()];
    if (isSaved()) { location.href = "/app/#bag"; return; }
    if (save()) { toast(t.toastSaved, [t.toastSee, "/app/#bag"], false, IOS && !STANDALONE ? t.iosKeep : ""); bar(); }
    else toast(t.noStore, null, true);
  }

  /* in the installed app, tag affiliate clicks as app-<calc> so Awin reports show what the app earns */
  function tagLinks() {
    if (!STANDALONE) return;
    [].forEach.call(document.querySelectorAll('#result a[href*="clickref=calc-"]'), function (a) { a.href = a.href.replace("clickref=calc-", "clickref=app-"); });
  }

  var stick = null, barVisible = true;
  function bar() {
    var r = $("result"), old = document.querySelector(".esp-bar");
    if (!read()) { if (old) old.remove(); if (stick) stick.classList.remove("on"); return; }
    tagLinks();
    var t = T[L()], saved = isSaved(), last = idx === CALCS.length - 1;
    var d = old || document.createElement("div"); d.className = "esp-bar";
    var nextBtn = setMode ? '<a class="esp-b pri" href="#" data-next>' + esc(last ? t.finish : t.next(t.club[CALCS[idx + 1]])) + "</a>" : "";
    d.innerHTML = '<div class="in"><h3>' + esc(t.barT) + "</h3><p>" + esc(t.barS) + '</p><div class="esp-row">' + nextBtn +
      '<button type="button" class="esp-b ' + (saved ? "ok" : setMode ? "" : "pri") + '" data-save>' + esc(saved ? t.saved : t.save) + "</button>" +
      '<button type="button" class="esp-b" data-share>' + esc(t.share) + "</button>" +
      (setMode ? "" : '<a class="esp-b" href="/app/#bag">' + esc(t.bag) + "</a>") +
      '</div><a class="esp-guide" href="' + GUIDE[calc] + '">' + esc(t.guide[calc]) + "</a></div>";
    if (!old) { r.parentNode.insertBefore(d, r.nextSibling); watchBar(d); }
    d.querySelector("[data-save]").onclick = onSave;
    d.querySelector("[data-share]").onclick = function () { var s = summary(); if (s) shareCard([s]); };
    var n = d.querySelector("[data-next]"); if (n) n.onclick = function (e) { e.preventDefault(); goNext(); };
    /* sticky bar at the bottom of the screen while the big box is out of view */
    if (!stick) { stick = document.createElement("div"); stick.className = "esp-stick"; document.body.appendChild(stick); }
    stick.innerHTML = setMode
      ? '<a class="esp-b pri" href="#" data-next>' + esc(last ? t.finishShort : t.nextShort(t.club[CALCS[idx + 1]])) + "</a>"
      : '<button type="button" class="esp-b ' + (saved ? "ok" : "pri") + '" data-save>' + esc(saved ? t.savedShort : t.save) + '</button><button type="button" class="esp-b" data-share>' + esc(t.share) + "</button>";
    var sn = stick.querySelector("[data-next]"); if (sn) sn.onclick = function (e) { e.preventDefault(); goNext(); };
    var ss = stick.querySelector("[data-save]"); if (ss) ss.onclick = onSave;
    var sh = stick.querySelector("[data-share]"); if (sh) sh.onclick = function () { var s = summary(); if (s) shareCard([s]); };
    stick.classList.toggle("on", !barVisible);
  }
  function watchBar(el) {
    if (!("IntersectionObserver" in window)) return;
    new IntersectionObserver(function (es) {
      barVisible = es[0].isIntersecting;
      var r = $("result"), shown = r && r.style.display !== "none" && r.getBoundingClientRect().top < innerHeight;
      if (stick) stick.classList.toggle("on", !barVisible && !!shown);
    }).observe(el);
  }

  ready(function () {
    prefill(); setBanner(); tabBar(0);
    var r = $("result"), busy = false;
    if (r) new MutationObserver(function () { if (busy) return; busy = true; setTimeout(function () { busy = false; bar(); }, 0); }).observe(r, { childList: true });
    var lt = $("langT"); if (lt) lt.addEventListener("click", function () { setTimeout(function () { refreshBanner(); bar(); }, 30); });
    addEventListener("scroll", function () {
      if (!stick || barVisible) return; var rr2 = $("result");
      stick.classList.toggle("on", !!(rr2 && rr2.style.display !== "none" && rr2.getBoundingClientRect().top < innerHeight));
    }, { passive: true });
  });
})();
