import os as _o; ROOT = _o.path.dirname(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))))
import sys
sys.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import build as B
from cards import STY, card, b, faq

# Rewritten 2026-11-15: the first version (≈380 English words) was "crawled - currently not indexed".
# Now a full guide: how each brand forges, line-ups with lofts and prices, head-to-head cards,
# set cost, where to buy, FAQ. Facts only from the sources listed at the bottom.

note = lambda t: f"<p style='font-size:.85rem;color:var(--muted)'>{t}</p>"

# ------------------------------------------------------------------ KOREAN
KO = STY + B.tldr("핵심 요약", [
 b("가격:")+"Miura는 주요 모델 모두 개당 $350, Mizuno Pro M-13·M-15·S-1은 $215입니다. 7개 세트면 약 $2,450 대 $1,505로 <b style='display:inline;color:#fff'>약 $945 차이</b>가 납니다.",
 b("만드는 방식:")+"Mizuno는 히로시마 공장의 특허 'Grain Flow Forging', Miura는 히메지 가족 공방의 소량 단조. 둘 다 연철(마일드 카본 스틸) 단조입니다.",
 b("고르는 법:")+"희소성·장인 감성이면 Miura TC-202·CB-302, 가성비·최신 기술이면 Mizuno Pro M-13·M-15."]) + \
"<p>'일본 단조 아이언' 하면 가장 먼저 떠오르는 두 이름이 <b>Miura(미우라)</b>와 <b>Mizuno(미즈노)</b>입니다. 한국 골퍼들 사이에서도 둘 다 '타감이 좋은 채'로 유명하지만, 실제로 사려고 보면 가격, 사는 곳, 모델 구성이 꽤 다릅니다. 이 글은 두 브랜드를 <b>만드는 방식 → 모델 구성 → 맞대결 → 로프트 → 세트 가격 → 구매처</b> 순서로 비교합니다. 숫자는 모두 아래 출처에서 확인한 값입니다.</p>" + \
"<h2>1. 두 브랜드는 어떻게 만드나</h2>" + \
"<h3>Mizuno — 히로시마의 Grain Flow Forging</h3>" + \
"<p>Mizuno의 단조 아이언 헤드는 모두 <b>일본 히로시마의 한 공장</b>에서 단조되며, 1968년부터 이곳에서 만들어 왔습니다. 핵심은 'Grain Flow Forging'이라는 공법입니다. Mizuno 엔지니어 Chris Voshall의 설명에 따르면, 이 공법은 Mizuno와 히로시마의 단조 업체 Chuo가 함께 가진 <b>특허</b>입니다. 일반 단조처럼 쇳덩이(빌렛)를 두드려 모양을 만들되, 그 전에 <b>늘리고 구부리는 과정</b>을 거쳐 금속 결이 헤드 전체에 길고 끊김 없이 이어지게 합니다.</p>" + \
"<p>소재는 주로 <b>1025E 마일드 카본 스틸</b>이고, 최근 모델은 도금 아래에 <b>구리층(copper underlay)</b>을 넣어 부드러운 타감을 냅니다. 미국 판매용은 헤드를 일본에서 가져와 조지아주 Braselton 공장에서 샤프트와 그립을 조립합니다.</p>" + \
"<h3>Miura — 히메지의 소량 수제 단조</h3>" + \
"<p>Miura는 일본 히메지에서 가족이 운영하는 소량 생산 단조 공방입니다. 창업자 미우라 카츠히로의 아들 <b>미우라 신에이(Shinei Miura)</b>가 최근 모델 설계를 맡고 있고, TC-202·CB-302는 <b>S20C 연철</b>로 단조합니다. Miura는 신제품을 자주 내지 않는 것으로도 유명한데, TC-201은 5년, 후속 TC-202는 다시 6년이 걸렸습니다. 대부분 주문 제작이라 받기까지 2~3주가 걸립니다.</p>" + \
"<div class='note'><b>타감 차이, 숫자로 말할 수 있을까?</b> '어느 쪽이 더 부드럽다'는 객관적인 측정값은 없습니다. 둘 다 연철 단조라 큰 틀의 느낌은 비슷하고, 실제 차이는 <b>헤드 크기·모양, 샤프트, 로프트</b>에서 더 크게 납니다. 그래서 두 브랜드 모두 피팅 후 주문을 권합니다.</div>" + \
"<h2>2. 모델 구성 한눈에 보기</h2>" + \
B.table(["브랜드 · 모델", "형태", "구조 · 소재", "7번 로프트", "개당 가격"], [
 ["Miura <b>MC-502</b>", "모던 블레이드", "블레이드 모양에 작은 캐비티의 편안함", "—", "$350"],
 ["Miura <b>TC-202</b>", "투어 캐비티", "S20C 연철 단조, T-웨이트 바", "33°", "$350"],
 ["Miura <b>CB-302</b>", "관용성 캐비티", "S20C, Miura 최대 솔 폭(7번 19mm)", "—", "$350"],
 ["Miura <b>IC-602</b>", "중공(할로우)", "8620 연철 바디 + 얇은 페이스", "—", "$350"],
 ["Mizuno <b>Pro S-1</b>", "머슬백", "1025E 원피스 단조", "—", "$215"],
 ["Mizuno <b>Pro S-3</b>", "스플릿 캐비티 머슬", "1025E 원피스 단조", "34°", "$200 출시 (현재 커스텀 $215~)"],
 ["Mizuno <b>Pro M-13</b>", "플레이어스 캐비티", "4~5번 크로몰리 포켓, 6~8번 마이크로슬롯, 9번~GW 원피스", "32°", "$215"],
 ["Mizuno <b>Pro M-15</b>", "플레이어스 디스턴스", "4~8번 중공 + 텅스텐, 9번~GW 부분 중공", "29°", "$215"],
 ["Mizuno <b>JPX 925 Forged</b>", "관용성 단조", "JPX 라인 단조 모델", "—", "커스텀 $215~"]]) + \
note("※ 7번 로프트는 출처에서 확인된 모델만 적었습니다. 가격은 미국 정가 기준이며 매장·시점에 따라 바뀝니다.") + \
"<p>구성을 보면 성격이 분명합니다. <b>Miura는 4개 모델이 모두 같은 가격($350)</b>이고 '블레이드 → 캐비티 → 중공'으로 관용성만 달라집니다. <b>Mizuno는 2025년 Signature(S-1, S-3)와 2026년 Modern(M-13, M-15) 두 줄</b>로 나눠, 전통 모양과 최신 기술을 따로 고를 수 있게 했습니다. M-13은 한 세트 안에 세 가지 구조가 섞여 있어 '처음부터 콤보 세트'라는 평을 받습니다.</p>" + \
"<h2>3. 맞대결: 핵심 모델 4종 장단점</h2>" + \
card("Miura", "TC-202", "$350/개", "MB-101(머슬백)과 CB-302(캐비티) 사이를 메우는 투어 캐비티. 2025년 4월 출시.",
     ["스크래치부터 중간 10대 핸디캡까지 칠 수 있는 관용성", "3번 아이언까지 제공 — 롱아이언을 쓰고 싶은 분께 선택지", "Y-Grind 솔로 잔디 빠짐을 개선"],
     ["오른손잡이 전용, 크롬 마감만", "세트(4~PW) 약 $2,450으로 부담"],
     "블레이드 느낌을 원하지만 약간의 도움도 필요한 중·상급자") + \
card("Miura", "CB-302", "$350/개", "Miura 역사상 가장 길고 관용성이 높은 단조 캐비티. 7번 솔 폭 19mm로 Miura 최대.",
     ["Plugged In Golf: 'Miura다운 훌륭한 타감'", "생각보다 관용성이 좋다는 평", "이전 CB-301보다 오프셋이 줄고 탄도가 강해짐"],
     ["Plugged In Golf: 최신 디스턴스 아이언과 비교하면 거리가 길지 않음", "가격은 TC-202와 같음"],
     "Miura 타감을 원하면서 관용성을 가장 중시하는 분") + \
card("Mizuno", "Pro M-13", "$215/개", "2024년 Pro 243의 후속. 롱·미들·숏 아이언이 서로 다른 구조인 '플레이어스 스피드 캐비티'.",
     ["4~5번은 크로몰리 페이스로 볼 스피드, 9번~GW는 1025E 원피스 단조로 컨트롤", "모든 번호에 구리층 — 부드러운 타감", "Miura 대비 개당 $135 저렴"],
     ["Golf Reviews Guide: 스윙이 빠른 골퍼에겐 숏아이언 스핀이 아쉬울 수 있음", "헤드가 작아 관용성은 '중간'"],
     "정통 Mizuno 모양에 최신 스피드를 더하고 싶은 중·상급자") + \
card("Mizuno", "Pro M-15", "$215/개", "Pro 245의 후속. 작은 헤드에 중공 구조와 텅스텐을 넣은 '플레이어스 디스턴스'.",
     ["M-13보다 탄도가 높게 설계 — 롱아이언이 쉬움", "Breaking Eighty: '역대 가장 접근하기 쉬운 Mizuno Pro일 수 있다'", "작은 모양 유지하면서 관용성 중상"],
     ["7번 29°로 로프트가 강함 — 다른 세트와 번호 비교 시 주의", "단조 원피스의 순수한 타감을 원하면 S 시리즈가 맞음"],
     "작은 헤드를 좋아하지만 거리와 탄도의 도움이 필요한 분") + \
"<h2>4. 로프트: 번호가 아니라 각도로 비교하세요</h2>" + \
"<p>같은 '7번 아이언'이라도 모델마다 로프트가 다릅니다. 로프트가 강할수록(숫자가 작을수록) 멀리 가지만 탄도는 낮아집니다. 두 브랜드를 비교하거나 콤보 세트를 만들 때는 반드시 각도로 맞춰 보세요.</p>" + \
B.table(["모델", "7번", "피칭웨지(PW)", "성격"], [
 ["Mizuno Pro S-3", "34°", "—", "전통 로프트"],
 ["Miura TC-202", "33°", "45~46° (출처마다 다름)", "전통에 가까움"],
 ["Mizuno Pro M-13", "32°", "44°", "중간"],
 ["Miura CB-302", "—", "44°", "약간 강함"],
 ["Mizuno Pro M-15", "29°", "43°", "강한 로프트(거리형)"]]) + \
"<p>예를 들어 M-15의 7번(29°)은 S-3의 7번(34°)보다 5° 강해서, 실제로는 한 클럽 가까이 길게 날아갈 수 있습니다. 그러니 '7번으로 몇 야드 나간다'는 비교는 같은 로프트끼리 해야 공정합니다.</p>" + \
"<h2>5. 세트 가격과 구매처</h2>" + \
B.table(["", "Miura", "Mizuno"], [
 ["개당 정가", "$350 (모든 주요 모델)", "$215 (Pro S-1·M-13·M-15)"],
 ["7개 세트(4~PW)", "약 <b>$2,450</b>", "약 <b>$1,505</b>"],
 ["사는 곳", "miuragolf.com, Fairway Jockey, 공인 피터(True Spec 등)", "일반 골프 매장, 피팅 센터, 온라인 전반"],
 ["받기까지", "주문 제작 2~3주", "재고품 또는 커스텀(보통 수일~2주)"],
 ["중고", "물량 적음 — 2nd Swing 등에서 가끔", "물량 많음 — 이전 모델(Pro 241·243·245)도 쉽게 찾음"]]) + \
"<p>가격 차이는 7개 세트 기준 약 <b>$945</b>입니다. 이 차이가 '희소성과 장인 감성'의 값어치가 있는지가 결정의 핵심입니다. 예산이 빠듯하다면 Mizuno 이전 세대(Pro 241·243·245)가 한 대형 매장에서 세트당 $1,155로 내려가 있던 것처럼, 신모델이 나오면 이전 모델 가격이 크게 내려가는 점도 참고하세요.</p>" + \
"<div class='note'><b>Miura 정품 구매가 걱정된다면</b> <a href='/blog/honma-miura'>미국에서 Honma·Miura 정품 사는 법</a>을 먼저 읽어 보세요. 공인 딜러 확인 방법을 정리했습니다.</div>" + \
"<h2>6. 그래서 누구에게 무엇이 맞나</h2>" + \
B.table(["이런 분이라면", "추천"], [
 ["블레이드 느낌 + 약간의 도움", "Miura TC-202 또는 Mizuno Pro S-3"],
 ["Miura 타감에 관용성 최우선", "Miura CB-302"],
 ["가성비 좋은 정통 단조", "Mizuno Pro M-13"],
 ["작은 헤드인데 거리·탄도가 필요", "Mizuno Pro M-15 또는 Miura IC-602"],
 ["순수 머슬백", "Mizuno Pro S-1 (Miura는 MB-101)"]]) + \
"<p>Mizuno 안에서 고민 중이라면 <a href='/blog/mizuno-jpx-vs-pro'>Mizuno JPX vs Mizuno Pro 비교</a>도 함께 보세요. 롱아이언이 부담스러운 시니어라면 <a href='/blog/senior-hybrids-2026'>롱아이언 대신 하이브리드</a> 글이 더 도움이 될 수 있습니다.</p>" + \
"<h2>7. 자주 묻는 질문</h2>" + faq([
 ("Miura가 Mizuno보다 더 좋은 아이언인가요?", "'더 좋다'는 객관적 기준은 없습니다. 둘 다 일본에서 연철로 단조하고, 성능 차이는 브랜드보다 모델(블레이드·캐비티·중공)과 피팅에서 더 크게 납니다. Miura는 소량 생산과 희소성, Mizuno는 넓은 선택지와 가격에서 강합니다."),
 ("Mizuno 아이언은 정말 일본에서 만드나요?", "단조 헤드는 모두 히로시마 공장에서 만듭니다. 미국 판매품은 조지아주 Braselton에서 샤프트·그립을 조립합니다."),
 ("핸디캡이 높아도 칠 수 있나요?", "Miura는 CB-302나 IC-602, Mizuno는 Pro M-15나 JPX 925 Forged가 상대적으로 쉽습니다. TC-202도 스크래치부터 중간 10대 핸디캡까지를 대상으로 합니다. 더 쉬운 채가 필요하면 디스턴스 아이언을 보는 것이 맞습니다."),
 ("두 브랜드를 섞어서 세트를 만들어도 되나요?", "됩니다. 다만 로프트·라이·샤프트 무게를 맞춰야 거리 간격이 고르게 나옵니다. Miura는 공식 사이트에서 자사 두 모델을 섞는 콤보 세트 주문도 받습니다.")]) + \
"<h2>구매 전 체크리스트</h2>" + B.check([
 "내 7번 아이언 거리와 탄도를 먼저 확인하세요 (아래 아이언 계산기로 헤드 종류 추천).",
 "모델 비교는 번호가 아니라 <b>로프트 각도</b>로 하세요.",
 "세트 가격 차이(약 $945)가 감수할 만한지 정하세요.",
 "Miura는 공식 사이트나 공인 딜러에서만 사세요.",
 "트레이드인과 이전 세대 모델을 활용하면 부담이 크게 줄어듭니다."])

# ------------------------------------------------------------------ ENGLISH
EN = STY + B.tldr("QUICK TAKE", [
 b("Price:")+"Every key Miura model is $350 per club; Mizuno Pro M-13, M-15 and S-1 are $215. A 7-club set runs about $2,450 vs $1,505 — <b style='display:inline;color:#fff'>a gap of roughly $945</b>.",
 b("How they're made:")+"Mizuno uses its patented Grain Flow Forging in Hiroshima; Miura is a small family forging house in Himeji. Both forge mild carbon steel.",
 b("How to choose:")+"Miura TC-202 or CB-302 for rarity and craft; Mizuno Pro M-13 or M-15 for value and modern tech."]) + \
"<p>Say \"Japanese forged irons\" and two names come up first: <b>Miura</b> and <b>Mizuno</b>. Both are famous for feel, but once you start shopping, price, availability and the model line-ups are quite different. This guide compares them in order: <b>how they're made → line-ups → head-to-head → lofts → set cost → where to buy</b>. Every number comes from the sources listed at the end.</p>" + \
"<h2>1. How each brand forges its irons</h2>" + \
"<h3>Mizuno — Grain Flow Forging in Hiroshima</h3>" + \
"<p>All of Mizuno's forged iron heads come from <b>a single plant in Hiroshima, Japan</b>, where Mizuno irons have been made since 1968. The key is a process called Grain Flow Forging. As Mizuno engineer Chris Voshall explains, it is a <b>patent held jointly</b> by Mizuno and the Chuo forging house in Hiroshima. Like any forging, it starts with a billet of steel pounded into shape — but first the billet is <b>stretched and bent</b>, so the metal's grain runs in longer, more continuous lines through the head.</p>" + \
"<p>The main material is <b>1025E mild carbon steel</b>, and recent models add a <b>copper underlay</b> beneath the chrome for a softer feel. Heads for the US market are shipped from Japan and assembled with shafts and grips in Braselton, Georgia.</p>" + \
"<h3>Miura — small-batch forging in Himeji</h3>" + \
"<p>Miura is a family-run, small-batch forging house in Himeji, Japan. <b>Shinei Miura</b>, son of founder Katsuhiro Miura, designs the current models, and the TC-202 and CB-302 are forged from <b>S20C soft carbon steel</b>. Miura is also famous for taking its time: the TC-201 was five years in the making, and its TC-202 successor took another six. Most orders are built to spec, so expect 2–3 weeks to delivery.</p>" + \
"<div class='note'><b>Can you measure the feel difference?</b> No objective test says one is \"softer.\" Both forge mild carbon steel, so the broad feel is similar; the bigger real differences come from <b>head size and shape, shaft and loft</b>. That's why both brands recommend a fitting before you order.</div>" + \
"<h2>2. The line-ups at a glance</h2>" + \
B.table(["Brand · model", "Type", "Construction · material", "7-iron loft", "Price/club"], [
 ["Miura <b>MC-502</b>", "Modern blade", "Blade looks with small-cavity playability", "—", "$350"],
 ["Miura <b>TC-202</b>", "Tour cavity", "S20C forged, T-weight bar", "33°", "$350"],
 ["Miura <b>CB-302</b>", "Forgiving cavity", "S20C, Miura's widest sole (19 mm, 7-iron)", "—", "$350"],
 ["Miura <b>IC-602</b>", "Hollow body", "8620 mild carbon body + thin face", "—", "$350"],
 ["Mizuno <b>Pro S-1</b>", "Muscle back", "1025E one-piece forged", "—", "$215"],
 ["Mizuno <b>Pro S-3</b>", "Split-cavity muscle", "1025E one-piece forged", "34°", "$200 at launch (custom now from $215)"],
 ["Mizuno <b>Pro M-13</b>", "Players cavity", "Chromoly pocket 4–5, micro-slot 6–8, one-piece 9–GW", "32°", "$215"],
 ["Mizuno <b>Pro M-15</b>", "Players distance", "Hollow + tungsten 4–8, partial hollow 9–GW", "29°", "$215"],
 ["Mizuno <b>JPX 925 Forged</b>", "Forgiving forged", "Forged model of the JPX line", "—", "Custom from $215"]]) + \
note("7-iron lofts are listed only where a source confirmed them. Prices are US list and vary by store and date.") + \
"<p>The line-ups show each brand's personality. <b>All four Miura models cost the same ($350)</b>; they differ only in forgiveness, from blade to cavity to hollow. <b>Mizuno splits its Pro irons into two families</b> — the 2025 Signature series (S-1, S-3) and the 2026 Modern series (M-13, M-15) — so you can choose classic shaping or the newest tech. The M-13 mixes three constructions in one set, which is why reviewers call it a combo set out of the box.</p>" + \
"<h2>3. Head-to-head: four key models</h2>" + \
card("Miura", "TC-202", "$350/club", "A tour cavity that bridges the MB-101 muscle back and the CB-302 cavity. Released April 2025.",
     ["Forgiving enough for scratch to mid-teen handicaps", "Offered down to a 3-iron for players who still want one", "Y-Grind sole for cleaner turf interaction"],
     ["Right-handed only, chrome finish only", "A 4–PW set is about $2,450"],
     "Better players who want a blade feel with a little help", ko=False) + \
card("Miura", "CB-302", "$350/club", "The longest, most forgiving forged cavity back Miura has made, with its widest sole (19 mm on the 7-iron).",
     ["Plugged In Golf: the wonderful feel you expect from Miura", "More forgiveness than reviewers expected", "Less offset and a stronger flight than the CB-301"],
     ["Plugged In Golf: not long compared with modern distance irons", "Same price as the TC-202"],
     "Golfers who want Miura feel with forgiveness as the top priority", ko=False) + \
card("Mizuno", "Pro M-13", "$215/club", "Successor to the 2024 Pro 243 — a \"players speed cavity\" with different constructions in the long, mid and short irons.",
     ["Chromoly faces in the 4–5 irons for ball speed; one-piece 1025E forgings from 9-iron to GW for control", "Copper underlay throughout for a soft feel", "$135 less per club than Miura"],
     ["Golf Reviews Guide: short-iron spin may underwhelm high-speed players", "Compact head means only mid forgiveness"],
     "Mid-to-better players who want classic Mizuno shaping with modern speed", ko=False) + \
card("Mizuno", "Pro M-15", "$215/club", "Successor to the Pro 245 — a hollow, tungsten-weighted players distance iron in a compact shape.",
     ["Designed for a higher flight than the M-13, so long irons get easier", "Breaking Eighty: possibly the most accessible Mizuno Pro irons ever", "Mid-high forgiveness without a bulky look"],
     ["Strong 29° 7-iron — compare by loft, not number", "For pure one-piece forged feel, the S series fits better"],
     "Players who like a small head but need help with distance and launch", ko=False) + \
"<h2>4. Lofts: compare angles, not numbers</h2>" + \
"<p>A \"7-iron\" isn't the same club from model to model. Stronger (lower) lofts go farther but fly lower. When you compare these brands or build a combo set, match by loft angle.</p>" + \
B.table(["Model", "7-iron", "Pitching wedge", "Character"], [
 ["Mizuno Pro S-3", "34°", "—", "Traditional lofts"],
 ["Miura TC-202", "33°", "45–46° (sources differ)", "Near traditional"],
 ["Mizuno Pro M-13", "32°", "44°", "Middle"],
 ["Miura CB-302", "—", "44°", "Slightly strong"],
 ["Mizuno Pro M-15", "29°", "43°", "Strong (distance)"]]) + \
"<p>The M-15's 29° 7-iron is 5° stronger than the S-3's 34°, so it can fly close to a full club longer. Any \"my 7-iron goes X yards\" comparison is only fair between equal lofts.</p>" + \
"<h2>5. Set cost and where to buy</h2>" + \
B.table(["", "Miura", "Mizuno"], [
 ["List price per club", "$350 (all key models)", "$215 (Pro S-1, M-13, M-15)"],
 ["7-club set (4–PW)", "About <b>$2,450</b>", "About <b>$1,505</b>"],
 ["Where to buy", "miuragolf.com, Fairway Jockey, authorized fitters such as True Spec", "Regular golf retailers, fitters, online"],
 ["Lead time", "Built to order, 2–3 weeks", "In stock or custom (days to ~2 weeks)"],
 ["Used market", "Thin — occasional sets at 2nd Swing and others", "Deep — previous Pro 241, 243 and 245 are easy to find"]]) + \
"<p>The set gap is roughly <b>$945</b>, and whether that's worth paying for rarity and craftsmanship is the real decision. On a budget, remember that previous generations drop sharply once new models arrive — one large retailer listed Mizuno's Pro 241, 243 and 245 sets at $1,155.</p>" + \
"<div class='note'><b>Worried about buying genuine Miura?</b> Read our guide to <a href='/blog/honma-miura'>buying genuine Honma and Miura in the US</a> first, including how to check for an authorized dealer.</div>" + \
"<h2>6. Who should buy which</h2>" + \
B.table(["If you want...", "Try"], [
 ["a blade feel with a little help", "Miura TC-202 or Mizuno Pro S-3"],
 ["Miura feel with maximum forgiveness", "Miura CB-302"],
 ["true forged feel at a fair price", "Mizuno Pro M-13"],
 ["a small head with more distance and launch", "Mizuno Pro M-15 or Miura IC-602"],
 ["a pure muscle back", "Mizuno Pro S-1 (Miura: MB-101)"]]) + \
"<p>Choosing within Mizuno? See <a href='/blog/mizuno-jpx-vs-pro'>Mizuno JPX vs Mizuno Pro</a>. If long irons are the real problem, our guide to <a href='/blog/senior-hybrids-2026'>hybrids that replace long irons</a> may help more than any forged set.</p>" + \
"<h2>7. FAQ</h2>" + faq([
 ("Is Miura better than Mizuno?", "There's no objective \"better.\" Both forge mild carbon steel in Japan, and performance differences come more from the model type (blade, cavity, hollow) and fitting than from the brand. Miura wins on rarity and small-batch craft; Mizuno on choice and price."),
 ("Are Mizuno irons really made in Japan?", "The forged heads all come from the Hiroshima plant. Clubs sold in the US are assembled with shafts and grips in Braselton, Georgia."),
 ("Can a higher handicap play these?", "The easier options are Miura's CB-302 or IC-602 and Mizuno's Pro M-15 or JPX 925 Forged; even the TC-202 targets scratch to mid-teen handicaps. If you need more help than that, look at distance irons instead."),
 ("Can I mix the two brands in one set?", "Yes, but match loft, lie and shaft weight so your gaps stay even. Miura also takes combo-set orders mixing two of its own models on its official site.")]) + \
"<h2>Checklist before you buy</h2>" + B.check([
 "Know your 7-iron distance and flight (our iron calculator below suggests a head type).",
 "Compare models by <b>loft angle</b>, not the number on the sole.",
 "Decide whether the roughly $945 set gap is worth it to you.",
 "Buy Miura only from its official site or an authorized dealer.",
 "Trade-ins and previous-generation models cut the cost a lot."])

P = dict(file="blog-miura-vs-mizuno.html", bg="jp2", calc="iron",
 cat_ko="일본채", cat_en="Japanese clubs",
 title_ko="Miura vs Mizuno 단조 아이언 비교: 만드는 방식·모델·로프트·세트 가격 (2026)",
 title_en="Miura vs Mizuno forged irons: how they're made, models, lofts and set cost (2026)",
 desc_ko="Miura TC-202·CB-302와 Mizuno Pro M-13·M-15를 단조 방식, 로프트, 개당·세트 가격, 미국 구매처로 비교했습니다. 7개 세트 기준 약 $945 차이.",
 sub_ko="둘 다 '일본 단조'지만 만드는 방식, 가격, 사는 곳은 꽤 다릅니다. 모델·로프트·세트 가격까지 숫자로 비교했습니다.",
 sub_en="Both are \"Japanese forged,\" but how they're made, what they cost and where you buy differ. We compare models, lofts and set prices with real numbers.",
 cta_ko=("어떤 헤드가 맞을까?","7번 아이언 거리로 플레이어스·디스턴스 중 맞는 헤드를 찾아보세요.","아이언 계산기 열기"),
 cta_en=("Which head fits you?","Use your 7-iron distance to find players vs distance heads.","Open the iron calculator"),
 body_ko=KO, body_en=EN,
 sources=[
  ("GolfMagic — Interview with Mizuno engineer Chris Voshall (Grain Flow Forging patent)","https://www.golfmagic.com/node/16563"),
  ("Golfers Authority — Where are Mizuno golf clubs manufactured?","https://golfersauthority.com/where-are-mizuno-golf-clubs-manufactured/"),
  ("Mizuno EMEA — Mizuno Pro S-3 (1025E, Hiroshima)","https://emea.mizuno.com/eu/en/mizuno-pro-s-3/34107SPX6.0.html"),
  ("GOLF.com — Mizuno launches Pro M-13 and M-15 (lofts, $215)","https://golf.com/gear/irons/mizuno-launches-m-13-m-15-irons"),
  ("Golf Digest — Mizuno Pro M-13 and M-15: what you need to know","https://www.golfdigest.com/story/mizuno-pro-m13-and-m15-irons-what-you-need-to-know"),
  ("MyGolfSpy — The new Mizuno Pro M-13 and M-15 irons","https://mygolfspy.com/news-opinion/classically-modern-the-new-mizuno-pro-m-13-and-m-15-irons/"),
  ("Golf Reviews Guide — Mizuno Pro M-13 & M-15 reviewed","https://golfreviewsguide.com/?p=109974"),
  ("Breaking Eighty — Mizuno's M-13 and M-15","https://breakingeighty.com/mizuno-pro-irons"),
  ("GolfDiscount — Mizuno Pro M-13 set pricing and construction","https://www.golfdiscount.com/collections/golf-clubs/products/mizuno-pro-m-13-irons-2026"),
  ("NCG — Mizuno Pro S-1 irons ($215)","https://www.nationalclubgolfer.com/us/equipment/mizuno-pro-s-1-irons-everything-you-need-to-know"),
  ("2nd Swing — Mizuno Pro S-3 specs","https://2ndswing.com/golf-clubs/iron-sets/mizuno-pro-s-3-iron-set/pro-s3-sts"),
  ("Golfer's Cove — Mizuno Pro S-3 launch price","https://golferscove.com/products/mizuno-pro-s-3-irons-2025"),
  ("Golf Galaxy — Mizuno iron prices","https://www.golfgalaxy.com/f/mizuno-golf-irons"),
  ("GOLF.com — Miura TC-202 price and availability","https://golf.com/?p=15559727"),
  ("Golf Reviews Guide — Miura TC-202 (S20C, lofts)","https://golfreviewsguide.com/miura-tc-202-irons"),
  ("GolfBox — Miura TC-202 (handicap range, lofts)","https://golfbox.com.au/golf-blog/miura-tc-202-irons"),
  ("GolfWRX — Miura launches TC-202","https://golfwrx.com/755803/miura-launches-new-tc-202-forged-irons/"),
  ("Australian Golf Digest — Miura TC-202: what you need to know","https://www.australiangolfdigest.com.au/miura-tc-202-irons-what-you-need-to-know/"),
  ("GOLF.com — Miura CB-302 review","https://golf.com/clubpage/miura-cb-302-irons-review/?amp=1"),
  ("Miura Golf — CB-302 (19 mm sole)","https://miuragolf.com/products/cb-302-stock"),
  ("Plugged In Golf — Miura CB-302 review","https://pluggedingolf.com/miura-cb-302-irons-review/"),
  ("True Spec Golf — Miura CB-302 review","https://truespecgolf.com/blog/2023/03/16/miura-cb-302-irons-review/"),
  ("GOLF.com — Miura MC-502 first look","https://golf.com/gear/miura-new-mc-502-irons-deliver-ultimate-player-performance/"),
  ("GOLF.com — Miura IC-602: everything you need to know","https://golf.com/gear/miuras-newest-ic-602-irons-everything-you-need-to-know/?amp=1"),
  ("2nd Swing — Miura CB-302 (custom lead time)","https://www.2ndswing.com/golf-clubs/iron-sets/miura-cb-302-iron-set/cb-302-new-sts"),
  ("Miura Golf — Build your combo set","https://miuragolf.com/products/miura-iron-combo-set-builder"),
  ("Miura Golf — Year in Review 2025","https://miuragolf.com/blogs/blog/year-in-review-2025"),
  ("Miura Golf — Where to try Miura","https://miuragolf.com/blogs/blog/where-to-try-miura-golf-clubs")])
open(ROOT + '/site/' + P["file"], 'w').write(B.page(P))
print("ok", P["file"])
