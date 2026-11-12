"""Fresh random scenarios for every QA run (new seed each time), so the check keeps looking for new problems
instead of only re-testing the fixed sets. Inputs cover the full allowed range, including unusual combinations."""
import random
def make(seed, n=150):
    R = random.Random(seed)
    def pick(l, blank=.2): return "" if R.random() < blank else R.choice(l)
    def age(): return 0 if R.random() < .1 else R.randint(10, 99)
    def height(): ft = R.choice([4, 5, 5, 5, 6, 6, 7]); return ft, (R.randint(0, 11) if ft < 7 else 0)
    out = {"driver": [], "iron": [], "wedge": [], "putter": []}
    for k in range(n):
        a = age(); ft, inch = height()
        # driver: half realistic-for-age, half anywhere in 80-350
        base = 290 - 2.2 * max(0, a - 25) if a else 220
        dist = R.randint(80, 350) if R.random() < .5 else int(max(80, min(350, R.gauss(base, 35))))
        i = {"dist": dist}
        if a: i["age"] = a
        if R.random() < .6: i["hft"] = ft; i["hin"] = inch
        if R.random() < .5: i["weight"] = R.randint(70, 400)
        v = {"flight": pick(["slice", "hook", "low", "high", "straight"]), "curFlex": pick(["L", "A", "R", "S", "X", "?"], .4)}
        out["driver"].append({"n": f"RD{k+1}", "v": v, "i": i, "meta": {"age": a, **i}})
        d7 = R.randint(60, 220) if R.random() < .5 else int(max(60, min(220, R.gauss((185 - 1.4 * max(0, a - 25)) if a else 150, 18))))
        i = {"dist": d7}
        if a: i["age"] = a
        if R.random() < .6:
            i["hft"] = ft; i["hin"] = inch
            if R.random() < .7: i["wtf"] = round(max(20, min(45, (ft * 12 + inch) * 0.486 + R.uniform(-4, 4))), 1)
        v = {"hcp": pick(["h0", "h1", "h2", "h3"]), "miss": pick(["fat", "thin", "slice", "low", "good"]), "cshaft": pick(["steel", "graphite", "unk"])}
        out["iron"].append({"n": f"RI{k+1}", "v": v, "i": i, "meta": {"age": a, **i, **v}})
        pw = R.choice([0] + list(range(40, 51)))
        v = {"hcp": pick(["h0", "h1", "h2", "h3"]), "swing": pick(["dig", "mid", "slide"]), "turf": pick(["soft", "norm", "firm"]),
             "bunker": pick(["hard", "ok", "good"]), "style": pick(["square", "open"]), "cnt": pick(["1", "2", "3"], .6), "pwq": "unk" if pw == 0 else ""}
        i = {}
        if pw: i["pw"] = pw
        if R.random() < .7: i["i7"] = d7
        if a: i["age"] = a
        out["wedge"].append({"n": f"RW{k+1}", "v": v, "i": i, "meta": {"age": a, **i, **v}})
        v = {"stroke": R.choice(["straight", "slight", "strong", "unk"]), "miss": pick(["push", "pull", "dist", "short"]), "hcp": pick(["h0", "h1", "h2", "h3"]),
             "posture": pick(["bent", "norm", "up"]), "headp": pick(["blade", "mid", "mallet", "any"]), "alignp": pick(["single", "multi", "none"]), "gripp": pick(["thin", "std", "fat"])}
        i = {}
        if a: i["age"] = a
        if R.random() < .7: i["hft"] = ft; i["hin"] = inch
        out["putter"].append({"n": f"RP{k+1}", "v": v, "i": i, "meta": {"age": a, **i, **v}})
    return out
