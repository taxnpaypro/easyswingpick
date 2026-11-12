import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys, io, contextlib
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import build_hot as H
B = H.B
B.CALC["wedge"] = "https://claude.ai/artifact/UHd2KFRkKYuNJ1QLsSUAm2"
B.HERO_BG["drv"] = "radial-gradient(120% 120% at 80% 0%,#1d4a66 0%,#0f2a3d 60%,#0a1c29 100%)"
B.HERO_BG["irn"] = "radial-gradient(120% 120% at 80% 0%,#2a5a3e 0%,#123222 60%,#081a10 100%)"
B.HERO_BG["wdg"] = "radial-gradient(120% 120% at 80% 0%,#6b4a12 0%,#3a2708 60%,#1f1504 100%)"
B.HERO_BG["ptr"] = "radial-gradient(120% 120% at 80% 0%,#5a1a24 0%,#2b0d13 60%,#170609 100%)"
S = H.P["sources"]
b = lambda s: f"<b style='display:inline;color:#fff'>{s}</b> "

def C(ko, en):  # card pair
    return ko, en

POSTS = [
dict(file="blog-hot-drivers-2026.html", bg="drv", calc="driver", tag="DRIVER",
 cat_ko="드라이버", cat_en="Drivers",
 title_ko="2026 핫한 드라이버 장단점 분석: Qi4D vs Quantum vs ZXi RKT",
 title_en="2026's hottest drivers, pros and cons: Qi4D vs Quantum vs ZXi RKT",
 desc_ko="TaylorMade Qi4D, Callaway Quantum Max·Max-D, Srixon ZXi RKT의 장점과 단점, 추천 대상을 정리했습니다.",
 sub_ko="2026년 리뷰에서 가장 많이 언급된 드라이버 3종을 장점·단점·추천 대상으로 비교합니다.",
 sub_en="The three most talked-about drivers of 2026, compared by pros, cons and who they suit.",
 tl_ko=[b("균형:")+"TaylorMade Qi4D — 2026 GolfWRX 회원 투표 1위", b("슬라이스:")+"Callaway Quantum Max-D", b("직진성:")+"Srixon ZXi RKT"],
 tl_en=[b("Balance:")+"TaylorMade Qi4D — GolfWRX members' 2026 pick", b("Slice fix:")+"Callaway Quantum Max-D", b("Straight:")+"Srixon ZXi RKT"],
 cards=[
  (("TaylorMade","Qi4D (패밀리)","$649.99","GolfWRX 회원 투표에서 2026년 최고의 드라이버로 뽑힌 모델. 일반·Max·LS 버전이 있습니다.",
    ["외관이 뛰어나고 볼 스피드·캐리가 좋음","방향이 꾸준하고 분산이 작음","로프트 슬리브 4° 조절로 탄도 맞추기 쉬움"],
    ["Max 버전은 일반 Qi4D보다 조절 기능이 적음","LS 버전은 관용성이 떨어지고 빗맞으면 성능 하락"],
    "대부분의 골퍼. 관용성이 더 필요하면 Max, 스윙이 빠르면 LS"),
   ("TaylorMade","Qi4D (family)","$649.99","Voted the best driver of 2026 by GolfWRX members, in standard, Max and LS versions.",
    ["Great looks, fast ball speed and carry","Consistently straight with tight dispersion","4° loft sleeve makes flight easy to dial in"],
    ["The Max lacks the core model's adjustability","The LS is less forgiving and drops off on mishits"],
    "Most golfers; Max for more forgiveness, LS for fast swings")),
  (("Callaway","Quantum Max / Max-D","$649.99","Callaway가 관용성 중심에서 다시 '속도'로 방향을 튼 2026년 라인입니다.",
    ["볼 스피드가 뛰어나고 타감이 단단함","조절 호젤이 쉽고 효과적","Max-D는 한 매체가 테스트한 드로우 드라이버 중 가장 멀리 나감"],
    ["캐리가 전작 Elyte를 확실히 넘지는 못했다는 평","가격이 비싼 편","Max-D의 드로우 성향은 모두에게 맞지 않음"],
    "Max는 속도를 원하는 중급자, Max-D는 슬라이스가 고민인 분"),
   ("Callaway","Quantum Max / Max-D","$649.99","Callaway's 2026 line, shifting focus from forgiveness back to speed.",
    ["Excellent ball speed and solid feel","Simple, effective adjustable hosel","Max-D was the longest draw driver one outlet has tested"],
    ["Carry didn't clearly beat last year's Elyte","Expensive","Max-D's draw bias won't suit everyone"],
    "Max for speed-seeking mid handicaps; Max-D for slicers")),
  (("Srixon","ZXi RKT","$649.99","2026년 10월 출시된 Srixon의 새 드라이버 라인. 투어 우승으로 화제가 됐습니다.",
    ["동급 최고 수준의 탄착 분산","한 리뷰어는 지금까지 써 본 가장 빠르고 곧은 드라이버라고 평가"],
    ["일부 경쟁 모델보다 비쌈","드로우·페이드를 일부러 치기 어렵다는 평","소리와 타감을 성능과 맞바꿨다는 평"],
    "똑바로 멀리 보내는 게 최우선인 분"),
   ("Srixon","ZXi RKT","$649.99","Srixon's new line launched in October 2026, already a tour winner.",
    ["Class-leading dispersion","One reviewer's fastest, straightest driver ever"],
    ["Pricier than some rivals","Hard to shape draws and fades on purpose","Some sound and feel traded for performance"],
    "Golfers who want long and straight above all"))],
 tbl_ko=(["모델","강점","약점","가격"],[["Qi4D","균형·직진성","LS는 관용성 낮음","$649.99"],["Quantum Max-D","슬라이스 교정·거리","드로우 성향 호불호","$649.99"],["ZXi RKT","분산·직진","샷 메이킹 어려움","$649.99"]]),
 tbl_en=(["Model","Strength","Weakness","Price"],[["Qi4D","Balance, straightness","LS less forgiving","$649.99"],["Quantum Max-D","Slice fix, distance","Draw bias not for all","$649.99"],["ZXi RKT","Dispersion, straight","Hard to shape","$649.99"]]),
 how_ko=["슬라이스가 자주 나면 드로우 모델(Max-D)이나 조절 슬리브로 드로우 세팅부터 확인","빗맞음이 잦으면 LS(로우스핀) 모델은 피하기","헤드보다 샤프트 강도와 무게가 더 중요할 수 있으니 스윙 스피드부터 확인"],
 how_en=["If you slice, start with a draw model (Max-D) or a draw sleeve setting","If you mishit often, avoid low-spin (LS) heads","Shaft flex and weight can matter more than the head — check your swing speed first"],
 cta_ko=("내 스윙엔 어떤 드라이버가 맞을까?","드라이버 거리만 넣으면 헤드스피드, 추천 모델, 샤프트까지 나옵니다.","드라이버 계산기 열기"),
 cta_en=("Which driver fits your swing?","Enter your drive distance for speed, model and shaft picks.","Open the driver calculator"),
 src=S[0:14]),

dict(file="blog-hot-irons-2026.html", bg="irn", calc="iron", tag="IRON",
 cat_ko="아이언", cat_en="Irons",
 title_ko="2026 핫한 아이언 장단점 분석: Srixon ZXiR vs Qi Max vs JPX 925 Hot Metal Pro",
 title_en="2026's hottest irons, pros and cons: Srixon ZXiR vs Qi Max vs JPX 925 Hot Metal Pro",
 desc_ko="Srixon ZXiR, TaylorMade Qi Max, Mizuno JPX 925 Hot Metal Pro 아이언의 장점과 단점, 추천 대상을 정리했습니다.",
 sub_ko="쉬운 아이언부터 거리형 상급자 아이언까지, 2026년 화제의 아이언 3종을 비교합니다.",
 sub_en="From easy game-improvement to distance-focused better-player irons: three 2026 standouts.",
 tl_ko=[b("올라운더:")+"Srixon ZXiR — 쉬움과 타감을 둘 다","…"+b("슬라이스:")+"TaylorMade Qi Max", b("가성비·거리:")+"Mizuno JPX 925 Hot Metal Pro"],
 tl_en=[b("All-rounder:")+"Srixon ZXiR — easy with real feel", b("Slice help:")+"TaylorMade Qi Max", b("Value & distance:")+"Mizuno JPX 925 Hot Metal Pro"],
 cards=[
  (("Srixon","ZXiR","$1,099부터 (7개)","Srixon의 첫 본격 게임 임프루브먼트 아이언. 한 매체 랭킹에서 2026 최고의 올라운더.",
    ["게임 임프루브먼트답지 않게 매우 부드러운 타감","관용성이 크고 외관도 좋음","빗맞아도 볼 스피드와 거리가 유지됨"],
    ["어드레스 때 헤드가 조금 커 보임","HL 모델은 탄도가 너무 높을 수 있음"],
    "쉬운 아이언이지만 타감도 포기하기 싫은 중·고핸디캡"),
   ("Srixon","ZXiR","From $1,099 (7 pcs)","Srixon's first true game-improvement iron; one outlet's best all-rounder of 2026.",
    ["Remarkably soft feel for a game-improvement iron","Lots of forgiveness and great looks","Holds ball speed and distance on mishits"],
    ["Slightly large look at address","The HL model may launch too high for some"],
    "Mid-high handicaps who want easy irons with feel")),
  (("TaylorMade","Qi Max","$1,099.99부터 (7개)","부피감을 줄여 '플레이어스 아이언처럼 보이는' 게임 임프루브먼트를 목표로 한 모델.",
    ["세트 전체 볼 스피드가 뛰어남","롱아이언이 오른쪽으로 새는 경향을 줄이는 설계","약한 드로우 성향으로 슬라이스에 도움"],
    ["2024년 Qi와 성능 차이가 거의 없다는 평","디자인이 이전보다 복잡하다는 의견"],
    "이전 세대 Qi가 없는 분, 깔끔한 모양의 쉬운 아이언을 원하는 분"),
   ("TaylorMade","Qi Max","From $1,099.99 (7 pcs)","A game-improvement iron designed to look more like a players iron.",
    ["Excellent ball speed through the set","Design reduces long irons leaking right","Slight draw bias helps slicers"],
    ["Little performance gain over the 2024 Qi","Busier look than before, per some testers"],
    "Golfers without the previous Qi who want a clean, easy iron")),
  (("Mizuno","JPX 925 Hot Metal Pro","약 $150/개","Hot Metal 라인의 상급자용. 탑라인이 가장 얇고 오프셋이 가장 작습니다.",
    ["폭발적인 볼 스피드와 높은 탄도","보기 좋은 외관","합리적인 가격"],
    ["가끔 거리가 튀는 '플라이어' 샷이 나옴"],
    "거리와 외관을 모두 원하는 로우~미드 핸디캡"),
   ("Mizuno","JPX 925 Hot Metal Pro","About $150/club","The better-player Hot Metal: thinnest topline, least offset.",
    ["Explosive speed and high launch","Great looks","Fair price"],
    ["Occasional jumpers (fliers)"],
    "Low to mid handicaps wanting distance and looks"))],
 tbl_ko=(["모델","강점","약점","가격"],[["ZXiR","타감·관용성","헤드가 커 보임","$1,099~"],["Qi Max","볼 스피드·드로우","전작과 차이 작음","$1,099.99~"],["JPX 925 HMP","거리·외관·가격","가끔 플라이어","약 $150/개"]]),
 tbl_en=(["Model","Strength","Weakness","Price"],[["ZXiR","Feel, forgiveness","Larger look","From $1,099"],["Qi Max","Speed, draw bias","Little gain over Qi","From $1,099.99"],["JPX 925 HMP","Distance, looks, price","Occasional fliers","~$150/club"]]),
 how_ko=["7번 아이언 거리가 짧고 탄도가 낮다면 게임 임프루브먼트(ZXiR·Qi Max)부터","이미 공이 높이 뜨면 HL 같은 고탄도 버전은 피하기","전작을 쓰고 있다면 바꾸기 전에 시타로 차이부터 확인"],
 how_en=["Short, low 7-iron? Start with game-improvement (ZXiR, Qi Max)","Already launching high? Skip high-launch versions like HL","Own the previous model? Test before upgrading"],
 cta_ko=("내게 맞는 아이언은?","7번 아이언 거리만 넣으면 카테고리, 모델, 샤프트까지 추천합니다.","아이언 계산기 열기"),
 cta_en=("Which irons fit you?","Enter your 7-iron carry for category, model and shaft picks.","Open the iron calculator"),
 src=S[14:20]),

dict(file="blog-hot-wedges-2026.html", bg="wdg", calc="wedge", tag="WEDGE",
 cat_ko="웨지", cat_en="Wedges",
 title_ko="2026 핫한 웨지 장단점 분석: Vokey SM11 vs TaylorMade MG5 vs Cleveland RTZ",
 title_en="2026's hottest wedges, pros and cons: Vokey SM11 vs TaylorMade MG5 vs Cleveland RTZ",
 desc_ko="Titleist Vokey SM11, TaylorMade MG5, Cleveland RTZ 웨지의 장점과 단점, 추천 대상을 정리했습니다.",
 sub_ko="투어 우승 웨지 3종을 스핀, 그라인드, 타감, 날씨별 성능으로 비교합니다.",
 sub_en="Three tour-winning wedges compared on spin, grinds, feel and wet-weather performance.",
 tl_ko=[b("무난한 선택:")+"Vokey SM11 — 2026 투어 최다 우승 웨지", b("스핀:")+"TaylorMade MG5", b("벙커·비:")+"Cleveland RTZ"],
 tl_en=[b("Safest pick:")+"Vokey SM11 — winningest tour wedge of 2026", b("Spin:")+"TaylorMade MG5", b("Bunkers & rain:")+"Cleveland RTZ"],
 cards=[
  (("Titleist","Vokey SM11","$199.99~$209.99","2026 시즌 PGA 투어 최다 우승 웨지이자 GolfWRX 회원 투표 1위.",
    ["젖은 조건에서도 스핀이 줄지 않은 유일한 웨지(한 테스트 기준)","그라인드 6종(F·S·M·K·L·D)으로 선택 폭이 넓음"],
    ["다른 테스트에서는 풀샷 스핀 순위가 11위로 기대보다 낮았음"],
    "그라인드를 맞춰 쓰고 싶은 모든 수준의 골퍼"),
   ("Titleist","Vokey SM11","$199.99–$209.99","The winningest PGA Tour wedge of the 2026 season and GolfWRX members' top pick.",
    ["The only wedge in one test that lost no spin in the wet","Six grinds (F, S, M, K, L, D)"],
    ["Ranked only 11th for full-shot spin in another test"],
    "Any golfer who wants to fine-tune grinds")),
  (("TaylorMade","MG5","$199.99","2026년 투어 7승으로 화려하게 데뷔한 TaylorMade의 새 웨지.",
    ["어프로치 같은 짧은 샷에서 스핀이 많음","그라인드 6종","부드러운 타감"],
    ["헤드가 작아 상급자 취향","곧은 리딩 엣지가 모두의 눈에 맞지는 않음"],
    "스핀과 컨트롤을 중시하는 중·상급자"),
   ("TaylorMade","MG5","$199.99","TaylorMade's new wedge, with seven tour wins in its debut year.",
    ["High spin on partial shots","Six grinds","Soft feel"],
    ["Compact head suits better players","Straighter leading edge won't appeal to everyone"],
    "Mid to low handicaps who value spin and control")),
  (("Cleveland","RTZ","$199.99 (Tour Rack 맞춤)","젖은 날에도 일관성이 좋다는 평을 받은 Cleveland의 투어 웨지.",
    ["매우 부드러운 타감","다양한 라이에서 깨끗한 컨택","벙커 성능이 좋고 하이 바운스 선택지"],
    ["토우 쪽 모양이 약간 각져 보임","정확도 점수가 상대적으로 약점이라는 테스트 결과"],
    "비 오는 날이 많거나 벙커가 고민인 분"),
   ("Cleveland","RTZ","$199.99 (Tour Rack custom)","Cleveland's tour wedge, praised for wet-weather consistency.",
    ["Very soft feel","Clean contact from many lies","Good from bunkers with high-bounce options"],
    ["Slightly square toe shape","Accuracy scored as its relative weak spot in one test"],
    "Golfers in wet climates or who struggle in bunkers"))],
 tbl_ko=(["모델","강점","약점","가격"],[["Vokey SM11","젖은 날 스핀·그라인드","풀샷 스핀 평가 엇갈림","$199.99~"],["MG5","짧은 샷 스핀·타감","작은 헤드","$199.99"],["RTZ","타감·벙커","정확도 점수","$199.99"]]),
 tbl_en=(["Model","Strength","Weakness","Price"],[["Vokey SM11","Wet spin, grinds","Mixed full-shot spin","From $199.99"],["MG5","Partial-shot spin, feel","Compact head","$199.99"],["RTZ","Feel, bunkers","Accuracy score","$199.99"]]),
 how_ko=["모델보다 로프트 간격(4~6°)과 바운스가 먼저","디봇이 깊고 벙커가 어렵다면 하이 바운스","헤드가 작은 모델(MG5)은 핸디캡이 높다면 신중하게"],
 how_en=["Loft gapping (4–6°) and bounce matter more than the model","Deep divots or bunker trouble? Go higher bounce","Compact heads like MG5 need care at higher handicaps"],
 cta_ko=("내 웨지 로프트 구성은?","PW 로프트와 거리만 넣으면 로프트 간격과 바운스까지 추천합니다.","웨지 계산기 열기"),
 cta_en=("What's your ideal wedge setup?","Enter your PW loft and distance for gapping and bounce picks.","Open the wedge calculator"),
 src=S[20:26] + [S[30]]),

dict(file="blog-hot-putters-2026.html", bg="ptr", calc="putter", tag="PUTTER",
 cat_ko="퍼터", cat_en="Putters",
 title_ko="2026 핫한 퍼터 장단점 분석: Odyssey S2S #7 vs L.A.B. DF3 vs Scotty Fastback OC",
 title_en="2026's hottest putters, pros and cons: Odyssey S2S #7 vs L.A.B. DF3 vs Scotty Fastback OC",
 desc_ko="Odyssey Ai-Dual Square 2 Square #7, L.A.B. DF3, Scotty Cameron Fastback OC 퍼터의 장점과 단점을 정리했습니다.",
 sub_ko="제로토크·로우토크 열풍 속에서 2026년 가장 주목받은 퍼터 3종을 비교합니다.",
 sub_en="Three standout putters from the 2026 zero- and low-torque wave, compared.",
 tl_ko=[b("입문 제로토크:")+"Odyssey S2S #7 — 2026 테스트 1위", b("짧은 퍼트:")+"L.A.B. DF3", b("전통 감성:")+"Scotty Cameron Fastback OC"],
 tl_en=[b("First zero-torque:")+"Odyssey S2S #7 — 2026 test winner", b("Short putts:")+"L.A.B. DF3", b("Traditional feel:")+"Scotty Cameron Fastback OC"],
 cards=[
  (("Odyssey","Ai-Dual Square 2 Square #7","$399.99","MyGolfSpy의 2026 테스트 1위 퍼터. 센터 샤프트 제로토크 설계.",
    ["2026 테스트에서 가장 좋은 성적","전통 퍼터를 쓰던 골퍼도 적응하기 쉬움","할인 행사가 잦음"],
    ["제로토크 셋업은 처음엔 낯설 수 있음","페이스 회전을 잘 조절하는 골퍼에게는 이점이 적을 수 있음"],
    "처음 제로토크를 써 보는 분, 짧은 퍼트가 불안한 분"),
   ("Odyssey","Ai-Dual Square 2 Square #7","$399.99","MyGolfSpy's best putter of 2026; center-shafted zero torque.",
    ["Top performer in 2026 testing","Easy transition from traditional putters","Frequently on sale"],
    ["Zero-torque setup can feel odd at first","Less benefit if you already control face rotation well"],
    "First-time zero-torque users and nervous short putters")),
  (("L.A.B. Golf","DF3","$449.99","제로토크 열풍을 이끈 L.A.B.의 대표 모델.",
    ["페이스 안정성이 매우 뛰어남","짧은 퍼트 자신감이 크게 올라감"],
    ["모양이 호불호가 강함","고가이고, 라이각 피팅이 중요함"],
    "모양보다 결과가 중요한 분"),
   ("L.A.B. Golf","DF3","$449.99","L.A.B.'s flagship, the putter that started the zero-torque wave.",
    ["Exceptional face stability","Big boost in short-putt confidence"],
    ["Polarizing looks","Pricey, and lie-angle fitting matters"],
    "Golfers who care about results over looks")),
  (("Scotty Cameron","Studio Style Fastback OC","확인 필요","Scotty Cameron의 로우토크 모델. 전통 감성과 안정성의 절충.",
    ["거리감(페이스 컨트롤)이 뛰어남","다른 제로토크보다 셋업이 자연스러움","클래식한 Scotty 디자인"],
    ["프리미엄 가격"],
    "전통 퍼터 느낌을 유지하면서 안정성을 더하고 싶은 분"),
   ("Scotty Cameron","Studio Style Fastback OC","TBC","Scotty Cameron's low-torque model, blending tradition and stability.",
    ["Excellent pace control","More natural setup than other zero-torque putters","Classic Scotty design"],
    ["Premium price"],
    "Golfers wanting a traditional feel with added stability"))],
 tbl_ko=(["모델","강점","약점","가격"],[["Odyssey S2S #7","테스트 1위·적응 쉬움","초기 낯섦","$399.99"],["L.A.B. DF3","페이스 안정성","모양 호불호·고가","$449.99"],["Fastback OC","거리감·자연스러운 셋업","프리미엄 가격","확인 필요"]]),
 tbl_en=(["Model","Strength","Weakness","Price"],[["Odyssey S2S #7","Test winner, easy switch","Odd at first","$399.99"],["L.A.B. DF3","Face stability","Polarizing, pricey","$449.99"],["Fastback OC","Pace control, natural setup","Premium price","TBC"]]),
 how_ko=["짧은 퍼트가 자주 좌우로 빠지면 제로토크부터 시타","이미 페이스 회전을 잘 다룬다면 기존 아크 스트로크용 퍼터가 나을 수 있음","제로토크는 라이각·길이 피팅 효과가 큼"],
 how_en=["Missing short putts left and right? Try zero torque first","Already control face rotation well? An arc-stroke putter may suit you better","Zero-torque putters benefit greatly from lie and length fitting"],
 cta_ko=("내 스트로크엔 어떤 퍼터가?","스트로크 유형과 키만 넣으면 토우행, 길이, 모델을 추천합니다.","퍼터 계산기 열기"),
 cta_en=("Which putter fits your stroke?","Enter your stroke type and height for toe hang, length and models.","Open the putter calculator"),
 src=S[26:32]),
]

for p in POSTS:
    ko_cards = "".join(H.card(*k) for k, e in p["cards"])
    en_cards = "".join(H.card(*e, ko=False) for k, e in p["cards"])
    p["tl_ko"] = [x.lstrip("…") for x in p["tl_ko"]]
    p["body_ko"] = H.STY + B.tldr("핵심 요약", p["tl_ko"]) + \
        f"<p>2026년 리뷰와 테스트에서 가장 많이 언급된 {p['cat_ko']} 3종을 골라, 여러 매체의 평가를 바탕으로 장점과 단점을 정리했습니다. 가격은 미국 기준 출시가 또는 판매가입니다.</p>" + \
        H.cat(p["tag"], f"{p['cat_ko']} 3종 장단점") + ko_cards + \
        "<h2>한눈에 비교</h2>" + B.table(*p["tbl_ko"]) + \
        "<h2>고르는 요령</h2>" + B.check(p["how_ko"]) + \
        "<div class='note'><b>전체 비교가 궁금하다면</b> <a href='https://claude.ai/artifact/NddLBxMeDgZubccoapKFRd' target='_blank' rel='noopener'>드라이버·아이언·웨지·퍼터 통합 분석</a>도 함께 보세요.</div>"
    p["body_en"] = H.STY + B.tldr("QUICK TAKE", p["tl_en"]) + \
        f"<p>We picked the three {p['cat_en'].lower()} that came up most in 2026 reviews and testing, and summarized their pros and cons from multiple outlets. Prices are US launch or retail prices.</p>" + \
        H.cat(p["tag"], f"3 {p['cat_en'].lower()}: pros and cons") + en_cards + \
        "<h2>Side by side</h2>" + B.table(*p["tbl_en"]) + \
        "<h2>How to choose</h2>" + B.check(p["how_en"]) + \
        "<div class='note'><b>Want the full picture?</b> See our <a href='https://claude.ai/artifact/NddLBxMeDgZubccoapKFRd' target='_blank' rel='noopener'>combined driver, iron, wedge and putter analysis</a>.</div>"
    p["sources"] = p["src"]
    open(ROOT + '/site/' + p["file"], 'w').write(B.page(p))
    print(p["file"])
