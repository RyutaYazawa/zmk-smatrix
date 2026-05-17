"""
smatrix Layer 0 keymap SVG generator
VIAL layout adapted to smatrix (3×6+thumb split, 50 keys)
"""

SCALE = 0.48
PAD = 24

# (x, y, w, h, main_label, sub_label, color)
# Coordinates from smatrix.dtsi physical layout
# Colors: alpha=#d8eaf8, mod=#c8e8c8, layer=#ffe4a0, td=#fde8c0, enc=#e0e0e0, sp=#f0f0f0

A  = "#d8eaf8"  # alpha
M  = "#c8e8c8"  # modifier
LY = "#ffc97a"  # layer key
TD = "#fde8c0"  # tap-dance
ENC= "#e0e0e0"  # encoder/BT
SP = "#f0f0f8"  # space/enter

keys_layer0 = [
    # ── Row 0 (y=0) ─────────────────────────────────────────────────────
    (   0,   0, 150, 100, "TAB",   "ESC↑↑", TD),   # tap-dance: TAB/ESC
    ( 150,   0, 100, 100, "Q",     "",       A),
    ( 250,   0, 100, 100, "W",     "",       A),
    ( 350,   0, 100, 100, "E",     "",       A),
    ( 450,   0, 100, 100, "R",     "",       A),
    ( 550,   0, 100, 100, "T",     "",       A),
    ( 950,   0, 100, 100, "Y",     "",       A),
    (1050,   0, 100, 100, "U",     "",       A),
    (1150,   0, 100, 100, "I",     "",       A),
    (1250,   0, 100, 100, "O",     "",       A),
    (1350,   0, 100, 100, "P",     "",       A),
    (1450,   0, 150, 100, "BSPC",  "",       M),

    # ── Row 1 (y=100) ───────────────────────────────────────────────────
    (   0, 100, 150, 100, "CTRL",  "",       M),
    ( 150, 100, 100, 100, "A",     "",       A),
    ( 250, 100, 100, 100, "S",     "",       A),
    ( 350, 100, 100, 100, "D",     "",       A),
    ( 450, 100, 100, 100, "F",     "",       A),
    ( 550, 100, 100, 100, "G",     "",       A),
    ( 950, 100, 100, 100, "H",     "",       A),
    (1050, 100, 100, 100, "J",     "",       A),
    (1150, 100, 100, 100, "K",     "",       A),
    (1250, 100, 100, 100, "L",     "",       A),
    (1350, 100, 100, 100, ";",     "",       A),
    (1450, 100, 150, 100, "'",     "",       A),

    # ── Row 2 (y=200) ── with 2 center encoder keys ─────────────────────
    (   0, 200, 150, 100, "SHFT",  "",       M),
    ( 150, 200, 100, 100, "Z",     "▼Ly2",   TD),   # hold → Layer2
    ( 250, 200, 100, 100, "X",     "",       A),
    ( 350, 200, 100, 100, "C",     "x2=PRT", TD),   # dbl-tap → PRTSC
    ( 450, 200, 100, 100, "V",     "",       A),
    ( 550, 200, 100, 100, "B",     "",       A),
    ( 650, 200, 100, 100, "BT+",   "enc",    ENC),  # encoder L (BT next)
    ( 850, 200, 100, 100, "COPY",  "enc",    ENC),  # encoder R (C-c)
    ( 950, 200, 100, 100, "N",     "",       A),
    (1050, 200, 100, 100, "M",     "",       A),
    (1150, 200, 100, 100, ",",     "",       A),
    (1250, 200, 100, 100, ".",     "",       A),
    (1350, 200, 100, 100, "/",     "",       A),
    (1450, 200, 150, 100, "CTRL",  "",       M),

    # ── Row 3 thumb (y=300) ─────────────────────────────────────────────
    # Left thumb (outer → inner)
    (   0, 300, 150, 100, "tog0",  "",       ENC),
    ( 150, 300, 100, 100, "⌘GUI",  "",       M),
    ( 250, 300, 100, 100, "★Ly3",  "",       LY),   # extra → VIAL MO(3) equiv
    ( 350, 300, 150, 100, "ALT",   "SPC?",   M),    # mt: LALT / SPACE
    ( 500, 300, 150, 100, "Ly1",   "SPACE",  LY),   # lt1: Layer1 / SPACE
    ( 650, 300, 100, 100, "SPC",   "",       SP),

    # Right thumb (inner → outer)
    ( 850, 300, 100, 100, "ENT",   "",       SP),
    ( 950, 300, 150, 100, "Ly2",   "SPACE",  LY),   # lt2: Layer2 / SPACE
    (1100, 300, 150, 100, "Ly4",   "→BT/F",  LY),   # &mo 4 (BT select / F-keys)
    (1250, 300, 100, 100, "↑",     "",       M),
    (1350, 300, 100, 100, "↓",     "",       M),
    (1450, 300, 150, 100, "C-c",   "",       M),
]

# Layer 1 (Raise / MO1) — VIAL Layer 1 rows 1-3 mapped directly (no F-row)
# Left stored outer→inner, right stored outer→inner in VIAL → reversed for smatrix inner→outer
keys_layer1 = [
    # Row 0: VIAL Layer1 row1 left / row6 right
    # Left (TAB..T = outer..inner): TRNS TRNS LANG1 UP LANG2 TRNS
    (   0,   0, 150, 100, "▽",     "",       ENC),
    ( 150,   0, 100, 100, "▽",     "",       ENC),
    ( 250,   0, 100, 100, "LANG1", "",       TD),
    ( 350,   0, 100, 100, "↑",     "",       A),
    ( 450,   0, 100, 100, "LANG2", "",       TD),
    ( 550,   0, 100, 100, "▽",     "",       ENC),
    # Right (Y..BSPC = inner..outer): DOT EQUAL BSLASH TRNS HOME PGUP
    ( 950,   0, 100, 100, ".",     "",        A),
    (1050,   0, 100, 100, "=",     "",        A),
    (1150,   0, 100, 100, "\\",    "",        A),
    (1250,   0, 100, 100, "▽",     "",        ENC),
    (1350,   0, 100, 100, "HOME",  "",        M),
    (1450,   0, 150, 100, "PgUp",  "",        M),

    # Row 1: VIAL Layer1 row2 left / row7 right
    # Left (CTRL..G): TRNS TRNS LEFT DOWN RIGHT PGUP
    (   0, 100, 150, 100, "▽",     "",       ENC),
    ( 150, 100, 100, 100, "▽",     "",       ENC),
    ( 250, 100, 100, 100, "←",     "",       A),
    ( 350, 100, 100, 100, "↓",     "",       A),
    ( 450, 100, 100, 100, "→",     "",       A),
    ( 550, 100, 100, 100, "PgUp",  "",       A),
    # Right (H..SQT): ~ MINUS GRAVE TRNS END PGDOWN
    ( 950, 100, 100, 100, "~",     "",        A),
    (1050, 100, 100, 100, "-",     "",        A),
    (1150, 100, 100, 100, "`",     "GRAVE",   A),
    (1250, 100, 100, 100, "▽",     "",        ENC),
    (1350, 100, 100, 100, "END",   "",        M),
    (1450, 100, 150, 100, "PgDn",  "",        M),

    # Row 2: VIAL Layer1 row3 left / row8 right
    # Left (SHFT..B): TRNS TRNS HOME PRTSC END PGDOWN
    (   0, 200, 150, 100, "▽",     "",       ENC),
    ( 150, 200, 100, 100, "▽",     "",       ENC),
    ( 250, 200, 100, 100, "HOME",  "",       M),
    ( 350, 200, 100, 100, "PRTSC", "",       M),
    ( 450, 200, 100, 100, "END",   "",       M),
    ( 550, 200, 100, 100, "PgDn",  "",       A),
    ( 650, 200, 100, 100, "▽",     "enc",    ENC),
    ( 850, 200, 100, 100, "▽",     "enc",    ENC),
    # Right (N..RCTRL): KP/ [ ] TRNS / TRNS
    ( 950, 200, 100, 100, "KP/",   "",        A),
    (1050, 200, 100, 100, "[",     "",        A),
    (1150, 200, 100, 100, "]",     "",        A),
    (1250, 200, 100, 100, "▽",     "",        ENC),
    (1350, 200, 100, 100, "/",     "",        A),
    (1450, 200, 150, 100, "▽",     "",        ENC),

    # Thumb
    (   0, 300, 150, 100, "▽",     "",       ENC),
    ( 150, 300, 100, 100, "▽",     "",       ENC),
    ( 250, 300, 100, 100, "▽",     "",       ENC),
    ( 350, 300, 150, 100, "▽",     "",       ENC),
    ( 500, 300, 150, 100, "▼Ly1",  "HOLD",   LY),
    ( 650, 300, 100, 100, "▽",     "",       ENC),
    ( 850, 300, 100, 100, "▽",     "",       ENC),
    ( 950, 300, 150, 100, "▽",     "",       ENC),
    (1100, 300, 150, 100, "▽",     "",       ENC),
    (1250, 300, 100, 100, "boot",  "",       M),
    (1350, 300, 100, 100, "boot",  "",       M),
    (1450, 300, 150, 100, "boot",  "",       M),
]

# Layer 2 — Numpad (Z hold) — from VIAL Layer 2
# Right side inner columns: 7-8-9 / 4-5-6 / 1-2-3-0, left all transparent
keys_layer2 = [
    # Row 0
    (   0,   0, 150, 100, "▽",    "",        ENC),
    ( 150,   0, 100, 100, "▽",    "",        ENC),
    ( 250,   0, 100, 100, "▽",    "",        ENC),
    ( 350,   0, 100, 100, "▽",    "",        ENC),
    ( 450,   0, 100, 100, "▽",    "",        ENC),
    ( 550,   0, 100, 100, "▽",    "",        ENC),
    ( 950,   0, 100, 100, "7",    "",        A),
    (1050,   0, 100, 100, "8",    "",        A),
    (1150,   0, 100, 100, "9",    "",        A),
    (1250,   0, 100, 100, "▽",    "",        ENC),
    (1350,   0, 100, 100, "▽",    "",        ENC),
    (1450,   0, 150, 100, "▽",    "",        ENC),

    # Row 1
    (   0, 100, 150, 100, "▽",    "",        ENC),
    ( 150, 100, 100, 100, "▽",    "",        ENC),
    ( 250, 100, 100, 100, "▽",    "",        ENC),
    ( 350, 100, 100, 100, "▽",    "",        ENC),
    ( 450, 100, 100, 100, "▽",    "",        ENC),
    ( 550, 100, 100, 100, "▽",    "",        ENC),
    ( 950, 100, 100, 100, "4",    "",        A),
    (1050, 100, 100, 100, "5",    "",        A),
    (1150, 100, 100, 100, "6",    "",        A),
    (1250, 100, 100, 100, "▽",    "",        ENC),
    (1350, 100, 100, 100, "▽",    "",        ENC),
    (1450, 100, 150, 100, "▽",    "",        ENC),

    # Row 2
    (   0, 200, 150, 100, "▽",    "",        ENC),
    ( 150, 200, 100, 100, "▼Z",   "HOLD",    LY),   # Z hold = this layer
    ( 250, 200, 100, 100, "▽",    "",        ENC),
    ( 350, 200, 100, 100, "▽",    "",        ENC),
    ( 450, 200, 100, 100, "▽",    "",        ENC),
    ( 550, 200, 100, 100, "▽",    "",        ENC),
    ( 650, 200, 100, 100, "▽",    "enc",     ENC),
    ( 850, 200, 100, 100, "▽",    "enc",     ENC),
    ( 950, 200, 100, 100, "1",    "",        A),
    (1050, 200, 100, 100, "2",    "",        A),
    (1150, 200, 100, 100, "3",    "",        A),
    (1250, 200, 100, 100, "0",    "",        A),
    (1350, 200, 100, 100, "▽",    "",        ENC),
    (1450, 200, 150, 100, "▽",    "",        ENC),

    # Thumb
    (   0, 300, 150, 100, "▽",    "",        ENC),
    ( 150, 300, 100, 100, "▽",    "",        ENC),
    ( 250, 300, 100, 100, "▽",    "",        ENC),
    ( 350, 300, 150, 100, "▽",    "",        ENC),
    ( 500, 300, 150, 100, "▽",    "",        ENC),
    ( 650, 300, 100, 100, "▽",    "",        ENC),
    ( 850, 300, 100, 100, "▽",    "",        ENC),
    ( 950, 300, 150, 100, "▽",    "",        ENC),
    (1100, 300, 150, 100, "▽",    "",        ENC),
    (1250, 300, 100, 100, "▽",    "",        ENC),
    (1350, 300, 100, 100, "▽",    "",        ENC),
    (1450, 300, 150, 100, "▽",    "",        ENC),
]

# Layer 3 (Lower / MO3) - symbols + numbers from VIAL layer 3
keys_layer3 = [
    # Row 0
    (   0,   0, 150, 100, "`",    "",        A),
    ( 150,   0, 100, 100, "!",    "Sft+1",   A),
    ( 250,   0, 100, 100, "@",    "Sft+2",   A),
    ( 350,   0, 100, 100, "#",    "Sft+3",   A),
    ( 450,   0, 100, 100, "$",    "Sft+4",   A),
    ( 550,   0, 100, 100, "%",    "Sft+5",   A),
    ( 950,   0, 100, 100, "^",    "Sft+6",   A),
    (1050,   0, 100, 100, "&",    "Sft+7",   A),
    (1150,   0, 100, 100, "*",    "Sft+8",   A),
    (1250,   0, 100, 100, "(",    "Sft+9",   A),
    (1350,   0, 100, 100, ")",    "Sft+0",   A),
    (1450,   0, 150, 100, "=",    "",        A),

    # Row 1
    (   0, 100, 150, 100, "▽",    "",        ENC),
    ( 150, 100, 100, 100, "▽",    "",        ENC),
    ( 250, 100, 100, 100, "▽",    "",        ENC),
    ( 350, 100, 100, 100, "▽",    "",        ENC),
    ( 450, 100, 100, 100, "▽",    "",        ENC),
    ( 550, 100, 100, 100, "▽",    "",        ENC),
    ( 950, 100, 100, 100, "▽",    "",        ENC),
    (1050, 100, 100, 100, "▽",    "",        ENC),
    (1150, 100, 100, 100, "▽",    "",        ENC),
    (1250, 100, 100, 100, "▽",    "",        ENC),
    (1350, 100, 100, 100, "▽",    "",        ENC),
    (1450, 100, 150, 100, "▽",    "",        ENC),

    # Row 2
    (   0, 200, 150, 100, "▽",    "",        ENC),
    ( 150, 200, 100, 100, "▽",    "",        ENC),
    ( 250, 200, 100, 100, "▽",    "",        ENC),
    ( 350, 200, 100, 100, "▽",    "",        ENC),
    ( 450, 200, 100, 100, "▽",    "",        ENC),
    ( 550, 200, 100, 100, "▽",    "",        ENC),
    ( 650, 200, 100, 100, "▽",    "enc",     ENC),
    ( 850, 200, 100, 100, "▽",    "enc",     ENC),
    ( 950, 200, 100, 100, "-",    "",        A),
    (1050, 200, 100, 100, "▽",    "",        ENC),
    (1150, 200, 100, 100, "[",    "",        A),
    (1250, 200, 100, 100, "]",    "",        A),
    (1350, 200, 100, 100, "\\",   "",        A),
    (1450, 200, 150, 100, "▽",    "",        ENC),

    # Row 3 thumb
    (   0, 300, 150, 100, "▽",    "",        ENC),
    ( 150, 300, 100, 100, "▽",    "",        ENC),
    ( 250, 300, 100, 100, "▽",    "",        ENC),
    ( 350, 300, 150, 100, "▽",    "",        ENC),
    ( 500, 300, 150, 100, "▽",    "",        ENC),
    ( 650, 300, 100, 100, "▽",    "",        ENC),
    ( 850, 300, 100, 100, "▽",    "",        ENC),
    ( 950, 300, 150, 100, "▽",    "",        ENC),
    (1100, 300, 150, 100, "▽",    "",        ENC),
    (1250, 300, 100, 100, "▽",    "",        ENC),
    (1350, 300, 100, 100, "▽",    "",        ENC),
    (1450, 300, 150, 100, "▽",    "",        ENC),
]


def xml_esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_key(x, y, w, h, label, sublabel, color):
    sx = x * SCALE + PAD
    sy = y * SCALE + PAD
    sw = w * SCALE - 2
    sh = h * SCALE - 2

    font_size = 8 if len(label) > 4 else (10 if len(label) > 3 else 12)
    cy = sh * 0.58

    parts = [
        f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{sw:.1f}" height="{sh:.1f}" '
        f'rx="4" fill="{color}" stroke="#8899aa" stroke-width="0.8"/>',
        f'<text x="{sx + sw/2:.1f}" y="{sy + cy:.1f}" '
        f'text-anchor="middle" font-family="monospace,Consolas" '
        f'font-size="{font_size}" fill="#1a2030" font-weight="600">{xml_esc(label)}</text>',
    ]
    if sublabel:
        parts.append(
            f'<text x="{sx + sw/2:.1f}" y="{sy + sh * 0.85:.1f}" '
            f'text-anchor="middle" font-family="monospace,Consolas" '
            f'font-size="6.5" fill="#5070a0">{xml_esc(sublabel)}</text>'
        )
    return "\n".join(parts)


def render_layer(keys, title, y_offset=0):
    total_w = int(1600 * SCALE + PAD * 2)
    total_h = int(400 * SCALE + PAD * 2 + 22)
    parts = [
        f'<!-- {title} -->',
        f'<g transform="translate(0,{y_offset})">',
        f'<text x="{PAD}" y="15" font-family="sans-serif" font-size="12" '
        f'font-weight="bold" fill="#334466">{title}</text>',
        f'<g transform="translate(0,20)">',
    ]
    for k in keys:
        parts.append(render_key(*k))
    parts.append('</g></g>')
    return "\n".join(parts), total_w, total_h


# Build full SVG with all 4 layers stacked
layer_height = int(400 * SCALE + PAD * 2 + 30)

l0, W, H = render_layer(keys_layer0, "Layer 0 — Default (VIAL adapted)",      y_offset=0)
l1, _, _ = render_layer(keys_layer1, "Layer 1 — Raise / MO(1)  [nav + sym]",  y_offset=layer_height)
l2, _, _ = render_layer(keys_layer2, "Layer 2 — Numpad  [Z hold]",             y_offset=layer_height * 2)
l3, _, _ = render_layer(keys_layer3, "Layer 3 — Lower / MO(3)  [symbols]",     y_offset=layer_height * 3)

total_h = layer_height * 4 + 10

legend = f"""
<g transform="translate({PAD},{total_h - 28})">
  <rect width="12" height="12" rx="2" fill="{A}"   stroke="#8899aa" stroke-width="0.8"/>
  <text x="16" y="10" font-size="9" font-family="sans-serif" fill="#334">alpha</text>
  <rect x="60" width="12" height="12" rx="2" fill="{M}"  stroke="#8899aa" stroke-width="0.8"/>
  <text x="76" y="10" font-size="9" font-family="sans-serif" fill="#334">modifier</text>
  <rect x="135" width="12" height="12" rx="2" fill="{LY}" stroke="#8899aa" stroke-width="0.8"/>
  <text x="151" y="10" font-size="9" font-family="sans-serif" fill="#334">layer key</text>
  <rect x="210" width="12" height="12" rx="2" fill="{TD}" stroke="#8899aa" stroke-width="0.8"/>
  <text x="226" y="10" font-size="9" font-family="sans-serif" fill="#334">tap-dance</text>
  <rect x="290" width="12" height="12" rx="2" fill="{ENC}" stroke="#8899aa" stroke-width="0.8"/>
  <text x="306" y="10" font-size="9" font-family="sans-serif" fill="#334">encoder / transparent</text>
</g>
"""

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{total_h + 10}">
  <rect width="{W}" height="{total_h + 10}" fill="#f5f7fa"/>
  {l0}
  {l1}
  {l2}
  {l3}
  {legend}
</svg>
"""

out_path = r"C:\Users\trans\Downloads\smatrix_keymap.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"SVG written to {out_path}")
print(f"Canvas: {W} × {total_h + 10} px")
