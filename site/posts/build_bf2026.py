import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import build as B
B.HERO_BG["bf"] = "radial-gradient(120% 120% at 80% 0%,#5a1a24 0%,#2a1016 55%,#120709 100%)"
b = lambda s: f"<b style='display:inline;color:#fff'>{s}</b> "

STY = """<style>
.br2{border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.br2 h3{margin:0 0 8px;font-size:1.08rem}.br2 h3 small{font-weight:600;color:var(--muted);font-size:.8rem;margin-left:6px}
.br2 ul{margin:0;padding-left:18px}.br2 li{margin-bottom:5px}
.br2 .tg{display:inline-block;font-size:.72rem;font-weight:700;border-radius:6px;padding:2px 7px;margin-right:4px;background:var(--bg);color:var(--navy)}
.vd{display:inline-block;font-size:.72rem;font-weight:800;border-radius:6px;padding:2px 8px;white-space:nowrap}
.vd.go{background:#e3f5ec;color:#16734c}.vd.ok{background:#fff4dc;color:#8a6416}.vd.wait{background:#fde8ea;color:#9b2c3a}
</style>"""
T = lambda s: f'<span class="tg">{s}</span>'
GO = lambda s: f'<span class="vd go">{s}</span>'
OK = lambda s: f'<span class="vd ok">{s}</span>'
WT = lambda s: f'<span class="vd wait">{s}</span>'
def brand(name, sub, items):
    return f'<div class="br2"><h3>{name}<small>{sub}</small></h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"

# ------------------------------------------------------------------ KOREAN
KO = STY + B.tldr("핵심 요약", [
 b("지금 사기 좋은 것:")+"후속 모델이 공개된 PING G440 (MAX·SFT·LST)와 이미 값이 내려간 Callaway Quantum Max",
 b("서두를 필요 없는 것:")+"TaylorMade Qi4D, Titleist GTS — 2027년에도 현역이라 '구형'이 되지 않습니다",
 b("기다리는 게 나은 것:")+"막 나온 퍼터(Odyssey TRTL, L.A.B. MEZZ.2i)와 PING G450을 원하시는 분"]) + \
"<p>올해 블랙프라이데이는 <b>11월 27일(금)</b>, 사이버먼데이는 <b>11월 30일(월)</b>입니다. 하지만 골프 매장들은 11월 초부터 할인을 시작했고, 인기 사이즈는 먼저 품절되기도 합니다. 그래서 '언제 사느냐'보다 <b>'무엇을 지금 사고, 무엇을 기다리느냐'</b>가 더 중요합니다.</p>" + \
"<p>2027년 신제품 소식이 하나둘 나오고 있어서, 브랜드마다 상황이 꽤 다릅니다. TaylorMade는 2027년에 새 드라이버를 내지 않겠다고 발표했고, PING은 G440 후속인 G450이 11월 2일 USGA 승인 목록에 올라왔습니다. 이런 차이 때문에 같은 블랙프라이데이라도 어떤 클럽은 지금이 최저가에 가깝고, 어떤 클럽은 할인이 크지 않을 수 있습니다. 브랜드별로 정리했습니다.</p>" + \
"<h2>1. 브랜드별 2027년 상황 한눈에 보기</h2>" + B.table(["브랜드", "현재 모델", "2027년 계획", "판단"], [
 ["PING", "G440 MAX·LST·SFT", "후속 G450 USGA 목록 등재 (11/2), 출시는 2027년 1월 예상", GO("지금 사기 좋음")],
 ["Callaway", "Quantum Max", "매년 신제품을 내는 브랜드", GO("할인 중")],
 ["TaylorMade", "Qi4D", "2027년 새 드라이버 없음, 다음은 2028년", OK("급하지 않음")],
 ["Titleist", "GTS2·GTS3·GTS4", "2026년 6월 출시, 2년 주기", OK("급하지 않음")],
 ["Odyssey · L.A.B.", "TRTL · MEZZ.2i 퍼터", "11월에 막 출시", WT("할인 기대 낮음")]]) + \
"<p style='font-size:.85rem;color:var(--muted)'>※ G450 출시일과 가격은 PING이 공식 발표하지 않았고, 매체의 예상입니다.</p>" + \
"<h2>2. 지금 사기 좋은 클럽</h2>" + \
brand("PING G440 MAX · SFT · LST", "후속 모델 공개 → 가격 인하", [
 T("상황")+"PING이 G440 MAX·LST·SFT 드라이버와 페어웨이우드·하이브리드 가격을 내렸습니다. 고관용 모델인 G440 K는 인하 대상이 아닙니다.",
 T("가격")+"미국 TGW와 Carl's Golfland에서 G440 MAX가 정가 $617에서 <b>$447</b>로 판매되고 있습니다 (약 28% 할인).",
 T("이런 분께")+"관용성이 중요한 분은 MAX, 슬라이스가 고민이면 드로우 성향의 SFT. 시니어 골퍼에게도 무난한 선택입니다.",
 T("주의")+"G450은 새 반발 기술(FASTFLEX로 보이는 구조)이 들어갈 것으로 보이지만, 성능 차이는 아직 테스트 결과가 없습니다."]) + \
brand("Callaway Quantum Max", "정가 대비 약 $200 인하", [
 T("가격")+"$649.99에서 <b>$449.98</b>로 내려갔습니다. 같은 시점 TaylorMade Qi4D는 $649.99 그대로입니다.",
 T("평가")+"MyGolfSpy 2026 드라이버 테스트에서 거리 1위, 정확도 2위를 기록했습니다.",
 T("배경")+"Callaway와 Cobra는 여전히 매년 새 드라이버를 내는 몇 안 되는 브랜드라, 연말에 현행 모델 할인이 나오는 편입니다."]) + \
"<h3>모델별 고르는 법 (PING G440)</h3>" + B.table(["모델", "특징", "이런 분께"], [
 ["G440 MAX", "가장 관용성이 높은 기본 모델", "대부분의 아마추어, 시니어"],
 ["G440 SFT", "드로우 성향 (슬라이스 교정)", "공이 오른쪽으로 휘는 분"],
 ["G440 LST", "저스핀", "스윙이 빠르고 공이 높이 뜨는 분"],
 ["G440 K", "최고 관용성 (이번 인하 제외)", "빗맞음이 잦은 분"]]) + \
"<p>참고로 G450은 USGA 목록에 MAX(9·10.5·12°), LST(7.5·9·10.5°), SFT(9·10.5°), 그리고 PING의 첫 미니 드라이버인 MiniMax(13°)로 올라왔습니다. 구성은 G440과 같은 틀을 유지합니다.</p>" + \
"<h2>3. 서두를 필요 없는 클럽</h2>" + \
brand("TaylorMade Qi4D", "2027년에도 최신 모델", [
 T("발표")+"TaylorMade는 드라이버를 2년 주기로 바꾸고, Qi4D를 2027년까지 주력으로 유지한다고 밝혔습니다. 다음 새 드라이버는 2028년 예정입니다.",
 T("의미")+"지금 사도 1~2개월 뒤 '구형'이 되지 않습니다. 대신 후속 모델 때문에 생기는 큰 할인도 기대하기 어렵습니다.",
 T("평가")+"MyGolfSpy 2026 테스트에서 종합 1위 드라이버였고, 관용성 점수 9.0으로 이 부문 최고 수준이었습니다.",
 T("팁")+"정가가 부담되면 블랙프라이데이 사은품·묶음 할인이나 중고(아래 6번)를 노리세요."]) + \
brand("Titleist GTS2 · GTS3 · GTS4", "2026년 6월 출시, $699", [
 T("상황")+"Titleist는 원래 2년 주기라 GTS는 2027년에도 현역입니다.",
 T("고르는 법")+"GTS2가 가장 관용성이 높아 대부분의 골퍼에게 기본 선택이고, GTS4는 스윙이 빠른 분을 위한 저스핀 모델입니다.",
 T("스펙")+"GTS2·GTS3는 8·9·10·11°, GTS4는 8·9·10°. 호젤로 로프트·라이를 16가지로 조절할 수 있습니다.",
 T("투어")+"투어 출시 후 PGA 투어 선수 50명 이상이 GTS로 바꿨고, Justin Thomas와 Jordan Spieth도 GTS2를 씁니다."]) + \
brand("Cobra OPTM", "2026년 1월 출시, $600", [
 T("모델")+"OPTM X(9·10.5°), Max-K(9·10.5·12°), Max-D(10.5·12°), LS(9·10.5°) 네 가지. 모두 ±2° 범위의 33단계 조절 호젤.",
 T("이런 분께")+"Max-K는 Cobra에서 관성모멘트(MOI)가 가장 높은 헤드라 빗맞음이 잦은 분, Max-D는 슬라이스가 고민인 분께 맞습니다.",
 T("시기")+"Cobra는 Callaway와 함께 매년 새 드라이버를 내는 브랜드라, 블랙프라이데이 가격을 지켜볼 만합니다."]) + \
"<h2>4. 시니어·느린 스윙을 위한 추천 조합</h2>" + \
"<p>헤드스피드가 느린 분은 '최신'보다 '띄우기 쉽고 빗맞아도 덜 휘는 클럽'이 훨씬 중요합니다. 할인 중인 모델 위주로 묶어 보면 이렇습니다.</p>" + B.table(["클럽", "추천", "가격", "이유"], [
 ["드라이버", "PING G440 MAX 또는 SFT", "$447 (할인가)", "관용성 + 후속 모델 공개로 할인"],
 ["드라이버 (대안)", "Callaway Quantum Max", "$449.98 (할인가)", "2026 테스트 거리 1위"],
 ["하이브리드", "Callaway Apex Ti Super Hybrid", "$419.99", "페어웨이우드가 어려운 분용"],
 ["아이언", "Srixon ZXiR · ZXiR HL", "$1,099.99 (7개, 스틸) / $1,199.99 (그라파이트)", "관용성 중심 라인"]]) + \
brand("Callaway Apex Ti Super Hybrid", "2H~5H (16·18·21·24°)", [
 T("특징")+"티타늄 페이스를 스틸 바디에 붙여 반발력과 안정성을 높였고, 바닥(Step Sole)이 잔디에 덜 걸리도록 설계했습니다.",
 T("이런 분께")+"Callaway는 페어웨이우드가 잘 안 맞거나 티샷이 불안한 골퍼를 위해 만들었다고 설명합니다. 3번 우드 대신 넣기 좋습니다.",
 T("참고")+"새 OptiFit4 호젤은 이전 버전 샤프트와 호환되지 않습니다."]) + \
"<p>경량 드라이버를 더 알아보시려면 <a href='/blog/lightweight-drivers'>느린 스윙을 위한 경량 드라이버 Best 5</a>도 함께 보세요.</p>" + \
"<h2>5. 미니 드라이버: 사도 될까, 기다릴까</h2>" + \
"<p>드라이버가 자꾸 휘는 분들 사이에서 '미니 드라이버'가 인기입니다. 드라이버보다 작은 헤드와 짧은 샤프트로 방향성을 얻는 클럽인데, 마침 PING도 G450 MiniMax로 처음 이 시장에 들어옵니다.</p>" + B.table(["모델", "헤드·로프트", "가격", "상태"], [
 ["Titleist GTS300", "305cc · 13°", "$549", "2026년 7월 출시"],
 ["PXG Secret Weapon (신형)", "300cc · 13° · 43.25인치", "-", "새 세대 출시"],
 ["PING G450 MiniMax", "13°", "미발표", "2027년 출시 예상"]]) + \
"<p>PXG 자체 데이터로는 Secret Weapon이 드라이버보다 약 20야드 짧고 3번 우드보다 약 10야드 멀리 나갑니다. PING을 좋아하신다면 MiniMax가 나올 때까지 기다리는 것도 방법입니다.</p>" + \
"<h2>6. 아이언은 이번 시즌 할인이 적을 수 있습니다</h2>" + \
"<p>Srixon은 2세대 ZXi 아이언을 10월 16일에 내놓았습니다. ZXi7·ZXi5·ZXi5+는 7개 스틸 세트 기준 $1,499.99이고, 모두 일본 Endo가 단조합니다. 막 나온 제품이라 큰 할인은 기대하기 어렵습니다. 아이언은 보통 2~3년 주기로 바뀌기 때문에, 직전 세대 모델의 할인·중고를 찾는 편이 가성비가 좋습니다. 내 7번 아이언 거리로 헤드 종류와 샤프트를 먼저 확인해 보세요 → <a href='/iron/'>아이언 계산기</a></p>" + \
"<h2>7. 새 클럽 대신 중고·트레이드인</h2>" + \
"<p>정가를 다 주기 부담스럽다면 쓰던 클럽을 팔고 그 돈으로 바꾸는 방법도 있습니다. 미국에서는 2nd Swing의 트레이드인이 대표적입니다.</p>" + B.check([
 "온라인 가치 조회(Value Guide)에서 내 클럽 시세를 확인합니다",
 "클럽을 2nd Swing으로 보내면 상태를 검수한 뒤 금액이 확정됩니다",
 "대금은 2ndswing.com 적립금, PayPal, 수표 중 선택 — 적립금으로 받으면 금액이 조금 더 높습니다",
 "새 클럽은 '데모 프로그램'으로 사면 배송일로부터 60일 안에 반품하고 100% 적립금으로 돌려받을 수 있습니다 (클럽 종류별 연 3개, 상태 기준 있음)"]) + \
"<h2>8. 기다리는 게 나은 경우</h2>" + B.table(["제품", "출시", "가격", "판단"], [
 ["Odyssey TRTL", "11월 6일", "$349.99 (TRTL Max S2S $399.99)", WT("막 출시")],
 ["L.A.B. MEZZ.2i", "공식몰 판매 중, 일반 매장 11월 17일", "$499 (커스텀 $599~)", WT("막 출시")],
 ["PING G450", "2027년 1월 예상", "약 $650 예상", WT("아직 미출시")]]) + \
"<p>TRTL은 일본에서 먼저 출시되어 판매 1~4위를 모두 차지할 만큼 인기가 많았던 고관용 말렛 퍼터입니다. 다만 신제품이라 블랙프라이데이 할인은 기대하기 어렵습니다. 선물용이라면 가격보다 길이(인치)와 그립을 먼저 확인하세요. 내 스트로크에 맞는 퍼터는 <a href='/putter/'>퍼터 계산기</a>에서, 제로토크 퍼터 비교는 <a href='/blog/zero-torque-putters'>이 글</a>에서 볼 수 있습니다.</p>" + \
"<h2>9. 예산별 선물 가이드</h2>" + B.table(["예산", "추천", "메모"], [
 ["$350~$400", "Odyssey TRTL ($349.99) / TRTL Max S2S ($399.99)", "신제품, 길이·그립 확인 필수"],
 ["약 $420", "Callaway Apex Ti Super Hybrid ($419.99)", "로프트(16~24°) 선택 필요"],
 ["약 $450", "PING G440 MAX ($447) / Quantum Max ($449.98)", "현재 할인가 기준"],
 ["$500~$550", "L.A.B. MEZZ.2i ($499) / Titleist GTS300 ($549)", "MEZZ.2i는 커스텀 $599~"]]) + \
"<p>클럽은 로프트·샤프트·길이가 맞아야 해서, 깜짝 선물보다는 상품권이나 '같이 고르기'가 실패가 적습니다. 직접 사신다면 2nd Swing의 60일 데모 프로그램처럼 반품이 쉬운 곳이 안전합니다.</p>" + \
"<h2>10. '진짜 할인'인지 확인하는 법</h2>" + B.check([
 "할인 전 가격이 제조사 정가와 같은지 확인 (예: G440 MAX 정가 $617)",
 "같은 모델을 두세 곳에서 비교 — 대형 매장은 할인가가 비슷하게 맞춰지는 경우가 많습니다",
 "'할인'이 기본 샤프트·스탁 스펙에만 적용되는지 확인 (커스텀은 제외될 수 있음)",
 "사은품(공·헤드커버) 대신 가격 할인이 나은지 계산",
 "중고 시세와 비교 — 신품 할인가와 차이가 작으면 신품이 낫습니다"]) + \
"<h2>11. 지금 사기 vs 기다리기</h2>" + B.table(["", "지금 사기", "기다리기"], [
 ["장점", "확실한 할인 (G440, Quantum Max), 시즌 전 연습 가능", "최신 기술, 2027년 피팅 데이터 반영"],
 ["단점", "몇 달 뒤 후속 모델 출시 (PING)", "출시 직후엔 정가, 인기 사이즈 품절 가능"],
 ["추천 대상", "가성비 중시, 시니어·중급 골퍼", "최신 모델을 꼭 원하는 분, 아직 피팅 전인 분"]]) + \
"<h2>12. 결제 전 체크리스트</h2>" + B.check([
 "내 헤드스피드에 맞는 로프트와 샤프트 강도를 먼저 확인 (계산기 활용)",
 "정가와 '할인가'를 두 곳 이상 매장에서 비교",
 "반품·교환 기간 확인 — 블랙프라이데이 상품은 조건이 다를 수 있습니다",
 "커스텀 주문은 배송이 늦어질 수 있으니 선물이면 여유 있게",
 "쓰던 클럽이 있으면 트레이드인 시세부터 조회"]) + \
"<div class='note'><b>할인보다 '내게 맞는지'가 먼저입니다.</b> 아무리 싸도 로프트와 샤프트가 맞지 않으면 거리가 줄어듭니다. 드라이버 거리만 넣으면 헤드스피드와 추천 모델·샤프트를 알려드립니다.</div>"

# ------------------------------------------------------------------ ENGLISH
EN = STY + B.tldr("Quick take", [
 b("Buy now:")+"PING G440 MAX/SFT/LST (successor revealed) and the already-discounted Callaway Quantum Max",
 b("No rush:")+"TaylorMade Qi4D and Titleist GTS stay current through 2027",
 b("Better to wait:")+"brand-new putters (Odyssey TRTL, L.A.B. MEZZ.2i) — or if you specifically want PING's G450"]) + \
"<p>Black Friday falls on <b>Friday, November 27</b> this year, with Cyber Monday on <b>Monday, November 30</b>. Golf retailers started discounting in early November, though, and popular specs can sell out first. So the real question isn't <i>when</i> to buy — it's <b>what to buy now and what to wait on</b>.</p>" + \
"<p>2027 news is trickling in and every brand is in a different spot. TaylorMade says it won't release a new driver in 2027, while PING's G440 successor, the G450, hit the USGA conforming list on November 2. That means some clubs are close to their lowest price right now, while others may see only modest discounts. Here's the brand-by-brand picture.</p>" + \
"<h2>1. Where each brand stands for 2027</h2>" + B.table(["Brand", "Current model", "2027 plan", "Verdict"], [
 ["PING", "G440 MAX/LST/SFT", "G450 on USGA list (Nov 2); retail expected Jan 2027", GO("Good time to buy")],
 ["Callaway", "Quantum Max", "Still launches a new driver every year", GO("On sale")],
 ["TaylorMade", "Qi4D", "No new driver in 2027; next one in 2028", OK("No rush")],
 ["Titleist", "GTS2/GTS3/GTS4", "Launched June 2026, two-year cycle", OK("No rush")],
 ["Odyssey / L.A.B.", "TRTL / MEZZ.2i putters", "Just released in November", WT("Little discount")]]) + \
"<p style='font-size:.85rem;color:var(--muted)'>Note: PING hasn't announced G450 pricing or a release date; those figures are media expectations.</p>" + \
"<h2>2. Clubs worth buying now</h2>" + \
brand("PING G440 MAX / SFT / LST", "successor revealed → price cut", [
 T("What happened")+"PING cut prices on the G440 MAX, LST and SFT drivers plus fairways and hybrids. The high-MOI G440 K is not included.",
 T("Price")+"TGW and Carl's Golfland list the G440 MAX at <b>$447</b>, down from $617 (about 28% off).",
 T("Who it suits")+"MAX for maximum forgiveness, SFT (draw-biased) if you fight a slice. A safe pick for senior golfers too.",
 T("Caveat")+"The G450 appears to add a new face-flex structure (FASTFLEX), but there's no test data yet on how much it helps."]) + \
brand("Callaway Quantum Max", "about $200 off", [
 T("Price")+"Down to <b>$449.98</b> from $649.99, while TaylorMade's Qi4D was still $649.99 at the same time.",
 T("Testing")+"First for distance and second for accuracy in MyGolfSpy's 2026 driver test.",
 T("Why")+"Callaway and Cobra are among the few brands still launching a driver every year, so current models tend to get discounted late in the year."]) + \
"<h3>Choosing a G440 model</h3>" + B.table(["Model", "What it is", "Best for"], [
 ["G440 MAX", "Most forgiving core model", "Most amateurs, seniors"],
 ["G440 SFT", "Draw-biased (slice fix)", "Golfers whose ball curves right"],
 ["G440 LST", "Low spin", "Fast swingers who launch it too high"],
 ["G440 K", "Max forgiveness (not in the price cut)", "Frequent mishits"]]) + \
"<p>For reference, the G450 hit the USGA list as MAX (9/10.5/12°), LST (7.5/9/10.5°), SFT (9/10.5°) and PING's first mini driver, the MiniMax (13°), keeping the same overall structure as G440.</p>" + \
"<h2>3. No need to rush</h2>" + \
brand("TaylorMade Qi4D", "still the flagship in 2027", [
 T("Announcement")+"TaylorMade moved its drivers to a two-year cycle and will keep Qi4D as its flagship through 2027; the next new driver is expected in 2028.",
 T("What it means")+"Buy now and it won't be 'last year's model' in two months — but don't expect a replacement-driven fire sale either.",
 T("Testing")+"MyGolfSpy's top-ranked driver of 2026, with a category-leading 9.0 forgiveness score.",
 T("Tip")+"If list price is a stretch, look for bundles and gift-with-purchase offers, or go used (section 7)."]) + \
brand("Titleist GTS2 / GTS3 / GTS4", "launched June 2026, $699", [
 T("Status")+"Titleist already runs two-year cycles, so GTS stays current through 2027.",
 T("How to choose")+"GTS2 is the most forgiving and the default fit for most golfers; GTS4 is the low-spin head for faster swingers.",
 T("Specs")+"GTS2/GTS3 in 8, 9, 10 and 11°; GTS4 in 8, 9 and 10°. The hosel offers 16 loft/lie settings.",
 T("Tour")+"More than 50 PGA Tour players switched after the tour launch, including Justin Thomas and Jordan Spieth (both GTS2)."]) + \
brand("Cobra OPTM", "launched Jan 2026, $600", [
 T("Models")+"OPTM X (9/10.5°), Max-K (9/10.5/12°), Max-D (10.5/12°) and LS (9/10.5°), all with a 33-way hosel (±2°).",
 T("Who it suits")+"Max-K is Cobra's highest-MOI head for frequent mishits; Max-D is for slicers.",
 T("Timing")+"Like Callaway, Cobra still launches a driver every year, so its Black Friday pricing is worth watching."]) + \
"<h2>4. Best combos for seniors and slower swings</h2>" + \
"<p>With a slower swing, 'easy to launch and forgiving' matters far more than 'newest.' Here's a bag built around clubs that are discounted or well suited right now.</p>" + B.table(["Club", "Pick", "Price", "Why"], [
 ["Driver", "PING G440 MAX or SFT", "$447 (sale)", "Forgiving, discounted as G450 arrives"],
 ["Driver (alt.)", "Callaway Quantum Max", "$449.98 (sale)", "No. 1 for distance in 2026 testing"],
 ["Hybrid", "Callaway Apex Ti Super Hybrid", "$419.99", "For golfers who struggle with fairway woods"],
 ["Irons", "Srixon ZXiR / ZXiR HL", "$1,099.99 (7pc steel) / $1,199.99 (graphite)", "Forgiveness-focused line"]]) + \
brand("Callaway Apex Ti Super Hybrid", "2H–5H (16/18/21/24°)", [
 T("Design")+"A titanium face brazed to a steel body for speed and stability, plus a Step Sole for cleaner turf contact.",
 T("Who it suits")+"Callaway built it for golfers who struggle off the tee or with fairway woods — a natural 3-wood replacement.",
 T("Note")+"The new OptiFit4 hosel isn't compatible with shafts fitted for the older version."]) + \
"<p>For more on light drivers, see <a href='/blog/lightweight-drivers'>Best 5 lightweight drivers for slower swings</a>.</p>" + \
"<h2>5. Mini drivers: buy or wait?</h2>" + \
"<p>Mini drivers are popular with golfers whose driver keeps wandering: a smaller head and shorter shaft trade a little distance for direction. PING is entering the category for the first time with the G450 MiniMax.</p>" + B.table(["Model", "Head / loft", "Price", "Status"], [
 ["Titleist GTS300", "305cc / 13°", "$549", "Released July 2026"],
 ["PXG Secret Weapon (new gen)", "300cc / 13° / 43.25 in", "-", "Next generation out now"],
 ["PING G450 MiniMax", "13°", "TBA", "Expected 2027"]]) + \
"<p>By PXG's own data, the Secret Weapon flies about 20 yards shorter than a driver and about 10 yards longer than a 3-wood. PING fans may want to wait for the MiniMax.</p>" + \
"<h2>6. Irons may see smaller discounts this season</h2>" + \
"<p>Srixon launched its second-generation ZXi irons on October 16. ZXi7, ZXi5 and ZXi5+ are $1,499.99 for a 7-piece steel set, all forged by Endo in Japan. As a brand-new release they're unlikely to see deep cuts. Irons usually turn over every two to three years, so the previous generation — new-old-stock or used — is often the better value. Check your head type and shaft first with our <a href='/iron/'>iron calculator</a>.</p>" + \
"<h2>7. Used and trade-in instead of new</h2>" + \
"<p>If full price stings, you can sell your current clubs and put the money toward new ones. In the US, 2nd Swing's trade-in program is the best-known option.</p>" + B.check([
 "Look up your club's value with the online Value Guide",
 "Ship the clubs to 2nd Swing; they inspect them and finalize the amount",
 "Get paid in 2ndswing.com credit, PayPal or check — store credit pays a bit more",
 "Buying new? Their Demo Program lets you return a new club within 60 days of delivery for 100% store credit (three items per club category per year; condition rules apply)"]) + \
"<h2>8. When waiting makes more sense</h2>" + B.table(["Product", "Release", "Price", "Verdict"], [
 ["Odyssey TRTL", "Nov 6", "$349.99 (TRTL Max S2S $399.99)", WT("Brand new")],
 ["L.A.B. MEZZ.2i", "On L.A.B. site now; retailers Nov 17", "$499 (custom from $599)", WT("Brand new")],
 ["PING G450", "Expected Jan 2027", "~$650 expected", WT("Not out yet")]]) + \
"<p>The TRTL launched first in Japan, where its models took the top four sales spots. It's a high-MOI mallet that many golfers want, but as a brand-new release it's unlikely to see real Black Friday discounts. If it's a gift, get the length and grip right before worrying about price. Match a putter to your stroke with our <a href='/putter/'>putter calculator</a>, or compare zero-torque models <a href='/blog/zero-torque-putters'>here</a>.</p>" + \
"<h2>9. Gift guide by budget</h2>" + B.table(["Budget", "Pick", "Note"], [
 ["$350–$400", "Odyssey TRTL ($349.99) / TRTL Max S2S ($399.99)", "Brand new; confirm length and grip"],
 ["About $420", "Callaway Apex Ti Super Hybrid ($419.99)", "Choose a loft (16–24°)"],
 ["About $450", "PING G440 MAX ($447) / Quantum Max ($449.98)", "Current sale prices"],
 ["$500–$550", "L.A.B. MEZZ.2i ($499) / Titleist GTS300 ($549)", "MEZZ.2i custom from $599"]]) + \
"<p>Clubs need the right loft, shaft and length, so a gift card or shopping together beats a surprise. If you buy it yourself, choose a retailer with easy returns, such as 2nd Swing's 60-day demo program.</p>" + \
"<h2>10. How to tell a real discount</h2>" + B.check([
 "Check the 'was' price matches the maker's list price (e.g., G440 MAX list $617)",
 "Compare two or three retailers — big shops often match each other",
 "See whether the deal covers only stock specs (custom builds may be excluded)",
 "Work out whether a gift-with-purchase beats a straight price cut",
 "Compare with used prices — if the gap to new is small, buy new"]) + \
"<h2>11. Buy now vs. wait</h2>" + B.table(["", "Buy now", "Wait"], [
 ["Pros", "Real discounts (G440, Quantum Max); practice before the season", "Newest tech; fit with 2027 data"],
 ["Cons", "Successor arrives in months (PING)", "Full price at launch; popular specs may sell out"],
 ["Best for", "Value-minded, senior and mid-handicap golfers", "Those set on the newest model, or not yet fitted"]]) + \
"<h2>12. Checklist before you pay</h2>" + B.check([
 "Confirm the loft and shaft flex that match your swing speed (use our calculator)",
 "Compare the list and sale price at two or more retailers",
 "Check the return window — Black Friday items can have different terms",
 "Custom orders can ship slowly; leave time for gifts",
 "Have old clubs? Check their trade-in value first"]) + \
"<div class='note'><b>Fit beats discount.</b> A cheap driver with the wrong loft or shaft costs you distance. Enter your drive distance to get your swing speed plus model and shaft picks.</div>"

P = dict(file="blog-black-friday-2026-clubs.html", bg="bf", calc="driver",
 cat_ko="미국 구매 가이드", cat_en="US buying guide",
 title_ko="2026 블랙프라이데이 골프채, 지금 살까 기다릴까? 브랜드별 총정리",
 title_en="Black Friday 2026 golf clubs: buy now or wait? A brand-by-brand guide",
 desc_ko="2027 신제품 일정(PING G450, TaylorMade 2년 주기, Titleist GTS)과 G440·Quantum Max 할인가, 2nd Swing 트레이드인까지 블랙프라이데이 골프채 구매 가이드.",
 sub_ko="PING G450 공개, TaylorMade의 2027년 신제품 중단, G440·Quantum Max 할인까지 — 지금 사야 할 클럽과 기다려야 할 클럽을 정리했습니다.",
 sub_en="PING's G450 reveal, TaylorMade skipping a 2027 driver, and G440 and Quantum Max discounts — what to buy now and what to wait on.",
 cta_ko=("할인 전에 내 스펙부터","드라이버 거리만 넣으면 헤드스피드와 추천 모델·샤프트가 나옵니다.","드라이버 계산기 열기"),
 cta_en=("Know your specs before the sale","Enter your drive distance for speed, model and shaft picks.","Open the driver calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("The Golf Shop Online — Black Friday 2026 dates","https://www.thegolfshoponline.co.uk/blog/?p=12222%2F"),
  ("GOLF.com — Ping G450 hits USGA conforming list","https://golf.com/gear/drivers/ping-g450-usga-conforming-list/"),
  ("Golf Reviews Guide — Ping G450 drivers (2027)","https://golfreviewsguide.com/ping-g450-drivers/"),
  ("MyGolfSpy — PING drops G440 driver prices","https://mygolfspy.com/news-opinion/ping-drops-g440-driver-prices-but-not-the-g440k/"),
  ("TGW — PING G440 drivers on sale","https://www.tgw.com/l/golf-clubs/deals-sale-clearance-bullseye/drivers/ping-drivers/-/ZD0xMDUmYz0xMDUwMCZzPTEwMDAwMDQmc249MTIzMjg="),
  ("Golf Monthly — G440 Max $170 off","https://www.golfmonthly.com/buying-advice/one-of-the-most-forgiving-drivers-ive-tested-has-usd170-off-right-now"),
  ("MyGolfSpy — Callaway Quantum price cuts","https://mygolfspy.com/news-opinion/callaway-quantum-sale/"),
  ("GolfMagic — TaylorMade two-year cycle","https://www.golfmagic.com/equipment/news/taylormade-stuns-golf-world-huge-driver-announcement"),
  ("Today's Golfer — No new TaylorMade driver in 2027","https://www.todays-golfer.com/news-and-events/equipment-news/rory-mcilroy-welcomes-taylormade-driver-cycle-change/"),
  ("GOLF.com — Four of six major OEMs on two-year cycles","https://golf.com/gear/drivers/rory-mcilroy-applauds-taylormades-qi4d-decision/"),
  ("GolfWRX — Titleist GTS launch report","https://golfwrx.com/777986/golfwrx-launch-report-2026-titleist-gts-drivers/"),
  ("Skratch — Titleist GTS retail details","https://www.skratch.golf/gear-equipment/gear-equipment/titleist-gts-driver-retail-launch-details-gts2"),
  ("Golfalot — Titleist GTS2 review","https://golfalot.com/equipment-review/titleist-gts2-driver-review"),
  ("GOLF.com — Odyssey TRTL putters","https://golf.com/gear/putters/odyssey-new-trtl-putters/"),
  ("Plugged In Golf — L.A.B. MEZZ.2i","https://pluggedingolf.com/golf-news-november-10-2026"),
  ("GolfWRX — Trade-in program powered by 2nd Swing","https://www.golfwrx.com/?p=725793"),
  ("2nd Swing — Online Demo Program","https://www.2ndswing.com/online-demo-program"),
  ("Titleist — GTS drivers media release","https://mediacenter.titleist.com/en-US/265314-titleist-introduces-new-gts-drivers/"),
  ("MyGolfSpy — Titleist GTS on tour (lofts)","https://mygolfspy.com/news-opinion/now-on-tour-titleist-gts-drivers/"),
  ("MyGolfSpy — Best golf deals of the week (Qi4D forgiveness)","https://mygolfspy.com/news-opinion/the-best-golf-deals-of-the-week-4/"),
  ("Golf Digest — Cobra OPTM drivers","https://www.golfdigest.com/story/cobra-optm-drivers--what-you-need-to-know"),
  ("The Golf Guys — Cobra OPTM Max-K","https://www.thegolfguys.com/products/cobra-2026-optm-max-k-driver"),
  ("Callaway — Apex Ti Super Hybrid specs","https://www.callawaygolf.ca/product/hybrids-2026-apex-ti-super"),
  ("Carl's Golfland — Apex Ti Super Hybrid $419.99","https://www.carlsgolfland.com/callaway-apex-ti-super-hybrid"),
  ("Plugged In Golf — Apex Ti Super Hybrid review","https://pluggedingolf.com/callaway-apex-ti-super-hybrid-review/"),
  ("Today's Golfer — Titleist GTS300 mini driver","https://www.todays-golfer.com/news-and-events/equipment-news/titleist-gts300-mini-driver-everything-you-need-to-know/"),
  ("New England Golf — GTS300 305cc","https://newengland.golf/titleist-gts300-mini-driver/"),
  ("GolfWRX — New PXG Secret Weapon mini driver","https://www.golfwrx.com/788385/pxg-releases-next-generation-secret-weapon-mini-driver-with-thinner-face-and-optimized-weighting/"),
  ("Golfers Authority — PXG Secret Weapon review","https://golfersauthority.com/pxg-secret-weapon-mini-driver-review/"),
  ("Newswire — Srixon second-generation ZXi irons","https://www.newswire.com/view/content/feel-perfected-srixon-launches-second-generation-zxi-irons")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
import re
for k, v in (("ko", KO), ("en", EN)):
    print(k, len(re.sub(r"<[^>]+>", "", v.split("</style>", 1)[1])), "chars")
