import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import build as B
import imgs
B.HERO_BG["hot"] = "radial-gradient(120% 120% at 80% 0%,#1d4a66 0%,#0f2a3d 55%,#3a2708 130%)"

STY = imgs.CSS + """<style>
.mc{border:1px solid var(--line);border-radius:16px;padding:18px;margin:16px 0;box-shadow:0 1px 2px rgba(15,42,61,.05)}
.mc .top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.mc .br{font-size:.72rem;font-weight:700;letter-spacing:.8px;color:var(--muted);text-transform:uppercase}
.mc h3{margin:2px 0 4px;font-size:1.15rem}
.mc .pr{font-size:.85rem;font-weight:700;color:var(--navy);background:var(--bg);border-radius:8px;padding:3px 9px}
.mc .one{color:var(--muted);font-size:.92rem;margin:6px 0 12px}
.pcx{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pcx div{border-radius:12px;padding:12px 14px;font-size:.9rem}
.pcx .p{background:var(--green-l)}.pcx .c{background:#fdecee}
.pcx b{display:block;font-size:.75rem;letter-spacing:.6px;margin-bottom:6px}
.pcx .p b{color:var(--green)}.pcx .c b{color:#b3261e}
.pcx ul{margin:0;padding-left:18px}.pcx li{margin-bottom:4px}
.mc .fit{margin-top:10px;font-size:.88rem}.mc .fit b{color:var(--green)}
.catH{display:flex;align-items:center;gap:10px;margin:44px 0 6px}
.catH span{background:var(--navy);color:#e3c06a;font-weight:800;font-size:.75rem;letter-spacing:1px;border-radius:8px;padding:5px 10px}
.catH h2{margin:0}
@media (max-width:600px){.pcx{grid-template-columns:1fr}}
</style>"""

def card(brand, name, price, one, pros, cons, fit, ko=True):
    P = "장점" if ko else "PROS"; C = "단점" if ko else "CONS"; F = "추천 대상:" if ko else "Best for:"
    return (f'<div class="mc">{imgs.fig(brand, name)}<div class="top"><div><div class="br">{brand}</div><h3>{name}</h3></div><span class="pr">{price}</span></div>'
            f'<p class="one">{one}</p><div class="pcx"><div class="p"><b>✓ {P}</b><ul>' + "".join(f"<li>{x}</li>" for x in pros) +
            f'</ul></div><div class="c"><b>✗ {C}</b><ul>' + "".join(f"<li>{x}</li>" for x in cons) +
            f'</ul></div></div><p class="fit"><b>{F}</b> {fit}</p>{B.buy(ko)}</div>')

def cat(tag, title):
    return f'<div class="catH"><span>{tag}</span><h2>{title}</h2></div>'

KO = STY + B.tldr("핵심 요약", [
 "<b style='display:inline;color:#fff'>드라이버:</b> 속도와 관용성의 균형은 TaylorMade Qi4D, 슬라이스 교정은 Callaway Quantum Max-D",
 "<b style='display:inline;color:#fff'>아이언:</b> 쉬우면서 타감까지 원하면 Srixon ZXiR",
 "<b style='display:inline;color:#fff'>웨지·퍼터:</b> 웨지는 Vokey SM11, 퍼터는 제로토크 Odyssey S2S #7이 2026년 테스트 상위"]) + \
 "<p>2026년 리뷰와 테스트에서 가장 많이 언급된 드라이버·아이언·웨지·퍼터를 골라, 여러 매체의 평가를 바탕으로 장점과 단점을 정리했습니다. 가격은 미국 기준 출시가 또는 판매가입니다.</p>" + \
 cat("DRIVER", "드라이버") + \
 card("TaylorMade", "Qi4D (패밀리)", "$649.99", "GolfWRX 회원 투표에서 2026년 최고의 드라이버로 뽑힌 모델. 일반·Max·LS 버전이 있습니다.",
      ["외관이 뛰어나고 볼 스피드·캐리가 좋음", "방향이 꾸준하고 분산이 작음", "로프트 슬리브 4° 조절로 탄도 맞추기 쉬움"],
      ["Max 버전은 일반 Qi4D보다 조절 기능이 적음", "LS 버전은 관용성이 떨어지고 빗맞으면 성능 하락"],
      "대부분의 골퍼. 관용성이 더 필요하면 Max, 스윙이 빠르면 LS") + \
 card("Callaway", "Quantum Max / Max-D", "$649.99", "Callaway가 관용성 중심에서 다시 '속도'로 방향을 튼 2026년 라인입니다.",
      ["볼 스피드가 뛰어나고 타감이 단단함", "조절 호젤이 쉽고 효과적", "Max-D는 한 매체가 테스트한 드로우 드라이버 중 가장 멀리 나감"],
      ["캐리가 전작 Elyte를 확실히 넘지는 못했다는 평", "가격이 비싼 편", "Max-D의 드로우 성향은 모두에게 맞지 않음"],
      "Max는 속도를 원하는 중급자, Max-D는 슬라이스가 고민인 분") + \
 card("Srixon", "ZXi RKT", "$649.99", "2026년 10월 출시된 Srixon의 새 드라이버 라인. 투어 우승으로 화제가 됐습니다.",
      ["동급 최고 수준의 탄착 분산", "한 리뷰어는 지금까지 써 본 가장 빠르고 곧은 드라이버라고 평가"],
      ["일부 경쟁 모델보다 비쌈", "드로우·페이드를 일부러 치기 어렵다는 평", "소리와 타감을 성능과 맞바꿨다는 평"],
      "똑바로 멀리 보내는 게 최우선인 분") + \
 cat("IRON", "아이언") + \
 card("Srixon", "ZXiR", "$1,099부터 (7개)", "Srixon의 첫 본격 게임 임프루브먼트 아이언. 한 매체 랭킹에서 2026 최고의 올라운더.",
      ["게임 임프루브먼트답지 않게 매우 부드러운 타감", "관용성이 크고 외관도 좋음", "빗맞아도 볼 스피드와 거리가 유지됨"],
      ["어드레스 때 헤드가 조금 커 보임", "HL 모델은 탄도가 너무 높을 수 있음"],
      "쉬운 아이언이지만 타감도 포기하기 싫은 중·고핸디캡") + \
 card("TaylorMade", "Qi Max", "$1,099.99부터 (7개)", "부피감을 줄여 '플레이어스 아이언처럼 보이는' 게임 임프루브먼트를 목표로 한 모델.",
      ["세트 전체 볼 스피드가 뛰어남", "롱아이언이 오른쪽으로 새는 경향을 줄이는 설계", "약한 드로우 성향으로 슬라이스에 도움"],
      ["2024년 Qi와 성능 차이가 거의 없다는 평", "디자인이 이전보다 복잡하다는 의견"],
      "이전 세대 Qi가 없는 분, 깔끔한 모양의 쉬운 아이언을 원하는 분") + \
 card("Mizuno", "JPX 925 Hot Metal Pro", "약 $150/개", "Hot Metal 라인의 상급자용. 탑라인이 가장 얇고 오프셋이 가장 작습니다.",
      ["폭발적인 볼 스피드와 높은 탄도", "보기 좋은 외관", "합리적인 가격"],
      ["가끔 거리가 튀는 '플라이어' 샷이 나옴"],
      "거리와 외관을 모두 원하는 로우~미드 핸디캡") + \
 cat("WEDGE", "웨지") + \
 card("Titleist", "Vokey SM11", "$199.99~$209.99", "2026 시즌 PGA 투어 최다 우승 웨지이자 GolfWRX 회원 투표 1위.",
      ["젖은 조건에서도 스핀이 줄지 않은 유일한 웨지(한 테스트 기준)", "그라인드 6종(F·S·M·K·L·D)으로 선택 폭이 넓음"],
      ["다른 테스트에서는 풀샷 스핀 순위가 11위로 기대보다 낮았음"],
      "그라인드를 맞춰 쓰고 싶은 모든 수준의 골퍼") + \
 card("TaylorMade", "MG5", "$199.99", "2026년 투어 7승으로 화려하게 데뷔한 TaylorMade의 새 웨지.",
      ["어프로치 같은 짧은 샷에서 스핀이 많음", "그라인드 6종", "부드러운 타감"],
      ["헤드가 작아 상급자 취향", "곧은 리딩 엣지가 모두의 눈에 맞지는 않음"],
      "스핀과 컨트롤을 중시하는 중·상급자") + \
 card("Cleveland", "RTZ", "$199.99 (Tour Rack 맞춤)", "젖은 날에도 일관성이 좋다는 평을 받은 Cleveland의 투어 웨지.",
      ["매우 부드러운 타감", "다양한 라이에서 깨끗한 컨택", "벙커 성능이 좋고 하이 바운스 선택지"],
      ["토우 쪽 모양이 약간 각져 보임", "정확도 점수가 상대적으로 약점이라는 테스트 결과"],
      "비 오는 날이 많거나 벙커가 고민인 분") + \
 cat("PUTTER", "퍼터") + \
 card("Odyssey", "Ai-Dual Square 2 Square #7", "$399.99", "MyGolfSpy의 2026 테스트 1위 퍼터. 센터 샤프트 제로토크 설계.",
      ["2026 테스트에서 가장 좋은 성적", "전통 퍼터를 쓰던 골퍼도 적응하기 쉬움", "할인 행사가 잦음"],
      ["제로토크 셋업은 처음엔 낯설 수 있음", "페이스 회전을 잘 조절하는 골퍼에게는 이점이 적을 수 있음"],
      "처음 제로토크를 써 보는 분, 짧은 퍼트가 불안한 분") + \
 card("L.A.B. Golf", "DF3", "$449.99", "제로토크 열풍을 이끈 L.A.B.의 대표 모델.",
      ["페이스 안정성이 매우 뛰어남", "짧은 퍼트 자신감이 크게 올라감"],
      ["모양이 호불호가 강함", "고가이고, 라이각 피팅이 중요함"],
      "모양보다 결과가 중요한 분") + \
 card("Scotty Cameron", "Studio Style Fastback OC", "확인 필요", "Scotty Cameron의 로우토크 모델. 전통 감성과 안정성의 절충.",
      ["거리감(페이스 컨트롤)이 뛰어남", "다른 제로토크보다 셋업이 자연스러움", "클래식한 Scotty 디자인"],
      ["프리미엄 가격"],
      "전통 퍼터 느낌을 유지하면서 안정성을 더하고 싶은 분") + \
 "<h2>한눈에 보는 결론</h2>" + B.table(["카테고리", "가장 무난한 선택", "이런 분은 이것"], [
   ["드라이버", "TaylorMade Qi4D", "슬라이스 → Quantum Max-D / 직진성 → Srixon ZXi RKT"],
   ["아이언", "Srixon ZXiR", "가성비 → Mizuno JPX 925 Hot Metal Pro"],
   ["웨지", "Vokey SM11", "스핀 → MG5 / 벙커·비 → Cleveland RTZ"],
   ["퍼터", "Odyssey S2S #7", "짧은 퍼트 공포 → L.A.B. DF3 / 전통 감성 → Fastback OC"]]) + \
 "<div class='note'><b>내게 맞는 모델이 궁금하다면</b> 드라이버·아이언·웨지·퍼터 추천 계산기로 먼저 확인해 보세요. 거리 하나만 넣으면 됩니다.</div>"

EN = STY + B.tldr("QUICK TAKE", [
 "<b style='display:inline;color:#fff'>Driver:</b> TaylorMade Qi4D for balance; Callaway Quantum Max-D to fix a slice",
 "<b style='display:inline;color:#fff'>Irons:</b> Srixon ZXiR for easy irons with real feel",
 "<b style='display:inline;color:#fff'>Wedges & putters:</b> Vokey SM11 and the zero-torque Odyssey S2S #7 top 2026 testing"]) + \
 "<p>We picked the drivers, irons, wedges and putters that came up most in 2026 reviews and testing, and summarized their pros and cons from multiple outlets. Prices are US launch or retail prices.</p>" + \
 cat("DRIVER", "Drivers") + \
 card("TaylorMade", "Qi4D (family)", "$649.99", "Voted the best driver of 2026 by GolfWRX members, in standard, Max and LS versions.",
      ["Great looks, fast ball speed and carry", "Consistently straight with tight dispersion", "4° loft sleeve makes flight easy to dial in"],
      ["The Max lacks the core model's adjustability", "The LS is less forgiving and drops off on mishits"],
      "Most golfers; Max for more forgiveness, LS for fast swings", ko=False) + \
 card("Callaway", "Quantum Max / Max-D", "$649.99", "Callaway's 2026 line, shifting focus from forgiveness back to speed.",
      ["Excellent ball speed and solid feel", "Simple, effective adjustable hosel", "Max-D was the longest draw driver one outlet has tested"],
      ["Carry didn't clearly beat last year's Elyte", "Expensive", "Max-D's draw bias won't suit everyone"],
      "Max for speed-seeking mid handicaps; Max-D for slicers", ko=False) + \
 card("Srixon", "ZXi RKT", "$649.99", "Srixon's new line launched in October 2026, already a tour winner.",
      ["Class-leading dispersion", "One reviewer's fastest, straightest driver ever"],
      ["Pricier than some rivals", "Hard to shape draws and fades on purpose", "Some sound and feel traded for performance"],
      "Golfers who want long and straight above all", ko=False) + \
 cat("IRON", "Irons") + \
 card("Srixon", "ZXiR", "From $1,099 (7 pcs)", "Srixon's first true game-improvement iron; one outlet's best all-rounder of 2026.",
      ["Remarkably soft feel for a game-improvement iron", "Lots of forgiveness and great looks", "Holds ball speed and distance on mishits"],
      ["Slightly large look at address", "The HL model may launch too high for some"],
      "Mid-high handicaps who want easy irons with feel", ko=False) + \
 card("TaylorMade", "Qi Max", "From $1,099.99 (7 pcs)", "A game-improvement iron designed to look more like a players iron.",
      ["Excellent ball speed through the set", "Design reduces long irons leaking right", "Slight draw bias helps slicers"],
      ["Little performance gain over the 2024 Qi", "Busier look than before, per some testers"],
      "Golfers without the previous Qi who want a clean, easy iron", ko=False) + \
 card("Mizuno", "JPX 925 Hot Metal Pro", "About $150/club", "The better-player Hot Metal: thinnest topline, least offset.",
      ["Explosive speed and high launch", "Great looks", "Fair price"],
      ["Occasional jumpers (fliers)"],
      "Low to mid handicaps wanting distance and looks", ko=False) + \
 cat("WEDGE", "Wedges") + \
 card("Titleist", "Vokey SM11", "$199.99–$209.99", "The winningest PGA Tour wedge of the 2026 season and GolfWRX members' top pick.",
      ["The only wedge in one test that lost no spin in the wet", "Six grinds (F, S, M, K, L, D)"],
      ["Ranked only 11th for full-shot spin in another test"],
      "Any golfer who wants to fine-tune grinds", ko=False) + \
 card("TaylorMade", "MG5", "$199.99", "TaylorMade's new wedge, with seven tour wins in its debut year.",
      ["High spin on partial shots", "Six grinds", "Soft feel"],
      ["Compact head suits better players", "Straighter leading edge won't appeal to everyone"],
      "Mid to low handicaps who value spin and control", ko=False) + \
 card("Cleveland", "RTZ", "$199.99 (Tour Rack custom)", "Cleveland's tour wedge, praised for wet-weather consistency.",
      ["Very soft feel", "Clean contact from many lies", "Good from bunkers with high-bounce options"],
      ["Slightly square toe shape", "Accuracy scored as its relative weak spot in one test"],
      "Golfers in wet climates or who struggle in bunkers", ko=False) + \
 cat("PUTTER", "Putters") + \
 card("Odyssey", "Ai-Dual Square 2 Square #7", "$399.99", "MyGolfSpy's best putter of 2026; center-shafted zero torque.",
      ["Top performer in 2026 testing", "Easy transition from traditional putters", "Frequently on sale"],
      ["Zero-torque setup can feel odd at first", "Less benefit if you already control face rotation well"],
      "First-time zero-torque users and nervous short putters", ko=False) + \
 card("L.A.B. Golf", "DF3", "$449.99", "L.A.B.'s flagship, the putter that started the zero-torque wave.",
      ["Exceptional face stability", "Big boost in short-putt confidence"],
      ["Polarizing looks", "Pricey, and lie-angle fitting matters"],
      "Golfers who care about results over looks", ko=False) + \
 card("Scotty Cameron", "Studio Style Fastback OC", "TBC", "Scotty Cameron's low-torque model, blending tradition and stability.",
      ["Excellent pace control", "More natural setup than other zero-torque putters", "Classic Scotty design"],
      ["Premium price"],
      "Golfers wanting a traditional feel with added stability", ko=False) + \
 "<h2>The bottom line</h2>" + B.table(["Category", "Safest pick", "If you..."], [
   ["Driver", "TaylorMade Qi4D", "slice → Quantum Max-D / want straight → Srixon ZXi RKT"],
   ["Irons", "Srixon ZXiR", "want value → Mizuno JPX 925 Hot Metal Pro"],
   ["Wedges", "Vokey SM11", "want spin → MG5 / play wet or sandy → Cleveland RTZ"],
   ["Putter", "Odyssey S2S #7", "fear short putts → L.A.B. DF3 / love tradition → Fastback OC"]]) + \
 "<div class='note'><b>Not sure which fits you?</b> Try the driver, iron, wedge and putter calculators — one distance is all it takes.</div>"

P = dict(file="blog-hot-clubs-2026.html", bg="hot", calc="driver",
 cat_ko="장비 분석", cat_en="Gear analysis",
 title_ko="2026 가장 핫한 드라이버·아이언·웨지·퍼터 장단점 분석",
 title_en="2026's hottest drivers, irons, wedges and putters: pros and cons",
 desc_ko="TaylorMade Qi4D, Callaway Quantum, Srixon ZXiR, Vokey SM11, Odyssey S2S 등 2026년 인기 골프채의 장점과 단점을 정리했습니다.",
 sub_ko="리뷰와 테스트에서 가장 많이 언급된 12개 모델을 카테고리별로 골라 장점과 단점을 한눈에 정리했습니다.",
 sub_en="Twelve of the most talked-about 2026 models, with pros and cons at a glance.",
 cta_ko=("내 스윙엔 어떤 모델이 맞을까?","드라이버 거리만 넣으면 헤드스피드와 추천 모델이 나옵니다.","드라이버 계산기 열기"),
 cta_en=("Which model fits your swing?","Enter your drive distance for speed and model picks.","Open the driver calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("GolfWRX — Best drivers of 2026 (member vote)","https://golfwrx.com/?p=783608"),
  ("Golfalot — Qi4D driver review","https://golfalot.com/equipment-review/taylormade-qi4d-driver-review"),
  ("Plugged In Golf — Qi4D driver review","https://pluggedingolf.com/?p=130371"),
  ("GolfMagic — Qi4D Max review","https://www.golfmagic.com/equipment/drivers/taylormade-qi4d-max-driver-review"),
  ("NCG — Qi4D LS review","https://www.nationalclubgolfer.com/us/reviews/drivers/taylormade-qi4d-ls-driver-review/"),
  ("Golfalot — Qi4D LS review","https://golfalot.com/equipment-review/taylormade-qi4d-ls-driver-review"),
  ("NCG — Callaway Quantum Max review","https://www.nationalclubgolfer.com/reviews/drivers/callaway-quantum-max-driver-review/"),
  ("Golfalot — Callaway Quantum Max review","https://golfalot.com/equipment-review/callaway-quantum-max-driver-review"),
  ("NCG — Callaway Quantum Max-D review","https://www.nationalclubgolfer.com/us/reviews/drivers/callaway-quantum-max-d-driver-review/"),
  ("GolfMagic — Callaway Quantum Max-D review","https://www.golfmagic.com/equipment/drivers/callaway-quantum-max-d-driver-review-big-forgiveness-small-catch"),
  ("Newswire — Srixon ZXi RKT pricing","https://www.newswire.com/news/raw-power-pure-sound-srixon-introduces-all-new-zxi-rkt-woods"),
  ("Golf Monthly — Srixon ZXi RKT review","https://www.golfmonthly.com/reviews/drivers/srixon-zxi-rkt-driver-review"),
  ("Plugged In Golf — Srixon ZXi RKT review","https://pluggedingolf.com/srixon-zxi-rkt-driver-review/"),
  ("Golfalot — Srixon ZXi RKT review","https://golfalot.com/equipment-review/srixon-zxi-rkt-driver-review"),
  ("GolfMagic — Srixon ZXiR review","https://www.golfmagic.com/equipment/irons/srixon-zxir-zxir-hl-irons-review-new-standard-game-improvement-irons"),
  ("NCG — Srixon ZXiR review","https://www.nationalclubgolfer.com/us/reviews/srixon-zxir-irons-review/"),
  ("Golfalot — Best golf irons 2026","https://golfalot.com/category/buying-guide/best-golf-irons-2026-every-new-model-tested-and-ranked"),
  ("NCG — TaylorMade Qi Max irons review","https://www.nationalclubgolfer.com/us/reviews/taylormade-qi-max-irons-review"),
  ("Golfstead — TaylorMade Qi Max irons review","https://golfstead.com/taylormade-qi-max-irons-review"),
  ("GolfMagic — JPX 925 Hot Metal Pro review","https://www.golfmagic.com/equipment/irons/mizuno-jpx-925-hot-metal-pro-irons-review"),
  ("GOLF.com — Winningest wedges 2026","https://golf.com/gear/wedges/winningest-wedges-pga-tour-2026/"),
  ("GolfWRX — Best wedges of 2026 (member vote)","https://golfwrx.com/?p=784646"),
  ("MyGolfSpy — 5 smartest wedge buys 2026","https://mygolfspy.com/news-opinion/5-smartest-wedge-buys-for-2026/"),
  ("Today's Golfer — Highest-spinning wedges 2026","https://www.todays-golfer.com/news-and-events/equipment-news/highest-spinning-golf-wedges-2026/"),
  ("Golf Monthly — Wedge reviews","https://www.golfmonthly.com/gear-finder/wedges"),
  ("NCG — Best wedges 2026","https://www.nationalclubgolfer.com/gb/best-golf-deals/best-wedges/"),
  ("MyGolfSpy — Odyssey putters 2026","https://mygolfspy.com/news-opinion/which-odyssey-putters-are-worth-buying-in-2026-we-tested-6-models/"),
  ("GolfWRX — Odyssey Ai-Dual S2S launch","https://golfwrx.com/772062/callaway-unveils-new-odyssey-line-of-ai-dual-square-2-square-putters/"),
  ("Plugged In Golf — 2026 putter trends","https://pluggedingolf.com/?p=140522"),
  ("Breaking Eighty — Which L.A.B. putter","https://breakingeighty.com/best-lab-putters"),
  ("Golf Galaxy — L.A.B. DF3 and wedge prices","https://www.golfgalaxy.com/f/golf-clubs"),
  ("NCG — Best zero torque putters 2026","https://www.nationalclubgolfer.com/us//best-golf-deals/best-zero-torque-putters/")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
print("ok")
