import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import build as B
B.HERO_BG["hyb"] = "radial-gradient(120% 120% at 80% 0%,#2f5a3a 0%,#163322 55%,#0a1a10 100%)"
b = lambda s: f"<b style='display:inline;color:#fff'>{s}</b> "

STY = """<style>
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
@media (max-width:600px){.pcx{grid-template-columns:1fr}}
</style>"""

def card(brand, name, price, one, pros, cons, fit, ko=True):
    P = "장점" if ko else "PROS"; C = "단점" if ko else "CONS"; F = "추천 대상:" if ko else "Best for:"
    return (f'<div class="mc"><div class="top"><div><div class="br">{brand}</div><h3>{name}</h3></div><span class="pr">{price}</span></div>'
            f'<p class="one">{one}</p><div class="pcx"><div class="p"><b>✓ {P}</b><ul>' + "".join(f"<li>{x}</li>" for x in pros) +
            f'</ul></div><div class="c"><b>✗ {C}</b><ul>' + "".join(f"<li>{x}</li>" for x in cons) +
            f'</ul></div></div><p class="fit"><b>{F}</b> {fit}</p>{B.buy(ko)}</div>')

# ------------------------------------------------------------------ KOREAN
KO = STY + B.tldr("핵심 요약", [
 b("테스트 1위:")+"Mizuno JPX One 하이브리드 — MyGolfSpy 2026 하이브리드 테스트 종합 1위·정확도 1위 ($279.99)",
 b("시니어 무난한 선택:")+"Titleist GT1·PING G440 — 두 매체 모두 '느린 스윙에 쉽게 뜬다'고 평가",
 b("슬라이스·가성비:")+"슬라이스엔 Callaway Quantum Max OS·TaylorMade Qi4D Max, 예산엔 Tour Edge Exotics Max ($229.99)"]) + \
"<p>나이가 들어 헤드스피드가 줄면 가장 먼저 어려워지는 클럽이 <b>3·4·5번 롱아이언</b>입니다. 공이 충분히 뜨지 않아 그린에 세우기 어렵고, 조금만 빗맞아도 거리가 크게 줄어듭니다. 그래서 많은 시니어 골퍼가 롱아이언을 하이브리드(유틸리티)로 바꿉니다. MyGolfSpy는 \"하이브리드는 롱아이언을 대신하기 위한 클럽\"이라고 설명하며, 골퍼에 따라 <b>5번이나 6번 아이언까지</b> 하이브리드로 바꿔도 된다고 말합니다. 아이언과 비교한 가장 큰 장점은 <b>더 좋은 발사 조건(높은 탄도)</b>을 만들기 쉽다는 점입니다.</p>" + \
"<p>마침 최근 MyGolfSpy가 2026년 하이브리드·페어웨이우드 테스트에서 <b>Mizuno JPX One이 두 부문 모두 종합 1위</b>를 했다는 기사를 내며 화제가 됐습니다. 한국에서도 익숙한 Mizuno라 관심이 큰 소식입니다. 이 글에서는 MyGolfSpy의 테스트 데이터와 Golf Monthly·National Club Golfer(NCG)의 시니어용 하이브리드 리뷰를 함께 보고, 느린 스윙 골퍼에게 맞는 모델을 정리했습니다.</p>" + \
"<h2>1. 2026 MyGolfSpy 하이브리드 테스트 결과</h2>" + \
"<p>MyGolfSpy 점수는 10점 만점이며 정확도 50%, 거리 25%, 관용성 25%로 계산합니다. 아래 캐리 거리는 MyGolfSpy 테스터들의 평균값입니다. 테스터 스윙이 시니어 평균보다 빠를 수 있으므로 <b>거리 숫자 자체보다 모델 간 차이</b>를 참고하세요.</p>" + \
B.table(["모델", "미국 가격", "종합", "정확도", "거리", "관용성", "캐리(yd)"], [
 ["Mizuno JPX One", "$279.99", "<b>9.3</b>", "9.8", "8.8", "8.9", "168.8"],
 ["Callaway Quantum Max OS", "$319.99", "9.1", "9.2", "9.3", "8.9", "169.7"],
 ["Tour Edge Exotics Max", "$229.99", "9.0", "9.1", "9.5", "8.5", "171.3"],
 ["Cobra OPTM", "$329.99", "8.9", "9.0", "7.5", "9.9", "167.2"],
 ["PXG Lightning", "$329.99", "8.6", "8.5", "8.0", "9.4", "167.5"],
 ["TaylorMade Qi4D", "$299.99", "8.1", "7.4", "9.4", "8.2", "170.8"]]) + \
"<p style='font-size:.85rem;color:var(--muted)'>※ 출처: MyGolfSpy Best Hybrids of 2026. 같은 표에서 2025년에 테스트한 PING G440, Titleist GT3, Srixon ZXi는 각각 8.7점이었습니다.</p>" + \
"<h2>2. 모델별 장단점</h2>" + \
card("Mizuno", "JPX One Hybrid", "$279.99", "MyGolfSpy 2026 종합 1위·정확도 1위. Golf Monthly는 '높이 띄우기 좋은 하이브리드'로, NCG는 '관용성 최고'로 꼽았습니다.",
     ["테스트 정확도 9.8점으로 가장 곧음", "Golf Monthly: 공을 띄우기 어려운 분께 좋은 선택", "NCG: 면 전체에서 볼 스피드와 스핀이 일정하고, 그린에 잘 섬"],
     ["MyGolfSpy 기준 스핀이 가장 많은 편 — 원래 스핀이 많은 분께는 불리", "광택 있는 크라운은 호불호"],
     "공이 잘 안 뜨는 분, 롱아이언을 더 쉬운 클럽으로 바꾸려는 분") + \
card("Titleist", "GT1 Hybrid", "$329", "Golf Monthly 시니어 하이브리드 1순위. 로프트 20·23·26·29°.",
     ["Golf Monthly: '느린 스윙의 시니어에게 아주 잘 맞는다'", "가볍고 띄우기 쉬우며, 무게추·호젤 조절 가능", "NCG 테스터 발사각이 40도를 넘을 만큼 높은 탄도"],
     ["GT 라인 중 파워는 조금 약함", "NCG: 스핀이 많고 약한 드로우 성향이라 낮은 탄도를 원하면 안 맞음"],
     "탄도가 낮아 고민인 시니어, 우드와 아이언 사이 간격을 메우려는 분") + \
card("PING", "G440 Hybrid", "$269~$299.99", "Golf Monthly '가장 관용성 높은 하이브리드'. 로프트 17~34°로 선택 폭이 넓습니다.",
     ["Golf Monthly: '느린 스윙 시니어가 만족할 만큼 쉽게 뜬다'", "NCG: 빗맞아도 관용성이 크고 탄도가 높고 일정함", "얕은 페이스로 높은 발사"],
     ["전작 대비 외관 변화가 거의 없음", "작고 전통적인 모양을 좋아하면 크게 느껴질 수 있음"],
     "빗맞음이 잦고 편하게 치고 싶은 분 (가격은 매체별 표기 차이)") + \
card("Callaway", "Quantum Max OS Hybrid", "$319.99", "MyGolfSpy 종합 2위, Golf Monthly '어떤 라이에서도 좋은' 모델, NCG '드로우 성향 최고'.",
     ["정확도·거리·관용성이 고르게 높음", "높고 곧은 탄도, 잔디 빠짐이 좋음", "드로우 성향으로 슬라이스 완화"],
     ["헤드가 다른 하이브리드보다 큼", "호젤 조절 방법이 복잡하다는 평"],
     "공이 오른쪽으로 휘는 분, 일관성을 최우선으로 하는 분") + \
card("TaylorMade", "Qi4D Max Hybrid", "$299.99", "Golf Monthly '슬라이서에게 최고'. 로프트 20~34°.",
     ["Golf Monthly: 오른쪽 미스가 훨씬 줄어듦", "후방 무게 배치로 쉽게 뜸", "거리·관용성이 인상적"],
     ["조절 기능 없음", "MyGolfSpy 점수 8.4로 상위권보다는 낮음"],
     "슬라이스가 고민이고 조절 기능이 필요 없는 분") + \
card("Tour Edge", "Exotics Max Hybrid", "$229.99", "MyGolfSpy 종합 3위이자 '거리 1위'. 가격까지 가장 저렴한 편입니다.",
     ["거리 점수 9.5로 테스트 최고", "테스트 상위권 중 가장 낮은 가격"],
     ["관용성은 '보통'", "조절 기능이 없고 타감이 구식이라는 평"],
     "예산을 아끼면서 거리를 원하는 분") + \
"<h2>3. 시니어 골퍼를 위한 선택법</h2>" + \
B.check([
 "<b>어떤 아이언을 바꿀까:</b> Golf Monthly는 200야드 이상 거리에서는 하이브리드가 롱아이언보다 더 관용적이고 효과적인 경우가 많다고 합니다. 3·4번부터 바꾸고, 5번 아이언도 띄우기 힘들면 5번까지 바꾸는 식이 무난합니다.",
 "<b>로프트:</b> 로프트는 제조사마다 조금씩 다릅니다. 숫자(3H·4H)보다 <b>로프트 각도</b>를 기준으로, 지금 가장 긴 아이언보다 거리가 한 클럽 더 나오면서 겹치지 않게 고르세요.",
 "<b>샤프트:</b> MyGolfSpy는 샤프트 강도가 스윙 속도와 맞아야 탄도가 맞는다고 설명합니다. 아이언을 스틸에서 그래파이트로 바꿀 시기라면 하이브리드도 가벼운 그래파이트·시니어(A) 플렉스를 함께 고려하세요.",
 "<b>스핀:</b> 원래 공이 높이 뜨고 스핀이 많은 분은 Mizuno JPX One이나 Wilson DYNAPWR처럼 스핀이 많은 모델이 오히려 거리를 줄일 수 있습니다."]) + \
"<h3>한눈에 보는 추천</h3>" + B.table(["이런 분이라면", "추천 모델"], [
 ["가장 곧게 치고 싶다", "Mizuno JPX One"],
 ["공이 잘 안 뜬다", "Titleist GT1, Mizuno JPX One"],
 ["빗맞음이 잦다", "PING G440, Cobra OPTM"],
 ["슬라이스가 고민", "Callaway Quantum Max OS, TaylorMade Qi4D Max"],
 ["예산이 중요", "Tour Edge Exotics Max ($229.99)"]]) + \
"<p>하이브리드는 블랙프라이데이 기간 할인 폭이 큰 편이고, 한두 시즌 지난 모델은 중고로도 좋은 상태를 찾기 쉽습니다. Golf Monthly 기준으로 Callaway Quantum Max OS는 $269.99, Cobra OPTM은 $249 특가가 표시돼 있었습니다(시점에 따라 바뀜). 하이브리드는 한 개만 사도 되기 때문에, 아이언 세트를 바꾸지 않고도 경기력을 바꿀 수 있는 가장 저렴한 방법입니다.</p>" + \
"<div class='note'><b>몇 번 아이언까지 하이브리드로 바꿀까?</b> 아이언 계산기에 7번 아이언 거리를 넣으면 헤드 종류와 샤프트를 추천해 드립니다. 롱아이언 대신 하이브리드가 필요한지 판단하는 데 참고하세요.</div>"

# ------------------------------------------------------------------ ENGLISH
EN = STY + B.tldr("QUICK TAKE", [
 b("Test winner:")+"Mizuno JPX One hybrid — #1 overall and #1 for accuracy in MyGolfSpy's 2026 test ($279.99)",
 b("Safe senior picks:")+"Titleist GT1 and PING G440 — both called easy to launch for slower swings",
 b("Slice & budget:")+"Callaway Quantum Max OS or TaylorMade Qi4D Max for a slice; Tour Edge Exotics Max ($229.99) on a budget"]) + \
"<p>When swing speed drops, the first clubs to get hard are the <b>3-, 4- and 5-irons</b>. The ball doesn't climb enough to hold greens, and small mishits cost a lot of distance. That's why so many senior golfers swap long irons for hybrids. MyGolfSpy puts it simply: \"Hybrids are meant as long-iron replacements,\" and some golfers may want to replace irons <b>up to a 5- or 6-iron</b>. The biggest advantage over an iron is the potential for <b>better launch conditions</b>.</p>" + \
"<p>The timing is good: MyGolfSpy recently reported that the <b>Mizuno JPX One finished first overall in both its 2026 hybrid and fairway wood tests</b>, a surprise sweep for a brand many Korean-American golfers already trust. Below we combine MyGolfSpy's test data with senior-focused hybrid reviews from Golf Monthly and National Club Golfer (NCG) to find the best fits for slower swings.</p>" + \
"<h2>1. MyGolfSpy 2026 hybrid test results</h2>" + \
"<p>MyGolfSpy scores out of 10, weighting accuracy 50%, distance 25% and forgiveness 25%. Carry numbers are the testers' averages. Their swings may be faster than a typical senior's, so focus on <b>the differences between models</b> rather than the yardages themselves.</p>" + \
B.table(["Model", "US price", "Overall", "Accuracy", "Distance", "Forgiveness", "Carry (yd)"], [
 ["Mizuno JPX One", "$279.99", "<b>9.3</b>", "9.8", "8.8", "8.9", "168.8"],
 ["Callaway Quantum Max OS", "$319.99", "9.1", "9.2", "9.3", "8.9", "169.7"],
 ["Tour Edge Exotics Max", "$229.99", "9.0", "9.1", "9.5", "8.5", "171.3"],
 ["Cobra OPTM", "$329.99", "8.9", "9.0", "7.5", "9.9", "167.2"],
 ["PXG Lightning", "$329.99", "8.6", "8.5", "8.0", "9.4", "167.5"],
 ["TaylorMade Qi4D", "$299.99", "8.1", "7.4", "9.4", "8.2", "170.8"]]) + \
"<p style='font-size:.85rem;color:var(--muted)'>Source: MyGolfSpy Best Hybrids of 2026. In the same table, the 2025-tested PING G440, Titleist GT3 and Srixon ZXi each scored 8.7.</p>" + \
"<h2>2. Pros and cons by model</h2>" + \
card("Mizuno", "JPX One Hybrid", "$279.99", "MyGolfSpy's 2026 overall and accuracy winner; Golf Monthly's pick for high launch and NCG's for forgiveness.",
     ["Straightest in the test (9.8 accuracy)", "Golf Monthly: a good option if you struggle to get the ball in the air", "NCG: ball speed and spin stay tight across the face, with real stopping power"],
     ["One of the highest-spinning hybrids in MyGolfSpy's test", "High-gloss crown won't appeal to everyone"],
     "Golfers who can't get the ball up, or want an easier long-iron replacement", ko=False) + \
card("Titleist", "GT1 Hybrid", "$329", "Golf Monthly's top senior hybrid. Lofts 20, 23, 26 and 29°.",
     ["Golf Monthly: a great fit for seniors with slower swing speeds", "Lightweight and easy to launch, with adjustable weights and hosel", "NCG's tester saw launch angles past 40 degrees"],
     ["Not quite as powerful as others in the GT line", "NCG: spin and a slight draw bias won't suit those wanting a lower, neutral flight"],
     "Seniors with low ball flight, or anyone bridging fairway woods and irons", ko=False) + \
card("PING", "G440 Hybrid", "$269–$299.99", "Golf Monthly's most forgiving hybrid, offered from 17 to 34°.",
     ["Golf Monthly: ease of launch will please many slower-swinging seniors", "NCG: very forgiving with a high, consistent flight", "Shallow face helps launch"],
     ["Little cosmetic change from the previous model", "May look large if you like a compact hybrid"],
     "Golfers who mishit often and want easy (prices vary by outlet)", ko=False) + \
card("Callaway", "Quantum Max OS Hybrid", "$319.99", "MyGolfSpy's runner-up, Golf Monthly's best from any lie, NCG's best draw bias.",
     ["Accuracy, distance and forgiveness all strong", "Straight, high flight with excellent turf interaction", "Draw bias tames a slice"],
     ["Larger footprint than most hybrids", "Hosel adjustment called complicated"],
     "Slicers and golfers who value consistency above all", ko=False) + \
card("TaylorMade", "Qi4D Max Hybrid", "$299.99", "Golf Monthly's best hybrid for slicers. Lofts 20 to 34°.",
     ["Golf Monthly: the right miss was far less apparent", "Rear weighting aids launch", "Impressive distance and forgiveness"],
     ["No adjustability", "Scored 8.4 at MyGolfSpy, below the leaders"],
     "Slicers who don't need adjustability", ko=False) + \
card("Tour Edge", "Exotics Max Hybrid", "$229.99", "MyGolfSpy's #3 overall and best for distance, at the lowest price of the leaders.",
     ["Top distance score in the test (9.5)", "Cheapest of the top finishers"],
     ["Forgiveness only average", "No adjustability; bonded build feels dated to testers"],
     "Budget buyers who want distance", ko=False) + \
"<h2>3. How seniors should choose</h2>" + \
B.check([
 "<b>Which irons to replace:</b> Golf Monthly says that from around 200 yards and beyond, a hybrid is often more forgiving and effective than a long iron. Start with the 3- and 4-iron, and add the 5 if it's hard to launch.",
 "<b>Loft:</b> Lofts vary by maker. Choose by <b>loft angle</b>, not the number on the sole, so the hybrid goes one club longer than your longest iron without overlapping.",
 "<b>Shaft:</b> MyGolfSpy notes that flex should match swing speed to get the right flight. If you're moving from steel to graphite irons, consider a light graphite senior (A) flex in your hybrids too.",
 "<b>Spin:</b> If you already launch it high with lots of spin, high-spin heads like the Mizuno JPX One or Wilson DYNAPWR may cost you distance."]) + \
"<h3>Quick picks</h3>" + B.table(["If you...", "Try"], [
 ["want the straightest hybrid", "Mizuno JPX One"],
 ["struggle to get the ball up", "Titleist GT1, Mizuno JPX One"],
 ["mishit often", "PING G440, Cobra OPTM"],
 ["fight a slice", "Callaway Quantum Max OS, TaylorMade Qi4D Max"],
 ["are on a budget", "Tour Edge Exotics Max ($229.99)"]]) + \
"<p>Hybrids often see solid Black Friday discounts, and one- or two-season-old models are easy to find in good used condition. Golf Monthly listed deals of $269.99 for the Callaway Quantum Max OS and $249 for the Cobra OPTM (prices change). Because you can buy just one, a hybrid is the cheapest way to change your game without replacing your iron set.</p>" + \
"<div class='note'><b>How many irons should you replace?</b> Enter your 7-iron distance in our iron calculator for head type and shaft picks — a good starting point for deciding where hybrids should take over.</div>"

P = dict(file="blog-senior-hybrids-2026.html", bg="hyb", calc="iron",
 cat_ko="시니어 · 하이브리드", cat_en="Seniors & hybrids",
 title_ko="시니어 롱아이언 대신 하이브리드: 2026 테스트 1위 Mizuno JPX One 외 5종 비교",
 title_en="Hybrids to replace long irons for seniors: Mizuno JPX One and 5 more compared (2026)",
 desc_ko="MyGolfSpy 2026 하이브리드 테스트 1위 Mizuno JPX One과 Titleist GT1, PING G440, Callaway Quantum Max OS 등 느린 스윙 골퍼를 위한 하이브리드를 비교했습니다.",
 sub_ko="롱아이언이 안 뜬다면 하이브리드로 바꿀 때입니다. 2026 테스트 1위 모델과 시니어용 추천 모델을 데이터로 정리했습니다.",
 sub_en="If your long irons won't launch, it's time for hybrids. We compare the 2026 test winner and senior-friendly picks with real data.",
 cta_ko=("내 아이언 세팅부터 점검하세요","7번 아이언 거리만 넣으면 헤드 종류와 샤프트를 추천합니다.","아이언 계산기 열기"),
 cta_en=("Check your iron setup first","Enter your 7-iron distance for head type and shaft picks.","Open the iron calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("MyGolfSpy — Best Hybrid Golf Clubs of 2026","https://mygolfspy.com/buyers-guides/hybrids/best-hybrid-golf-clubs-of-2026/"),
  ("MyGolfSpy — Mizuno Just Pulled Off The Most Unexpected Equipment Sweep Of 2026","https://mygolfspy.com/news-opinion/mizuno-just-pulled-off-the-most-unexpected-equipment-sweep-of-2026/"),
  ("Golf Monthly — Best Hybrid Golf Clubs For Seniors 2026","https://www.golfmonthly.com/best-golf-deals/best-hybrid-golf-clubs-for-seniors-208967"),
  ("National Club Golfer — Best hybrids for seniors 2026","https://www.nationalclubgolfer.com/us/best-golf-deals/best-hybrids-for-seniors/")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
print("ok")
