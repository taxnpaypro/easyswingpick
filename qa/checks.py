"""Consistency rules applied to every scenario result (run by qa/run.py). Prints problems and exits 1 if any."""
import os;SET=os.environ.get("SET","100")
import json,re,collections
issues=collections.defaultdict(list)
def L(t):return [x.strip() for x in t.split("\n") if x.strip()]
def parse(t,setHdr,whyHdr,stopHdrs):
    ls=L(t);kv={};why=[];picks=[]
    try:
        a=ls.index(setHdr);b=ls.index(whyHdr)
        seg=ls[a+1:b]
        for k in range(len(seg)-1):kv.setdefault(seg[k],seg[k+1])
        e=b+1
        while e<len(ls) and ls[e] not in stopHdrs:why.append(ls[e]);e+=1
        cur=None
        for x in ls[e:]:
            if x=="BEST MATCH" or re.fullmatch(r"추천 \d|Pick \d",x):
                cur={"lines":[]};picks.append(cur)
            elif cur is not None:cur["lines"].append(x)
    except ValueError:pass
    for p in picks:
        ln=p["lines"];p["brand"]=ln[0] if ln else "";p["model"]=ln[1] if len(ln)>1 else ""
        p["pct"]=int(ln[2].rstrip("%")) if len(ln)>2 and ln[2].endswith("%") else None
        p["text"]=" ".join(ln)
    return kv,why,picks
def generic(c,n,t,picks,why,meta):
    for bad in ["undefined","NaN","null","[object"]:
        if bad in t:issues[c].append((n,f"text contains {bad}"))
    if not why:issues[c].append((n,"no reasons"))
    if len(picks)!=3:issues[c].append((n,f"{len(picks)} picks"))
    ps=[p["pct"] for p in picks]
    if any(p is None or p<55 or p>97 for p in ps) or ps!=sorted(ps,reverse=True):issues[c].append((n,f"pct {ps}"))
    if len({p['model'] for p in picks})!=len(picks):issues[c].append((n,"duplicate pick"))
    if len(set(why))!=len(why):issues[c].append((n,"duplicate reason"))
    age=meta.get("age",0)
    if any("60세 이상" in w for w in why) and not (age and age>=60):issues[c].append((n,"60+ text but age "+str(age)))
    for p in picks:
        if "60세 이상" in p["text"] and not(age and age>=60):issues[c].append((n,"pick 60+ text, age "+str(age)))
def run(c,setHdr,stop,fn):
    data=json.load(open(f"{c}.ko.out.json"));inp={x["n"]:x for x in json.load(open(f"{c}.{SET}.in"))}
    for r in data:
        if r.get("err"):issues[c].append((r["n"],"ERR "+r["err"]));continue
        m=inp[r["n"]];meta={**m["meta"],**m["v"]}
        kv,why,picks=parse(r["t"],setHdr,"이렇게 추천한 이유",stop)
        if not kv:issues[c].append((r["n"],"parse fail"));continue
        generic(c,r["n"],r["t"],picks,why,meta);fn(r["n"],kv,why,picks,meta,r["t"])
    en=json.load(open(f"{c}.en.out.json"))
    for r in en:
        for bad in ["undefined","NaN","[object"]:
            if bad in r.get("t",""):issues[c].append((r["n"],"EN contains "+bad))
        if re.search(r"[가-힣]",r.get("t","").replace("한국어","").replace("한","")):
            k=re.findall(r"[^\n]*[가-힣][^\n]*",r["t"]);k=[x for x in k if x.strip() not in("한","한국어")]
            if k:issues[c].append((r["n"],"EN has Korean: "+k[0][:60]))
# ---------- DRIVER
def drv(n,kv,why,picks,m,t):
    s=int(re.search(r"약 (\d+)mph",why[0]).group(1))
    exp="L" if s<72 else "A" if s<82 else "R" if s<92 else "S" if s<105 else "X"
    if kv.get("강도")!=exp:issues["driver"].append((n,f"flex {kv.get('강도')} vs {exp} @{s}"))
    if abs(s-round(m["dist"]/2.4))>1:issues["driver"].append((n,"speed calc"))
    fl=m["flight"]
    top=picks[0]["text"]
    if fl=="slice" and not any(x in top for x in["드로우","슬라이스"]) and "무게추를 힐" not in " ".join(why):issues["driver"].append((n,"slice but top pick no draw: "+picks[0]["model"]))
    if fl=="hook":
        for p in picks:
            if re.search(r"적합도 [^가-힣]*드로우|\b드로우\b",p["text"]) and "드로우 설계가 없는" not in p["text"] and " 드로우 " in " "+p["text"]+" ":issues["driver"].append((n,"hook but draw pick "+p["model"]))
    if fl=="high" and "저스핀" not in top and s>=95:issues["driver"].append((n,"high flight fast, top not low spin "+picks[0]["model"]))
    if m.get("age",0)>=60 and s<85 and "경량" not in top:issues["driver"].append((n,f"senior slow ({s}) top not light: "+picks[0]["model"]))
    if m.get("age",0) and m["age"]<50 and s>=100 and "경량" in top:issues["driver"].append((n,"young fast but light top"))
    h=m.get("hft",0)*12+m.get("hin",0) if m.get("hft") else 0
    ln=kv.get("길이","")
    if h:
        cm=h*2.54;e="표준" if 165<=cm<=185 else("−0.5인치" if cm<165 else "+0.5인치")
        if ln!=e:issues["driver"].append((n,f"len {ln} vs {e} h{h}"))
    cf=m.get("curFlex")
    if cf and cf!="?":
        F="LARSX";ci,ri=F.index(cf),F.index(exp)
        w=" ".join(why)
        want="약할 수" if ci<ri else "강할 수" if ci>ri else "잘 맞습니다"
        if want not in w:issues["driver"].append((n,f"curFlex {cf} vs {exp} msg missing"))
    lo=kv.get("로프트","")
    if fl=="low" and s>=100 and lo.startswith("9"):issues["driver"].append((n,"low flight still 9°"))
    for p in picks:
        mm=re.search(r"권장 구간\((\d+)~(\d+)mph\)",p["text"])
        if mm:
            a,b=int(mm.group(1)),int(mm.group(2))
            if a<=s<=b and "들어갑니다" not in p["text"]:issues["driver"].append((n,"range msg"))
            if (s<a-5 or s>b+5) and "벗어나지만" not in p["text"]:issues["driver"].append((n,"out msg"))
run("driver","추천 샤프트 세팅",{"추천 샤프트 예시"},drv)
# ---------- IRON
def iro(n,kv,why,picks,m,t):
    w=" ".join(why);s=int(re.search(r"약 (\d+)mph",why[0]).group(1))
    hc=m.get("hcp");head=kv.get("헤드 종류")
    hmap={"h0":("플레이어스","블레이드"),"h1":("플레이어스 디스턴스",),"h2":("게임 임프루브먼트",),"h3":("슈퍼 게임 임프루브먼트",)}
    if hc and head not in hmap[hc] and "조정했습니다" not in w:issues["iron"].append((n,f"hcp {hc} head {head}"))
    mat=kv.get("샤프트 소재")
    age=m.get("age",0)
    if age>=60 and mat!="그라파이트" and s<80:issues["iron"].append((n,f"senior {age} slow {s} not graphite ({mat})"))
    if mat=="그라파이트" and age and age<60 and s>=80:issues["iron"].append((n,f"young fast graphite"))
    if mat=="스틸" and s<75:issues["iron"].append((n,"slow but heavy steel"))
    if hc=="h0" and age>=70 and s<70 and head in("블레이드",):issues["iron"].append((n,"old slow blade"))
    # head type mismatch with picks
    for p in picks:
        if head and head not in p["brand"] and "일치" in p["text"]:issues["iron"].append((n,"pick says match but brand type differs"))
    if not any(head in p["brand"] for p in picks):issues["iron"].append((n,f"no pick of head type {head}: "+"|".join(p['brand'] for p in picks)))
    if "wtf" in m and "hft" in m:
        h=m["hft"]*12+m["hin"];d=m["wtf"]-h*0.486
        e="1° 업라이트" if d>1 else "1° 플랫" if d<-1 else "표준"
        if kv.get("라이각")!=e:issues["iron"].append((n,f"lie {kv.get('라이각')} vs {e}"))
    ms=m.get("miss")
    if ms=="slice" and "슬라이스" not in w:issues["iron"].append((n,"slice msg"))
    if ms=="fat" and not any("넓은 솔" in p["text"] for p in picks) and "솔이 넓은 모델도" not in w:issues["iron"].append((n,"fat but no wide sole pick"))
    if m.get("cshaft")=="graphite" and mat=="경량 스틸" and "스틸로 바꾸면" in w:issues["iron"].append((n,"graphite->light steel advice"))
    if m.get("cshaft")=="steel" and mat=="그라파이트" and "그라파이트로 바꾸면" not in w:issues["iron"].append((n,"steel->graphite note missing"))
    if m.get("cshaft")=="graphite" and mat=="스틸" and "스틸" not in w.split("이 속도")[-1]:issues["iron"].append((n,"graphite->steel note missing"))
    for p in picks:
        if "60세 이상" in p["text"] and "경량" not in p["text"]:pass
run("iron","추천 아이언 세팅",{"추천 샤프트 예시"},iro)
# ---------- WEDGE
NAMES={"어프로치 웨지","갭웨지","샌드웨지","로브웨지","샌드·로브 겸용"}
def wed(n,kv,why,picks,m,t):
    ls=L(t);a=ls.index("웨지별 추천 세팅");b=ls.index("이렇게 추천한 이유")
    seg=ls[a+1:b];rows=[]
    for k,x in enumerate(seg):
        if re.fullmatch(r"\d+°",x) and k+2<len(seg) and seg[k+1] in NAMES:
            parts=seg[k+2].split("\t") if "\t" in seg[k+2] else [seg[k+2]]
            rows.append((int(x[:-1]),seg[k+1],seg[k+2]))
    w=" ".join(why)
    pw=m.get("pw",45)
    lofts=[r[0] for r in rows];all_=[pw]+lofts;g=[all_[i+1]-all_[i] for i in range(len(lofts))]
    if not rows:issues["wedge"].append((n,"no rows"));return
    if any(x<3 or x>8 for x in g):issues["wedge"].append((n,f"gaps {all_}"))
    if m.get("cnt") and len(rows)!=int(m["cnt"]) and "줄였습니다" not in w:issues["wedge"].append((n,f"cnt {m['cnt']} rows {len(rows)}"))
    top=lofts[-1];mm=re.search(r"(\d+)°로 잡았|(\d+)° 이상으로|(\d+)° 전후",w)
    if "56° 전후" in w and top>56:issues["wedge"].append((n,"top56 msg but "+str(top)))
    if ("58° 이상" in w or "58°로" in w) and top<58:issues["wedge"].append((n,"top58 msg but "+str(top)))
    if m.get("bunker")=="hard":
        mm=re.search(r"쓰실 (\d+)° 웨지",w)
        if not mm:
            if "하나 더" not in w:issues["wedge"].append((n,"bunker msg missing"))
        else:
            r=[x for x in rows if x[0]==int(mm.group(1))]
            if not r:issues["wedge"].append((n,"bunker wedge not in rows"))
            elif "로우" in r[0][2].split("\t")[0] or r[0][2].startswith("로우"):issues["wedge"].append((n,"bunker wedge low bounce "+r[0][2]))
    names=[r[1] for r in rows]
    if names.count("갭웨지")>1:issues["wedge"].append((n,"two gap wedges"))
    if top>60:issues["wedge"].append((n,f"top {top} too high"))
    tm=re.search(r"(\d+)°로 잡았습니다",w)
    if tm and int(tm.group(1))!=top:issues["wedge"].append((n,"top text mismatch"))
    if names.count("샌드웨지")+names.count("샌드·로브 겸용")>1:issues["wedge"].append((n,"two sand wedges"))
    if "디봇이 깊거나" in w and m.get("swing")!="dig" and m.get("turf")!="soft":issues["wedge"].append((n,"hi msg without dig/soft"))
    if "잔디를 스치듯" in w and m.get("swing")!="slide" and m.get("turf")!="firm":issues["wedge"].append((n,"lo msg w/o slide/firm"))
    if "yd" in t:
        ds=[int(x) for x in re.findall(r"(\d+) yd",t)]
        if ds!=sorted(ds,reverse=True):issues["wedge"].append((n,f"dists {ds}"))
    if m.get("style")=="open" and m.get("hcp") in("h0","h1") and picks and "투어" not in picks[0]["text"]:issues["wedge"].append((n,"open but top not tour"))
    age=m.get("age",0)
    if (m.get("hcp")=="h3" or (age>=60 and m.get("hcp") not in("h0","h1"))) and picks and all("투어형" in p["text"] for p in picks) and m.get("style")!="open":issues["wedge"].append((n,"senior/high hcp all tour picks"))
run("wedge","웨지별 추천 세팅",{"추천 웨지"},wed) if False else None
# wedge has no kv section; custom
data=json.load(open("wedge.ko.out.json"));inp={x["n"]:x for x in json.load(open(f"wedge.{SET}.in"))}
for r in data:
    m={**inp[r["n"]]["meta"],**inp[r["n"]]["v"]};t=r["t"];ls=L(t)
    if r.get("err"):issues["wedge"].append((r["n"],"ERR "+r["err"]));continue
    try:b=ls.index("이렇게 추천한 이유")
    except:issues["wedge"].append((r["n"],"parse"));continue
    why=[];e=b+1
    while ls[e]!="추천 웨지":why.append(ls[e]);e+=1
    _,_,picks=parse(t,"웨지별 추천 세팅","이렇게 추천한 이유",{"추천 웨지"})
    generic("wedge",r["n"],t,picks,why,m);wed(r["n"],{},why,picks,m,t)
en=json.load(open("wedge.en.out.json"))
for r in en:
    for bad in ["undefined","NaN","[object"]:
        if bad in r.get("t",""):issues["wedge"].append((r["n"],"EN "+bad))
# ---------- PUTTER
def put(n,kv,why,picks,m,t):
    w=" ".join(why);sk=m["stroke"];sk2="slight" if sk=="unk" else sk
    hang=kv.get("헤드 균형");ms=m.get("miss")
    exp={"straight":"제로토크" if ms in("short","push","pull") else "페이스 밸런스","slight":"제로토크" if ms=="short" else "약한 토우행","strong":"강한 토우행"}[sk2]
    if hang!=exp:issues["putter"].append((n,f"hang {hang} vs {exp} ({sk},{ms})"))
    shape=kv.get("헤드 모양");hp=m.get("headp")
    SH={"blade":"블레이드","mid":"미드 말렛","mallet":"말렛"}
    if hp and hp!="any" and shape!=SH[hp]:issues["putter"].append((n,f"shape {shape} vs pref {hp}"))
    ln=float(kv.get("길이","34").rstrip('"'))
    if not 32<=ln<=36:issues["putter"].append((n,"len "+str(ln)))
    if "hft" in m:
        h=m["hft"]*12+m["hin"];e=33 if h<66 else 34 if h<72 else 35 if h<75 else 35.5
        e+= -1 if m.get("posture")=="bent" else 1 if m.get("posture")=="up" else 0;e=max(32,min(36,e))
        if ln!=e:issues["putter"].append((n,f"len {ln} vs {e}"))
    if "hft" not in m and ln!=34 and "34인치로 추천" in w:issues["putter"].append((n,"len text 34 but "+str(ln)))
    gr=kv.get("그립")
    if m.get("gripp"):
        G={"thin":"가는","std":"표준","fat":"굵은"}
        if gr!=G[m["gripp"]]:issues["putter"].append((n,"grip pref ignored"))
    if "굵은 그립을 추천" in w and gr!="굵은":issues["putter"].append((n,"fat grip msg but "+gr))
    if "제로토크를 우선" in w and hang!="제로토크":issues["putter"].append((n,"ZT msg but "+hang))
    hp_t={"제로토크":"제로토크","페이스 밸런스":None,"약한 토우행":None,"강한 토우행":None}
    if hang=="제로토크" and not any("제로토크" in p["text"] for p in picks[:1]):issues["putter"].append((n,"ZT setup but top not ZT "+picks[0]["model"]))
    if hang=="강한 토우행" and any("제로토크" in p["text"].split("적합도")[1][:20] for p in picks):issues["putter"].append((n,"strong arc but ZT pick"))
    if hp and hp!="any" and not any(SH[hp] in p["brand"] for p in picks) and "적어 다른 모양" not in w:issues["putter"].append((n,"pref shape absent no note"))
    for p in picks:
        if "선호하신 헤드 모양" in p["text"] and not(hp and hp!="any" and SH[hp] in p["brand"]):issues["putter"].append((n,"headOk wrong "+p["brand"]))
    if (m.get("age",0)>=60 or m.get("hcp")=="h3") and not hp and shape=="블레이드" and sk2!="strong":issues["putter"].append((n,"senior blade"))
run("putter","추천 퍼터 세팅",{"추천 퍼터"},put)
tot=0
for c,v in issues.items():
    cnt=collections.Counter(x[1].split(" (")[0].split(":")[0][:40] for x in v)
    print("==",c,len(v));tot+=len(v)
    for k,nn in cnt.most_common():print("  ",nn,k, [x[0] for x in v if x[1].startswith(k)][:6])
print("total",tot)
json.dump({c:v for c,v in issues.items()},open("issues.json","w"),ensure_ascii=False,indent=0)
import sys
sys.exit(1 if tot else 0)
