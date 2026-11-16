import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import build as B
from cards import STY, card, b, faq

# Rewritten 2026-11-15: the first version (≈575 English words, few specs) was "crawled - currently not indexed".
# Now built around a spec table (club/head/shaft weight, lofts, length, price) the other posts don't have,
# plus how-to-choose by swing speed, cards and FAQ. Facts only from the sources listed at the bottom.

note = lambda t: f"<p style='font-size:.85rem;color:var(--muted)'>{t}</p>"

# ------------------------------------------------------------------ KOREAN
KO = STY + B.tldr("핵심 요약", [
 b("가장 가벼운 선택:")+"XXIO 14 — 드라이버 총중량 283g, 샤프트 36g(R). 처음부터 느린 스윙을 위해 만든 모델 ($799.99)",
 b("최신 경량 3종:")+"PXG Lightning Max Lite·TaylorMade Qi4D Max Lite·PING G440 K HL — 모두 약 $650",
 b("예산 + 슬라이스:")+"Cleveland Launcher XL 2 Draw — 일반 모델보다 9g 가볍고 드로우 설계, 약 $300"]) + \
"<p>나이가 들어 헤드스피드가 줄면, 무거운 일반 드라이버를 더 세게 휘두르기보다 <b>클럽 자체를 가볍게 해서 같은 힘으로 더 빠르게</b> 휘두르는 편이 효과적입니다. 그래서 각 브랜드가 '경량(Lite)' 드라이버를 따로 내놓습니다. 다만 '가볍다'는 말만으로는 비교가 어렵습니다. 이 글은 <b>총중량·헤드 무게·샤프트 무게·로프트·길이·가격</b>을 한 표에 모아, 느린 스윙 골퍼가 숫자로 고를 수 있게 정리했습니다.</p>" + \
"<h2>1. 얼마나 가벼워야 '경량'일까</h2>" + \
"<p>기준을 잡아 보겠습니다. 한 리뷰어는 PXG의 이전 경량 모델(Black Ops Ultra Lite)을 <b>277g으로 일반 드라이버보다 약 30g 가볍다</b>고 설명했습니다. 즉 일반 드라이버는 대략 300g 초반입니다. XXIO 14 드라이버는 <b>283g</b>이고, Australian Golf Digest는 이것이 같은 회사의 Srixon ZXi보다 약 <b>42g 가볍다</b>고 전했습니다. 핵심은 샤프트로, XXIO 14의 기본 샤프트는 <b>36g</b>밖에 되지 않습니다.</p>" + \
"<p>무게를 줄이는 방법은 브랜드마다 다릅니다.</p>" + B.check([
 "<b>샤프트·그립을 가볍게:</b> XXIO 14(36g 샤프트 + 33g 그립), TaylorMade Qi4D Max Lite(40g대 REAX MR40 샤프트)",
 "<b>헤드 무게추를 줄이기:</b> PXG Lightning Max Lite는 형제 모델의 솔 무게추를 빼서 14g을 줄였고, 헤드 무게가 189g(일반형 203g)입니다.",
 "<b>헤드 소재를 바꾸기:</b> TaylorMade Qi4D Max Lite는 티타늄 대신 7075 알루미늄 칼라를 쓴, TaylorMade의 첫 현대식 비(非)티타늄 드라이버입니다.",
 "<b>길이를 늘려 속도 내기:</b> PING G440 K HL 빌드는 46인치에 가벼운 샤프트(Alta Quick 35·45)를 씁니다."]) + \
"<h2>2. 경량 드라이버 스펙 비교표</h2>" + \
B.table(["모델", "총중량", "헤드", "기본 샤프트", "로프트", "길이", "미국 가격"], [
 ["<b>XXIO 14</b>", "283g", "200g", "36g (R)", "9.5·10.5·11.5°", "46\"", "$799.99"],
 ["<b>XXIO 14+</b>", "299g", "201g", "42g (R)", "9.5·10.5°", "45.75\"", "$799.99"],
 ["<b>PXG Lightning Max Lite</b>", "—", "189g", "경량 시니어 옵션", "10.5·11.5°", "—", "$649"],
 ["<b>TaylorMade Qi4D Max Lite</b>", "—", "—", "REAX MR40 (R·A)", "10.5·12°", "45.75\"", "$649.99"],
 ["<b>PING G440 K (HL 빌드)</b>", "—", "—", "Alta Quick 35·45", "9·10.5·12°", "46\"", "$649"],
 ["<b>Cleveland Launcher XL 2 Draw</b>", "—", "—", "Aldila Ascent", "9·10.5·12°", "—", "약 $299.99"]]) + \
note("※ '—'는 제조사·리뷰에서 확인되지 않은 값입니다. Launcher XL 2 가격은 2026년 10월 온라인 신품 일반형 기준입니다. 가격은 시점에 따라 바뀝니다.") + \
"<p>표에서 보듯 <b>총중량을 공개한 곳은 XXIO뿐</b>입니다. 다른 브랜드는 '가장 가벼운 헤드·샤프트·그립 조합'이라고만 밝혀, 매장에서 실제로 잡아 보는 것이 가장 정확합니다.</p>" + \
"<h2>3. 내 스윙 속도에 맞는 선택</h2>" + \
B.table(["드라이버 스윙 속도", "출발점", "이유"], [
 ["약 70~85mph", "XXIO 14, 시니어(A) 플렉스", "한 피팅 업체는 이 구간에서 A 플렉스가 에너지 전달과 탄도에 도움이 된다고 봅니다."],
 ["약 85~100mph", "XXIO 14+, PXG Max Lite, Qi4D Max Lite", "XXIO 14+는 스윙 속도 100mph 이하 골퍼를 겨냥해 처음 나온 라인입니다."],
 ["100mph 이상", "일반 드라이버", "너무 가벼우면 오히려 타이밍이 흔들릴 수 있습니다."]]) + \
"<p>참고로 Golf Digest가 인용한 Trackman 자료에 따르면 LPGA 투어 평균 드라이버 스윙 속도가 약 96mph입니다. XXIO 14+가 '100mph 이하'를 겨냥한다는 것은, 생각보다 많은 남성 골퍼가 경량 드라이버의 대상이라는 뜻입니다. 내 속도를 모르면 <b>드라이버 거리만으로</b> 추정할 수 있습니다. 글 아래 드라이버 계산기를 이용해 보세요.</p>" + \
"<h2>4. 모델별 장단점</h2>" + \
card("XXIO", "XXIO 14 Driver", "$799.99", "2025년 11월 공개. 느린 스윙의 여성·시니어를 주 대상으로 하는 경량 드라이버의 기준.",
     ["총중량 283g, 샤프트 36g — 비교 모델 중 가장 가벼움", "XXIO 남성용 최초로 로프트 조절 호젤(±1.5°)", "닫힌 페이스 각도로 슬라이스 완화"],
     ["가격이 가장 비쌈", "스윙이 빠른 분에겐 너무 가벼울 수 있음 → 그래서 14+가 따로 나옴"],
     "가장 가벼운 드라이버가 필요한 분, 헤드스피드가 많이 줄어든 시니어") + \
card("XXIO", "XXIO 14+ Driver", "$799.99", "XXIO 최초의 '조금 더 빠른 스윙'용. 총중량 299g, 52g대 Fujikura 옵션도 있음.",
     ["스윙 속도 100mph 이하 골퍼 대상", "스핀이 적고 탄도가 곧게 뻗는 설계", "일반 XXIO 14보다 타구음이 조용함"],
     ["14보다 16g 무거움", "닫힌 페이스가 아니라 슬라이스 교정 효과는 덜함"],
     "가벼운 채를 원하지만 XXIO 14는 너무 가볍게 느껴지는 분") + \
card("PXG", "Lightning Max Lite", "$649", "Black Ops Ultra Lite의 후속. 형제 모델 Max 10K에서 솔 무게추를 빼 14g을 줄였습니다.",
     ["헤드 189g으로 일반 Lightning(203g)보다 가벼움", "뒤쪽 12.5g 무게추로 관용성 확보", "PXG 기준 '매우 높은' 관용성, 높은 탄도"],
     ["로프트 10.5·11.5° 두 가지뿐", "무게추가 하나라 세밀한 조정은 제한적"],
     "가벼우면서도 방향 안정성을 원하는 중간 스윙 속도 골퍼") + \
card("TaylorMade", "Qi4D Max Lite", "$649.99", "2026 Qi4D 라인의 가장 가벼운 모델. TaylorMade 첫 현대식 비티타늄 드라이버.",
     ["7075 알루미늄 칼라 — 티타늄보다 가벼움", "Qi4D 라인에서 가장 가벼운 헤드·샤프트·그립", "Plugged In Golf: 가벼운 설계 덕에 헤드스피드가 올랐다는 테스트 결과"],
     ["로프트 10.5·12°만", "총중량 등 세부 무게는 공개되지 않음"],
     "익숙한 대형 브랜드의 최신 경량 드라이버를 원하는 분") + \
card("PING", "G440 K (HL 빌드)", "$649", "PING에서 가장 관용성 높은 드라이버. HL(High Launch)은 느린 스윙용 경량 빌드입니다.",
     ["PING 역사상 가장 높은 MOI(일부 설정 10.4k 이상) — 빗맞아도 곧게", "HL 빌드: 46인치, 28g 뒤 무게(일반 32g), 가벼운 샤프트", "뒤 무게로 드로우·페이드 조정"],
     ["헤드가 길고 페이스가 얕아 모양은 호불호", "일반 빌드는 경량이 아님 — 반드시 HL로 주문"],
     "거리보다 페어웨이 안착이 중요한 분") + \
card("Cleveland", "Launcher XL 2 Draw", "약 $299.99", "일반 Launcher XL 2보다 9g 가벼운 드로우 모델. 이 비교의 가성비 선택.",
     ["가격이 다른 모델의 절반 이하", "고탄도 Aldila Ascent 샤프트 기본", "드로우 설계로 슬라이스 완화"],
     ["경량 전용 모델이 아니라 일반 모델의 드로우 버전(9g 차이)", "총중량 등 세부 무게 정보가 적음"],
     "슬라이스가 있고 예산이 중요한 분") + \
"<h2>5. 고르기 전에 꼭 확인할 것</h2>" + B.check([
 "<b>로프트는 10.5° 이상부터:</b> 느린 스윙은 공을 띄우는 힘이 부족해 로프트가 높아야 캐리가 늘어납니다. 위 모델 대부분이 11.5~12°를 제공합니다.",
 "<b>슬라이스가 있다면:</b> XXIO 14(닫힌 페이스), Launcher XL 2 Draw처럼 드로우 성향 모델부터 시타하세요.",
 "<b>너무 가벼운 것도 문제:</b> 스윙이 빠른 편인데 너무 가벼운 채를 쓰면 타이밍이 흔들릴 수 있습니다. XXIO가 14와 14+를 나눈 이유입니다.",
 "<b>샤프트 플렉스:</b> 70~85mph라면 시니어(A) 플렉스를 먼저 시타해 보세요.",
 "<b>중고도 좋은 선택:</b> 드라이버는 한 세대만 지나도 가격이 크게 내립니다. 이전 세대(XXIO 13, PXG Black Ops Ultra Lite 등)도 같은 원리의 경량 모델입니다."]) + \
"<p>드라이버 말고 롱아이언도 어렵다면 <a href='/blog/senior-hybrids-2026'>시니어를 위한 하이브리드 비교</a>를, 할인 시기가 궁금하다면 <a href='/blog/black-friday-2026-clubs'>2026 블랙프라이데이 골프채 가이드</a>를 함께 보세요.</p>" + \
"<h2>6. 자주 묻는 질문</h2>" + faq([
 ("경량 드라이버를 쓰면 정말 거리가 늘어나나요?", "같은 힘으로 더 빠르게 휘두를 수 있으면 볼 스피드가 올라 거리가 늘 수 있습니다. Plugged In Golf도 Qi4D Max Lite 테스트에서 가벼운 설계 덕에 헤드스피드가 올랐다고 했습니다. 다만 개인차가 크므로 시타가 가장 정확합니다."),
 ("XXIO 14와 14+ 중 무엇을 사야 하나요?", "스윙이 많이 느려졌다면 더 가벼운 XXIO 14(283g), 아직 스윙이 빠른 편이면 14+(299g)가 맞습니다. 14+는 스핀이 적고 탄도가 곧게 뻗는 대신, 14의 닫힌 페이스가 없어 슬라이스 교정 효과는 덜합니다."),
 ("왜 다른 브랜드는 총중량을 공개하지 않나요?", "샤프트·그립·길이에 따라 무게가 바뀌기 때문에, 대부분의 브랜드는 '라인에서 가장 가벼운 조합'이라고만 밝힙니다. 매장에서 실제 조립품을 저울에 올려 보거나 피터에게 물어보는 것이 정확합니다."),
 ("여성용 드라이버를 써도 되나요?", "가능합니다. 예를 들어 XXIO 14 Ladies는 259~264g으로 더 가볍고 짧습니다. 다만 길이와 그립 굵기가 손에 맞는지 확인하세요.")])

# ------------------------------------------------------------------ ENGLISH
EN = STY + B.tldr("QUICK TAKE", [
 b("Lightest:")+"XXIO 14 — 283 g total with a 36 g stock shaft, built from the ground up for slower swings ($799.99)",
 b("Newest light trio:")+"PXG Lightning Max Lite, TaylorMade Qi4D Max Lite and PING G440 K HL — all about $650",
 b("Budget + slice:")+"Cleveland Launcher XL 2 Draw — 9 g lighter than the standard model with draw bias, about $300"]) + \
"<p>When swing speed drops, swinging a heavy standard driver harder rarely works. A better fix is a <b>lighter club you can swing faster with the same effort</b> — which is why every major brand now sells a \"Lite\" driver. But \"light\" alone is hard to compare. This guide puts <b>total weight, head weight, shaft weight, lofts, length and price</b> in one table so slower-swinging golfers can choose by the numbers.</p>" + \
"<h2>1. How light is \"lightweight\"?</h2>" + \
"<p>Start with a baseline. One reviewer described PXG's previous light model, the Black Ops Ultra Lite, as <b>277 grams — about 30 grams lighter than a typical driver</b>, which puts a standard driver in the low 300s. The XXIO 14 driver weighs <b>283 grams</b>, which Australian Golf Digest says is about <b>42 grams lighter</b> than its sister brand's Srixon ZXi. The secret is the shaft: XXIO 14's stock shaft weighs as little as <b>36 grams</b>.</p>" + \
"<p>Brands save weight in different ways:</p>" + B.check([
 "<b>Lighter shaft and grip:</b> XXIO 14 (36 g shaft + 33 g grip) and TaylorMade Qi4D Max Lite (40-gram-class REAX MR40 shaft).",
 "<b>Fewer head weights:</b> PXG removed the sole weights from the Max 10K to save 14 g; the Max Lite head is 189 g versus 203 g for the other Lightning heads.",
 "<b>Different head material:</b> The Qi4D Max Lite uses a 7075 aluminum collar instead of titanium — TaylorMade's first modern non-titanium driver.",
 "<b>Length for speed:</b> PING's G440 K HL build is 46 inches with light Alta Quick 35 and 45 shafts."]) + \
"<h2>2. Lightweight driver spec table</h2>" + \
B.table(["Model", "Total", "Head", "Stock shaft", "Lofts", "Length", "US price"], [
 ["<b>XXIO 14</b>", "283&nbsp;g", "200&nbsp;g", "36&nbsp;g (R)", "9.5, 10.5, 11.5°", "46\"", "$799.99"],
 ["<b>XXIO 14+</b>", "299&nbsp;g", "201&nbsp;g", "42&nbsp;g (R)", "9.5, 10.5°", "45.75\"", "$799.99"],
 ["<b>PXG Lightning Max Lite</b>", "—", "189&nbsp;g", "Light senior options", "10.5, 11.5°", "—", "$649"],
 ["<b>TaylorMade Qi4D Max Lite</b>", "—", "—", "REAX MR40 (R, A)", "10.5, 12°", "45.75\"", "$649.99"],
 ["<b>PING G440 K (HL build)</b>", "—", "—", "Alta Quick 35, 45", "9, 10.5, 12°", "46\"", "$649"],
 ["<b>Cleveland Launcher XL 2 Draw</b>", "—", "—", "Aldila Ascent", "9, 10.5, 12°", "—", "~$299.99"]]) + \
note("\"—\" means the maker or reviewers didn't publish it. The Launcher XL 2 price is the standard model sold new online in October 2026. Prices change.") + \
"<p>Notice that <b>only XXIO publishes a total club weight</b>. The others simply say theirs is the lightest head, shaft and grip in the family, so picking one up in a store is the most reliable comparison.</p>" + \
"<h2>3. Match the driver to your swing speed</h2>" + \
B.table(["Driver swing speed", "Start with", "Why"], [
 ["About 70–85 mph", "XXIO 14, senior (A) flex", "One fitter says an A flex helps energy transfer and launch in this range."],
 ["About 85–100 mph", "XXIO 14+, PXG Max Lite, Qi4D Max Lite", "XXIO 14+ is the brand's first line aimed at swing speeds of 100 mph or less."],
 ["Over 100 mph", "A standard driver", "Going too light can upset your timing."]]) + \
"<p>For perspective, Golf Digest cites Trackman data putting the average LPGA Tour driver swing speed at about 96 mph. If XXIO is targeting \"100 mph or less,\" a lot more men fit the lightweight category than you might think. Don't know your speed? You can estimate it from <b>drive distance alone</b> with the driver calculator below.</p>" + \
"<h2>4. Pros and cons by model</h2>" + \
card("XXIO", "XXIO 14 Driver", "$799.99", "Unveiled November 2025. The benchmark lightweight driver for slower-swinging women and seniors.",
     ["283 g total and a 36 g shaft — the lightest here", "First XXIO men's driver with an adjustable hosel (±1.5°)", "Closed face angle helps tame a slice"],
     ["Most expensive in this group", "Can feel too light for faster swings — hence the 14+"],
     "Golfers who need the lightest possible driver, or seniors who have lost a lot of speed", ko=False) + \
card("XXIO", "XXIO 14+ Driver", "$799.99", "XXIO's first model for slightly faster swings: 299 g total, with a 52 g Fujikura option.",
     ["Aimed at swing speeds of 100 mph or less", "Lower spin and a more penetrating flight", "Quieter sound than the standard XXIO 14"],
     ["16 g heavier than the 14", "No closed face, so less slice help"],
     "Golfers who want a light driver but find the XXIO 14 too light", ko=False) + \
card("PXG", "Lightning Max Lite", "$649", "Successor to the Black Ops Ultra Lite. PXG dropped the Max 10K's sole weights to save 14 g.",
     ["189 g head versus 203 g for other Lightning heads", "Single 12.5 g rear weight keeps forgiveness high", "PXG rates launch high and forgiveness very high"],
     ["Only 10.5° and 11.5° lofts", "One weight port limits fine-tuning"],
     "Moderate swing speeds that want light weight and direction control", ko=False) + \
card("TaylorMade", "Qi4D Max Lite", "$649.99", "The lightest model in the 2026 Qi4D family and TaylorMade's first modern non-titanium driver.",
     ["7075 aluminum collar — lighter than titanium", "Lightest head, shaft and grip in the Qi4D line", "Plugged In Golf saw clubhead speed rise thanks to the lighter design"],
     ["Only 10.5° and 12° lofts", "No published total weight"],
     "Golfers who want the newest lightweight driver from a familiar brand", ko=False) + \
card("PING", "G440 K (HL build)", "$649", "PING's most forgiving driver; the HL (High Launch) build is the light version for slower swings.",
     ["Highest MOI PING has made (10.4k+ in some setups) — straight on mishits", "HL build: 46\", 28 g back weight (32 g standard), light shafts", "Back weight adjusts for draw or fade"],
     ["Long, shallow head isn't for everyone", "Standard build isn't light — order the HL"],
     "Golfers who value fairways over yards", ko=False) + \
card("Cleveland", "Launcher XL 2 Draw", "~$299.99", "Nine grams lighter than the standard Launcher XL 2 with draw bias — the value pick here.",
     ["Less than half the price of the others", "High-launch Aldila Ascent shaft as standard", "Draw bias tames a slice"],
     ["A draw version of a standard model, not a dedicated lightweight (9 g lighter)", "Few published weight details"],
     "Slicers on a budget", ko=False) + \
"<h2>5. Check these before you buy</h2>" + B.check([
 "<b>Start at 10.5° or more:</b> slower swings need loft to carry the ball; most models here offer 11.5–12°.",
 "<b>If you slice:</b> try draw-leaning heads first, such as the XXIO 14 (closed face) or Launcher XL 2 Draw.",
 "<b>Too light is a problem too:</b> a club that's too light for your speed can hurt timing — the reason XXIO split the 14 and 14+.",
 "<b>Shaft flex:</b> at 70–85 mph, start with a senior (A) flex.",
 "<b>Used works:</b> drivers drop sharply after one generation, and older models like the XXIO 13 or PXG Black Ops Ultra Lite use the same lightweight idea."]) + \
"<p>If long irons are hard too, see our <a href='/blog/senior-hybrids-2026'>hybrid comparison for seniors</a>; for the best time to buy, see the <a href='/blog/black-friday-2026-clubs'>Black Friday 2026 club guide</a>.</p>" + \
"<h2>6. FAQ</h2>" + faq([
 ("Will a lightweight driver really add distance?", "If you can swing it faster with the same effort, ball speed and distance can go up; Plugged In Golf saw clubhead speed increase in its Qi4D Max Lite test. Results vary a lot by golfer, so a demo is the best test."),
 ("XXIO 14 or 14+?", "If you've lost a lot of speed, the lighter XXIO 14 (283 g); if you still swing fairly quickly, the 14+ (299 g). The 14+ spins less and flies flatter, but lacks the 14's closed face, so it helps a slice less."),
 ("Why don't other brands publish total weight?", "Weight changes with the shaft, grip and length, so most brands just say theirs is the lightest combination in the family. Ask a fitter or weigh the built club in the store."),
 ("Can I use a women's driver?", "Yes. The XXIO 14 Ladies, for example, weighs 259–264 g and is shorter. Just make sure the length and grip size suit your hands.")])

P = dict(file="blog-lightweight-drivers.html", bg="senior", calc="driver",
 cat_ko="시니어 · 경량 클럽", cat_en="Seniors & lightweight",
 title_ko="느린 스윙을 위한 경량 드라이버 비교: 무게·로프트·가격 스펙표 (2026)",
 title_en="Lightweight drivers for slower swings: weights, lofts and prices compared (2026)",
 desc_ko="XXIO 14(283g), PXG Lightning Max Lite, TaylorMade Qi4D Max Lite, PING G440 K HL, Cleveland Launcher XL 2 Draw의 총중량·헤드·샤프트 무게와 로프트, 가격을 한 표로 비교했습니다.",
 sub_ko="헤드스피드가 줄었다면 더 세게가 아니라 더 가볍게. 2026년 경량 드라이버 6종의 무게·로프트·가격을 숫자로 비교했습니다.",
 sub_en="Lost swing speed? Swing lighter, not harder. We compare six 2026 lightweight drivers by weight, loft and price.",
 cta_ko=("내 헤드스피드부터 확인하세요","드라이버 거리만 넣으면 샤프트 강도와 추천 드라이버가 나옵니다.","드라이버 계산기 열기"),
 cta_en=("Check your swing speed first","Enter your drive distance for flex and driver picks.","Open the driver calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("Golf Digest — XXIO 14 woods & irons: what you need to know (283 g, 14+, LPGA 96 mph)","https://www.golfdigest.com/story/xxio-14-woods--irons--what-you-need-to-know"),
  ("Australian Golf Digest — XXIO 14 (42 g lighter, 36 g shaft)","https://www.australiangolfdigest.com.au/xxio-14-woods-irons-what-you-need-to-know/"),
  ("Dunlop Sports US — XXIO 14 Driver specs and price","https://us.dunlopsports.com/xxio/clubs/drivers/xxio-14-drivers/xxio-14-driver/MX14DRV.html"),
  ("Dunlop Sports US — XXIO 14+ Driver specs and price","https://us.dunlopsports.com/xxio/clubs/drivers/xxio-14-drivers/xxio-14%2B-driver/MX14PLUSDRV.html"),
  ("Dunlop Sports US — XXIO 14 Ladies Driver specs","https://us.dunlopsports.com/xxio/clubs/drivers/xxio-14-drivers/xxio-14-ladies-driver/MX14LDRV.html"),
  ("Just Golf Stuff — XXIO 14 Driver spec table","https://justgolfstuff.ca/products/xxio-14-driver"),
  ("Golf Reviews Guide — XXIO 14 & 14+ drivers","https://golfreviewsguide.com/?p=108303"),
  ("Dormy — XXIO 14 Driver (±1.5° hosel)","https://www.dormy.com/en/brands/xxio/14-02026694"),
  ("Golfers Authority — PXG Black Ops Ultra Lite note (277 g)","https://golfersauthority.com/?p=186003"),
  ("Golf Reviews Guide — PXG Lightning drivers (Max Lite 14 g lighter)","https://golfreviewsguide.com/?p=106047"),
  ("PXG UK — Lightning driver specs (Max Lite 189 g head)","https://uk.pxg.com/products/lightning-drivers"),
  ("PXG — Lightning drivers (launch, forgiveness ratings)","https://www.pxg.com/products/lightning-drivers"),
  ("Fairway Jockey — PXG Lightning Max Lite price","https://fairwayjockey.com/collections/mid-spin-drivers/products/pxg-lightning-max-lite-custom-driver"),
  ("GolfWRX — 2026 TaylorMade Qi4D drivers launch report","https://golfwrx.com/771324/2026-taylormade-qi4d-drivers-golfwrx-launch-report/"),
  ("Golf Digest Hot List — TaylorMade Qi4D Max Lite","https://www.golfdigest.com/hot-list/drivers/taylormade-qi4d-max-lite"),
  ("Golf Galaxy — Qi4D Max Lite specs","https://www.golfgalaxy.com/p/taylormade-qi4d-max-lite-custom-driver-25tymmq4dmxltdvrcspw/25tymmq4dmxltdvrcspw?stockReferral=true"),
  ("Golfballs.com — Qi4D Max Lite (7075 aluminum collar)","https://www.golfballs.com/Clubs/Driver/TaylorMade-Qi4D-Max-Lite-Driver.htm"),
  ("Plugged In Golf — TaylorMade Qi4D Max Lite review","https://pluggedingolf.com/taylormade-qi4d-max-lite-driver-review/"),
  ("GOLF.com — PING G440 K driver (MOI, $649)","https://golf.com/gear/drivers/ping-g440-k-driver-fast-forgiving"),
  ("GlobalGolf — PING G440 K HL build details","https://www.globalgolf.com/golf-clubs/1088577-ping-g440-k-driver/?bnc=25&flx=4&styp=2"),
  ("Tony Valentine — PING G440 K HL (Alta Quick shafts)","https://tonyvalentine.com/products/ping-g440-k-hl-driver"),
  ("Golf Monthly — Launcher XL 2 Draw review","https://golfmonthly.com/reviews/drivers/cleveland-launcher-xl-2-draw-driver-review"),
  ("Golfers Authority — Launcher XL 2 price check","https://golfersauthority.com/blogs/golf/cleveland-launcher-xl-2-driver-review"),
  ("PlayBetter — Best drivers for senior golfers (A flex at 70–85 mph)","https://www.playbetter.com/blogs/golf-tips/the-best-drivers-for-senior-golfers")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
print("ok", P["file"])
