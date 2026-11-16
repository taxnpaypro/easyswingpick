import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import json, html
CSS = open(__import__('os').path.join(ROOT,'post_css.html')).read()
CALC = {
 "driver": "https://claude.ai/artifact/8qNVFjbmMa2iMgjhxoeWmA",
 "iron": "https://claude.ai/artifact/Dz35Q1crsGFwXLvyTx4swA",
 "putter": "https://claude.ai/artifact/YQSj4S2ynmVwf1edh6gM68",
}
HERO_BG = {
 "senior": "radial-gradient(120% 120% at 80% 0%,#3a5a1a 0%,#1d3a12 60%,#0d1f08 100%)",
 "jp": "radial-gradient(120% 120% at 80% 0%,#21506d 0%,#0f2a3d 60%,#0a1c29 100%)",
 "jp2": "radial-gradient(120% 120% at 80% 0%,#5a1a24 0%,#2b0d13 60%,#170609 100%)",
 "putter": "radial-gradient(120% 120% at 80% 0%,#6b4a12 0%,#3a2708 60%,#1f1504 100%)",
}

def buy(ko=True):
    return f'<a class="buy" href="#" onclick="return false">{"구매처 보기 (준비 중)" if ko else "Where to buy (coming soon)"}</a>'

def page(p):
    srcs = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a></li>' for t,u in p["sources"])
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title_ko"]} | EasySwingPick</title>
<meta name="description" content="{html.escape(p["desc_ko"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+KR:wght@400;500;700;800&display=swap" rel="stylesheet">
{CSS.replace('</style>', '.hero{background:'+HERO_BG[p["bg"]]+'}</style>')}
</head>
<body>
<header><div class="hd">
 <a class="logo" href="index.html"><svg width="30" height="30" viewBox="0 0 34 34" aria-hidden="true"><circle cx="17" cy="17" r="16" fill="#fff" opacity=".12"/><circle cx="17" cy="13" r="6" fill="#fff"/><path d="M17 19v9" stroke="#c89b3c" stroke-width="2.2" stroke-linecap="round"/></svg>EasySwingPick</a>
 <div class="lang" id="langT"><button data-lang="ko" class="on">한국어</button><button data-lang="en">EN</button></div>
</div></header>
<section class="hero"><div class="wrap">
 <div class="crumb"><a href="index.html">홈</a> › <span data-l="ko">{p["cat_ko"]}</span><span data-l="en">{p["cat_en"]}</span></div>
 <span class="cat"><span data-l="ko">{p["cat_ko"]}</span><span data-l="en">{p["cat_en"].upper()}</span></span>
 <div data-l="ko"><h1>{p["title_ko"]}</h1><p class="sub">{p["sub_ko"]}</p></div>
 <div data-l="en"><h1>{p["title_en"]}</h1><p class="sub">{p["sub_en"]}</p></div>
 <div class="meta">EasySwingPick · <span data-l="ko">2026년 11월</span><span data-l="en">November 2026</span></div>
</div></section>
<div class="wrap">
 <div class="disc"><span data-l="ko">이 글의 일부 링크는 제휴(어필리에이트) 링크로, 링크를 통해 구매하시면 수수료를 받을 수 있습니다. 추천 내용은 제휴 여부와 관계없이 작성했습니다.</span><span data-l="en">Some links in this post are affiliate links. We may earn a commission if you buy through them. Our picks are independent.</span></div>
<article data-l="ko">{p["body_ko"]}
 <div class="cta"><div><h3>{p["cta_ko"][0]}</h3><p>{p["cta_ko"][1]}</p></div><a href="{CALC[p["calc"]]}" target="_blank" rel="noopener">{p["cta_ko"][2]} →</a></div>
</article>
<article data-l="en">{p["body_en"]}
 <div class="cta"><div><h3>{p["cta_en"][0]}</h3><p>{p["cta_en"][1]}</p></div><a href="{CALC[p["calc"]]}" target="_blank" rel="noopener">{p["cta_en"][2]} →</a></div>
</article>
 <div class="src"><b data-l="ko">출처</b><b data-l="en">Sources</b><ol>{srcs}</ol></div>
</div>
<footer><span data-l="ko">© 2026 EasySwingPick · 상표는 각 소유자에게 있습니다. 가격은 작성 시점 공개 정보 기준이며 바뀔 수 있습니다.</span><span data-l="en">© 2026 EasySwingPick · Trademarks belong to their owners. Prices reflect public listings at the time of writing and may change.</span></footer>
<script>
document.getElementById("langT").onclick=e=>{{const b=e.target.closest("button");if(!b)return;document.documentElement.lang=b.dataset.lang;
 document.querySelectorAll("#langT button").forEach(x=>x.classList.toggle("on",x===b));document.title=b.dataset.lang==="ko"?{json.dumps(p["title_ko"]+" | EasySwingPick")}:{json.dumps(p["title_en"]+" | EasySwingPick")};}};
</script>
</body>
</html>'''

def tldr(title, items):
    return f'<div class="tldr"><b>{title}</b><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"

def table(head, rows):
    return '<div class="tw"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + '</tr></thead><tbody>' + \
        "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + '</tbody></table></div>'

def picks(items, ko=True):
    return '<div class="pick">' + "".join(f'<div class="pc"><div class="w">{w}</div><h4>{h}</h4><p>{t}</p>{buy(ko)}</div>' for w,h,t in items) + '</div>'

def check(items):
    return '<ul class="check">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

POSTS = []
# lightweight-drivers -> build_light_drivers.py, miura-vs-mizuno -> build_miura_mizuno.py (rewritten 2026-11-15)

# ---------------------------------------------------------------- Mizuno JPX vs Pro
POSTS.append(dict(
 file="blog-mizuno-jpx-vs-pro.html", bg="jp", calc="iron",
 cat_ko="일본채", cat_en="Japanese clubs",
 title_ko="Mizuno JPX vs Mizuno Pro 아이언, 내 핸디에 맞는 라인은?",
 title_en="Mizuno JPX vs Mizuno Pro irons: which line fits your handicap?",
 desc_ko="Mizuno JPX 925 Hot Metal·HL·Pro·Forged와 2026 Mizuno Pro M-13·M-15·S-1·S-3를 핸디캡별로 비교했습니다.",
 sub_ko="같은 Mizuno라도 JPX와 Pro는 대상이 완전히 다릅니다. 8개 모델을 핸디캡별로 정리했습니다.",
 sub_en="Same brand, very different golfers. Eight models sorted by handicap.",
 cta_ko=("내게 맞는 헤드 종류는?","7번 아이언 거리만 넣으면 헤드 종류와 샤프트가 나옵니다.","아이언 계산기 열기"),
 cta_en=("Which head type fits you?","Enter your 7-iron distance for head type and shaft.","Open the iron calculator"),
 body_ko=tldr("핵심 요약",[
   "<b style='display:inline;color:#fff'>JPX:</b> 거리와 관용성 중심. 핸디캡 15 이상이면 Hot Metal 또는 HL부터.",
   "<b style='display:inline;color:#fff'>Pro:</b> 단조 타감과 컨트롤 중심. 2026년 M-13·M-15가 새로 나왔습니다.",
   "<b style='display:inline;color:#fff'>중간 지대:</b> JPX 925 Forged와 Pro M-15가 두 라인 사이를 잇습니다."])+
  "<h2>JPX와 Pro, 무엇이 다를까</h2><p>Golfweek는 JPX 시리즈가 볼 스피드(거리)를, Mizuno Pro 계열은 반복 가능한 강한 스윙을 가진 골퍼를 위한 클래식 아이언을 지향한다고 정리했습니다. 쉽게 말해 <b>JPX는 '쉽고 멀리', Pro는 '정확하고 부드럽게'</b>입니다.</p>"
  "<h2>JPX 925 라인 (2025~)</h2><p>JPX 925는 Hot Metal, Hot Metal Pro, Hot Metal HL, Forged 네 모델로 구성됩니다.</p>"+table(["모델","대상","특징","가격(미국)"],[
   ["<b>Hot Metal HL</b>","느린~중간 스윙","라인에서 관용성이 가장 높고 로프트가 가장 약해 높이 띄우기 쉬움","약 $150/개"],
   ["<b>Hot Metal</b>","가장 넓은 골퍼층","GolfMagic은 핸디캡 15 이상에게 추천","약 $150/개"],
   ["<b>Hot Metal Pro</b>","관용성을 조금 원하는 상급자","라인에서 탑라인이 가장 얇고 오프셋이 가장 작음","약 $150/개"],
   ["<b>JPX 925 Forged</b>","중상급자","Hot Metal과 Pro 사이를 잇는 단조 아이언","확인 필요"]])+
  "<p>Golf.com에 따르면 Mizuno는 이번 겨울 새 JPX 아이언을 낼 가능성이 높습니다. 새 모델이 나오면 925 라인은 할인 폭이 커질 수 있어, 급하지 않다면 지켜볼 만합니다.</p>"
  "<h2>Mizuno Pro 라인 (2026)</h2>"+table(["모델","구분","특징","가격(미국)"],[
   ["<b>Pro M-15</b>","플레이어스 디스턴스","Pro 245의 후속. 중공 구조로 롱아이언도 높이 띄움","$215/개"],
   ["<b>Pro M-13</b>","플레이어스","Pro 243 후속. 롱아이언은 포켓 캐비티, 숏아이언은 원피스 단조","$215/개"],
   ["<b>Pro S-3</b>","플레이어스","스플릿 캐비티 머슬. 블레이드 모양에 약간의 관용성","확인 필요"],
   ["<b>Pro S-1</b>","블레이드","1025E 연철 한 덩어리로 만든 순수 머슬백","확인 필요"]])+
  "<h2>핸디캡별 추천</h2>"+table(["핸디캡","1순위","대안"],[
   ["20 이상 / 시니어","JPX 925 Hot Metal HL","JPX 925 Hot Metal"],["13~20","JPX 925 Hot Metal","Hot Metal Pro"],
   ["6~12","JPX 925 Hot Metal Pro 또는 Forged","Pro M-15"],["0~5","Pro M-13","Pro S-3"],["상급 볼 스트라이커","Pro S-1","Pro S-3"]])+
  "<h2>상황별 추천</h2>"+picks([("쉽게 멀리","JPX 925 Hot Metal HL","높이 띄우기 가장 쉬운 Mizuno 아이언."),("가성비 거리","JPX 925 Hot Metal Pro","개당 약 $150에 얇은 탑라인과 거리."),("단조 + 거리","Pro M-15","Mizuno Pro 타감에 중공 구조의 거리."),("타감 최우선","Pro M-13","단조 타감과 적당한 관용성.")])+
  "<div class='note'><b>Miura와 Mizuno, 단조 아이언끼리 비교하면?</b> <a href='/blog/miura-vs-mizuno'>Miura vs Mizuno 단조 아이언 비교</a>에서 만드는 방식, 로프트, 세트 가격을 숫자로 정리했습니다.</div><h2>구매 전 체크리스트</h2>"+check(["내 7번 아이언 거리와 헤드스피드를 알고 있나요? (아이언 계산기)","핸디캡보다 '평소 미스'를 기준으로 고르세요. 뒤땅·탑핑이 잦으면 관용성 모델.","Mizuno는 피팅 후 맞춤 주문이 일반적입니다.","새 JPX 출시 전후로 925 라인 할인을 확인하세요."]),
 body_en=tldr("QUICK TAKE",[
   "<b style='display:inline;color:#fff'>JPX:</b> distance and forgiveness. At 15+ handicap, start with Hot Metal or HL.",
   "<b style='display:inline;color:#fff'>Pro:</b> forged feel and control. New M-13 and M-15 arrived in 2026.",
   "<b style='display:inline;color:#fff'>The bridge:</b> JPX 925 Forged and Pro M-15 sit between the lines."])+
  "<h2>JPX vs Pro: the difference</h2><p>Golfweek sums it up: JPX chases ball speed, while the Mizuno Pro family serves golfers with repeatable, powerful swings who want classic irons. In short, <b>JPX is easy and long; Pro is precise and soft</b>.</p>"
  "<h2>The JPX 925 line</h2><p>JPX 925 includes four models: Hot Metal, Hot Metal Pro, Hot Metal HL and Forged.</p>"+table(["Model","For","Highlights","US price"],[
   ["<b>Hot Metal HL</b>","Slow to moderate speeds","Most forgiving, weakest lofts for height","About $150/club"],
   ["<b>Hot Metal</b>","The widest range of golfers","GolfMagic recommends it for 15+ handicaps","About $150/club"],
   ["<b>Hot Metal Pro</b>","Better players wanting help","Thinnest topline, least offset in the line","About $150/club"],
   ["<b>JPX 925 Forged</b>","Mid to low handicaps","Bridges Hot Metal and the Pro irons","TBC"]])+
  "<p>Golf.com expects new JPX irons this winter. If you're not in a hurry, the 925 line may see bigger discounts once they land.</p>"
  "<h2>The 2026 Mizuno Pro line</h2>"+table(["Model","Type","Highlights","US price"],[
   ["<b>Pro M-15</b>","Players distance","Successor to the Pro 245; hollow body launches long irons high","$215/club"],
   ["<b>Pro M-13</b>","Players","Successor to the Pro 243; pocket-cavity long irons, one-piece forged short irons","$215/club"],
   ["<b>Pro S-3</b>","Players","Split-cavity muscle; blade look with a hint of help","TBC"],
   ["<b>Pro S-1</b>","Blade","Pure muscle back forged from a single billet of 1025E","TBC"]])+
  "<h2>By handicap</h2>"+table(["Handicap","First pick","Alternative"],[
   ["20+ / seniors","JPX 925 Hot Metal HL","JPX 925 Hot Metal"],["13–20","JPX 925 Hot Metal","Hot Metal Pro"],
   ["6–12","Hot Metal Pro or JPX 925 Forged","Pro M-15"],["0–5","Pro M-13","Pro S-3"],["Elite ball strikers","Pro S-1","Pro S-3"]])+
  "<h2>Picks by situation</h2>"+picks([("EASY DISTANCE","JPX 925 Hot Metal HL","The easiest Mizuno iron to launch."),("VALUE DISTANCE","JPX 925 Hot Metal Pro","A thin topline and distance at about $150 a club."),("FORGED + DISTANCE","Pro M-15","Mizuno Pro feel with hollow-body distance."),("FEEL FIRST","Pro M-13","Forged feel with sensible forgiveness.")],ko=False)+
  "<div class='note'><b>Comparing Miura and Mizuno forged irons?</b> See <a href='/blog/miura-vs-mizuno'>Miura vs Mizuno forged irons</a> for how they're made, lofts and set prices.</div><h2>Checklist</h2>"+check(["Know your 7-iron distance and speed (iron calculator).","Choose by your usual miss, not just handicap — frequent fat or thin shots call for forgiveness.","Mizuno irons are usually custom-built after a fitting.","Watch for 925 discounts around the next JPX launch."]),
 sources=[("Golfweek via Yahoo — Mizuno Pro M-13, M-15","https://global.zph.com.cn/mizuno-pro-modern-series-irons-blend-forged-feel-with-modern-speed-11888.html"),
  ("GOLF.com — JPX 925 Forged and Hot Metal","https://golf.com/clubpage/mizuno-jpx-925-forged-hot-metal-irons-reviews-player-testing-2025/"),
  ("GOLF.com — JPX 925 line and pricing","https://golf.com/?p=15557349"),
  ("Golfweek via Yahoo — JPX 925 Hot Metal family","https://ca.sports.yahoo.com/news/mizuno-jpx-925-hot-metal-140020856.html"),
  ("GolfMagic — JPX 925 Hot Metal review","https://www.golfmagic.com/equipment/irons/mizuno-jpx-925-hot-metal-irons-review"),
  ("Plugged In Golf — JPX925 Forged review","https://pluggedingolf.com/mizuno-jpx925-forged-irons-review/"),
  ("GOLF.com — 2027 irons outlook","https://golf.com/gear/irons/after-what-ive-seen-tour-2027-irons-year/?amp=1"),
  ("MyGolfSpy — Mizuno Pro M-13 and M-15","https://mygolfspy.com/news-opinion/classically-modern-the-new-mizuno-pro-m-13-and-m-15-irons/"),
  ("Golf Reviews Guide — Mizuno Pro M-13 & M-15","https://golfreviewsguide.com/?p=109974"),
  ("Golf Monthly — Best Mizuno irons 2026","https://www.golfmonthly.com/best-golf-deals/best-mizuno-irons-164593"),
  ("The Golf Shop Online — Mizuno Pro buyer's guide","https://www.thegolfshoponline.co.uk/blog/?p=11002%2F")]))

# ---------------------------------------------------------------- Zero torque putters
POSTS.append(dict(
 file="blog-zero-torque-putters.html", bg="putter", calc="putter",
 cat_ko="퍼터", cat_en="Putters",
 title_ko="제로토크 퍼터 비교: L.A.B. vs Odyssey vs Spider ZT (2026)",
 title_en="Zero-torque putters compared: L.A.B. vs Odyssey vs Spider ZT (2026)",
 desc_ko="짧은 퍼트가 불안한 골퍼를 위한 2026 제로토크 퍼터 비교. L.A.B., Odyssey Square 2 Square, TaylorMade Spider ZT, Scotty Cameron.",
 sub_ko="짧은 퍼트에서 페이스가 돌아가 자꾸 빠진다면 제로토크 퍼터가 답일 수 있습니다. 2026년 주요 모델을 비교했습니다.",
 sub_en="If the face keeps rotating on short putts, zero torque may help. We compare 2026's main models.",
 cta_ko=("제로토크가 내게 맞을까?","스트로크 모양만 고르면 토우행과 헤드 모양을 추천합니다.","퍼터 계산기 열기"),
 cta_en=("Is zero torque right for you?","Pick your stroke type for toe hang and head picks.","Open the putter calculator"),
 body_ko=tldr("핵심 요약",[
   "<b style='display:inline;color:#fff'>테스트 1위:</b> Odyssey Ai-Dual Square 2 Square #7 (MyGolfSpy 2026)",
   "<b style='display:inline;color:#fff'>원조·인기:</b> L.A.B. Golf — 피팅 업체 판매 데이터에서 가장 큰 비중",
   "<b style='display:inline;color:#fff'>주의:</b> 강한 아크 스트로크에는 오히려 안 맞을 수 있습니다."])+
  "<h2>제로토크 퍼터란</h2><p>일반 퍼터는 스트로크 중에 헤드가 비틀리려는 힘(토크)이 생깁니다. 제로토크 퍼터는 샤프트 위치와 무게 배치를 바꿔 이 힘을 거의 없앤 퍼터입니다. 예를 들어 Odyssey는 Square 2 Square 라인이 센터 샤프트 설계로 토우가 위를 향하며 균형을 잡아 '제로토크' 범주에 든다고 설명합니다.</p>"
  "<h2>왜 지금 인기인가</h2><p>한 피팅 업체(Club Champion)에서는 올해 판매 데이터에서 제로토크 퍼터가 압도적이었고, 그중 L.A.B.가 가장 큰 비중이었다고 합니다. 같은 인터뷰에서 Odyssey는 전통 퍼터를 쓰던 골퍼도 쉽게 적응하도록 잘 만들었다는 평을 받았습니다.</p>"
  "<p>MyGolfSpy가 2026년 테스트한 모든 퍼터를 점수로 줄 세웠더니 상위 15개가 전부 제로토크였고, 전체 1위는 Odyssey Ai-Dual Square 2 Square #7이었습니다.</p>"
  "<h2>주요 모델 비교</h2>"+table(["모델","특징","가격(미국)","이런 분께"],[
   ["<b>Odyssey Ai-Dual Square 2 Square #7</b>","MyGolfSpy 2026 테스트 1위. 정렬선이 많은 말렛","$399.99 (출시가)","처음 제로토크를 써 보는 분"],
   ["<b>L.A.B. Golf DF3</b>","L.A.B. 기술이 가장 잘 드러나는 최고 안정성 모델","$449.99 (Golf Galaxy 정가)","짧은 퍼트가 가장 불안한 분"],
   ["<b>L.A.B. Golf Mezz.1 Max</b>","익숙한 말렛 모양의 L.A.B.","$499부터","L.A.B. 성능 + 익숙한 모양"],
   ["<b>L.A.B. Golf LINK.2.1</b>","2026 신모델. 블레이드 모양에 힐 샤프트","확인 필요","블레이드 모양을 포기 못 하는 분"],
   ["<b>TaylorMade Spider ZT Max</b>","고관용성 Spider의 제로토크 버전","$449.99","Spider를 쓰던 분"],
   ["<b>Scotty Cameron Fastback OC</b>","로우토크. 거리감과 자연스러운 셋업이 강점","확인 필요","전통 타감과 거리감 중시"]])+
  "<h2>누구에게 안 맞을까</h2><p>앞의 피팅 업체 관계자는 제로토크를 '도구 상자 속 도구 하나'라고 표현했습니다. 페이스 회전을 이미 잘 조절하는 골퍼에게는 회전을 없애는 게 오히려 도움이 안 될 수 있다는 것입니다. 그래서 Scotty Cameron과 PING이 내놓은 '로우토크' 퍼터가 많은 골퍼에게 합리적인 중간 지점이라고 봤습니다.</p>"
  "<div class='note'><b>간단한 기준:</b> 백스윙 때 헤드가 몸 쪽으로 많이 들어오는 강한 아크 스트로크라면, 제로토크보다 토우행이 있는 블레이드가 더 자연스러울 수 있습니다. 퍼터 계산기로 먼저 확인해 보세요.</div>"
  "<h2>상황별 추천</h2>"+picks([("첫 제로토크","Odyssey S2S #7","테스트 1위에 가격도 합리적. 할인 행사도 잦습니다."),("짧은 퍼트 불안","L.A.B. DF3","페이스 안정성이 가장 뛰어난 모델."),("블레이드 모양","L.A.B. LINK.2.1","제로토크인데 블레이드처럼 보입니다."),("전통 타감","Scotty Fastback OC","로우토크로 거리감까지.")])+
  "<h2>구매 전 체크리스트</h2>"+check(["내 스트로크가 일자형인지 아크형인지 알고 있나요? (퍼터 계산기)","제로토크는 셋업이 낯설 수 있습니다. 꼭 시타해 보세요.","L.A.B.는 라이각 피팅이 중요합니다. 온라인 피팅이나 매장 피팅을 받으세요.","Odyssey S2S는 할인 행사가 잦으니 가격을 비교하세요."]),
 body_en=tldr("QUICK TAKE",[
   "<b style='display:inline;color:#fff'>Test winner:</b> Odyssey Ai-Dual Square 2 Square #7 (MyGolfSpy 2026)",
   "<b style='display:inline;color:#fff'>The original:</b> L.A.B. Golf — the biggest share in one fitter's sales data",
   "<b style='display:inline;color:#fff'>Caution:</b> Strong-arc strokes may not suit zero torque."])+
  "<h2>What is a zero-torque putter?</h2><p>A normal putter wants to twist during the stroke. Zero-torque designs move the shaft and weight to nearly cancel that twist. Odyssey, for example, says its Square 2 Square line uses a center-shafted design that balances toe-up, placing it in the zero-torque category.</p>"
  "<h2>Why they're hot</h2><p>At Club Champion, zero-torque putters dominated this year's sales, with L.A.B. the biggest player. The same interview credited Odyssey with making the concept approachable for golfers coming from traditional putters.</p>"
  "<p>When MyGolfSpy ranked every putter it tested in 2026, the top 15 were all zero torque, and the overall winner was the Odyssey Ai-Dual Square 2 Square #7.</p>"
  "<h2>Main models</h2>"+table(["Model","Highlights","US price","Best for"],[
   ["<b>Odyssey Ai-Dual Square 2 Square #7</b>","MyGolfSpy's 2026 test winner; multi-line mallet","$399.99 (launch)","Your first zero-torque putter"],
   ["<b>L.A.B. Golf DF3</b>","The clearest showcase of L.A.B. stability","$449.99 (Golf Galaxy list)","The most nervous short putters"],
   ["<b>L.A.B. Golf Mezz.1 Max</b>","L.A.B. in a familiar mallet shape","From $499","L.A.B. performance, familiar look"],
   ["<b>L.A.B. Golf LINK.2.1</b>","New for 2026: blade shape, heel shafted","TBC","Blade lovers"],
   ["<b>TaylorMade Spider ZT Max</b>","Zero-torque version of the high-MOI Spider","$449.99","Current Spider users"],
   ["<b>Scotty Cameron Fastback OC</b>","Low torque; strong pace control, natural setup","TBC","Traditional feel and touch"]])+
  "<h2>Who it may not suit</h2><p>That fitter called zero torque \"another tool in the toolbox.\" Golfers who already control face rotation well may not benefit from removing it, which is why low-torque putters from Scotty Cameron and PING make a sensible middle ground for many players.</p>"
  "<div class='note'><b>Simple rule:</b> If your putter swings well inside on the backstroke (a strong arc), a toe-hang blade may feel more natural than zero torque. Check with the putter calculator first.</div>"
  "<h2>Picks by situation</h2>"+picks([("FIRST ZT","Odyssey S2S #7","Test winner at a fair price, often on sale."),("SHORT-PUTT NERVES","L.A.B. DF3","The most face-stable model."),("BLADE LOOK","L.A.B. LINK.2.1","Zero torque that looks like a blade."),("TRADITIONAL FEEL","Scotty Fastback OC","Low torque with great pace.")],ko=False)+
  "<h2>Checklist</h2>"+check(["Do you know if your stroke is straight or arced? (putter calculator)","Zero-torque setups can feel odd — demo first.","L.A.B. depends on lie-angle fitting; get fit online or in store.","Odyssey S2S is often discounted — compare prices."]),
 sources=[("Australian Golf Digest — Odyssey Square 2 Square","https://www.australiangolfdigest.com.au/2026-equipment-guide-callaway/"),
  ("Plugged In Golf — Biggest trends in 2026 putters","https://pluggedingolf.com/?p=140522"),
  ("MyGolfSpy — Best putters of 2026","https://mygolfspy.com/buyers-guide/best-putters-of-2026-test-data-from-75-putters/"),
  ("MyGolfSpy — Which Odyssey putters are worth buying","https://mygolfspy.com/news-opinion/which-odyssey-putters-are-worth-buying-in-2026-we-tested-6-models/"),
  ("GolfWRX — Odyssey Ai-Dual Square 2 Square launch","https://golfwrx.com/772062/callaway-unveils-new-odyssey-line-of-ai-dual-square-2-square-putters/"),
  ("Golf Galaxy — L.A.B. DF3 listing","https://www.golfgalaxy.com/f/golf-clubs"),
  ("Golf Galaxy — Spider ZT Max listing","https://www.golfgalaxy.com/f/new-arrivals-clubs"),
  ("Breaking Eighty — Which L.A.B. putter is right","https://breakingeighty.com/best-lab-putters"),
  ("Plugged In Golf — L.A.B. LINK.2.1 review","https://pluggedingolf.com/lab-golf-link-2-1-putter-review/"),
  ("Parwest Golf — Zero-torque putters 2026","https://www.parwestgolf.com/blogs/content/zero-torque-putters-2026-lab-golf-vs-odyssey-vs-taylormade-vs-scotty-cameron"),
  ("NCG — Best zero torque putters","https://www.nationalclubgolfer.com/us//best-golf-deals/best-zero-torque-putters/"),
  ("MyGolfSpy — Golf deals of the week (Odyssey Ai-Dual)","https://mygolfspy.com/news-opinion/the-best-golf-deals-of-the-week-6/")]))

for p in POSTS:
    open(ROOT + '/site/' + p["file"], 'w').write(page(p))
    print(p["file"])
