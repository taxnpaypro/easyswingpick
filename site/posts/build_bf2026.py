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
"<h2>3. 서두를 필요 없는 클럽</h2>" + \
brand("TaylorMade Qi4D", "2027년에도 최신 모델", [
 T("발표")+"TaylorMade는 드라이버를 2년 주기로 바꾸고, Qi4D를 2027년까지 주력으로 유지한다고 밝혔습니다. 다음 새 드라이버는 2028년 예정입니다.",
 T("의미")+"지금 사도 1~2개월 뒤 '구형'이 되지 않습니다. 대신 후속 모델 때문에 생기는 큰 할인도 기대하기 어렵습니다.",
 T("팁")+"정가가 부담되면 블랙프라이데이 사은품·묶음 할인이나 중고(아래 4번)를 노리세요."]) + \
brand("Titleist GTS2 · GTS3 · GTS4", "2026년 6월 출시, $699", [
 T("상황")+"Titleist는 원래 2년 주기라 GTS는 2027년에도 현역입니다.",
 T("고르는 법")+"GTS2가 가장 관용성이 높아 대부분의 골퍼에게 기본 선택이고, GTS4는 스윙이 빠른 분을 위한 저스핀 모델입니다."]) + \
"<h2>4. 새 클럽 대신 중고·트레이드인</h2>" + \
"<p>정가를 다 주기 부담스럽다면 쓰던 클럽을 팔고 그 돈으로 바꾸는 방법도 있습니다. 미국에서는 2nd Swing의 트레이드인이 대표적입니다.</p>" + B.check([
 "온라인 가치 조회(Value Guide)에서 내 클럽 시세를 확인합니다",
 "클럽을 2nd Swing으로 보내면 상태를 검수한 뒤 금액이 확정됩니다",
 "대금은 2ndswing.com 적립금, PayPal, 수표 중 선택 — 적립금으로 받으면 금액이 조금 더 높습니다",
 "새 클럽은 '데모 프로그램'으로 사면 배송일로부터 60일 안에 반품하고 100% 적립금으로 돌려받을 수 있습니다 (클럽 종류별 연 3개, 상태 기준 있음)"]) + \
"<h2>5. 기다리는 게 나은 경우</h2>" + B.table(["제품", "출시", "가격", "판단"], [
 ["Odyssey TRTL", "11월 6일", "$349.99 (TRTL Max S2S $399.99)", WT("막 출시")],
 ["L.A.B. MEZZ.2i", "공식몰 판매 중, 일반 매장 11월 17일", "$499 (커스텀 $599~)", WT("막 출시")],
 ["PING G450", "2027년 1월 예상", "약 $650 예상", WT("아직 미출시")]]) + \
"<p>TRTL은 일본에서 먼저 출시되어 판매 1~4위를 모두 차지할 만큼 인기가 많았던 고관용 말렛 퍼터입니다. 다만 신제품이라 블랙프라이데이 할인은 기대하기 어렵습니다. 선물용이라면 가격보다 길이(인치)와 그립을 먼저 확인하세요.</p>" + \
"<h2>6. 지금 사기 vs 기다리기</h2>" + B.table(["", "지금 사기", "기다리기"], [
 ["장점", "확실한 할인 (G440, Quantum Max), 시즌 전 연습 가능", "최신 기술, 2027년 피팅 데이터 반영"],
 ["단점", "몇 달 뒤 후속 모델 출시 (PING)", "출시 직후엔 정가, 인기 사이즈 품절 가능"],
 ["추천 대상", "가성비 중시, 시니어·중급 골퍼", "최신 모델을 꼭 원하는 분, 아직 피팅 전인 분"]]) + \
"<h2>7. 결제 전 체크리스트</h2>" + B.check([
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
"<h2>3. No need to rush</h2>" + \
brand("TaylorMade Qi4D", "still the flagship in 2027", [
 T("Announcement")+"TaylorMade moved its drivers to a two-year cycle and will keep Qi4D as its flagship through 2027; the next new driver is expected in 2028.",
 T("What it means")+"Buy now and it won't be 'last year's model' in two months — but don't expect a replacement-driven fire sale either.",
 T("Tip")+"If list price is a stretch, look for bundles and gift-with-purchase offers, or go used (section 4)."]) + \
brand("Titleist GTS2 / GTS3 / GTS4", "launched June 2026, $699", [
 T("Status")+"Titleist already runs two-year cycles, so GTS stays current through 2027.",
 T("How to choose")+"GTS2 is the most forgiving and the default fit for most golfers; GTS4 is the low-spin head for faster swingers."]) + \
"<h2>4. Used and trade-in instead of new</h2>" + \
"<p>If full price stings, you can sell your current clubs and put the money toward new ones. In the US, 2nd Swing's trade-in program is the best-known option.</p>" + B.check([
 "Look up your club's value with the online Value Guide",
 "Ship the clubs to 2nd Swing; they inspect them and finalize the amount",
 "Get paid in 2ndswing.com credit, PayPal or check — store credit pays a bit more",
 "Buying new? Their Demo Program lets you return a new club within 60 days of delivery for 100% store credit (three items per club category per year; condition rules apply)"]) + \
"<h2>5. When waiting makes more sense</h2>" + B.table(["Product", "Release", "Price", "Verdict"], [
 ["Odyssey TRTL", "Nov 6", "$349.99 (TRTL Max S2S $399.99)", WT("Brand new")],
 ["L.A.B. MEZZ.2i", "On L.A.B. site now; retailers Nov 17", "$499 (custom from $599)", WT("Brand new")],
 ["PING G450", "Expected Jan 2027", "~$650 expected", WT("Not out yet")]]) + \
"<p>The TRTL launched first in Japan, where its models took the top four sales spots. It's a high-MOI mallet that many golfers want, but as a brand-new release it's unlikely to see real Black Friday discounts. If it's a gift, get the length and grip right before worrying about price.</p>" + \
"<h2>6. Buy now vs. wait</h2>" + B.table(["", "Buy now", "Wait"], [
 ["Pros", "Real discounts (G440, Quantum Max); practice before the season", "Newest tech; fit with 2027 data"],
 ["Cons", "Successor arrives in months (PING)", "Full price at launch; popular specs may sell out"],
 ["Best for", "Value-minded, senior and mid-handicap golfers", "Those set on the newest model, or not yet fitted"]]) + \
"<h2>7. Checklist before you pay</h2>" + B.check([
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
  ("2nd Swing — Online Demo Program","https://www.2ndswing.com/online-demo-program")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
import re
for k, v in (("ko", KO), ("en", EN)):
    print(k, len(re.sub(r"<[^>]+>", "", v.split("</style>", 1)[1])), "chars")
