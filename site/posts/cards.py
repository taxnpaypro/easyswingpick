# Shared product-card style used by the 2026-11 rewrites (same look as build_senior_hybrids.py)
import build as B
b = lambda s: f"<b style='display:inline;color:#fff'>{s}</b> "
STY = """<style>
.mc{border:1px solid var(--line);border-radius:16px;padding:18px;margin:16px 0;box-shadow:0 1px 2px rgba(15,42,61,.05)}
.mc .top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.mc .br{font-size:.72rem;font-weight:700;letter-spacing:.8px;color:var(--muted);text-transform:uppercase}
.mc h3{margin:2px 0 4px;font-size:1.15rem}
.mc .pr{font-size:.85rem;font-weight:700;color:var(--navy);background:var(--bg);border-radius:8px;padding:3px 9px}
.mc .one{color:var(--muted);font-size:.92rem;margin:6px 0 12px}
.pcx{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pcx div{border-radius:12px;padding:12px 14px;font-size:.9rem}
.pcx .p{background:var(--green-l)}.pcx .c{background:#fdecee}
.pcx b{display:block;font-size:.75rem;letter-spacing:.6px;margin-bottom:6px}
.pcx .p b{color:var(--green)}.pcx .c b{color:#b3261e}
.pcx ul{margin:0;padding-left:18px}.pcx li{margin-bottom:4px}
.mc .fit{margin-top:10px;font-size:.88rem}.mc .fit b{color:var(--green)}
@media (max-width:600px){.pcx{grid-template-columns:1fr}}
</style>"""

def card(brand, name, price, one, pros, cons, fit, ko=True):
    P = "장점" if ko else "PROS"; C = "단점" if ko else "CONS"; F = "추천 대상:" if ko else "Best for:"
    return (f'<div class="mc"><div class="top"><div><div class="br">{brand}</div><h3>{name}</h3></div><span class="pr">{price}</span></div>'
            f'<p class="one">{one}</p><div class="pcx"><div class="p"><b>✓ {P}</b><ul>' + "".join(f"<li>{x}</li>" for x in pros) +
            f'</ul></div><div class="c"><b>✗ {C}</b><ul>' + "".join(f"<li>{x}</li>" for x in cons) +
            f'</ul></div></div><p class="fit"><b>{F}</b> {fit}</p>{B.buy(ko)}</div>')

def faq(items):
    return '<div class="faq">' + ''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in items) + '</div>'
