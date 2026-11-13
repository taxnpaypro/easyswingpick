import re, os, shutil, html, datetime
DOMAIN = "https://easyswingpick.com"   # change if the domain differs
EMAIL = "hello@easyswingpick.com"      # create via Cloudflare Email Routing (free)
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/deploy"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(f"{OUT}/assets"); os.makedirs(f"{OUT}/blog")

CALC = {"8qNVFjbmMa2iMgjhxoeWmA": "/driver/", "Dz35Q1crsGFwXLvyTx4swA": "/iron/",
        "UHd2KFRkKYuNJ1QLsSUAm2": "/wedge/", "YQSj4S2ynmVwf1edh6gM68": "/putter/"}
POSTF = {"2GgBRU6suf51Z1WnW5W9cC": "mizuno-jpx-vs-pro", "VYPzdx276EPSbYg95PERPb": "miura-vs-mizuno",
         "F1FxAeTP8VkRwP26d6CEKg": "lightweight-drivers", "Lobmv73sYz1aiPpos3bNAd": "honma-miura",
         "NWpmwJSA5cBGYK6q7ra3AY": "zero-torque-putters", "NddLBxMeDgZubccoapKFRd": "hot-clubs-2026",
         "HLgovE5tVXDHSs1jQ67GvE": "hot-drivers-2026", "TLfXUU4CWcnazHDbCK9rNh": "hot-irons-2026",
         "X72PkRChyN87rWw6uq5Sn4": "hot-wedges-2026", "JcP6M1R2JwKM38jouZpLhy": "hot-putters-2026",
         "W3otpxg6ms9gbrFk1R3cu1": "driver-adjust-guide"}
MAP = dict(CALC); MAP.update({k: f"/blog/{v}" for k, v in POSTF.items()})
# every site/blog-<slug>.html is published, so new posts need no entry here
SLUGS = list(POSTF.values()) + sorted(os.path.basename(p)[5:-5] for p in __import__("glob").glob(f"{H}/site/blog-*.html") if os.path.basename(p)[5:-5] not in POSTF.values())

# ---------- assets ----------
shutil.copytree(f"{H}/site/img", f"{OUT}/assets/img")
shutil.copy(f"{H}/logo/c.svg", f"{OUT}/assets/logo.svg")
shutil.copy(f"{H}/logo/c.svg", f"{OUT}/assets/favicon.svg")
shutil.copy(f"{H}/logo/wordmark.svg", f"{OUT}/assets/wordmark.svg")
HEAD = ('<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">'
        '<link rel="icon" href="/assets/favicon-32.png" sizes="32x32">'
        '<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">')

def logo_img(n): return f'<img src="/assets/logo.svg" width="{n}" height="{n}" alt="" style="border-radius:{n//4}px">'

def fix(s, path):
    for k, v in MAP.items():
        s = s.replace(f'"https://claude.ai/artifact/{k}" target="_blank" rel="noopener"', f'"{v}"')
        s = s.replace(f"'https://claude.ai/artifact/{k}' target='_blank' rel='noopener'", f"'{v}'")
        s = s.replace(f"https://claude.ai/artifact/{k}", v)
    assert "claude.ai/artifact" not in s, path
    s = re.sub(r'<svg width="(30|34)" height="\1" viewBox="0 0 34 34" aria-hidden="true">.*?</svg>',
               lambda m: logo_img(int(m.group(1))), s, flags=re.S)
    s = s.replace('href="index.html"', 'href="/"')
    s = s.replace("</head>", f'{HEAD}<link rel="canonical" href="{DOMAIN}{path}">\n</head>', 1)
    return s

# ---------- homepage ----------
s = open(f"{H}/site/index.html").read()
s = s.replace(" (시연판)", "")
s = s.replace('href="${LINKS[k]}" target="_blank" rel="noopener"', 'href="${LINKS[k]}"')
s = s.replace('href="${p.u}" target="_blank" rel="noopener"', 'href="${p.u}"')
s = s.replace('id="ctaDriver" target="_blank" rel="noopener"', 'id="ctaDriver"')
s = s.replace('["#about","#top","#about","#about"]', '["/about","/disclosure","/privacy","/contact"]')
s = s.replace('<a class="logo" href="#top">', '<a class="logo" href="/">')
s = fix(s, "/")
open(f"{OUT}/index.html", "w").write(s)

# ---------- calculators ----------
for name, path in [("driver", "/driver/"), ("iron", "/iron/"), ("wedge", "/wedge/"), ("putter", "/putter/")]:
    s = open(f"{H}/{name}-fit/index.html").read()
    s = fix(s, path)
    s = s.replace(" (시연판)", "").replace("시연판입니다. ", "").replace("Demo version. ", "")
    s = s.replace(", 구매 링크는 아직 연결되지 않았습니다.", ", 결과는 추정치입니다. 일부 링크는 제휴 링크일 수 있습니다.")
    s = s.replace("; buy links are not connected yet.", "; results are estimates. Some links may be affiliate links.")
    # no yellow notice above the form: nothing to buy before the analysis; the affiliate notice sits at the top of the result (next to the links) and the estimate note is in the footer
    s = s.replace('<div class="demo" data-t="demo"></div>', "")
    s = re.sub(r'<div class="logo">(\s*<img[^>]*>\s*<div>.*?</div>\s*)</div>',
               r'<a class="logo" href="/" style="color:inherit;text-decoration:none" title="EasySwingPick">\1</a>', s, count=1, flags=re.S)
    os.makedirs(f"{OUT}{path}", exist_ok=True)
    open(f"{OUT}{path}index.html", "w").write(s)

# ---------- blog ----------
for slug in SLUGS:
    src = f"{H}/site/blog-{slug}.html"
    s = fix(open(src).read(), f"/blog/{slug}")
    s = s.replace('<div class="meta">EasySwingPick · <span data-l="ko">2026년 11월</span><span data-l="en">November 2026</span></div>',
        '<div class="meta"><span data-l="ko">글 EasySwingPick 편집부 · 최종 업데이트 2026년 11월</span><span data-l="en">By EasySwingPick Editors · Updated November 2026</span></div>')
    AB = ('<div class="abox" style="display:flex;gap:14px;align-items:center;border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:28px 0 8px">'
          '<img src="/assets/logo.svg" width="48" height="48" alt="" style="border-radius:12px;flex:none">'
          '<div style="font-size:.9rem"><b data-l="ko">EasySwingPick 편집부</b><b data-l="en">EasySwingPick Editors</b><br>'
          '<span data-l="ko" style="color:var(--muted)">공개된 리뷰·테스트 자료를 비교하고 출처를 밝혀 한국어와 영어로 씁니다. <a href="/about">소개 보기</a></span>'
          '<span data-l="en" style="color:var(--muted)">We compare published reviews and testing, cite every source, and write in Korean and English. <a href="/about">About us</a></span></div></div>')
    # disclosure: one short line up top (before any affiliate link), full text at the end
    DISC_RE = r'<div class="disc"><span data-l="ko">(.*?)</span><span data-l="en">(.*?)</span></div>'
    m = re.search(DISC_RE, s)
    if m:
        s = s.replace(m.group(0),
            '<p class="disc1"><span data-l="ko">이 글에는 제휴 링크가 있습니다. <a href="#disclosure">자세히 보기</a></span>'
            '<span data-l="en">This post contains affiliate links. <a href="#disclosure">Learn more</a></span></p>', 1)
        AB = ('<div class="disc" id="disclosure" style="margin:28px 0 0;background:none;padding:0;border-radius:0;color:var(--muted);font-size:.85rem"><span data-l="ko"><b>제휴 안내</b> · ' + m.group(1) + ' <a href="/disclosure">제휴 정책 전문</a></span>'
              '<span data-l="en"><b>Affiliate disclosure</b> · ' + m.group(2) + ' <a href="/disclosure">Full policy</a></span></div>') + AB
        s = s.replace("</style>", ".disc1{font-size:.8rem;color:var(--muted);margin:14px 0 0}.disc1 a{color:inherit;text-decoration:underline}</style>", 1)
    s = s.replace('<div class="src">', AB + '<div class="src">', 1)
    assert "편집부 · 최종" in s and "abox" in s, slug
    open(f"{OUT}/blog/{slug}.html", "w").write(s)

# ---------- info pages ----------
CSS = open(f"{H}/post_css.html").read()
def info(slug, t_ko, t_en, ko, en):
    page = f'''<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t_ko} | EasySwingPick</title><meta name="description" content="EasySwingPick {t_ko}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+KR:wght@400;500;700;800&display=swap" rel="stylesheet">
{CSS.replace('</style>', '.hero{background:radial-gradient(120% 120% at 80% 0%,#21506d 0%,#0f2a3d 60%,#0a1c29 100%);padding-bottom:34px}</style>')}
{HEAD}<link rel="canonical" href="{DOMAIN}/{slug}"></head><body>
<header><div class="hd"><a class="logo" href="/">{logo_img(30)}<span>EasySwingPick</span></a>
<div class="lang" id="langT"><button data-lang="ko" class="on">한국어</button><button data-lang="en">EN</button></div></div></header>
<section class="hero"><div class="wrap"><div class="crumb"><a href="/">홈</a> › <span data-l="ko">{t_ko}</span><span data-l="en">{t_en}</span></div>
<h1><span data-l="ko">{t_ko}</span><span data-l="en">{t_en}</span></h1></div></section>
<div class="wrap"><article data-l="ko">{ko}</article><article data-l="en">{en}</article></div>
<footer><span data-l="ko">© 2026 EasySwingPick · <a href="/about">소개</a> · <a href="/disclosure">제휴 링크 고지</a> · <a href="/privacy">개인정보처리방침</a> · <a href="/contact">문의</a></span><span data-l="en">© 2026 EasySwingPick · <a href="/about">About</a> · <a href="/disclosure">Affiliate disclosure</a> · <a href="/privacy">Privacy</a> · <a href="/contact">Contact</a></span></footer>
<script>document.getElementById("langT").onclick=e=>{{const b=e.target.closest("button");if(!b)return;document.documentElement.lang=b.dataset.lang;document.querySelectorAll("#langT button").forEach(x=>x.classList.toggle("on",x===b));}};</script>
</body></html>'''
    open(f"{OUT}/{slug}.html", "w").write(page)

UPD_KO = "최종 업데이트: 2026년 11월"; UPD_EN = "Last updated: November 2026"
M = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

info("about", "소개", "About",
 f"""<p>EasySwingPick은 <b>내 스윙에 맞는 골프채를 쉽게 찾도록</b> 돕는 한·영 골프 장비 가이드입니다. 미국에 사는 한인 골퍼, 그리고 시니어 골퍼를 위해 만들었습니다.</p>
<h2>무엇을 하나요</h2><ul class="check"><li><b>추천 계산기</b> — 드라이버·아이언·웨지·퍼터 계산기에 거리와 키 같은 기본 정보만 넣으면 헤드스피드를 추정하고 맞는 모델과 샤프트를 이유와 함께 추천합니다.</li>
<li><b>장비 분석</b> — 2026년 최신 모델의 장단점, 브랜드 비교, 세팅 가이드를 공개 리뷰·테스트 자료를 바탕으로 정리합니다.</li>
<li><b>한국어 정보</b> — 일본 브랜드(XXIO, Honma, Mizuno, Miura 등)와 미국 구매 방법처럼 한국어 자료가 부족한 주제를 다룹니다.</li></ul>
<h2>콘텐츠 원칙</h2><ul class="check"><li>모든 분석 글에 출처를 표시합니다.</li><li>확인되지 않은 가격·사양은 "확인 필요"로 표시합니다.</li><li>제휴 수수료 여부와 관계없이 추천합니다. 자세한 내용은 <a href="/disclosure">제휴 링크 고지</a>를 확인하세요.</li><li>계산기 결과는 일반적인 기준에 따른 추정치이며, 실제 피팅을 대신하지 않습니다.</li></ul>
<h2>연락처</h2><p>제안, 정정 요청, 제휴 문의는 {M}로 보내주세요.</p>""",
 f"""<p>EasySwingPick is a bilingual (Korean/English) golf equipment guide that helps golfers <b>find clubs that fit their swing</b>. It's built for Korean-American golfers in the US and for senior golfers.</p>
<h2>What we do</h2><ul class="check"><li><b>Fitting calculators</b> — Enter basic info like distance and height in our driver, iron, wedge and putter calculators for an estimated swing speed and model and shaft picks, with reasons.</li>
<li><b>Gear analysis</b> — Pros and cons of 2026 models, brand comparisons and setup guides, based on published reviews and testing.</li>
<li><b>Korean-language coverage</b> — Topics like Japanese brands (XXIO, Honma, Mizuno, Miura) and buying in the US.</li></ul>
<h2>Our principles</h2><ul class="check"><li>Every analysis cites its sources.</li><li>Unverified prices and specs are marked "TBC".</li><li>Recommendations are made regardless of commissions — see our <a href="/disclosure">affiliate disclosure</a>.</li><li>Calculator results are estimates based on general guidelines and don't replace a professional fitting.</li></ul>
<h2>Contact</h2><p>Suggestions, corrections and partnership inquiries: {M}</p>""")

info("disclosure", "제휴 링크 고지", "Affiliate Disclosure",
 f"""<p class="meta" style="color:var(--muted)">{UPD_KO}</p>
<p>EasySwingPick은 제휴(어필리에이트) 마케팅 프로그램에 참여하고 있습니다. 이 사이트의 일부 링크를 통해 제품을 구매하시면, <b>구매자에게 추가 비용 없이</b> 저희가 소정의 수수료를 받을 수 있습니다.</p>
<h2>현재 참여 중인 프로그램</h2><ul class="check"><li><b>2nd Swing Golf</b> — Awin 제휴 네트워크를 통해 참여합니다. 계산기 결과와 글의 "가격 보기" 버튼이 이 링크입니다.</li></ul><p>새 프로그램에 참여하면 이 목록에 추가하고 최종 업데이트 날짜를 고칩니다.</p>
<h2>추천 원칙</h2><ul class="check"><li>수수료는 어떤 제품을 추천할지, 순위를 어떻게 매길지에 영향을 주지 않습니다.</li><li>제휴 프로그램이 없는 브랜드(예: L.A.B. Golf, Miura)도 똑같이 다룹니다.</li><li>제휴 링크가 있는 글에는 링크 근처에 고지를 표시합니다.</li></ul>
<p>이 고지는 미국 연방거래위원회(FTC)의 추천·후기 가이드에 따라 작성했습니다. 질문은 {M}로 보내주세요.</p>""",
 f"""<p class="meta" style="color:var(--muted)">{UPD_EN}</p>
<p>EasySwingPick participates in affiliate marketing programs. When you buy through some links on this site, we may earn a small commission <b>at no extra cost to you</b>.</p>
<h2>Programs we currently participate in</h2><ul class="check"><li><b>2nd Swing Golf</b> — through the Awin affiliate network. The "Check price" buttons in calculator results and posts use these links.</li></ul><p>When we join a new program, we add it here and update the date above.</p>
<h2>How we recommend</h2><ul class="check"><li>Commissions never decide which products we recommend or how we rank them.</li><li>Brands without affiliate programs (e.g., L.A.B. Golf, Miura) get the same coverage.</li><li>Posts with affiliate links show a disclosure near those links.</li></ul>
<p>This disclosure follows the US Federal Trade Commission's Endorsement Guides. Questions: {M}</p>""")

info("privacy", "개인정보처리방침", "Privacy Policy",
 f"""<p class="meta" style="color:var(--muted)">{UPD_KO}</p>
<h2>1. 수집하는 정보</h2><ul class="check"><li><b>계산기 입력값</b>(키, 몸무게, 거리 등)은 브라우저 안에서만 계산되며 서버로 전송되거나 저장되지 않습니다.</li>
<li><b>방문 통계</b>: 사이트 개선을 위해 쿠키를 쓰지 않는 방문 통계(예: Cloudflare Web Analytics)를 사용할 수 있습니다. 개인을 식별하지 않는 페이지 조회 수 등만 집계됩니다.</li>
<li><b>이메일 문의</b>: 이메일을 보내시면 답변을 위해 이메일 주소와 내용을 보관합니다.</li></ul>
<h2>2. 제3자 서비스</h2><ul class="check"><li><b>제휴 링크</b>: 제휴 링크를 클릭하면 해당 판매처나 제휴 네트워크(현재 Awin과 2nd Swing Golf)가 구매 추적을 위해 자체 쿠키를 사용할 수 있습니다. 해당 회사의 개인정보처리방침이 적용됩니다.</li>
<li><b>글꼴</b>: Google Fonts를 사용하며, 글꼴을 불러올 때 IP 주소 등이 Google에 전달될 수 있습니다.</li>
<li><b>호스팅</b>: 사이트는 Cloudflare에서 호스팅되며, 보안과 운영을 위해 기본 접속 기록이 처리될 수 있습니다.</li></ul>
<h2>3. 판매하지 않습니다</h2><p>EasySwingPick은 개인정보를 판매하거나 공유하지 않습니다.</p>
<h2>4. 캘리포니아 거주자</h2><p>캘리포니아 소비자 개인정보 보호법(CCPA/CPRA)에 따라 수집된 정보의 열람·삭제를 요청할 수 있습니다. {M}로 요청해 주세요.</p>
<h2>5. 어린이</h2><p>이 사이트는 13세 미만 어린이를 대상으로 하지 않으며, 어린이의 정보를 고의로 수집하지 않습니다.</p>
<h2>6. 변경</h2><p>이 방침이 바뀌면 이 페이지에 게시하고 최종 업데이트 날짜를 수정합니다.</p>
<h2>7. 문의</h2><p>{M}</p>""",
 f"""<p class="meta" style="color:var(--muted)">{UPD_EN}</p>
<h2>1. Information we collect</h2><ul class="check"><li><b>Calculator inputs</b> (height, weight, distances) are processed in your browser only and are never sent to or stored on a server.</li>
<li><b>Analytics</b>: We may use cookieless analytics (e.g., Cloudflare Web Analytics) that count page views without identifying you.</li>
<li><b>Email</b>: If you email us, we keep your address and message to reply.</li></ul>
<h2>2. Third-party services</h2><ul class="check"><li><b>Affiliate links</b>: Retailers and affiliate networks (currently Awin and 2nd Swing Golf) may set their own cookies to track purchases. Their privacy policies apply.</li>
<li><b>Fonts</b>: We use Google Fonts; loading them may send your IP address to Google.</li>
<li><b>Hosting</b>: The site is hosted on Cloudflare, which may process basic access logs for security and operations.</li></ul>
<h2>3. We don't sell your data</h2><p>EasySwingPick does not sell or share personal information.</p>
<h2>4. California residents</h2><p>Under the CCPA/CPRA you may request access to or deletion of information we hold. Email {M}.</p>
<h2>5. Children</h2><p>This site is not directed to children under 13, and we don't knowingly collect their information.</p>
<h2>6. Changes</h2><p>We'll post any changes on this page and update the date above.</p>
<h2>7. Contact</h2><p>{M}</p>""")

info("contact", "문의", "Contact",
 f"""<p>EasySwingPick에 대한 제안, 정보 정정 요청, 브랜드·제휴 문의를 환영합니다.</p>
<div class="note"><b>이메일</b> {M}</div><p>보통 2~3 영업일 안에 답변드립니다. 한국어와 영어 모두 가능합니다.</p>
<p>개인 맞춤 피팅이 궁금하시면 먼저 <a href="/driver/">드라이버</a>·<a href="/iron/">아이언</a>·<a href="/wedge/">웨지</a>·<a href="/putter/">퍼터</a> 계산기를 사용해 보세요.</p>""",
 f"""<p>We welcome suggestions, corrections, and brand or partnership inquiries.</p>
<div class="note"><b>Email</b> {M}</div><p>We usually reply within 2–3 business days, in Korean or English.</p>
<p>Curious about your fit? Try our <a href="/driver/">driver</a>, <a href="/iron/">iron</a>, <a href="/wedge/">wedge</a> and <a href="/putter/">putter</a> calculators first.</p>""")

info("404", "페이지를 찾을 수 없습니다", "Page not found",
 '<p>주소가 바뀌었거나 없는 페이지입니다. <a href="/">홈으로 가기</a></p>',
 '<p>This page has moved or doesn\'t exist. <a href="/">Go home</a></p>')


# ---------- blog index (/blog/) ----------
import json as _json
import html as _html_mod
src = open(f"{H}/site/index.html").read()
P = []
# registry entries use either an old artifact link or the final /blog/<slug> path (newer posts)
for m in re.finditer(r'\{u:"(?:https://claude.ai/artifact/([A-Za-z0-9]+)|/blog/([a-z0-9-]+))",cat:"(\w+)",ko:"([^"]*)",en:"([^"]*)",dko:"([^"]*)",den:"([^"]*)",c:"(#[0-9a-fA-F]+)"\}', src):
    k, slug, cat, ko, en, dko, den, c = m.groups()
    P.append(dict(u=f"/blog/{POSTF[k] if k else slug}", cat=cat, ko=ko, en=en, dko=dko, den=den, c=c))
assert sorted(p["u"][6:] for p in P) == sorted(SLUGS), ("POSTS registry and site/blog-*.html differ", sorted(p["u"][6:] for p in P), sorted(SLUGS))
CN = {"ko": {"all": "전체", "gear": "장비 분석", "setup": "세팅 가이드", "jp": "일본채", "senior": "시니어", "buy": "구매 가이드", "putter": "퍼터"},
      "en": {"all": "All", "gear": "Gear", "setup": "Setup", "jp": "Japanese", "senior": "Seniors", "buy": "Buying", "putter": "Putters"}}
cats = ["all"] + [c for c in CN["ko"] if c != "all" and any(p["cat"] == c for p in P)]
BCSS = """<style>.chips{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 20px}.chips a{border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-weight:700;font-size:.88rem;color:var(--navy);text-decoration:none}
.chips a.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.bl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.bp{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;background:#fff}
.bp .th{height:86px;display:flex;align-items:flex-end;padding:12px}.bp .th span{background:rgba(255,255,255,.92);color:var(--navy);font-size:.72rem;font-weight:700;border-radius:6px;padding:3px 8px}
.bp .bd{padding:14px 16px 16px}.bp h3{margin:0 0 6px;font-size:1rem;line-height:1.45;overflow-wrap:anywhere}.bp p{margin:0;color:var(--muted);font-size:.86rem;overflow-wrap:anywhere}
@media(max-width:640px){.bl{grid-template-columns:1fr}}</style>"""
BJS = "<script>const BP=" + _json.dumps(P, ensure_ascii=False) + ",CN=" + _json.dumps(CN, ensure_ascii=False) + ",CATS=" + _json.dumps(cats) + """;
function L(){return document.documentElement.lang==="en"?"en":"ko";}
function cur(){const c=new URLSearchParams(location.search).get("c");return CATS.includes(c)?c:"all";}
function draw(){const l=L(),c=cur();
 document.querySelectorAll(".chipsbox").forEach(b=>b.innerHTML=CATS.map(x=>`<a href="?c=${x}" class="${x===c?"on":""}" data-c="${x}">${CN[l][x]}</a>`).join(""));
 const list=BP.filter(p=>c==="all"||p.cat===c);
 document.querySelectorAll(".blbox").forEach(b=>b.innerHTML=list.map(p=>`<a class="bp" href="${p.u}"><div class="th" style="background:linear-gradient(140deg,${p.c},#0a1c29)"><span>${CN[l][p.cat]}</span></div><div class="bd"><h3>${l==="en"?p.en:p.ko}</h3><p>${l==="en"?p.den:p.dko}</p></div></a>`).join(""));
 document.querySelectorAll(".chipsbox a").forEach(a=>a.onclick=e=>{e.preventDefault();history.replaceState(null,"","?c="+a.dataset.c);draw();});}
document.getElementById("langT").addEventListener("click",()=>setTimeout(draw,0));draw();</script>"""
info("blog/index", "전체 글", "All posts",
     BCSS + '<p>골프채 비교·추천·세팅 가이드를 한 곳에 모았습니다.</p><div class="chips chipsbox"></div><div class="bl blbox"></div>',
     '<p>All our club comparisons, picks and setup guides in one place.</p><div class="chips chipsbox"></div><div class="bl blbox"></div>')
b = open(f"{OUT}/blog/index.html").read().replace(f'{DOMAIN}/blog/index"', f'{DOMAIN}/blog/"').replace("</body>", BJS + "\n</body>", 1)
# Pre-render the post cards into the HTML so search engines see real <a href> links (the script still redraws them
# for filters and language switching; visitors see no difference).
_e = _html_mod.escape
def _card(p):
    return (f'<a class="bp" href="{p["u"]}"><div class="th" style="background:linear-gradient(140deg,{p["c"]},#0a1c29)">'
            f'<span><span data-l="ko">{_e(CN["ko"][p["cat"]])}</span><span data-l="en">{_e(CN["en"][p["cat"]])}</span></span></div>'
            f'<div class="bd"><h3><span data-l="ko">{_e(p["ko"])}</span><span data-l="en">{_e(p["en"])}</span></h3>'
            f'<p><span data-l="ko">{_e(p["dko"])}</span><span data-l="en">{_e(p["den"])}</span></p></div></a>')
_chips = "".join(f'<a href="?c={x}" class="{"on" if x=="all" else ""}" data-c="{x}"><span data-l="ko">{CN["ko"][x]}</span><span data-l="en">{CN["en"][x]}</span></a>' for x in cats)
assert b.count('<div class="bl blbox"></div>') == 2 and b.count('<div class="chips chipsbox"></div>') == 2
b = b.replace('<div class="bl blbox"></div>', '<div class="bl blbox">' + "".join(_card(p) for p in P) + '</div>')
b = b.replace('<div class="chips chipsbox"></div>', '<div class="chips chipsbox">' + _chips + '</div>')
open(f"{OUT}/blog/index.html", "w").write(b)
# Homepage "latest guides": same idea, newest 6 in English (the default language); the script redraws in the visitor's language
_home = open(f"{OUT}/index.html").read()
_HCAT = {"deal": "Deals", "jp": "Japanese", "senior": "Seniors", "buy": "Buying", "putter": "Putters", "gear": "Gear", "setup": "Setup"}
_hc = "".join(f'<a class="post" href="{p["u"]}"><div class="th" style="background:linear-gradient(140deg,{p["c"]},#0a1c29)"><span>{_HCAT.get(p["cat"], p["cat"])}</span></div>'
              f'<div class="bd"><h4>{_e(p["en"])}</h4><p>{_e(p["den"])}</p><div class="meta"><span>EasySwingPick</span><span class="soon">Read →</span></div></div></a>' for p in P[:6])
assert _home.count('<div class="posts" id="postGrid"></div>') == 1
open(f"{OUT}/index.html", "w").write(_home.replace('<div class="posts" id="postGrid"></div>', '<div class="posts" id="postGrid">' + _hc + '</div>'))

# ---------- robots / sitemap ----------
today = datetime.date.today().isoformat()
urls = ["/", "/blog/", "/driver/", "/iron/", "/wedge/", "/putter/", "/about", "/disclosure", "/privacy", "/contact"] + [f"/blog/{v}" for v in SLUGS]
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("built", sum(len(f) for _, _, f in os.walk(OUT)), "files")


# ---------- Pinterest: pin images + RSS feed (/feed.xml) ----------
# Pinterest "Auto-publish" reads /feed.xml and turns each new post into a pin (image = pin A).
# Pins B and C go into deploy/pins.csv for Pinterest "Bulk create Pins" (upload once a month).
# Pin PNGs are cached in site/pins/ and only re-rendered when the post text or PIN_VER changes.
import hashlib, subprocess as _sp2, glob as _glob, csv as _csv, html as _html
from email.utils import format_datetime as _fmtdt
PIN_VER = "2"
PIN_PHOTO = {"gear": "hero", "setup": "c-driver", "senior": "g-senior", "buy": "g-buy", "jp": "g-jp", "putter": "g-putter"}
PIN_BOARD = {"gear": "Golf Club Reviews", "setup": "Golf Fitting Tips", "senior": "Senior Golf Gear",
             "buy": "Golf Gear Deals & Gifts", "jp": "Japanese Golf Clubs", "putter": "Putters & Putting"}
PIN_TAG = {"gear": "CLUB REVIEW", "setup": "FITTING GUIDE", "senior": "FOR SENIOR GOLFERS", "buy": "BUYING GUIDE", "jp": "JAPANESE CLUBS", "putter": "PUTTER GUIDE"}
PIN_CTA = {"gear": "Find your driver in 1 minute", "setup": "Free driver fitting calculator", "senior": "Free fitting calculator for slower swings",
           "buy": "Free club fitting calculator", "jp": "Free club fitting calculator", "putter": "Free putter fitting calculator"}
PD = f"{H}/site/pins"; os.makedirs(PD, exist_ok=True); os.makedirs(f"{OUT}/assets/pins", exist_ok=True)
PIN_CSS = """*{box-sizing:border-box}body{margin:0;width:1000px;height:1500px;font-family:Inter,'Noto Sans',sans-serif;overflow:hidden}
.wm{height:64px;width:auto;display:block;align-self:flex-start}.tag{display:inline-block;font-weight:800;letter-spacing:3px;font-size:26px;padding:10px 20px;border-radius:8px}
h1{font-weight:800;letter-spacing:-1.5px;line-height:1.12;margin:0}.d{font-size:34px;line-height:1.4;margin:0}
.cta{display:inline-block;font-weight:800;font-size:32px;padding:20px 32px;border-radius:999px}.url{font-weight:700;font-size:30px;letter-spacing:1px}"""
PIN_FIT = """<script>(function(){var h=document.querySelector('h1'),box=document.querySelector('.fit'),s=parseInt(getComputedStyle(h).fontSize);
while(box.scrollHeight>box.clientHeight&&s>40){s-=3;h.style.fontSize=s+'px';}})();</script>"""
def _pin_html(style, p, photo):
    t, d, tag, cta = _html.escape(p["en"]), _html.escape(p["den"]), PIN_TAG[p["cat"]], PIN_CTA[p["cat"]]
    wm, wmd = f"file://{H}/logo/wordmark-og.svg", f"file://{H}/logo/wordmark.svg"
    if style == "a":   # photo on top, navy panel with title
        body = f"""<div style="height:640px;background:url('{photo}') center/cover"></div>
<div style="height:860px;background:{p['c']};background:linear-gradient(160deg,{p['c']},#0a1c29 75%);color:#fff;padding:56px 64px;display:flex;flex-direction:column;gap:30px">
<span class="tag" style="background:#e3c06a;color:#0a1c29;align-self:flex-start">{tag}</span>
<div class="fit" style="flex:1;overflow:hidden;display:flex;flex-direction:column;gap:26px"><h1 style="font-size:78px">{t}</h1><p class="d" style="opacity:.85">{d}</p></div>
<div style="display:flex;justify-content:space-between;align-items:center"><img class="wm" src="{wm}"><span class="url" style="color:#e3c06a">easyswingpick.com</span></div></div>"""
    elif style == "b":  # bold navy, big title, calculator CTA
        body = f"""<div style="height:1500px;background:radial-gradient(120% 90% at 90% 0%,#21506d 0%,#0f2a3d 55%,#0a1c29 100%);color:#fff;padding:90px 72px;display:flex;flex-direction:column;gap:40px">
<img class="wm" src="{wm}" style="height:72px"><span class="tag" style="border:3px solid #e3c06a;color:#e3c06a;align-self:flex-start">{tag}</span>
<div class="fit" style="flex:1;overflow:hidden;display:flex;flex-direction:column;justify-content:center;gap:34px"><h1 style="font-size:96px">{t}</h1>
<div style="width:120px;height:10px;background:#5fd3a2;border-radius:5px"></div><p class="d" style="opacity:.85;font-size:38px">{d}</p></div>
<span class="cta" style="background:#5fd3a2;color:#0a1c29;align-self:flex-start">{cta} →</span><span class="url" style="opacity:.7">easyswingpick.com</span></div>"""
    else:               # light card, photo band at bottom
        body = f"""<div style="height:1500px;background:#f6f3ea;color:#0f2a3d;display:flex;flex-direction:column">
<div style="padding:80px 72px 40px;flex:1;display:flex;flex-direction:column;gap:34px;min-height:0">
<span style="align-self:flex-start;background:#0f2a3d;border-radius:12px;padding:16px 22px;display:flex"><img class="wm" src="{wm}" style="height:56px"></span><span class="tag" style="background:#0f2a3d;color:#fff;align-self:flex-start">{tag}</span>
<div class="fit" style="flex:1;overflow:hidden;display:flex;flex-direction:column;gap:28px"><h1 style="font-size:86px;color:#0f2a3d">{t}</h1><p class="d" style="color:#4b5b68">{d}</p></div>
<span class="cta" style="background:#0f2a3d;color:#fff;align-self:flex-start">Read the guide →</span></div>
<div style="height:470px;background:url('{photo}') center/cover;position:relative"><span class="url" style="position:absolute;right:40px;bottom:30px;background:#e3c06a;color:#0a1c29;padding:10px 20px;border-radius:8px">easyswingpick.com</span></div></div>"""
    return f"<html><head><meta charset='utf-8'><style>{PIN_CSS}</style></head><body>{body}{PIN_FIT}</body></html>"
def _pin_jpg(png, jpg):
    from PIL import Image
    Image.open(png).convert("RGB").save(jpg, "JPEG", quality=86, optimize=True, progressive=True); os.remove(png)
def _added(slug):
    r = _sp2.run(["git", "-C", H, "log", "--diff-filter=A", "--format=%aI", "--", f"site/blog-{slug}.html"], capture_output=True, text=True).stdout.split()
    return datetime.datetime.fromisoformat(r[-1]) if r else datetime.datetime.now(datetime.timezone.utc)
rendered = 0
for p in P:
    slug = p["u"][6:]
    key = hashlib.sha1(("|".join([PIN_VER, p["en"], p["den"], p["cat"], p["c"]])).encode()).hexdigest()[:12]
    stamp = f"{PD}/{slug}.key"
    have = all(os.path.exists(f"{PD}/{slug}-{x}.jpg") for x in "abc")
    if not (have and os.path.exists(stamp) and open(stamp).read().strip() == key):
        photo = f"file://{H}/site/img/{PIN_PHOTO[p['cat']]}.webp"
        for x in "abc":
            tmp = f"{PD}/_t.html"; open(tmp, "w").write(_pin_html(x, p, photo))
            _sp2.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--window-size=1000,1500",
                      "--virtual-time-budget=3000", f"--screenshot={PD}/_t.png", f"file://{tmp}"], capture_output=True)
            _pin_jpg(f"{PD}/_t.png", f"{PD}/{slug}-{x}.jpg"); os.remove(tmp)
        open(stamp, "w").write(key + "\n"); rendered += 1
    for x in "abc": shutil.copy(f"{PD}/{slug}-{x}.jpg", f"{OUT}/assets/pins/{slug}-{x}.jpg")
    p["_date"] = _added(slug)
_keep = {f"{q['u'][6:]}{e}" for q in P for e in ("-a.jpg", "-b.jpg", "-c.jpg", ".key")}
for f in _glob.glob(f"{PD}/*"):   # drop pins of removed posts
    if os.path.basename(f) not in _keep: os.remove(f)
x = lambda v: _html.escape(v, quote=True)
items = []
for p in sorted(P, key=lambda q: q["_date"], reverse=True):
    slug = p["u"][6:]; img = f"{DOMAIN}/assets/pins/{slug}-a.jpg"; size = os.path.getsize(f"{OUT}/assets/pins/{slug}-a.jpg")
    items.append(f"""<item><title>{x(p['en'])}</title><link>{DOMAIN}{p['u']}</link><guid isPermaLink="true">{DOMAIN}{p['u']}</guid>
<pubDate>{_fmtdt(p['_date'])}</pubDate><category>{x(PIN_BOARD[p['cat']])}</category>
<description>{x(p['den'] + ' ' + PIN_CTA[p['cat']] + ' at EasySwingPick.')}</description>
<enclosure url="{img}" length="{size}" type="image/jpeg"/><media:content url="{img}" medium="image" type="image/jpeg" width="1000" height="1500"/></item>""")
open(f"{OUT}/feed.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<title>EasySwingPick — Golf Club Guides</title><link>{DOMAIN}/blog/</link><atom:link href="{DOMAIN}/feed.xml" rel="self" type="application/rss+xml"/>
<description>Golf club comparisons, buying guides and fitting tips for senior and Korean-American golfers.</description><language>en-us</language>
<lastBuildDate>{_fmtdt(datetime.datetime.now(datetime.timezone.utc))}</lastBuildDate>
{chr(10).join(items)}
</channel></rss>
""")
# extra pins (B, C) for Pinterest Bulk create: scheduled 7 and 14 days after the post, 10:00 Pacific (18:00 UTC)
with open(f"{OUT}/pins.csv", "w", newline="", encoding="utf-8") as fh:
    w = _csv.writer(fh); w.writerow(["Title", "Media URL", "Pinterest board", "Thumbnail", "Description", "Link", "Publish date", "Keywords"])
    # at most one extra pin per day: each pin goes on its target day (post +7 / +14 days) or the next free day after it
    _last = datetime.datetime.now(datetime.timezone.utc).replace(hour=18, minute=0, second=0, microsecond=0)
    want = list(((p["_date"] + datetime.timedelta(days=days)).astimezone(datetime.timezone.utc).replace(hour=18, minute=0, second=0, microsecond=0), p, k)
                  for p in P for k, days in (("b", 7), ("c", 14)))
    for when, p, k in sorted(want, key=lambda r: (r[0], r[1]["u"], r[2])):
        when = max(when, _last + datetime.timedelta(days=1)); _last = when; slug = p["u"][6:]
        w.writerow([p["en"][:100], f"{DOMAIN}/assets/pins/{slug}-{k}.jpg", PIN_BOARD[p["cat"]], "", (p["den"] + " " + PIN_CTA[p["cat"]] + ".")[:500],
                    f"{DOMAIN}{p['u']}", when.strftime("%Y-%m-%dT%H:%M:%S"), "golf clubs, golf equipment, " + PIN_BOARD[p["cat"]].lower()])
for f in (f"{OUT}/index.html", f"{OUT}/blog/index.html"):
    s_ = open(f).read(); open(f, "w").write(s_.replace("</head>", f'<link rel="alternate" type="application/rss+xml" title="EasySwingPick" href="{DOMAIN}/feed.xml">\n</head>', 1))
# Pinterest website claim (Settings > Claimed accounts > Websites) — keep on the homepage
PIN_VERIFY = "06fbd72d4027a8ccd471db19e4500c61"
_h = open(f"{OUT}/index.html").read()
open(f"{OUT}/index.html", "w").write(_h.replace("</head>", f'<meta name="p:domain_verify" content="{PIN_VERIFY}"/>\n</head>', 1))
print(f"pins ok ({rendered} rendered, {len(P)} posts) · feed.xml · pins.csv")


# ---------- header wordmark (A) ----------
WM = '<img src="/assets/wordmark.svg" height="{h}" alt="EasySwingPick" style="display:block;height:{h}px;width:auto">'
for d, _, fs in os.walk(OUT):
    for f in fs:
        if not f.endswith(".html"): continue
        p = os.path.join(d, f); s = open(p).read(); o = s
        s = re.sub(r'<img src="/assets/logo.svg" width="34" height="34" alt="" style="border-radius:8px">\s*<div>[^<]*<small data-t="\w+"></small></div>', WM.format(h=38), s)
        s = re.sub(r'<img src="/assets/logo.svg" width="30" height="30" alt="" style="border-radius:7px">(<span>)?EasySwingPick(</span>)?', WM.format(h=36), s)
        s = s.replace('</head>', '<style>@media(max-width:420px){img[src="/assets/wordmark.svg"]{height:30px!important}}</style></head>', 1)
        if s != o: open(p, "w").write(s)
        else: print("no header logo:", p)

# ---------- affiliate links (Awin -> 2nd Swing, publisher 3153241) ----------
# clickref tells us in Awin reports which page earned the click: "calc-driver", "blog-honma-miura", ...
AWIN_BASE = "https://www.awin1.com/cread.php?awinmid=95935&awinaffid=3153241"
AWIN = AWIN_BASE + "&ued="
SEARCH = "https://www.2ndswing.com/catalogsearch/result/?q="
import urllib.parse as _up
def aff(q, ref=""): return AWIN_BASE + (f"&clickref={ref}" if ref else "") + "&ued=" + _up.quote(SEARCH + _up.quote_plus(q), safe="")
BUY_KO, BUY_EN = "2nd Swing에서 가격 보기", "Check price at 2nd Swing"
def AFF_JS(ref): return ('<script>window.AFF=function(q){return "' + AWIN_BASE + '&clickref=' + ref + '&ued="+encodeURIComponent("' + SEARCH + '"+encodeURIComponent(q).replace(/%20/g,"+"))};</script>')
for calc in ("driver", "iron", "wedge", "putter"):
    p = f"{OUT}/{calc}/index.html"; s = open(p).read()
    s = s.replace('<a class="buy" href="#" onclick="return false">${t.buy}</a>',
                  '<a class="buy" href="${AFF(m.b+\' \'+m.m)}" target="_blank" rel="sponsored noopener">${t.buy}</a>')
    s = re.sub(r'buy:"구매처 보기[^"]*"', f'buy:"{BUY_KO} →"', s)
    s = re.sub(r'buy:"See where to buy[^"]*"', f'buy:"{BUY_EN} →"', s)
    s = s.replace("buy links are not connected yet", "buy links go to 2nd Swing (affiliate)")
    s = s.replace("</head>", AFF_JS("calc-" + calc) + "</head>", 1)
    assert "AFF(m.b" in s, calc
    open(p, "w").write(s)
def _pc(m):
    blk = m.group(0); h = re.search(r"<h4>(.*?)</h4>", blk)
    if not h: return blk
    name = re.sub(r"<[^>]+>", "", h.group(1)).split("(")[0].strip()
    ko = "구매처 보기" in blk
    return re.sub(r'<a class="buy" href="#" onclick="return false">[^<]*</a>',
                  f'<a class="buy" href="{_html.escape(aff(name))}" target="_blank" rel="sponsored noopener">{BUY_KO if ko else BUY_EN} →</a>', blk)
import html as _html
PH = re.compile(r'<a class="buy" href="#" onclick="return false">([^<]*)</a>')
def _link_all(s, ref=""):
    out, last = [], 0
    for m in PH.finditer(s):
        before = s[max(0, m.start() - 4000):m.start()]
        hs = re.findall(r"<h[34]>(.*?)</h[34]>", before, re.S)
        if not hs: continue
        name = re.sub(r"<[^>]+>", "", hs[-1])
        name = re.split(r"\s*\(|\s+/\s*|\s*·", name)[0].strip()
        tail = before[before.rfind("<h"):] if "<h" in before else before
        br = re.findall(r'class="br">([^<]+)<', before[-1500:])
        if br and br[-1].lower() not in name.lower(): name = br[-1] + " " + name
        ko = "구매처" in m.group(1)
        out.append(s[last:m.start()] + f'<a class="buy" href="{_html.escape(aff(name, ref))}" target="_blank" rel="sponsored noopener">{BUY_KO if ko else BUY_EN} →</a>')
        last = m.end()
    return "".join(out) + s[last:]
DISC1_RE = re.compile(r'<p class="disc1">.*?</p>', re.S)
DISC_FULL_RE = re.compile(r'<div class="disc" id="disclosure"[^>]*>.*?</div>', re.S)
NO_AFF = []
for f in os.listdir(f"{OUT}/blog"):
    p = f"{OUT}/blog/{f}"; s = open(p).read()
    s2 = _link_all(s, "blog-" + f[:-5])
    # affiliate notice only where the post actually has an affiliate link
    if 'rel="sponsored' not in s2 and "awin1.com" not in s2:
        s3 = DISC_FULL_RE.sub("", DISC1_RE.sub("", s2))
        if s3 != s2: NO_AFF.append(f); s2 = s3
    if s2 != s: open(p, "w").write(s2)
if NO_AFF: print("no affiliate links -> disclosure removed:", ", ".join(sorted(NO_AFF)))

# ---------- default language: English first, remember the visitor's choice ----------
LANG_HEAD = '<script>try{document.documentElement.lang=localStorage.getItem("esp_lang")||"en"}catch(e){document.documentElement.lang="en"}</script>'
LANG_END = ('<script>(function(){var l="en";try{l=localStorage.getItem("esp_lang")||"en"}catch(e){}'
            'var t=document.getElementById("langT");if(!t)return;'
            'var b=t.querySelector(\'button[data-lang="\'+l+\'"]\');if(b&&!b.classList.contains("on"))b.click();'
            't.addEventListener("click",function(e){var x=e.target.closest("button");if(x)try{localStorage.setItem("esp_lang",x.dataset.lang)}catch(_){}});})();</script>')
for d, _, fs in os.walk(OUT):
    for f in fs:
        if not f.endswith(".html"): continue
        p = os.path.join(d, f); s = open(p).read()
        if 'id="langT"' not in s or "esp_lang" in s: continue
        s = s.replace("<head>", "<head>" + LANG_HEAD, 1)
        i = s.rfind("</body>"); s = s[:i] + LANG_END + s[i:]
        open(p, "w").write(s)

# ---------- PNG icons ----------
import subprocess
A = f"{OUT}/assets"
for n, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"), (512, "logo-512.png")]:
    open(f"{A}/t.html", "w").write(f"<html><body style='margin:0'><img src='logo.svg' width={n} height={n} style='display:block'></body></html>")
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--default-background-color=00000000",
                    "--hide-scrollbars", f"--window-size={n},{n}", f"--screenshot={A}/{name}", f"file://{A}/t.html"], capture_output=True)
os.remove(f"{A}/t.html")
print("icons ok")

# ---------- bilingual <title> / description for search ----------
SEO = {
 "index.html": ("EasySwingPick — Golf Club Fitting Calculators | 내 스윙에 맞는 골프채 찾기",
   "Free driver, iron, wedge and putter fitting calculators plus bilingual gear guides for Korean-American and senior golfers. 거리만 넣으면 드라이버·아이언·웨지·퍼터와 샤프트를 추천합니다."),
 "driver/index.html": ("Driver Fitting Calculator — Swing Speed & Shaft | 드라이버 추천 계산기 | EasySwingPick",
   "Enter your drive distance to estimate swing speed and get driver and shaft picks. 드라이버 거리만 넣으면 헤드스피드와 추천 드라이버·샤프트를 알려드립니다."),
 "iron/index.html": ("Iron Fitting Calculator — Head Type, Shaft, Length | 아이언 추천 계산기 | EasySwingPick",
   "Use your 7-iron carry to find iron head type, steel vs graphite, length and lie. 7번 아이언 거리로 헤드 종류, 샤프트, 길이·라이각을 추천합니다."),
 "wedge/index.html": ("Wedge Gapping & Bounce Calculator | 웨지 추천 계산기 | EasySwingPick",
   "Your PW loft sets wedge gapping, bounce and grind picks. PW 로프트로 웨지 간격, 바운스, 그라인드를 추천합니다."),
 "putter/index.html": ("Putter Fitting Calculator — Toe Hang & Zero Torque | 퍼터 추천 계산기 | EasySwingPick",
   "Match toe hang, zero-torque and head shape to your stroke. 스트로크 모양으로 토우행, 제로토크 여부, 헤드 모양을 찾습니다."),
 "blog/index.html": ("Golf Club Guides & Comparisons | 골프채 가이드 전체 글 | EasySwingPick",
   "All EasySwingPick club comparisons, buying guides and setup tips in English and Korean. 골프채 비교·추천·세팅 가이드 모음."),
 "about.html": ("About EasySwingPick | 소개", None),
 "disclosure.html": ("Affiliate Disclosure | 제휴 안내 | EasySwingPick", None),
 "privacy.html": ("Privacy Policy | 개인정보 처리방침 | EasySwingPick", None),
 "contact.html": ("Contact | 연락처 | EasySwingPick", None),
}
def _set(s, title, desc):
    s = re.sub(r"<title>.*?</title>", "<title>" + _html.escape(title, quote=False) + "</title>", s, count=1, flags=re.S)
    if desc:
        if '<meta name="description"' in s:
            s = re.sub(r'<meta name="description" content="[^"]*"', '<meta name="description" content="' + _html.escape(desc) + '"', s, count=1)
        else:
            s = s.replace("</title>", '</title><meta name="description" content="' + _html.escape(desc) + '">', 1)
    return s
for rel, (t, d) in SEO.items():
    p = f"{OUT}/{rel}"
    if os.path.exists(p):
        _s = _set(open(p).read(), t, d); open(p, "w").write(_s)
for f in os.listdir(f"{OUT}/blog"):
    if f == "index.html" or not f.endswith(".html"): continue
    p = f"{OUT}/blog/{f}"; s = open(p).read()
    ko = re.search(r'<div data-l="ko"><h1>(.*?)</h1>', s, re.S); en = re.search(r'<div data-l="en"><h1>(.*?)</h1><p class="sub">(.*?)</p>', s, re.S)
    strip = lambda x: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x)).replace(" +", " +").strip()
    if not (ko and en):
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        if len(h1) < 2: continue
        open(p, "w").write(_set(s, f"{strip(h1[1])} | {strip(h1[0])}", None)); continue
    dm = re.search(r'<meta name="description" content="([^"]*)"', s)
    desc = strip(en.group(2)) + " " + (_html.unescape(dm.group(1)) if dm else "")
    open(p, "w").write(_set(s, f"{strip(en.group(1))} | {strip(ko.group(1))}", desc[:320]))

# ---------- share previews (Open Graph) ----------
import html as _html
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,630",
                f"--screenshot={A}/og.png", f"file://{H}/logo/og.html"], capture_output=True)
DEF = "드라이버·아이언·웨지·퍼터 추천 계산기와 한·영 골프채 가이드"
for d, _, fs in os.walk(OUT):
    for f in fs:
        if not f.endswith(".html"): continue
        p = os.path.join(d, f); s = open(p).read()
        if 'property="og:title"' in s: continue
        t = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
        dm = re.search(r'<meta name="description" content="([^"]*)"', s)
        desc = dm.group(1) if dm else DEF
        rel = "/" + os.path.relpath(p, OUT).replace("\\", "/")
        rel = rel[:-10] if rel.endswith("/index.html") else rel[:-5]
        rel = rel or "/"
        tags = (f'<meta property="og:type" content="website"><meta property="og:site_name" content="EasySwingPick">'
                f'<meta property="og:title" content="{_html.escape(t, quote=True)}"><meta property="og:description" content="{desc}">'
                f'<meta property="og:url" content="{DOMAIN}{rel}"><meta property="og:image" content="{DOMAIN}/assets/og.png">'
                f'<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
                f'<meta property="og:locale" content="ko_KR"><meta property="og:locale:alternate" content="en_US">'
                f'<meta name="twitter:card" content="summary_large_image">')
        if not dm: tags = f'<meta name="description" content="{DEF}">' + tags
        open(p, "w").write(s.replace("</head>", tags + "\n</head>", 1))
print("og ok")

# ---------- structured data (JSON-LD) for search results: Article + breadcrumbs, calculators, organization ----------
import subprocess as _sp2
def _gitdate(path, first):
    try:
        out = _sp2.run(["git", "log", "--follow", "--format=%cI", "--", path], cwd=H, capture_output=True, text=True).stdout.split()
        return (out[-1] if first else out[0]) if out else None
    except Exception:
        return None
_NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
ORG = {"@type": "Organization", "@id": DOMAIN + "/#org", "name": "EasySwingPick", "url": DOMAIN + "/",
       "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/logo-512.png", "width": 512, "height": 512}}
def _ld(objs):
    return '<script type="application/ld+json">' + _json.dumps({"@context": "https://schema.org", "@graph": objs}, ensure_ascii=False).replace("</", "<\\/") + "</script>"
def _crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}
def _put(path, objs):
    f = f"{OUT}/{path}"; x = open(f).read()
    if "application/ld+json" in x: return
    open(f, "w").write(x.replace("</head>", _ld(objs) + "\n</head>", 1))
_put("index.html", [ORG, {"@type": "WebSite", "@id": DOMAIN + "/#site", "name": "EasySwingPick", "url": DOMAIN + "/",
                          "inLanguage": ["en", "ko"], "publisher": {"@id": DOMAIN + "/#org"}}])
for slug, name in [("driver", "Driver Fitting Calculator"), ("iron", "Iron Fitting Calculator"),
                   ("wedge", "Wedge Fitting Calculator"), ("putter", "Putter Fitting Calculator")]:
    u = f"{DOMAIN}/{slug}/"
    _put(f"{slug}/index.html", [{"@type": "WebApplication", "name": name, "url": u, "applicationCategory": "SportsApplication",
                                  "operatingSystem": "Any", "inLanguage": ["en", "ko"], "isAccessibleForFree": True,
                                  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "publisher": {"@id": DOMAIN + "/#org"}},
                                 _crumbs([("Home", DOMAIN + "/"), (name, u)]), ORG])
for p in P:
    slug = p["u"].split("/")[-1]; u = DOMAIN + p["u"]; src_f = f"site/blog-{slug}.html"
    pub = _gitdate(src_f, True) or _NOW; mod = _gitdate(src_f, False) or pub
    art = {"@type": "Article", "headline": p["en"][:110], "alternativeHeadline": p["ko"], "description": p["den"],
           "mainEntityOfPage": u, "url": u, "inLanguage": ["en", "ko"], "datePublished": pub, "dateModified": mod,
           "image": [f"{DOMAIN}/assets/pins/{slug}-a.jpg", DOMAIN + "/assets/og.png"],
           "author": {"@type": "Organization", "name": "EasySwingPick Editors", "url": DOMAIN + "/about"},
           "publisher": {"@id": DOMAIN + "/#org"}}
    _put(f"blog/{slug}.html", [art, _crumbs([("Home", DOMAIN + "/"), ("Blog", DOMAIN + "/blog/"), (p["en"][:110], u)]), ORG])
print("json-ld ok")

# ---- Calculator QA: every build re-runs ~1,700 scenarios + golden cases (qa/run.py).
# If anything looks wrong (reversed advice, text vs table mismatch, broken English page...) the build fails
# and must not be committed or published. Set SKIP_QA=1 only for layout-only work on non-calculator pages.
if os.environ.get("SKIP_QA") != "1":
    import subprocess as _sp, sys as _sys
    _r = _sp.run([_sys.executable, os.path.join(H, "qa", "run.py")])
    if _r.returncode:
        print("BUILD FAILED: calculator QA found problems (see above). Do not commit or publish."); _sys.exit(1)
