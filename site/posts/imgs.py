# Product image slots.
# PHOTO: fill with image URLs from affiliate programs (Awin/FlexOffers product feeds, Amazon SiteStripe)
# once approved. Until then, a generic club illustration is shown.
PHOTO = {
  # "Qi4D (패밀리)": "https://...",
}

CAT = {
 "Qi4D (패밀리)": "driver", "Qi4D (family)": "driver", "Quantum Max / Max-D": "driver", "ZXi RKT": "driver",
 "ZXiR": "iron", "Qi Max": "iron", "JPX 925 Hot Metal Pro": "iron",
 "Vokey SM11": "wedge", "MG5": "wedge", "RTZ": "wedge",
 "Ai-Dual Square 2 Square #7": "mallet", "DF3": "mallet", "Studio Style Fastback OC": "mallet2",
}

BG = {"TaylorMade": ("#1b2b3a", "#33536f"), "Callaway": ("#1d2633", "#3c4f6b"), "Srixon": ("#2a1e1e", "#6b3434"),
      "Mizuno": ("#13283f", "#2b5d8f"), "Titleist": ("#1e1e22", "#4a4a55"), "Cleveland": ("#1f2a24", "#3f6150"),
      "Odyssey": ("#1a1f2e", "#3a4a7a"), "L.A.B. Golf": ("#14261e", "#2f6a50"), "Scotty Cameron": ("#2b2416", "#6b5a2e")}

STEEL = '<linearGradient id="st{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/><stop offset=".5" stop-color="#b9c2cc"/><stop offset="1" stop-color="#7d8894"/></linearGradient>'
DARK = '<linearGradient id="dk{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a5562"/><stop offset=".55" stop-color="#1c232b"/><stop offset="1" stop-color="#0b0f13"/></linearGradient>'

SHAPES = {
 # shaft enters from top-right, head on the ground line y=150
 "driver": '<path d="M318 18 L262 92" stroke="url(#st{u})" stroke-width="4" stroke-linecap="round"/>'
           '<path d="M266 86 C250 92 238 104 236 112 C150 104 96 112 88 136 C84 150 104 158 150 158 C214 158 262 150 276 132 C284 118 280 100 266 86Z" fill="url(#dk{u})" stroke="#9aa6b2" stroke-width="1.2"/>'
           '<path d="M96 140 C130 132 200 130 268 126" stroke="#e3c06a" stroke-width="2" fill="none" opacity=".8"/>',
 "iron": '<path d="M318 18 L246 98" stroke="url(#st{u})" stroke-width="4" stroke-linecap="round"/>'
         '<path d="M250 92 L236 108 C200 108 140 112 120 118 C104 124 98 140 104 154 C150 158 220 158 256 152 C262 136 262 112 250 92Z" fill="url(#st{u})" stroke="#5c6772" stroke-width="1.2"/>'
         '<path d="M120 128 L240 120 M118 136 L244 128 M116 144 L246 136" stroke="#7d8894" stroke-width="1.2"/>'
         '<path d="M150 150 C190 150 230 148 252 144" stroke="#e3c06a" stroke-width="3" fill="none"/>',
 "wedge": '<path d="M318 18 L248 96" stroke="url(#st{u})" stroke-width="4" stroke-linecap="round"/>'
          '<path d="M252 90 L238 106 C196 98 140 96 118 104 C100 112 96 140 106 156 C150 160 222 158 258 152 C266 132 264 108 252 90Z" fill="url(#st{u})" stroke="#5c6772" stroke-width="1.2"/>'
          + "".join(f'<path d="M{118-i} {112+i*7} L{242} {108+i*6}" stroke="#6d7884" stroke-width="1.1"/>' for i in range(6)),
 "mallet": '<path d="M200 10 L200 112" stroke="url(#st{u})" stroke-width="4" stroke-linecap="round"/>'
           '<path d="M120 116 L282 116 C292 116 296 124 294 132 L288 152 C286 156 282 158 276 158 L124 158 C118 158 114 156 112 152 L106 132 C104 124 110 116 120 116Z" fill="url(#dk{u})" stroke="#9aa6b2" stroke-width="1.2"/>'
           '<path d="M200 118 L200 156" stroke="#e3c06a" stroke-width="3"/>',
 "mallet2": '<path d="M232 10 L214 108" stroke="url(#st{u})" stroke-width="4" stroke-linecap="round"/>'
            '<path d="M214 106 C214 112 210 116 204 118" stroke="url(#st{u})" stroke-width="5" fill="none"/>'
            '<path d="M118 120 L270 120 C280 120 286 128 284 138 L280 152 C278 156 274 158 268 158 L126 158 C120 158 116 156 114 152 L108 136 C106 126 110 120 118 120Z" fill="url(#st{u})" stroke="#5c6772" stroke-width="1.2"/>'
            '<path d="M196 122 L196 156" stroke="#1c232b" stroke-width="3"/>',
}

_n = [0]
def fig(brand, name):
    if name in PHOTO:
        return f'<div class="fig"><img src="{PHOTO[name]}" alt="{brand} {name}" loading="lazy"></div>'
    return ''  # no photo -> no image block
    _n[0] += 1; u = _n[0]
    a, b = BG.get(brand, ("#0f2a3d", "#21506d"))
    shape = SHAPES[CAT.get(name, "driver")].replace("{u}", str(u))
    return (f'<div class="fig"><svg viewBox="0 0 400 176" role="img" aria-label="{brand} {name}">'
            f'<defs><radialGradient id="bg{u}" gradientUnits="userSpaceOnUse" cx="300" cy="0" r="520"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{a}"/></radialGradient>'
            + STEEL.replace("{u}", str(u)) + DARK.replace("{u}", str(u)) +
            f'</defs><rect x="-600" width="1600" height="176" fill="url(#bg{u})"/>'
            f'<ellipse cx="190" cy="162" rx="130" ry="7" fill="#000" opacity=".35"/>{shape}'
            f'<text x="40" y="28" fill="#fff" opacity=".55" font-size="11" font-weight="700" letter-spacing="1.5" font-family="Inter,sans-serif">{brand.upper()}</text>'
            f'</svg></div>')

CSS = ('<style>.mc .fig{margin:-18px -18px 14px;border-radius:16px 16px 0 0;overflow:hidden;line-height:0}'
       '.mc .fig svg,.mc .fig img{width:100%;height:190px;display:block;object-fit:contain;background:#f3f5f7}@media(max-width:600px){.mc .fig svg,.mc .fig img{height:auto;aspect-ratio:400/176}}'
       '.imgnote{font-size:.78rem;color:var(--muted);margin:-4px 0 10px}</style>')
