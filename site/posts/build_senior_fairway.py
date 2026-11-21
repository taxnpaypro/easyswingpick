import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import build as B
B.HERO_BG["fw"] = "radial-gradient(120% 120% at 80% 0%,#1f4f5e 0%,#0f2e38 55%,#07181e 100%)"
b = lambda s: f"<b style='display:inline;color:#fff'>{s}</b> "
from build_senior_hybrids import STY, card  # same model-card style as the hybrids post

SM = "<p style='font-size:.85rem;color:var(--muted)'>{}</p>"

# ------------------------------------------------------------------ KOREAN
KO = STY + B.tldr("핵심 요약", [
 b("3번 우드가 어렵다면:")+"로프트가 큰 5번(18° 전후)·7번(21° 전후) 우드가 더 쉽게 뜨고 그린에 잘 섭니다.",
 b("로봇 테스트 결론:")+"Golf Digest가 3번 우드 14개를 로봇으로 친 결과, 스핀이 많은 헤드일수록 빗맞아도 거리 손해가 적었습니다.",
 b("시니어 추천:")+"관용성은 TaylorMade Qi4D Max·PING G440 Max, 정확도는 Mizuno JPX One, 가성비는 Wilson DYNAPWR Max ($279.99)"]) + \
"<p>드라이버 다음으로 긴 클럽인 <b>3번 우드</b>는 많은 시니어 골퍼에게 가방 안에서 가장 어려운 클럽입니다. 로프트가 15° 안팎으로 작아서, 헤드스피드가 줄면 잔디 위에 놓인 공을 충분히 띄우기 어렵기 때문입니다. 그래서 요즘은 3번 우드 대신 <b>5번·7번, 심지어 9번 우드</b>를 넣는 골퍼가 늘고 있습니다. MyGolfSpy는 롱아이언을 일관되게 치기 어려운 현상이 \"스윙 속도가 줄수록 특히 흔하다\"고 설명합니다.</p>" + \
"<p>마침 Golf Digest가 10월 30일 <b>3번 우드 14개를 스윙 로봇으로 테스트</b>한 결과를 발표했습니다. 이 글에서는 그 로봇 테스트에서 시니어에게 의미 있는 결과, MyGolfSpy의 2026 페어웨이우드 테스트에서 정확도 2위를 한 Mizuno JPX One, 그리고 National Club Golfer(NCG)·GolfMagic의 시니어용 페어웨이우드 리뷰를 모아 <b>몇 번 우드를, 어떤 모델로</b> 고르면 좋을지 정리했습니다.</p>" + \
"<h2>1. Golf Digest 로봇 테스트: 3번 우드 14개에서 배운 것</h2>" + \
"<p>Golf Digest는 Golf Laboratories의 스윙 로봇으로 5개 브랜드 14개 3번 우드(기본 로프트 14.5~16°)를 시험했습니다. 헤드마다 18번씩, 정타 6번·토(앞쪽) 6번·힐(안쪽) 6번을 쳐서 스핀, 캐리, 볼 스피드, 빗맞았을 때 줄어드는 거리를 쟀습니다. 기사에 로봇의 스윙 속도는 나와 있지 않으므로 <b>거리 숫자 자체보다 모델 간 차이</b>를 보세요.</p>" + \
B.check([
 "<b>거리를 가른 건 스핀:</b> 정타 볼 스피드는 135~139.4mph로 큰 차이가 없었고, 캐리는 대략 <b>스핀 100rpm당 1야드</b>씩 달라졌습니다.",
 "<b>저스핀 헤드는 빗맞으면 손해가 큼:</b> 스핀이 가장 적은 5개 헤드는 힐에 맞았을 때 평균 <b>17.3야드</b>를 잃었고, 스핀이 가장 많은 5개 헤드는 <b>9.9야드</b>만 잃었습니다.",
 "<b>빗맞아도 거리 유지가 가장 좋았던 모델:</b> TaylorMade Qi4D Max(평균 7.1야드 손실), PING G440 SFT(9.1야드), Callaway Quantum Max D(9.5야드). Golf Digest는 2야드 정도 차이는 같은 수준으로 보라고 합니다.",
 "<b>가장 균형 잡힌 모델:</b> PING G440 Max는 볼 스피드가 가장 빨랐고(139.4mph), 정타·토·힐 평균 캐리 210.3야드로 2위였습니다. Golf Digest는 자신의 미스 방향을 모르는 골퍼에게 '가장 균형 잡힌 선택'이라고 했습니다."]) + \
B.table(["모델", "정타 캐리", "정타 스핀", "빗맞을 때", "한 줄 평"], [
 ["PING G440 LST", "224.9yd (1위)", "2,840rpm", "힐 타격 시 204.8yd", "가장 멀지만 스핀 편차가 가장 큼(±337rpm)"],
 ["Cobra OPTM LS", "218.2yd", "—", "—", "정타가 좋은 골퍼용 저스핀"],
 ["PING G440 Max", "—", "—", "힐 −10.5yd, 토 −10.6yd", "평균 캐리 210.3yd, 가장 균형적"],
 ["TaylorMade Qi4D Max", "206.2yd", "4,300rpm", "평균 −7.1yd (최소)", "빗맞음에 가장 강함"],
 ["PING G440 SFT", "—", "—", "평균 −9.1yd", "스핀 편차 최소(±126rpm), 슬라이스 보정"],
 ["Callaway Quantum Max D", "—", "—", "평균 −9.5yd", "발사각이 가장 일정(±0.19°)"]]) + \
SM.format("※ 출처: Golf Digest, \"Which 3-wood is right for you? We put 14 on the swing robot to find out\" (2026.10.30). '—'는 기사에 해당 숫자가 없는 항목입니다.") + \
"<p>시니어 골퍼에게 주는 의미는 분명합니다. 헤드스피드가 느리면 정타 확률도 낮아지기 쉽고, 공을 띄우려면 어느 정도 스핀이 필요합니다. Golf Digest도 \"타점이 힐 쪽으로 몰린다면 스핀이 많은 헤드가 지켜준다\"며, <b>자신의 미스를 먼저 알고 쇼핑하라</b>고 결론을 냈습니다. 투어 선수용 저스핀 모델(LST, LS, Tour)은 정타가 꾸준한 골퍼에게만 거리 보너스를 줍니다.</p>" + \
"<h2>2. 3번 vs 5번 vs 7번 vs 9번 우드</h2>" + \
"<p>MyGolfSpy는 로프트가 큰 페어웨이우드가 \"공을 띄우도록 만들어졌다\"고 설명합니다. 무게중심, 더 큰 헤드, 더 긴 샤프트, 더 큰 로프트가 모두 높이를 만들기 쉽게 해 준다는 것입니다. 아래는 MyGolfSpy가 제시한 일반적인 로프트 범위입니다.</p>" + \
B.table(["클럽", "일반적 로프트", "역할 (GolfMagic·MyGolfSpy)"], [
 ["3번 우드", "약 15°", "드라이버가 안 맞을 때 티샷 대안, 거리 손해가 적음"],
 ["5번 우드", "약 18°", "롱아이언보다 높게 뜨고 부드럽게 떨어짐, 페이스가 넓음"],
 ["7번 우드", "20~23°", "높은 탄도와 스핀으로 그린에 잘 섬"],
 ["9번 우드", "23~26°", "롱아이언·하이브리드를 대신하는 높은 탄도"],
 ["하이브리드", "19~26°", "아이언에 가까운 모양, 러프에서 다루기 쉬움"],
 ["롱아이언", "18~25°", "느린 스윙에서는 띄우기 어려움"]]) + \
SM.format("※ 3·5번 로프트는 대표값이며 제조사마다 다릅니다. 7·9번, 하이브리드, 롱아이언 범위는 MyGolfSpy 기준.") + \
B.check([
 "<b>3번 우드를 빼도 될까:</b> 페어웨이에서 3번 우드가 잘 안 뜬다면 5번 우드를 가장 긴 우드로 쓰는 것이 보통 더 쉽습니다. NCG 리뷰어도 \"추가 높이가 좋아서\" 16.5° 헤드(4번 우드)로 피팅받았다고 썼습니다.",
 "<b>하이브리드와 겹친다면:</b> MyGolfSpy는 \"잘 맞지 않는 22° 하이브리드가 있다면 7번 우드를 시도해 보라\"고 조언합니다.",
 "<b>거리 간격 확인:</b> MyGolfSpy의 예처럼 5번 아이언 170야드, 4번 아이언 174야드라면 두 클럽을 다 들고 다닐 이유가 거의 없습니다. 그 자리를 7번·9번 우드로 바꾸세요."]) + \
"<h2>3. 시니어에게 맞는 페어웨이우드 모델별 장단점</h2>" + \
card("TaylorMade", "Qi4D Max Fairway", "$379", "Golf Digest 로봇 테스트에서 빗맞았을 때 거리 손실이 가장 적었던 3번 우드. NCG 시니어 리스트 1순위.",
     ["로봇 테스트 평균 거리 손실 7.1야드로 최소, 한쪽 미스에서는 3.3야드만 손실", "NCG: 띄우기 쉽고 탄도가 높으며 관용성이 큼", "GolfMagic: 일반 Qi4D(185cc)보다 큰 200cc 헤드"],
     ["NCG: '가장 멀리 가는 페어웨이우드는 분명 아니다'", "스핀이 많아(정타 4,300rpm) 빠른 스윙에는 거리 손해"],
     "타점이 일정하지 않은 분, 파5 두 번째 샷과 긴 파4 세컨드샷이 고민인 분") + \
card("PING", "G440 Max Fairway", "$349", "로봇 테스트의 '가장 균형 잡힌' 모델. 로프트 15~24°로 7·9번 우드급까지 고를 수 있습니다.",
     ["볼 스피드 1위(139.4mph), 정타·미스 평균 캐리 2위", "스핀 편차 ±127rpm으로 매우 일정", "NCG: 띄우기 쉽고 관용성이 매우 큼"],
     ["로봇 테스트 최장 거리는 같은 PING의 LST 모델", "GolfMagic 기준 SFT(슬라이스용)·HL(느린 스윙용) 등 선택지가 많아 고르기 헷갈림"],
     "미스 방향을 잘 모르는 분. 슬라이스가 심하면 SFT, 스윙이 아주 느리면 HL 버전 확인") + \
card("Mizuno", "JPX One Fairway", "$350", "MyGolfSpy 2026 페어웨이우드 테스트 정확도 2위·관용성 2위(종합 8.9). 로프트 3·5·7번.",
     ["MyGolfSpy: 목표 근접 36.3야드로 20개 평균보다 약 9야드 가까움", "샷의 91% 이상이 '플레이 가능'", "NCG: 볼 스피드가 좋고 아주 쉽게 뜨며 잔디에서도 관용적"],
     ["MyGolfSpy 캐리 12위·총거리 14위 — 최장 거리용은 아님", "스핀이 많은 편이라 원래 스핀이 많은 분은 꼭 시타"],
     "거리보다 '어디로 갈지 아는' 우드를 원하는 분, 한국에서 Mizuno를 써 온 분") + \
card("Wilson", "DYNAPWR Max Fairway", "$279.99", "NCG 시니어 리스트에서 가장 저렴한 모델. 로프트 15·18·21°.",
     ["NCG: 관용성이 충분하고 탄도가 높음", "UST Helium NCT 4 경량 샤프트 선택 가능", "주요 브랜드보다 약 $70~100 저렴"],
     ["NCG: 다른 모델만큼 볼 스피드가 빠르지 않음", "조절 기능·샤프트 선택 폭이 상대적으로 좁음"],
     "예산을 아끼면서 가벼운 우드를 원하는 분") + \
card("Cobra", "OPTM Max Fairway", "$369.99", "띄우기·관용성·드로우 성향을 목표로 한 모델. FutureFit33 호젤로 로프트·라이 조절.",
     ["NCG: 볼 스피드가 좋고 조절 기능이 다양함", "드로우 성향으로 슬라이스 완화"],
     ["NCG 비교 시타에서 3개 모델 중 볼 스피드 최저·스핀 최고·캐리 최단", "같은 Cobra의 OPTM X는 로봇 테스트에서 미스 시 20.8야드 손실"],
     "슬라이스가 있고 로프트를 직접 조절해 보고 싶은 분") + \
"<h3>한눈에 비교</h3>" + B.table(["모델", "미국 정가", "로프트", "강점", "이런 분께"], [
 ["TaylorMade Qi4D Max", "$379", "—", "빗맞음 관용성 1위", "타점이 들쭉날쭉"],
 ["PING G440 Max", "$349", "15~24°", "균형·일관성", "미스 방향을 모름"],
 ["Mizuno JPX One", "$350", "3·5·7번", "정확도", "방향이 우선"],
 ["Wilson DYNAPWR Max", "$279.99", "15·18·21°", "가격·경량 샤프트", "예산 중시"],
 ["Cobra OPTM Max", "$369.99", "조절식", "드로우·조절 기능", "슬라이스"]]) + \
SM.format("※ 가격: NCG가 표기한 미국 권장소비자가(RRP). 할인·중고 가격은 시점에 따라 다릅니다. '—'는 출처에 로프트 정보가 없는 항목.") + \
"<h2>4. 고르는 순서 (체크리스트)</h2>" + \
B.check([
 "<b>① 미스 방향 확인:</b> 힐(안쪽)에 자주 맞으면 스핀이 많은 Max 계열, 정타가 꾸준하면 저스핀 모델도 고려 (Golf Digest).",
 "<b>② 가장 긴 우드의 로프트:</b> 3번(15°)이 안 뜨면 5번(18°)부터 시작. 4번 우드(16.5°)도 좋은 중간 선택입니다.",
 "<b>③ 샤프트:</b> GolfMagic은 \"가볍고 덜 단단한 샤프트는 더 높고 왼쪽으로 휘는 탄도를, 무겁고 단단한 샤프트는 낮은 탄도를 만든다\"고 설명합니다. 드라이버를 시니어(A) 플렉스로 쓰고 있다면 우드도 같은 강도로 맞추세요.",
 "<b>④ 시타·피팅:</b> 리뷰 숫자는 테스터 스윙 기준입니다. 같은 모델도 샤프트에 따라 달라지므로 구매 전 시타를 권합니다."]) + \
"<h2>상황별 추천</h2>" + B.picks([
 ("빗맞음이 잦다", "TaylorMade Qi4D Max", "로봇 테스트에서 미스 시 거리 손실이 가장 적었습니다."),
 ("무난한 첫 선택", "PING G440 Max", "15~24°까지 로프트가 다양하고 가장 균형적입니다."),
 ("방향이 우선", "Mizuno JPX One", "MyGolfSpy 정확도 2위, 3·5·7번 우드."),
 ("가성비·경량", "Wilson DYNAPWR Max", "$279.99, 경량 샤프트 선택 가능.")]) + \
"<p>7번·9번 우드로 롱아이언을 바꾸는 방법은 <a href='/blog/senior-7-wood-9-wood'>시니어 7번·9번 우드 가이드</a>에 따로 정리했습니다. 롱아이언 자리를 무엇으로 채울지 고민이라면 <a href='/blog/senior-hybrids-2026'>시니어를 위한 하이브리드 비교</a>를, 드라이버까지 가볍게 바꾸고 싶다면 <a href='/blog/lightweight-drivers'>느린 스윙을 위한 경량 드라이버 6종</a>을 함께 보세요. 연말 할인 시기는 <a href='/blog/black-friday-2026-clubs'>2026 블랙프라이데이 골프채 가이드</a>에 정리했습니다.</p>" + \
"<div class='note'><b>우드 샤프트 강도부터 맞추세요.</b> 드라이버 계산기에 스윙 정보를 넣으면 맞는 샤프트 강도와 무게를 알려 드립니다. 페어웨이우드도 보통 같은 강도 계열로 맞춥니다.</div>"

# ------------------------------------------------------------------ ENGLISH
EN = STY + B.tldr("QUICK TAKE", [
 b("If your 3-wood won't launch:")+"a higher-lofted 5-wood (about 18°) or 7-wood (about 21°) gets up easier and holds greens better.",
 b("Robot test lesson:")+"in Golf Digest's 14-head 3-wood test, higher-spin heads lost far less distance on mishits.",
 b("Senior picks:")+"TaylorMade Qi4D Max or PING G440 Max for forgiveness, Mizuno JPX One for accuracy, Wilson DYNAPWR Max ($279.99) on a budget"]) + \
"<p>After the driver, the <b>3-wood</b> is the hardest club in many senior golfers' bags. With only about 15° of loft, it needs real clubhead speed to launch a ball sitting on the fairway. That's why more golfers now skip the 3-wood and carry a <b>5-, 7- or even 9-wood</b>. MyGolfSpy notes that inconsistent long-iron striking \"is particularly common as swing speed decreases\" — and high-lofted fairway woods are one of the simplest fixes.</p>" + \
"<p>The timing is good: on October 30 Golf Digest published a <b>swing-robot test of 14 current 3-woods</b>. Below we pull out what matters for slower swings, add MyGolfSpy's 2026 fairway wood data on the Mizuno JPX One (second in accuracy), and combine senior-focused reviews from National Club Golfer (NCG) and GolfMagic to answer two questions: <b>which wood numbers to carry, and which models to try</b>.</p>" + \
"<h2>1. Golf Digest's robot test: what 14 3-woods taught us</h2>" + \
"<p>Golf Digest used a Golf Laboratories swing robot on 14 3-woods from five brands (stock lofts 14.5 to 16°). Each head took 18 swings — six centered, six toward the toe and six toward the heel — measuring spin, carry, ball speed and the carry lost on mishits. The article doesn't state the robot's swing speed, so focus on <b>the differences between models</b> rather than the yardages.</p>" + \
B.check([
 "<b>Spin decided distance:</b> center-strike ball speed only ran from 135 to 139.4 mph, while carry tracked spin at roughly <b>a yard for every 100 rpm</b>.",
 "<b>Low-spin heads punish mishits:</b> the five lowest-spin heads lost an average of <b>17.3 yards</b> on heel strikes; the five highest-spin heads lost only <b>9.9</b>.",
 "<b>Best at holding distance on misses:</b> TaylorMade Qi4D Max (7.1 yards average loss), PING G440 SFT (9.1) and Callaway Quantum Max D (9.5). Golf Digest says to treat gaps of about two yards as ties.",
 "<b>Most balanced:</b> the PING G440 Max had the fastest ball speed (139.4 mph) and the second-best average carry across the face (210.3 yards) — Golf Digest's pick if you can't say where you miss."]) + \
B.table(["Model", "Center carry", "Center spin", "On mishits", "Takeaway"], [
 ["PING G440 LST", "224.9 yd (1st)", "2,840 rpm", "204.8 yd on heel strikes", "Longest, but least repeatable spin (±337 rpm)"],
 ["Cobra OPTM LS", "218.2 yd", "—", "—", "Low spin for pure strikers"],
 ["PING G440 Max", "—", "—", "−10.5 yd heel, −10.6 yd toe", "210.3 yd average carry, most balanced"],
 ["TaylorMade Qi4D Max", "206.2 yd", "4,300 rpm", "−7.1 yd average (least)", "Most forgiving on misses"],
 ["PING G440 SFT", "—", "—", "−9.1 yd average", "Tightest spin spread (±126 rpm), slice help"],
 ["Callaway Quantum Max D", "—", "—", "−9.5 yd average", "Most consistent launch (±0.19°)"]]) + \
SM.format("Source: Golf Digest, \"Which 3-wood is right for you? We put 14 on the swing robot to find out\" (Oct 30, 2026). A dash means the article gave no number.") + \
"<p>For seniors the message is clear. Slower swings usually mean fewer centered strikes, and you need some spin to keep the ball in the air. Golf Digest says that \"if your strikes cluster toward the heel, the higher-spin heads protect you,\" and concludes that you should <b>know your miss before you shop</b>. Tour-style low-spin heads (LST, LS, Tour) only pay off for golfers who find the center consistently.</p>" + \
"<h2>2. 3-wood vs 5-wood vs 7-wood vs 9-wood</h2>" + \
"<p>MyGolfSpy explains that higher-lofted fairway woods \"are built to help launch the ball\": the center of gravity, larger head, longer shaft and extra loft all make height easier. Typical lofts and roles:</p>" + \
B.table(["Club", "Typical loft", "Role (GolfMagic, MyGolfSpy)"], [
 ["3-wood", "about 15°", "Fallback off the tee with little distance drop-off"],
 ["5-wood", "about 18°", "Higher, softer-landing alternative to a long iron"],
 ["7-wood", "20–23°", "High launch and spin for stopping power on greens"],
 ["9-wood", "23–26°", "High-flying replacement for long irons and hybrids"],
 ["Hybrid", "19–26°", "Iron-like shape, handy from the rough"],
 ["Long iron", "18–25°", "Hard to launch with a slower swing"]]) + \
SM.format("3- and 5-wood lofts are typical values and vary by maker; the 7-wood, 9-wood, hybrid and long-iron ranges are MyGolfSpy's.") + \
B.check([
 "<b>Should you drop the 3-wood?</b> If it won't get airborne off the fairway, making a 5-wood your longest wood is usually easier. NCG's reviewer even got fitted into a 16.5° head (a 4-wood) because he liked \"the extra height.\"",
 "<b>Overlapping with hybrids?</b> MyGolfSpy's advice: \"If you have a 22-degree hybrid that you rarely hit well, try a 7-wood.\"",
 "<b>Check your gaps:</b> in MyGolfSpy's example, if your 5-iron carries 170 and your 4-iron 174, there's little reason to carry both — use that slot for a 7- or 9-wood."]) + \
"<h2>3. Fairway woods for seniors: pros and cons</h2>" + \
card("TaylorMade", "Qi4D Max Fairway", "$379", "The 3-wood that lost the least distance on mishits in Golf Digest's robot test, and NCG's top senior pick.",
     ["Smallest average loss in the robot test (7.1 yd), as little as 3.3 yd on one side", "NCG: easy to launch, high flight, very forgiving", "GolfMagic: 200cc head vs 185cc on the standard Qi4D"],
     ["NCG: \"Definitely not the longest fairway wood out there\"", "High spin (4,300 rpm centered) costs faster swingers distance"],
     "Golfers with inconsistent strike, and anyone facing long second shots on par 5s and long par 4s", ko=False) + \
card("PING", "G440 Max Fairway", "$349", "The robot test's most balanced head, offered from 15° to 24° — into 7- and 9-wood territory.",
     ["Fastest ball speed (139.4 mph) and second-best average carry", "Very repeatable spin (±127 rpm)", "NCG: easy to launch and very forgiving"],
     ["The longest head in the test was PING's own LST, not the Max", "Many versions (SFT for slices, HL for slower swings per GolfMagic) can be confusing"],
     "Golfers unsure of their miss; check the SFT for a big slice and the HL for very slow swings", ko=False) + \
card("Mizuno", "JPX One Fairway", "$350", "Second in accuracy and forgiveness in MyGolfSpy's 2026 fairway test (8.9 overall). Offered as 3-, 5- and 7-wood.",
     ["MyGolfSpy: 36.3 yd proximity, about nine yards better than the 20-wood average", "More than 91% of shots playable", "NCG: strong ball speed, very easy to launch, forgiving off the turf"],
     ["12th in carry and 14th in total distance at MyGolfSpy — not the longest", "Spins on the high side; high-spin players should test it"],
     "Golfers who want to know where the ball is going more than maximum distance", ko=False) + \
card("Wilson", "DYNAPWR Max Fairway", "$279.99", "The least expensive model on NCG's senior list. Lofts 15, 18 and 21°.",
     ["NCG: plenty of forgiveness and a high flight", "Available with the lightweight UST Helium NCT 4 shaft", "About $70–100 less than the big brands"],
     ["NCG: not as quick off the face as other models", "Less adjustability and fewer shaft options"],
     "Budget buyers who want a light, easy wood", ko=False) + \
card("Cobra", "OPTM Max Fairway", "$369.99", "Built for launch, forgiveness and draw bias, with a FutureFit33 hosel for loft and lie changes.",
     ["NCG: strong ball speed and lots of adjustability", "Draw bias helps a slice"],
     ["In NCG's three-model comparison it had the lowest ball speed, highest spin and shortest carry", "Its sibling OPTM X lost 20.8 yd on mishits in the robot test"],
     "Slicers who like to tinker with loft settings", ko=False) + \
"<h3>Side-by-side</h3>" + B.table(["Model", "US list price", "Lofts", "Strength", "Best for"], [
 ["TaylorMade Qi4D Max", "$379", "—", "Most forgiving on misses", "Inconsistent strike"],
 ["PING G440 Max", "$349", "15–24°", "Balance, consistency", "Unsure of your miss"],
 ["Mizuno JPX One", "$350", "3, 5, 7 wood", "Accuracy", "Direction first"],
 ["Wilson DYNAPWR Max", "$279.99", "15, 18, 21°", "Price, light shaft", "Budget"],
 ["Cobra OPTM Max", "$369.99", "Adjustable", "Draw bias, adjustability", "Slicers"]]) + \
SM.format("Prices: US RRP as listed by NCG; sale and used prices change. A dash means the source gave no loft list.") + \
"<h2>4. How to choose (checklist)</h2>" + \
B.check([
 "<b>1. Know your miss:</b> heel strikes favor higher-spin Max heads; consistent center contact can justify a low-spin model (Golf Digest).",
 "<b>2. Set your longest wood's loft:</b> if a 15° 3-wood won't launch, start at a 5-wood (18°). A 16.5° 4-wood is a good middle ground.",
 "<b>3. Shaft:</b> GolfMagic notes that \"lighter, less stiff shafts will produce a higher, right-to-left biased ball flight, while heavier, stiff shafts will launch the ball lower.\" If your driver is a senior (A) flex, match your woods.",
 "<b>4. Test before you buy:</b> review numbers reflect the testers' swings, and the shaft changes everything, so hit it first."]) + \
"<h2>Picks by situation</h2>" + B.picks([
 ("FREQUENT MISHITS", "TaylorMade Qi4D Max", "Lost the least distance on misses in the robot test."),
 ("SAFE FIRST CHOICE", "PING G440 Max", "Lofts from 15 to 24° and the most balanced performance."),
 ("DIRECTION FIRST", "Mizuno JPX One", "Second in accuracy at MyGolfSpy; 3-, 5- and 7-wood."),
 ("BUDGET & LIGHT", "Wilson DYNAPWR Max", "$279.99 with a lightweight shaft option.")], ko=False) + \
"<p>Replacing long irons with a 7- or 9-wood? See our <a href='/blog/senior-7-wood-9-wood'>7-wood and 9-wood guide for seniors</a>. Deciding what replaces your long irons? See our <a href='/blog/senior-hybrids-2026'>hybrid comparison for seniors</a>. Want a lighter driver too? Read <a href='/blog/lightweight-drivers'>lightweight drivers for slower swings</a>. For the best time to buy, see the <a href='/blog/black-friday-2026-clubs'>Black Friday 2026 club guide</a>.</p>" + \
"<div class='note'><b>Match your wood shafts first.</b> Enter your swing details in our driver calculator to get a shaft flex and weight. Fairway woods are usually fitted in the same flex family.</div>"

P = dict(file="blog-senior-fairway-woods-2026.html", bg="fw", calc="driver",
 cat_ko="시니어 · 페어웨이우드", cat_en="Seniors & fairway woods",
 title_ko="3번 우드가 안 뜬다면: 시니어 페어웨이우드 고르는 법 (2026 로봇 테스트)",
 title_en="Can't launch your 3-wood? Fairway woods for seniors (2026 robot test)",
 desc_ko="Golf Digest 3번 우드 14개 로봇 테스트와 MyGolfSpy·NCG 리뷰로 시니어에게 맞는 5번·7번 우드와 Qi4D Max, G440 Max, JPX One 등을 비교했습니다.",
 sub_ko="3번 우드 대신 5번·7번 우드가 답일 수 있습니다. 14개 3번 우드 로봇 테스트와 시니어용 모델 5종을 정리했습니다.",
 sub_en="A 5- or 7-wood may beat your 3-wood. We break down a 14-head robot test and five senior-friendly models.",
 cta_ko=("우드 샤프트 강도부터 확인하세요","스윙 정보를 넣으면 맞는 샤프트 강도와 무게를 추천합니다.","드라이버 계산기 열기"),
 cta_en=("Check your shaft flex first","Enter your swing details for shaft flex and weight picks.","Open the driver calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("Golf Digest — Which 3-wood is right for you? We put 14 on the swing robot to find out (Oct 30, 2026)","https://www.golfdigest.com/story/2026-fairway-woods-robotic-testing-analysis"),
  ("MyGolfSpy — Mizuno Just Pulled Off The Most Unexpected Equipment Sweep Of 2026","https://mygolfspy.com/news-opinion/mizuno-just-pulled-off-the-most-unexpected-equipment-sweep-of-2026/"),
  ("MyGolfSpy — Who Would Benefit From A High-Lofted Fairway Wood?","https://mygolfspy.com/news-opinion/instruction/who-would-benefit-from-a-high-lofted-fairway-wood/"),
  ("National Club Golfer — Best Fairway Woods for Senior Golfers 2026","https://www.nationalclubgolfer.com/best-golf-deals/best-fairway-woods-for-senior-golfers/"),
  ("GolfMagic — Best Fairway Woods 2026","https://www.golfmagic.com/equipment/buying-guides/best-fairway-woods")])
if __name__ == "__main__":
    open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
    print("ok")
