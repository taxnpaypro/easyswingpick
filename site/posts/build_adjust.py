import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import build as B
B.HERO_BG["adj"] = "radial-gradient(120% 120% at 80% 0%,#2b4a5e 0%,#14283a 60%,#0a1621 100%)"
b = lambda s: f"<b style='display:inline;color:#fff'>{s}</b> "

STY = """<style>
.br2{border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.br2 h3{margin:0 0 8px;font-size:1.08rem}.br2 h3 small{font-weight:600;color:var(--muted);font-size:.8rem;margin-left:6px}
.br2 ul{margin:0;padding-left:18px}.br2 li{margin-bottom:5px}
.br2 .tg{display:inline-block;font-size:.72rem;font-weight:700;border-radius:6px;padding:2px 7px;margin-right:4px;background:var(--bg);color:var(--navy)}
.steps{counter-reset:s;list-style:none;padding:0}.steps li{counter-increment:s;position:relative;padding:10px 12px 10px 46px;margin:8px 0;background:var(--bg);border-radius:12px}
.steps li:before{content:counter(s);position:absolute;left:12px;top:9px;width:24px;height:24px;border-radius:50%;background:var(--navy);color:#e3c06a;font-weight:800;font-size:.8rem;display:flex;align-items:center;justify-content:center}
</style>"""

def brand(name, sub, items):
    return f'<div class="br2"><h3>{name}<small>{sub}</small></h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
def steps(items):
    return '<ol class="steps">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"
T = lambda s: f'<span class="tg">{s}</span>'

KO = STY + B.tldr("핵심 요약", [
 b("방법:")+"렌치로 풀고 → 표시 맞추고 → '딸깍' 소리까지 조이기",
 b("슬라이스:")+"로프트 올리기, 드로우(D·UPRIGHT) 설정, 무게추를 힐 쪽으로",
 b("너무 높이 뜨면:")+"로프트 내리기, 무게추를 앞쪽으로"]) + \
"<p>요즘 드라이버는 대부분 슬리브(호젤)와 무게추로 탄도와 구질을 바꿀 수 있습니다. 하지만 표시 방식과 조절 범위가 제조사마다 달라 헷갈리기 쉽습니다. 2026년 인기 드라이버를 기준으로 브랜드별 조절법을 정리했습니다.</p>" + \
"<h2>1. 공통 조절 순서</h2>" + steps([
 "헤드 바닥 힐 쪽 나사에 전용 렌치를 꽂고 시계 반대 방향으로 돌려 샤프트를 분리합니다.",
 "슬리브에서 원하는 표시를 헤드의 기준선(또는 점)에 맞춰 다시 끼웁니다.",
 "시계 방향으로 조이다가 '딸깍' 소리가 나면 멈춥니다. 더 조이지 않습니다."]) + \
"<h2>2. 바꾸면 무엇이 달라지나</h2>" + B.table(["조절", "결과", "이런 분께"], [
 ["로프트 ↑", "발사각 ↑, 스핀 ↑", "공이 낮게 깔리는 분"],
 ["로프트 ↓", "발사각 ↓, 스핀 ↓", "공이 너무 높이 뜨는 분"],
 ["업라이트·드로우 설정", "페이스가 닫혀 왼쪽 출발", "슬라이스"],
 ["무게추 힐 쪽", "드로우 성향", "슬라이스"],
 ["무게추 앞쪽", "탄도·스핀 ↓, 관용성 ↓", "스윙이 빠른 분"],
 ["무게추 뒤쪽", "탄도·스핀 ↑, 관용성 ↑", "빗맞음이 잦은 분"]]) + \
"<h2>3. 제조사별 조절법</h2>" + \
brand("TaylorMade Qi4D", "FCT 슬리브 + TAS 무게추", [
 T("슬리브")+"로프트 ±2°, 12개 위치로 0.5~0.75°씩 조절. 로프트·라이·페이스 각도가 함께 바뀝니다.",
 T("UPRIGHT")+"슬리브를 UPRIGHT 쪽으로 돌리면 토우가 들려 공이 약간 왼쪽으로 출발 → 드로우에 유리.",
 T("무게추")+"기본 4g×2, 9g×2. 슬리브와 조합하면 기본 구성만으로 128가지 설정."]) + \
brand("Callaway Quantum Max", "OptiFit 호젤 + 10g 무게추", [
 T("위 링=로프트")+"S(표기 로프트), +1, +2 등으로 조절.",
 T("아래 링=라이")+"N(중립), D(드로우). 두 링이 따로 돌아 모두 8가지 조합.",
 T("무게추")+"10g 무게추로 중립·드로우 선택. Max-D는 드로우 무게가 헤드 안에 고정."]) + \
brand("PING G440", "Trajectory Tuning 2.0 + 뒤 무게추", [
 T("슬리브")+"8개 위치, 로프트 ±1.5°, 라이는 표준에서 최대 3° 플랫.",
 T("MAX·LST")+"29g 뒤 무게추를 드로우·중립·페이드 세 위치로.",
 T("SFT")+"23g 무게추를 드로우·드로우+ 두 위치로 (슬라이스 교정용).",
 T("K")+"32g 조절식 뒤 무게추."]) + \
brand("Titleist GT / GTS", "SureFit 호젤", [
 T("슬리브")+"숫자 슬리브(1~4)와 알파벳 링(A~D)을 조합해 16가지. 드라이버는 0.75°씩.",
 T("방향")+"오른손잡이 기준 차트 왼쪽으로 가면 드로우, 오른쪽은 페이드.",
 T("무게추")+"GTS2는 앞뒤 두 무게추 위치를 바꿔 탄도 조절. 교체 무게추로 스윙웨이트 조절."]) + \
brand("Srixon ZXi RKT", "QTS 1.5 슬리브 + 솔 무게추", [
 T("슬리브")+"12개 위치, 로프트·라이·페이스 각도 ±1.5°.",
 T("RKT")+"힐 10g·토우 4g이 기본(직진). 힐 2g·토우 16g → 약 9.5야드 왼쪽, 힐 16g·토우 2g → 약 5.5야드 왼쪽.",
 T("RKT LS")+"앞 16g·뒤 2g → 스핀 약 −100rpm, 앞 2g·뒤 16g → 약 +250rpm.",
 T("RKT MAX")+"뒤쪽 14g 하나. 바꾸면 주로 스윙웨이트가 달라짐."]) + \
brand("PXG Lightning", "8단계 호젤 + 무게추", [
 T("슬리브")+"모든 Lightning 드라이버가 8단계 조절 호젤.",
 T("방향")+"가장 플랫한 설정은 페이드, 가장 업라이트한 '점(Dot)' 설정은 드로우 쪽.",
 T("무게추")+"무거운 무게추를 힐 쪽으로 옮기면 드로우."]) + \
brand("XXIO 14 · 14+", "QTS 슬리브", [
 T("슬리브")+"XXIO 역사상 처음으로 드라이버에 1.5° 로프트 슬리브 탑재.",
 T("주의")+"XXIO 14 페어웨이 우드는 조절 불가."]) + \
brand("Honma BERES 10", "고정형으로 보임", [
 "판매처 사양표에 렌치·샤프트 교체가 'No'로 표시. 피팅 단계에서 로프트·샤프트를 정확히 고르는 게 중요합니다 (구매 전 판매처 확인 권장)."]) + \
brand("Mizuno ST-Max 230", "Quick Switch 호젤", [
 T("슬리브")+"4° 범위 조절.",
 T("참고")+"단종 모델이며 후속은 JPX ONE. 중고로 살 때 로프트를 바꿀 수 있어 부담이 적습니다."]) + \
"<h2>4. 실패 없이 조절하는 요령</h2>" + B.check([
 "한 번에 하나만 바꾸고, 같은 조건에서 5~10개씩 쳐서 비교하기",
 "제조사 전용 렌치 사용 — 슬리브는 대부분 같은 브랜드끼리만 호환",
 "처음 위치를 사진으로 찍어 두기",
 "경기 중에는 조절 불가 (라운드 전에 끝내기)",
 "큰 변화가 필요하면 슬리브보다 샤프트·로프트 피팅이 먼저"]) + \
"<div class='note'><b>내 스윙 스피드부터 확인하세요.</b> 드라이버 계산기에 거리만 넣으면 헤드스피드와 맞는 모델·샤프트를 추천합니다.</div>"

EN = STY + B.tldr("QUICK TAKE", [
 b("How:")+"Loosen with the wrench → align the mark → tighten until it clicks",
 b("Slice:")+"Add loft, use draw/UPRIGHT settings, move weight to the heel",
 b("Too high:")+"Lower loft, move weight forward"]) + \
"<p>Most modern drivers let you change flight and shot shape with an adjustable sleeve (hosel) and movable weights — but the markings and ranges differ by brand. Here's how to adjust 2026's popular drivers.</p>" + \
"<h2>1. The basic steps</h2>" + steps([
 "Insert the brand's wrench into the heel-side screw on the sole and turn counterclockwise to remove the shaft.",
 "Align the desired mark on the sleeve with the line (or dot) on the head.",
 "Tighten clockwise until you hear the click — then stop."]) + \
"<h2>2. What each change does</h2>" + B.table(["Change", "Result", "For"], [
 ["More loft", "Higher launch, more spin", "Low ball flight"],
 ["Less loft", "Lower launch, less spin", "Ballooning drives"],
 ["Upright / draw setting", "Face closes, starts left", "Slicers"],
 ["Weight to heel", "Draw bias", "Slicers"],
 ["Weight forward", "Lower launch & spin, less forgiving", "Fast swingers"],
 ["Weight back", "Higher launch & spin, more forgiving", "Frequent mishits"]]) + \
"<h2>3. Brand by brand</h2>" + \
brand("TaylorMade Qi4D", "FCT sleeve + TAS weights", [
 T("Sleeve")+"±2° loft, 12 positions in 0.5–0.75° steps; loft, lie and face angle move together.",
 T("UPRIGHT")+"Turning to the UPRIGHT side raises the toe and starts the ball slightly left — helps a draw.",
 T("Weights")+"Stock 4g×2 and 9g×2; 128 combinations with the stock parts."]) + \
brand("Callaway Quantum Max", "OptiFit hosel + 10g weight", [
 T("Upper cog = loft")+"S (stated loft), +1, +2, etc.",
 T("Lower cog = lie")+"N (neutral) or D (draw); the cogs turn independently for 8 combinations.",
 T("Weight")+"10g weight for neutral or draw. Max-D has fixed internal draw weighting."]) + \
brand("PING G440", "Trajectory Tuning 2.0 + back weight", [
 T("Sleeve")+"8 positions, ±1.5° loft, up to 3° flatter lie.",
 T("MAX / LST")+"29g back weight: draw, neutral or fade.",
 T("SFT")+"23g weight: Draw or Draw+ (slice correction).",
 T("K")+"32g adjustable back weight."]) + \
brand("Titleist GT / GTS", "SureFit hosel", [
 T("Sleeve")+"Numbered sleeve (1–4) + lettered ring (A–D) = 16 settings; 0.75° steps for drivers.",
 T("Direction")+"For right-handers, moving left on the chart adds draw, right adds fade.",
 T("Weights")+"GTS2 swaps front/back weights for flight; interchangeable weights set swingweight."]) + \
brand("Srixon ZXi RKT", "QTS 1.5 sleeve + sole weights", [
 T("Sleeve")+"12 positions, ±1.5° loft, lie and face angle.",
 T("RKT")+"Stock 10g heel / 4g toe = straight. 2g heel / 16g toe ≈ 9.5 yds left; 16g heel / 2g toe ≈ 5.5 yds left.",
 T("RKT LS")+"16g front / 2g rear ≈ −100 rpm; 2g front / 16g rear ≈ +250 rpm.",
 T("RKT MAX")+"Single 14g rear weight; changes mainly affect swingweight."]) + \
brand("PXG Lightning", "8-way hosel + weights", [
 T("Sleeve")+"All Lightning drivers have an eight-way adjustable hosel.",
 T("Direction")+"Flattest setting leans fade; the most upright 'Dot' setting leans draw.",
 T("Weights")+"Moving the heavy weight toward the heel promotes a draw."]) + \
brand("XXIO 14 · 14+", "QTS sleeve", [
 T("Sleeve")+"First XXIO driver with an adjustable 1.5° loft sleeve.",
 T("Note")+"XXIO 14 fairway woods are not adjustable."]) + \
brand("Honma BERES 10", "appears fixed", [
 "Retailer specs list wrench and interchangeable shaft as 'No' — get loft and shaft right at the fitting (confirm with the seller)."]) + \
brand("Mizuno ST-Max 230", "Quick Switch hosel", [
 T("Sleeve")+"4° of adjustment.",
 T("Note")+"Discontinued; replaced by JPX ONE. Adjustability makes a used one less of a gamble."]) + \
"<h2>4. Tips for adjusting</h2>" + B.check([
 "Change one thing at a time and hit 5–10 balls per setting",
 "Use the brand's wrench — sleeves rarely cross brands",
 "Photograph the original setting first",
 "No adjusting during a round",
 "For big changes, shaft and loft fitting come before sleeve tweaks"]) + \
"<div class='note'><b>Know your swing speed first.</b> Enter your drive distance in our driver calculator for speed, model and shaft picks.</div>"

P = dict(file="blog-driver-adjust-guide.html", bg="adj", calc="driver",
 cat_ko="세팅 가이드", cat_en="Setup guide",
 title_ko="드라이버 슬리브·무게추 조절법: 제조사별 총정리 (2026)",
 title_en="How to adjust your driver's sleeve and weights: every brand (2026)",
 desc_ko="TaylorMade, Callaway, PING, Titleist, Srixon, PXG, XXIO, Honma, Mizuno 드라이버의 슬리브 각도와 무게추 조절법을 정리했습니다.",
 sub_ko="TaylorMade, Callaway, PING, Titleist, Srixon, PXG, XXIO 등 브랜드별 로프트 슬리브와 무게추 설정을 한 번에 정리했습니다.",
 sub_en="Loft sleeves and weight settings for TaylorMade, Callaway, PING, Titleist, Srixon, PXG, XXIO and more.",
 cta_ko=("내게 맞는 로프트와 샤프트는?","드라이버 거리만 넣으면 헤드스피드와 추천 모델·샤프트가 나옵니다.","드라이버 계산기 열기"),
 cta_en=("Which loft and shaft fit you?","Enter your drive distance for speed, model and shaft picks.","Open the driver calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("TaylorMade — Qi35 driver adjustment tips","https://taylormadegolf.fr/clubhouse/965041-three-ways-to-optimize-your-new-qi35-driver.html?lang=fr_FR"),
  ("customclubs — TaylorMade adapter guide","https://www.customclubs.dk/da/info/adapter-guide-taylormade/?popup=1"),
  ("Golf Reviews Guide — Qi4D adjustment","https://golfreviewsguide.com/how-to-adjust-a-taylormade-qi4d-driver/"),
  ("GOLF.com — Qi4D fitting","https://golf.com/gear/drivers/fitters-matter-taylormades-qi4d-fully-equipped"),
  ("TGW — Qi4D review","https://www.tgw.com/golf-guide/taylormade-qi4d-driver-review/"),
  ("Callaway — OptiFit instructions","https://www.callawaygolf.ca/fr/optifitinstructions"),
  ("Callaway Pre-Owned — OptiFit","https://callawaygolfpreowned.com/more/optifit-instructions"),
  ("Callaway — Quantum Max specs","https://www.callawaygolf.com/golf-clubs/drivers/spr6081392.html"),
  ("Golf Discount — Quantum Max","https://www.golfdiscount.com/products/callaway-quantum-max-driver-2026"),
  ("PGA Tour — PING G440 line","https://www.pgatour.com/article/news/equipment-report/2025/01/14/what-to-know-about-pings-new-g440-club-line"),
  ("Dick's — PING G440 MAX","https://www.dickssportinggoods.com/p/ping-g440-max-driver-24pngmg440mxdrltcdrv/24pngmg440mxdrltcdrv&amp"),
  ("Scheels — PING G440 K","https://www.scheels.com/p/805863-44350"),
  ("Titleist — SureFit guide (GT)","https://www.titleist.com/fitting/golf-club-fitting/surefit-gt-metals"),
  ("Titleist — SureFit performance guide","https://titleist.com/golf-clubs/surefit"),
  ("GlobalGolf — SureFit chart","https://www.globalgolf.com/articles/titleist-surefit-hosel-adjustment-guide/?amid=29"),
  ("The Golf Shop Online — ZXi RKT LS","https://www.thegolfshoponline.co.uk/srixon-zxi-rkt-ls-golf-driver/"),
  ("Dunlop — ZXi/RKT weight kit","https://za.dunlopsports.com/ZXiWK24.html"),
  ("Golf Digest — PXG Lightning","https://www.golfdigest.com/story/pxg-lightning-driver-fairway-wood-hybrid-preview"),
  ("customclubs — PXG hosel guide","https://www.customclubs.eu/en/blog/guide-how-pxgs-driver-hosel-works/"),
  ("PXG — weighting system","https://www.pxg.com/blogs/the-range/the-technology-behind-pxgs-weighting-system"),
  ("GOLF.com — XXIO 14","https://golf.com/gear/xxio-14-pushes-lightweight-tech-first-adjustable-driver/?amp=1"),
  ("Golf Reviews Guide — XXIO 14 fairways","https://golfreviewsguide.com/how-to-adjust-xxio-14-fairway-woods"),
  ("Golfio — Honma BERES 10","https://www.golfio.com/products/honma-beres-10-driver-460cc-26-men"),
  ("Golfers Authority — Mizuno ST-Max 230","https://golfersauthority.com/mizuno-st-max-230-driver-review/"),
  ("Today's Golfer — Driver settings","https://todays-golfer.com/news-and-events/equipment-news/how-to-adjust-golf-driver-settings-to-gain-20-yards")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
print("ok")
