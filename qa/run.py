"""Calculator QA: runs every scenario in qa/scenarios/ through the built calculators (deploy/) in headless Chrome,
in Korean and English, then applies the consistency rules in checks.py and the expected answers in golden.json.
Exit code 0 = all clear, 1 = problems found. build_deploy.py runs this automatically after building.
Usage: python3 qa/run.py [--quick]   (--quick = set1 only)"""
import json, os, re, sys, html, subprocess, time, shutil, socket
Q = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(Q); DEP = os.path.join(ROOT, "deploy"); OUT = os.path.join(Q, "out")
CALCS = ["driver", "iron", "wedge", "putter"]
SETS = ["set1"] if "--quick" in sys.argv else ["set1", "set2"]
# Fresh random set every run (seed printed so any failure can be reproduced: python3 qa/run.py --seed N)
SEED = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else int.from_bytes(os.urandom(4), "big")
CLEAR = ["dist", "age", "weight", "hft", "hin", "wtf", "pw", "i7"]

def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p

def run_page(port, calc, scen, lang):
    src = open(f"{DEP}/{calc}/index.html").read()
    head = '<script>try{localStorage.setItem("esp_lang","%s")}catch(e){}</script>' % lang
    js = """<script>window.addEventListener("load",()=>{setTimeout(async()=>{const S=%s,out=[];
for(const sc of S){for(const id of %s){const e=document.getElementById(id);if(e)e.value="";}
for(const [k,v] of Object.entries(sc.v||{}))eval(k+"="+JSON.stringify(v));
for(const [k,v] of Object.entries(sc.i||{}))document.getElementById(k).value=v;
try{run(true);}catch(e){out.push({n:sc.n,err:String(e)});continue;}
await new Promise(r=>setTimeout(r,250));
out.push({n:sc.n,t:document.getElementById("result").innerText,err:""});}
const p=document.createElement("textarea");p.id="QA";p.textContent=JSON.stringify(out);document.body.appendChild(p);},500);});</script>""" % (json.dumps(scen), json.dumps(CLEAR))
    name = f"qa_{lang}.html"; path = f"{DEP}/{calc}/{name}"
    open(path, "w").write(src.replace("<head>", "<head>" + head, 1).replace("</body>", js + "</body>"))
    try:
        dom = subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-background-networking", "--disable-component-update", "--no-first-run", "--virtual-time-budget=300000",
                              "--dump-dom", f"http://127.0.0.1:{port}/{calc}/{name}"], capture_output=True, text=True, timeout=600).stdout
    finally:
        os.remove(path)
    m = re.search(r'<textarea id="QA">(.*?)</textarea>', dom, re.S)
    res = json.loads(html.unescape(m.group(1))) if m else []
    if len(res) != len(scen): raise SystemExit(f"QA harness: {calc}/{lang} returned {len(res)} of {len(scen)} results")
    return res

def golden_check(port):
    """Expected answers for fixed cases. Each case lists exact values the result must contain."""
    G = json.load(open(os.path.join(Q, "golden.json"))); bad = []
    for calc in CALCS:
        cases = [c for c in G if c["calc"] == calc]
        if not cases: continue
        res = {r["n"]: r for r in run_page(port, calc, cases, "ko")}
        for c in cases:
            t = res[c["n"]].get("t", ""); lines = [x.strip() for x in t.split("\n") if x.strip()]
            for label, want in c.get("expect", {}).items():
                got = lines[lines.index(label) + 1] if label in lines else None
                if got != want: bad.append(f'{c["n"]} ({c["desc"]}): {label} = {got!r}, expected {want!r}')
            for s in c.get("contains", []):
                if s not in t: bad.append(f'{c["n"]} ({c["desc"]}): missing "{s}"')
            for s in c.get("absent", []):
                if s in t: bad.append(f'{c["n"]} ({c["desc"]}): must not show "{s}"')
    return bad

def main():
    shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
    port = free_port()
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"], cwd=DEP,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.2); problems = []; n = 0
    try:
        sys.path.insert(0, Q); import gen
        fresh = gen.make(SEED)
        for st in SETS + ["fresh"]:
            for calc in CALCS:
                scen = fresh[calc] if st == "fresh" else json.load(open(f"{Q}/scenarios/{calc}.{st}.json")); n += len(scen) * 2
                json.dump(scen, open(f"{OUT}/{calc}.{st}.in", "w"), ensure_ascii=False)
                for lang in ("ko", "en"):
                    json.dump(run_page(port, calc, scen, lang), open(f"{OUT}/{calc}.{lang}.out.json", "w"), ensure_ascii=False)
                if calc == CALCS[-1]: pass
            r = subprocess.run([sys.executable, os.path.join(Q, "checks.py")], cwd=OUT, env={**os.environ, "SET": st}, capture_output=True, text=True)
            if r.returncode or "total 0" not in r.stdout:
                problems.append(f"[{st}{' seed '+str(SEED) if st=='fresh' else ''}]\n" + r.stdout + r.stderr)
                if st == "fresh":  # keep the failing fresh scenarios so they become permanent regression cases once fixed
                    bad = json.load(open(f"{OUT}/issues.json")); keep = {}
                    for calc, lst in bad.items():
                        ids = {x[0] for x in lst}; keep[calc] = [x for x in fresh[calc] if x["n"] in ids]
                    json.dump(keep, open(f"{OUT}/found_seed{SEED}.json", "w"), ensure_ascii=False, indent=1)
        g = golden_check(port)
        if g: problems.append("[golden]\n" + "\n".join(g))
    finally:
        srv.kill()
    if problems:
        print("QA FAILED (seed %d)\n" % SEED + "\n".join(problems)); return 1
    print(f"QA OK: {n} scenario runs (KO+EN, incl. {len(fresh['driver'])*4} new random cases, seed {SEED}) + golden cases, 0 problems"); return 0

if __name__ == "__main__":
    sys.exit(main())
