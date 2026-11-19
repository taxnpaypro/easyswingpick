import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import build as B
B.HERO_BG["woods"] = "radial-gradient(120% 120% at 80% 0%,#2c4f63 0%,#14303f 55%,#081a24 100%)"
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

SMALL = "style='font-size:.85rem;color:var(--muted)'"

# ------------------------------------------------------------------ KOREAN
KO = STY + B.tldr("핵심 요약", [
 b("누구에게:")+"4·5번 아이언이 잘 안 뜨고, 하이브리드도 손에 잘 안 맞는 분",
 b("로프트:")+"7번 우드는 약 21°(4번 아이언·3~4번 하이브리드 자리), 9번 우드는 약 23~26°(5번 아이언·4~5번 하이브리드 자리)",
 b("먼저 볼 모델:")+"Mizuno JPX One(7W·9W), TaylorMade Qi4D Max(7W·9W), Callaway Quantum Max(7·9·11W), PING G440 MAX(최대 24°)"]) + \
"<p>롱아이언을 하이브리드로 바꿨는데도 여전히 공이 낮게 날아가거나, 하이브리드가 손에 잘 맞지 않는 분이 많습니다. 이럴 때 요즘 다시 주목받는 클럽이 <b>7번 우드와 9번 우드</b>입니다. 예전에는 '시니어·여성용'이라는 인식이 강했지만, MyGolfSpy가 집계한 PGA 투어 우승자 클럽 구성 38개 중 <b>12개에 7번 우드</b>가 들어 있었을 만큼 이제는 투어 선수들도 많이 씁니다. 최근에는 PING이 투어에서 공개한 신제품 G450 MAX 7번 우드(21°)를 Tyrrell Hatton이 바로 백에 넣었고, Mizuno도 9번 우드까지 포함된 새 JPX One Max 페어웨이우드를 USGA 적합 목록에 올렸습니다.</p>" + \
"<p>MyGolfSpy는 \"로프트 높은 페어웨이우드는 느린 스윙만을 위한 해결책이 아니다\"라고 하면서도, 롱아이언 사이 거리 차이가 사라지는 문제는 <b>스윙 속도가 줄수록 특히 흔하다</b>고 설명합니다. 그래서 헤드스피드가 줄어든 시니어 골퍼에게 특히 검토할 가치가 있습니다. 이 글에서는 MyGolfSpy, National Club Golfer(NCG), Golf365의 테스트·리뷰를 바탕으로 7·9번 우드가 맞는 사람과 모델별 장단점, 미국 가격을 정리했습니다.</p>" + \
"<h2>1. 7번·9번 우드는 어떤 클럽을 대신하나</h2>" + \
"<p>MyGolfSpy가 정리한 표를 기준으로 보면 다음과 같습니다. 로프트는 제조사마다 1~2° 차이가 있으니 숫자(7W·9W)보다 <b>로프트 각도</b>로 비교하세요.</p>" + \
B.table(["클럽", "보통 로프트", "대신하는 클럽"], [
 ["7번 우드", "20~23°", "3·4번 하이브리드, 3·4번 아이언"],
 ["9번 우드", "23~26°", "4·5번 하이브리드, 4·5번 아이언"],
 ["하이브리드", "19~26°", "롱아이언"],
 ["롱아이언", "18~25°", "—"]]) + \
f"<p {SMALL}>※ 출처: MyGolfSpy \"Who Would Benefit From A High-Lofted Fairway Wood?\". 골프 용품점 ParWest 가이드는 11번 우드를 26~28°로 소개합니다.</p>" + \
"<p>MyGolfSpy가 든 예시가 이해하기 쉽습니다. 5번 아이언 캐리가 170야드인데 4번 아이언이 174야드라면 <b>두 클럽을 다 들고 다닐 이유가 거의 없습니다.</b> 이럴 때 4번 아이언 자리에 7번 우드를 넣으면 롱아이언보다 볼 스피드가 빠르고 더 높이 떠서, 5번 아이언보다 10~15야드 더 보내는 클럽이 될 수 있다고 합니다. 또 같은 캐리 거리라도 <b>더 높이 올라가고 더 가파르게 떨어져</b> 그린에 잘 섭니다.</p>" + \
"<h2>2. 하이브리드 대신 우드가 맞는 경우</h2>" + \
"<p>하이브리드와 7번 우드는 로프트가 겹치지만 성격이 다릅니다. Golf365는 페어웨이우드가 하이브리드보다 <b>솔이 넓고 무게중심이 낮으며 샤프트가 조금 더 길다</b>고 설명합니다. 페이스가 얕아 라이가 좋지 않을 때도 공을 띄우기 쉽다는 평가입니다. 반면 아이언만큼 구질을 만들기는 어렵습니다.</p>" + \
B.table(["", "7번 우드", "하이브리드"], [
 ["탄도", "더 높게, 부드럽게 떨어짐", "중간~높음, 런이 더 많음"],
 ["깊은 러프", "보통", "더 쉬움 (ParWest)"],
 ["길이·크기", "샤프트가 길고 헤드가 큼", "짧고 작아 아이언 느낌"]]) + \
f"<p {SMALL}>※ 탄도·러프 비교는 Golf365, ParWest 설명 기준입니다. 개인차가 크니 두 클럽 모두 시타해 보세요.</p>" + \
B.check([
 "<b>22° 하이브리드가 잘 안 맞는다면:</b> MyGolfSpy는 7번 우드를 시도해 보라고 권합니다. 24~25° 하이브리드라면 9번 우드를 비교해 보세요.",
 "<b>그린에 공이 안 선다면:</b> 7번 우드는 하이브리드보다 스핀이 많고 높게 떠서 굴러가는 거리가 짧습니다(ParWest).",
 "<b>러프에서 자주 친다면:</b> 깊은 러프는 하이브리드가 더 쉽다는 평가도 있으니 둘 다 쳐 보고 고르세요.",
 "<b>헤드스피드가 많이 느리다면:</b> ParWest는 드라이버 스윙 스피드 85mph 미만이면 9번·11번 우드를 고려하라고 합니다(판매점의 경험칙으로, 테스트 데이터는 아님). 내 헤드스피드는 드라이버 계산기에서 거리만 넣으면 추정할 수 있습니다."]) + \
"<h2>3. 2026 페어웨이우드 테스트에서 눈에 띈 모델</h2>" + \
"<p>MyGolfSpy의 2026 페어웨이우드 테스트(20개 모델, 6,000샷)는 대부분 <b>15° 3번 우드</b>로 진행됐습니다. 7·9번 우드 자체의 데이터는 아니지만, 같은 헤드 설계를 높은 로프트로 쓰기 때문에 헤드 성격(정확도·관용성)을 비교하는 데는 참고가 됩니다. 점수는 10점 만점이며 정확도 40%, 거리 40%, 관용성 20%입니다.</p>" + \
B.table(["모델", "종합", "정확도", "거리", "관용성", "높은 로프트"], [
 ["Mizuno JPX One", "<b>8.9</b>", "9.2", "8.5", "9.4", "7W·9W"],
 ["Callaway Quantum Max D", "<b>8.9</b>", "9.5", "8.6", "8.4", "3HL(드로우)"],
 ["TaylorMade Qi4D", "8.8", "8.6", "9.2", "8.4", "7W·9W"],
 ["Tour Edge Exotics Max", "8.6", "8.9", "7.7", "9.7", "—"],
 ["Callaway Quantum Max", "8.5", "8.1", "9.2", "7.8", "7W·9W·11W"]]) + \
f"<p {SMALL}>※ 점수 출처: MyGolfSpy Best Fairway Woods of 2026. '높은 로프트' 칸은 ParWest 판매 페이지 기준이며, Exotics Max는 이번에 확인한 자료에 7·9번 우드 표기가 없었습니다.</p>" + \
"<h2>4. 모델별 장단점과 미국 가격</h2>" + \
card("Mizuno", "JPX One Fairway (7W 21° · 9W 24°)", "$299.99~$349.99", "MyGolfSpy 2026 페어웨이우드 종합 1위. Golf365는 7번 우드 실전 테스트에서 '2026 최고의 7번 우드 후보'로 다뤘습니다.",
     ["관용성 9.4·정확도 9.2로 매우 안정적", "NCG: '띄우기 아주 쉽고' 잔디 위에서 관용성이 좋음", "7번 우드는 ±2° 로프트 조절·업라이트 설정 가능(Golf365)"],
     ["MyGolfSpy: 거리는 '평균 수준'", "스핀이 많은 편이라 원래 스핀이 많은 분은 거리 손해"],
     "가장 곧고 일정한 우드를 원하는 분, 공이 잘 안 뜨는 분") + \
card("TaylorMade", "Qi4D Max Fairway (7W 21° · 9W 24°)", "$379", "NCG 시니어 페어웨이우드 목록 첫 모델. 높은 탄도와 관용성이 강점입니다.",
     ["NCG: 띄우기 쉽고 탄도가 높으며 관용성이 높음", "7번·9번 우드 둘 다 선택 가능"],
     ["NCG: '가장 멀리 나가는 우드는 아님'", "가격대가 높은 편"],
     "거리보다 쉽게 띄우는 것이 우선인 분") + \
card("Callaway", "Quantum Max / Max Fast (7W · 9W · 11W)", "$399.99~$429.99", "MyGolfSpy 테스트 거리 2위·볼 스피드 1위 헤드. ParWest 기준 7·9·11번 우드까지 고를 수 있습니다.",
     ["테스트 평균 볼 스피드 1위", "11번 우드까지 있어 5번 아이언 자리도 대체 가능", "경량 'Max Fast' 버전 선택 가능"],
     ["MyGolfSpy: 정확도·관용성은 하위권", "가장 비싼 편"],
     "거리 손실이 가장 아쉬운 분, 11번 우드까지 쓰려는 분") + \
card("PING", "G440 MAX Fairway (15~24°)", "$349", "NCG 시니어 추천. 로프트가 24°(9번 우드급)까지 나오고 초경량 HL 옵션이 있습니다.",
     ["NCG: 띄우기 쉽고 관용성이 매우 높음", "HL 버전은 ALTA Quick 35/45 초경량 샤프트", "G450 출시 예정으로 할인 가능성(블프 글 참고)"],
     ["신제품 G450이 2027년 초 출시 예상", "새 모델이 나오면 재고 로프트·샤프트 선택이 줄 수 있음"],
     "가벼운 샤프트가 필요한 시니어, 할인 모델을 노리는 분") + \
card("Wilson", "DYNAPWR MAX Fairway (15·18·21°)", "$279.99", "NCG 목록 중 가장 저렴한 축. 경량 샤프트(UST Helium NCT 4)를 선택할 수 있습니다.",
     ["NCG: 관용성이 좋고 탄도가 높음", "가격 부담이 적음"],
     ["NCG: 볼 스피드는 다른 모델보다 느린 편", "9번 우드급(23° 이상) 로프트는 확인되지 않음"],
     "예산을 아끼면서 7번 우드(21°)를 처음 써 보려는 분") + \
"<h2>5. 시니어 골퍼를 위한 선택 체크리스트</h2>" + \
B.check([
 "<b>거리 간격부터:</b> 지금 가장 긴 아이언과 그다음 아이언의 캐리 차이가 5야드 안팎이면, 긴 쪽을 7번(또는 9번) 우드로 바꿀 후보입니다.",
 "<b>5번 우드와 겹치지 않게:</b> 5번 우드는 보통 18~19°입니다. 7번 우드(21°)와 3° 정도 차이가 나야 거리가 겹치지 않습니다.",
 "<b>샤프트:</b> MyGolfSpy는 요즘 페어웨이우드 샤프트가 대부분 그래파이트라고 합니다. 드라이버와 같은 강도·비슷한 무게대로 맞추면 무난하고, 가벼운 HL·경량 옵션도 확인하세요.",
 "<b>슬라이스가 있다면:</b> Golf365에 따르면 로프트를 올리거나 업라이트로 설정하면 오른쪽 미스를 줄이는 데 도움이 됩니다.",
 "<b>새 제품 vs 지난 모델:</b> PING G450, Mizuno JPX One Max 등 2027년 신제품이 대기 중이라, 지금은 2026 모델 할인과 중고를 노리기 좋은 시기입니다."]) + \
"<h3>한눈에 보는 추천</h3>" + B.table(["이런 분이라면", "추천"], [
 ["4번 아이언이 5번과 거리가 같다", "7번 우드 (약 21°)"],
 ["5번 아이언·24° 하이브리드도 어렵다", "9번 우드 (약 24°)"],
 ["가장 곧게 치고 싶다", "Mizuno JPX One"],
 ["쉽게 높이 띄우고 싶다", "TaylorMade Qi4D Max, PING G440 MAX"],
 ["거리 손실이 제일 아쉽다", "Callaway Quantum Max"],
 ["예산이 중요", "Wilson DYNAPWR MAX ($279.99)"]]) + \
"<p>가격은 판매처와 시점에 따라 다릅니다. 예를 들어 Mizuno JPX One은 MyGolfSpy 표기 $349.99, NCG $350, ParWest $299.99로 차이가 있었습니다. 7·9번 우드는 한 개만 사도 되기 때문에, 중고로 상태 좋은 지난 모델을 찾으면 부담 없이 시도해 볼 수 있습니다.</p>" + \
"<h3>이 글에서 다룬 모델 가격 보기</h3>" + B.picks([
 ("테스트 1위", "Mizuno JPX One Fairway", "7W·9W. 가장 곧고 관용성 높은 헤드."),
 ("쉽게 띄우기", "TaylorMade Qi4D Max Fairway", "높은 탄도, 7W·9W 선택."),
 ("거리·11번 우드", "Callaway Quantum Max Fairway", "볼 스피드 1위 헤드, 7·9·11W."),
 ("경량·할인 노리기", "PING G440 MAX Fairway", "최대 24°, HL 초경량 옵션.")]) + \
"<div class='note'><b>롱아이언 어디까지 바꿀까?</b> 아이언 계산기에 7번 아이언 거리를 넣으면 헤드 종류와 샤프트를 추천해 드립니다. 하이브리드가 고민이라면 <a href='/blog/senior-hybrids-2026'>시니어 하이브리드 비교</a>도 함께 보세요.</div>"

# ------------------------------------------------------------------ ENGLISH
EN = STY + B.tldr("QUICK TAKE", [
 b("Who it's for:")+"golfers whose 4- and 5-irons won't launch, or who never got comfortable with hybrids",
 b("Lofts:")+"a 7-wood is about 21° (4-iron / 3–4 hybrid slot); a 9-wood is about 23–26° (5-iron / 4–5 hybrid slot)",
 b("Models to try first:")+"Mizuno JPX One (7W, 9W), TaylorMade Qi4D Max (7W, 9W), Callaway Quantum Max (7, 9, 11W), PING G440 MAX (up to 24°)"]) + \
"<p>Plenty of golfers swap long irons for hybrids and still see low shots or a hybrid they never quite trust. That's where the <b>7-wood and 9-wood</b> come in. They used to be seen as clubs for seniors and beginners, but MyGolfSpy found a <b>7-wood in 12 of the 38 PGA Tour-winning bags</b> it tracked. The trend is still moving: PING's new G450 MAX 7-wood (21°) went straight into Tyrrell Hatton's bag at its tour launch, and Mizuno's new JPX One Max fairway woods, including a 9-wood, just appeared on the USGA conforming list.</p>" + \
"<p>MyGolfSpy stresses that \"high-lofted fairway woods are not solutions just for slow swing speed players,\" but notes that long-iron gapping problems are <b>particularly common as swing speed decreases</b>. That makes them well worth a look for senior golfers who have lost some speed. Below we use testing and reviews from MyGolfSpy, National Club Golfer (NCG) and Golf365 to explain who should carry a 7- or 9-wood, the pros and cons of each model, and current US prices.</p>" + \
"<h2>1. What a 7-wood and 9-wood replace</h2>" + \
"<p>Here is MyGolfSpy's breakdown. Lofts vary by a degree or two between brands, so compare <b>loft angles</b>, not the number on the sole.</p>" + \
B.table(["Club", "Typical loft", "Replaces"], [
 ["7-wood", "20–23°", "3/4-hybrid, 3/4-iron"],
 ["9-wood", "23–26°", "4/5-hybrid, 4/5-iron"],
 ["Hybrid", "19–26°", "Long irons"],
 ["Long iron", "18–25°", "—"]]) + \
f"<p {SMALL}>Source: MyGolfSpy, \"Who Would Benefit From A High-Lofted Fairway Wood?\" Retailer ParWest lists an 11-wood at 26–28°.</p>" + \
"<p>MyGolfSpy's example makes the point: if your 5-iron carries 170 yards and your 4-iron carries 174, <b>there really isn't much reason to carry both.</b> A 7-wood in that slot can give you more ball speed and a higher launch than the long iron it replaces, potentially going 10 or 15 yards farther than your 5-iron. It can also produce a similar carry with a <b>higher peak height and a steeper descent</b>, so the ball stops faster on the green.</p>" + \
"<h2>2. When a wood beats a hybrid</h2>" + \
"<p>A hybrid and a 7-wood can share the same loft but behave differently. Golf365 points out that a fairway wood has a <b>wider sole, a lower center of gravity and a slightly longer shaft</b> than a hybrid, and its shallow face makes it easier to launch from a poor lie. The trade-off: it isn't as workable as an iron.</p>" + \
B.table(["", "7-wood", "Hybrid"], [
 ["Ball flight", "Higher, lands softer", "Mid to high, more roll"],
 ["Thick rough", "Average", "Easier (ParWest)"],
 ["Length & size", "Longer shaft, bigger head", "Shorter, more iron-like"]]) + \
f"<p {SMALL}>Flight and rough notes are from Golf365 and ParWest. Results vary by golfer, so test both.</p>" + \
B.check([
 "<b>Can't hit your 22° hybrid?</b> MyGolfSpy suggests trying a 7-wood. If your hybrid is 24–25°, test a 9-wood.",
 "<b>Shots won't hold the green?</b> A 7-wood spins more and launches higher than a hybrid, so it rolls out less (ParWest).",
 "<b>Often in the rough?</b> Some testers find a hybrid easier from thick rough, so hit both before you buy.",
 "<b>Very slow swing?</b> ParWest suggests a 9- or 11-wood if your driver swing speed is under 85 mph (a retailer's rule of thumb, not test data). Our driver calculator estimates your speed from your driver distance."]) + \
"<h2>3. Standouts from the 2026 fairway wood test</h2>" + \
"<p>MyGolfSpy's 2026 fairway wood test (20 models, 6,000 shots) used mostly <b>15° 3-woods</b>. It isn't 7- or 9-wood data, but the higher lofts share the same head design, so it's a useful guide to each head's accuracy and forgiveness. Scores are out of 10, weighted 40% accuracy, 40% distance and 20% forgiveness.</p>" + \
B.table(["Model", "Overall", "Accuracy", "Distance", "Forgiveness", "High lofts"], [
 ["Mizuno JPX One", "<b>8.9</b>", "9.2", "8.5", "9.4", "7W, 9W"],
 ["Callaway Quantum Max D", "<b>8.9</b>", "9.5", "8.6", "8.4", "3HL (draw)"],
 ["TaylorMade Qi4D", "8.8", "8.6", "9.2", "8.4", "7W, 9W"],
 ["Tour Edge Exotics Max", "8.6", "8.9", "7.7", "9.7", "—"],
 ["Callaway Quantum Max", "8.5", "8.1", "9.2", "7.8", "7W, 9W, 11W"]]) + \
f"<p {SMALL}>Scores: MyGolfSpy Best Fairway Woods of 2026. High-loft options are from ParWest's listings; we found no 7- or 9-wood listing for the Exotics Max in the sources we read.</p>" + \
"<h2>4. Pros, cons and US prices by model</h2>" + \
card("Mizuno", "JPX One Fairway (7W 21° · 9W 24°)", "$299.99–$349.99", "MyGolfSpy's 2026 best overall fairway wood. Golf365 tested the 7-wood on course as a contender for best 7-wood of 2026.",
     ["Very consistent: 9.4 forgiveness, 9.2 accuracy", "NCG: extremely easy to launch and forgiving off the turf", "7-wood has 2° of loft adjustability and an upright setting (Golf365)"],
     ["MyGolfSpy: distance is merely average", "Spins a lot, which costs distance for high-spin players"],
     "Golfers who want the straightest, most consistent wood, or struggle to get the ball up", ko=False) + \
card("TaylorMade", "Qi4D Max Fairway (7W 21° · 9W 24°)", "$379", "First pick on NCG's senior fairway wood list, built for high launch and forgiveness.",
     ["NCG: easy to launch, high flight, very forgiving", "Offered as both a 7-wood and a 9-wood"],
     ["NCG: definitely not the longest fairway wood", "On the pricier side"],
     "Golfers who care more about easy launch than raw distance", ko=False) + \
card("Callaway", "Quantum Max / Max Fast (7W · 9W · 11W)", "$399.99–$429.99", "The head with the #2 distance and #1 ball speed in MyGolfSpy's test, offered up to an 11-wood (ParWest).",
     ["Fastest average ball speed in the test", "11-wood option can cover the 5-iron slot", "Lighter Max Fast version available"],
     ["MyGolfSpy: near the bottom for accuracy and forgiveness", "Among the most expensive"],
     "Golfers who miss distance most, or want an 11-wood", ko=False) + \
card("PING", "G440 MAX Fairway (15–24°)", "$349", "An NCG senior pick with lofts up to 24° (9-wood territory) and an ultralight HL option.",
     ["NCG: easy to launch and very forgiving", "HL build uses ultralight ALTA Quick 35/45 shafts", "G450 is coming, so watch for G440 discounts (see our Black Friday post)"],
     ["The new G450 is expected in early 2027", "Loft and shaft choices may thin out once stock clears"],
     "Seniors who need a light shaft, or deal hunters", ko=False) + \
card("Wilson", "DYNAPWR MAX Fairway (15, 18, 21°)", "$279.99", "One of the most affordable on NCG's list, with a lightweight UST Helium NCT 4 shaft option.",
     ["NCG: forgiving with a high flight", "Easy on the budget"],
     ["NCG: not as quick as other models", "No 23°+ (9-wood) loft found in our sources"],
     "Budget buyers trying a 21° 7-wood for the first time", ko=False) + \
"<h2>5. Checklist for senior golfers</h2>" + \
B.check([
 "<b>Start with your gaps:</b> if your two longest irons carry within about 5 yards of each other, the longer one is a candidate for a 7- (or 9-) wood.",
 "<b>Don't overlap your 5-wood:</b> a 5-wood is usually 18–19°. Leave about 3° to a 21° 7-wood so the distances don't overlap.",
 "<b>Shaft:</b> MyGolfSpy notes nearly all fairway wood shafts are graphite now. Matching your driver's flex and a similar weight is a safe start; check HL or lightweight options too.",
 "<b>Fighting a slice?</b> Golf365 says adding loft or an upright setting can help reduce the right miss.",
 "<b>New vs last year:</b> with PING G450 and Mizuno JPX One Max on the way for 2027, now is a good time to look for 2026 discounts and used clubs."]) + \
"<h3>Quick picks</h3>" + B.table(["If you...", "Try"], [
 ["hit your 4-iron as far as your 5-iron", "7-wood (about 21°)"],
 ["struggle with the 5-iron and a 24° hybrid", "9-wood (about 24°)"],
 ["want the straightest wood", "Mizuno JPX One"],
 ["want easy, high launch", "TaylorMade Qi4D Max, PING G440 MAX"],
 ["miss distance most", "Callaway Quantum Max"],
 ["are on a budget", "Wilson DYNAPWR MAX ($279.99)"]]) + \
"<p>Prices vary by store and date. For example, the Mizuno JPX One was listed at $349.99 by MyGolfSpy, $350 by NCG and $299.99 by ParWest. Because you only need one, a lightly used previous model is a low-risk way to try a 7- or 9-wood.</p>" + \
"<h3>Check prices on models in this guide</h3>" + B.picks([
 ("Test winner", "Mizuno JPX One Fairway", "7W and 9W. Straightest, most forgiving head."),
 ("Easy launch", "TaylorMade Qi4D Max Fairway", "High flight, 7W or 9W."),
 ("Distance & 11-wood", "Callaway Quantum Max Fairway", "Fastest ball speed head, 7/9/11W."),
 ("Light & on sale", "PING G440 MAX Fairway", "Up to 24°, ultralight HL option.")], ko=False) + \
"<div class='note'><b>How far should the woods go down your bag?</b> Enter your 7-iron distance in our iron calculator for head type and shaft picks. Weighing hybrids instead? See our <a href='/blog/senior-hybrids-2026'>senior hybrid comparison</a>.</div>"

P = dict(file="blog-senior-7-wood-9-wood.html", bg="woods", calc="iron",
 cat_ko="시니어 · 페어웨이우드", cat_en="Seniors & fairway woods",
 title_ko="시니어 7번·9번 우드 가이드: 롱아이언·하이브리드가 어렵다면 (2026)",
 title_en="7-wood and 9-wood for seniors: when long irons and hybrids won't launch",
 desc_ko="7번 우드(약 21°)·9번 우드(약 24°)가 대신하는 클럽, 하이브리드와 차이, Mizuno JPX One·TaylorMade Qi4D Max·Callaway Quantum Max·PING G440 MAX 장단점과 미국 가격을 정리했습니다.",
 sub_ko="롱아이언을 하이브리드로 바꿨는데도 공이 안 뜬다면 다음 답은 7·9번 우드입니다. 로프트, 하이브리드와 차이, 2026 테스트 모델을 정리했습니다.",
 sub_en="If hybrids didn't fix your long game, a 7- or 9-wood might. Lofts, wood vs hybrid, and the 2026 test standouts.",
 cta_ko=("내 롱게임 세팅부터 점검하세요","7번 아이언 거리만 넣으면 헤드 종류와 샤프트를 추천합니다.","아이언 계산기 열기"),
 cta_en=("Check your long-game setup first","Enter your 7-iron distance for head type and shaft picks.","Open the iron calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("MyGolfSpy — Who Would Benefit From A High-Lofted Fairway Wood?","https://mygolfspy.com/news-opinion/instruction/who-would-benefit-from-a-high-lofted-fairway-wood/"),
  ("MyGolfSpy — Best Fairway Woods of 2026","https://mygolfspy.com/buyers-guides/fairway-woods/best-fairway-woods-of-2026/"),
  ("National Club Golfer — Best Fairway Woods for Senior Golfers 2026","https://www.nationalclubgolfer.com/us/best-golf-deals/best-fairway-woods-for-senior-golfers/"),
  ("Golf365 — The best 7-wood of 2026? Mizuno JPX One 7-Wood tested on course","https://www.golf365.com/news/the-best-7-wood-of-2026-mizuno-jpx-one-7-wood-tested-on-course"),
  ("ParWest Golf — 7-Wood, 9-Wood And 3HL guide","https://www.parwestgolf.com/blogs/content/7-wood-9-wood-3hl-guide"),
  ("Golf.com — Ping 'Tour Launches' new driver, metalwoods with success","https://golf.com/gear/ping-tour-launches-new-driver-woods-with-success-tour-report/"),
  ("MyGolfSpy — New GTS Hybrids, Mizuno Max and Srixon Blade: What The USGA List Just Revealed","https://mygolfspy.com/news-opinion/new-gts-hybrids-mizuno-max-and-srixon-blade-what-the-usga-list-just-revealed/")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
print("ok")
