#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build one portrait-longform, native-object PowerPoint from the three locked SVGs.

Route: LibreOffice UNO (headless Impress) so that a custom page size and native,
individually editable objects are possible. Every SVG rect / text / line / curve /
polygon becomes its own presentation object; no raster page image is used.

Page size: 1200 x 1900 px reference canvas (317.50 x 502.71 mm), i.e. portrait
longform. It is intentionally NOT labelled A3.

Layout safety: every text block is fitted to its containing card - the font size is
reduced stepwise and the string is wrapped at separators until it fits inside the
parent frame, so no label overflows a card edge (fixing the inherited SVG overflow).
Connector labels that sit between cards get an opaque white chip so they never
collide visually with card borders.
"""
from __future__ import annotations

import math
import re
import time
from pathlib import Path
from xml.etree import ElementTree as ET

import uno
from com.sun.star.awt import Point, Size
from com.sun.star.beans import PropertyValue

ROOT = Path(__file__).resolve().parent
SVG_FILES = [
    ROOT / "番医项目_图01_总体生态与系统能力架构_V0.1.svg",
    ROOT / "番医项目_图02_核心对象与SKU关系架构_V0.1.svg",
    ROOT / "番医项目_图03_业务工作链与受控进化流程_V0.1.svg",
]
OUT_ODP = ROOT / "番医项目_双数智引擎架构图_V0.1_竖版长图_可编辑源稿.odp"
OUT_PPTX = ROOT / "番医项目_双数智引擎架构图_V0.1_竖版长图_可编辑PPTX.pptx"

W, H = 1200, 1900
PX2HMM = 2540.0 / 96.0           # px -> 1/100 mm
PX2PT = 72.0 / 96.0              # px -> point (LibreOffice CharHeight uses points)
PAGE_W = int(round(W * PX2HMM))
PAGE_H = int(round(H * PX2HMM))

PAGE_BG = "F7F9FC"
INK = "161A25"
MUTED = "667085"
WHITE = "FFFFFF"

FONT_ZH = "PingFang SC"
FONT_EN = "Space Grotesk"
FONT_MONO = "IBM Plex Mono"

SIZE_BY_CLASS = {
    "title": 30.0, "sub": 14.0, "section": 16.0, "cardtitle": 15.0,
    "body": 12.0, "small": 10.8, "label": 10.0, "rel": 10.0,
}
MUTED_CLASSES = {"sub", "body", "small", "rel"}

MIN_TEXT_SIZE = 6.6

FILL_NONE = uno.Enum("com.sun.star.drawing.FillStyle", "NONE")
FILL_SOLID = uno.Enum("com.sun.star.drawing.FillStyle", "SOLID")
LINE_NONE = uno.Enum("com.sun.star.drawing.LineStyle", "NONE")
LINE_SOLID = uno.Enum("com.sun.star.drawing.LineStyle", "SOLID")
PARA_LEFT = uno.Enum("com.sun.star.style.ParagraphAdjust", "LEFT")
PARA_CENTER = uno.Enum("com.sun.star.style.ParagraphAdjust", "CENTER")
PARA_RIGHT = uno.Enum("com.sun.star.style.ParagraphAdjust", "RIGHT")
PAPER_PORTRAIT = uno.Enum("com.sun.star.view.PaperOrientation", "PORTRAIT")

DOC = None


# --------------------------------------------------------------------------- UNO
def pv(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p


def connect():
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local)
    for _ in range(80):
        try:
            ctx = resolver.resolve(
                "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
            return ctx.ServiceManager.createInstanceWithContext(
                "com.sun.star.frame.Desktop", ctx)
        except Exception:
            time.sleep(0.25)
    raise RuntimeError("LibreOffice UNO bridge unavailable")


def hmm(v: float) -> int:
    return int(round(v * PX2HMM))


def rgb(hexstr: str) -> int:
    return int(hexstr.lstrip("#"), 16)


def new_shape(slide, service, x, y, w, h, name=None):
    shape = DOC.createInstance(service)
    shape.Position = Point(hmm(x), hmm(y))
    shape.Size = Size(max(hmm(w), 1), max(hmm(h), 1))
    if name:
        shape.Name = name
    slide.add(shape)
    return shape


def add_rect(slide, x, y, w, h, fill=WHITE, stroke=None, line_w=1.0, radius=0.0, name=None):
    sh = new_shape(slide, "com.sun.star.drawing.RectangleShape", x, y, w, h, name)
    sh.FillStyle = FILL_SOLID
    sh.FillColor = rgb(fill)
    if stroke:
        sh.LineStyle = LINE_SOLID
        sh.LineColor = rgb(stroke)
        sh.LineWidth = max(1, hmm(line_w))
    else:
        sh.LineStyle = LINE_NONE
    if radius:
        try:
            sh.CornerRadius = hmm(radius)
        except Exception:
            pass
    return sh


def add_polygon(slide, points, fill=None, stroke=None, line_w=1.0, name=None):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x0, y0 = min(xs), min(ys)
    # LibreOffice renders PolyPolygon vertices in absolute page coordinates and
    # ignores the shape offset, so the vertices are passed absolutely.
    sh = new_shape(slide, "com.sun.star.drawing.PolyPolygonShape", 0, 0,
                   max(max(xs) - x0, 1), max(max(ys) - y0, 1), name)
    pts = []
    for px_, py_ in points:
        p = uno.createUnoStruct("com.sun.star.awt.Point")
        p.X = hmm(px_)
        p.Y = hmm(py_)
        pts.append(p)
    sh.PolyPolygon = (tuple(pts),)
    if fill:
        sh.FillStyle = FILL_SOLID
        sh.FillColor = rgb(fill)
    else:
        sh.FillStyle = FILL_NONE
    if stroke:
        sh.LineStyle = LINE_SOLID
        sh.LineColor = rgb(stroke)
        sh.LineWidth = max(1, hmm(line_w))
    else:
        sh.LineStyle = LINE_NONE
    return sh


def add_segment(slide, p1, p2, color, width=1.7, dash=False, name=None):
    """One straight LineShape per segment: deterministic rendering, still editable."""
    sh = new_shape(slide, "com.sun.star.drawing.LineShape", p1[0], p1[1],
                   p2[0] - p1[0], p2[1] - p1[1], name)
    sh.FillStyle = FILL_NONE
    sh.LineStyle = LINE_SOLID
    sh.LineColor = rgb(color)
    sh.LineWidth = max(1, hmm(width))
    if dash:
        try:
            sh.LineDashName = "Dashed"
        except Exception:
            pass
    return sh


def add_polyline(slide, points, color, width=1.7, dash=False, name=None):
    """PolyLineShape anchored at the bounding-box origin: geometry is preserved
    exactly and each vertex stays independently editable."""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x0, y0 = min(xs), min(ys)
    # See add_polygon: vertices are absolute, the anchor stays at the page origin.
    sh = new_shape(slide, "com.sun.star.drawing.PolyLineShape", 0, 0,
                   max(max(xs) - x0, 1), max(max(ys) - y0, 1), name)
    pts = []
    for px_, py_ in points:
        p = uno.createUnoStruct("com.sun.star.awt.Point")
        p.X = hmm(px_)
        p.Y = hmm(py_)
        pts.append(p)
    sh.PolyPolygon = (tuple(pts),)
    sh.FillStyle = FILL_NONE
    sh.LineStyle = LINE_SOLID
    sh.LineColor = rgb(color)
    sh.LineWidth = max(1, hmm(width))
    if dash:
        try:
            sh.LineDashName = "Dashed"
        except Exception:
            pass
    return sh


def add_segment(slide, p1, p2, color, width=1.7, dash=False, name=None):
    return add_polyline(slide, [p1, p2], color, width, dash, name)


def add_arrow_head(slide, p_from, p_to, color, size=9.0, name=None):
    ang = math.atan2(p_to[1] - p_from[1], p_to[0] - p_from[0])
    length, half = size, size * 0.42
    tip = p_to
    bx = tip[0] - math.cos(ang) * length
    by = tip[1] - math.sin(ang) * length
    nx, ny = -math.sin(ang), math.cos(ang)
    return add_polygon(slide, [tip, (bx + nx * half, by + ny * half),
                               (bx - nx * half, by - ny * half)],
                       fill=color, stroke=None, name=name)


def add_text_shape(slide, x, y, w, h, lines, font, size_pt, color, bold, align,
                   line_h_px=None, name=None):
    sh = new_shape(slide, "com.sun.star.drawing.TextShape", x, y, w, h, name)
    sh.FillStyle = FILL_NONE
    sh.LineStyle = LINE_NONE
    sh.String = lines
    sh.TextAutoGrowHeight = False
    sh.TextAutoGrowWidth = False
    sh.TextWordWrap = False
    for attr in ("TextLeftDistance", "TextRightDistance", "TextUpperDistance", "TextLowerDistance"):
        try:
            setattr(sh, attr, 0)
        except Exception:
            pass
    sh.CharFontName = font
    sh.CharFontNameAsian = font
    sh.CharHeight = size_pt
    sh.CharHeightAsian = size_pt
    sh.CharColor = rgb(color)
    weight = 150.0 if bold else 100.0
    sh.CharWeight = weight
    sh.CharWeightAsian = weight
    sh.ParaAdjust = {"left": PARA_LEFT, "center": PARA_CENTER, "right": PARA_RIGHT}[align]
    try:
        sh.TextVerticalAdjust = 0
    except Exception:
        pass
    if line_h_px and lines.count("\n") >= 1:
        try:
            text_obj = sh.getText()
            for i in range(text_obj.getCount()):
                para = text_obj.getByIndex(i)
                para.LineSpacing = uno.createUnoStruct("com.sun.star.style.LineSpacing")
                para.LineSpacing.Mode = uno.Enum("com.sun.star.style.LineSpacingMode", "PROP")
                para.LineSpacing.Height = hmm(line_h_px)
        except Exception:
            pass
    return sh


# ----------------------------------------------------------------- SVG parsing
NS = "{http://www.w3.org/2000/svg}"


def is_cjk(ch: str) -> bool:
    o = ord(ch)
    return (0x2E80 <= o <= 0x9FFF) or (0xFF00 <= o <= 0xFFEF) or \
           (0x3000 <= o <= 0x303F) or (0xFE30 <= o <= 0xFE4F)


def est_width(text: str, size: float) -> float:
    total = 0.0
    for ch in text:
        if is_cjk(ch):
            total += size
        elif ch == " ":
            total += size * 0.30
        else:
            total += size * 0.56
    return total


def text_lines_of(el) -> list[str]:
    kids = [c for c in el if c.tag == NS + "tspan"]
    if kids:
        out = []
        for c in kids:
            parts = [c.text or ""]
            for sub in c:
                parts.append(sub.text or "")
            out.append("".join(parts).strip())
        return [s for s in out if s]
    raw = (el.text or "")
    for c in el:
        raw += (c.text or "")
    return [raw.strip()] if raw.strip() else []


def class_style(el):
    classes = (el.attrib.get("class") or "").split()
    size = 12.0
    for key in ("title", "sub", "section", "cardtitle", "body", "small", "label", "rel"):
        if key in classes:
            size = SIZE_BY_CLASS[key]
            break
    if "mono" in classes:
        family = FONT_MONO
    elif "en" in classes:
        family = FONT_EN
    else:
        family = FONT_ZH
    bold = any(k in classes for k in ("title", "section", "cardtitle", "label", "rel"))
    default_color = MUTED if any(k in classes for k in MUTED_CLASSES) else INK
    fill = (el.attrib.get("fill") or "").strip()
    color = fill.lstrip("#") if fill.startswith("#") else default_color
    return family, size, bold, color, classes


def parse_d(d: str):
    tokens = re.findall(r"[MLCZmlcz]|-?\d*\.?\d+", d)
    pts, cur, i = [], (0.0, 0.0), 0
    while i < len(tokens):
        t = tokens[i]
        if t in "ML":
            cur = (float(tokens[i + 1]), float(tokens[i + 2]))
            pts.append(cur)
            i += 3
        elif t in "Cc":
            x1, y1, x2, y2, x3, y3 = (float(v) for v in tokens[i + 1:i + 7])
            p0 = cur
            for s in range(1, 13):
                u = s / 12.0
                mu = 1 - u
                bx = (mu ** 3) * p0[0] + 3 * (mu ** 2) * u * x1 + 3 * mu * (u ** 2) * x2 + (u ** 3) * x3
                by = (mu ** 3) * p0[1] + 3 * (mu ** 2) * u * y1 + 3 * mu * (u ** 2) * y2 + (u ** 3) * y3
                pts.append((bx, by))
            cur = (x3, y3)
            i += 7
        else:
            i += 1
    return pts


def blend(color_hex: str, alpha: float, base: str = "FFFFFF") -> str:
    c = rgb(color_hex)
    b = rgb(base)
    r = int(round(((c >> 16) & 255) * alpha + ((b >> 16) & 255) * (1 - alpha)))
    g = int(round(((c >> 8) & 255) * alpha + ((b >> 8) & 255) * (1 - alpha)))
    bl = int(round((c & 255) * alpha + (b & 255) * (1 - alpha)))
    return f"{r:02X}{g:02X}{bl:02X}"


def collect_ops(svg_path: Path):
    root = ET.parse(svg_path).getroot()
    ops, order = [], 0

    def walk(el):
        nonlocal order
        for child in el:
            tag = child.tag.replace(NS, "")
            if tag in ("defs", "style", "title", "desc", "marker"):
                continue
            if tag == "g":
                walk(child)
                continue
            a = child.attrib
            order += 1
            if tag == "rect":
                x, y = float(a.get("x", 0)), float(a.get("y", 0))
                w, h = float(a.get("width", 0)), float(a.get("height", 0))
                if w >= W - 1 and h >= H - 1:
                    continue  # page background handled by the slide background
                fill = (a.get("fill") or "").strip()
                fill = fill.lstrip("#") if fill.startswith("#") else WHITE
                alpha = float(a.get("opacity", 1) or 1)
                if alpha < 1:
                    fill = blend(fill, alpha)
                stroke = (a.get("stroke") or "").strip()
                stroke = stroke.lstrip("#") if stroke.startswith("#") else None
                ops.append({"kind": "rect", "order": order, "x": x, "y": y, "w": w, "h": h,
                            "fill": fill, "stroke": stroke,
                            "line_w": float(a.get("stroke-width", 1) or 1),
                            "radius": float(a.get("rx", 0) or 0),
                            "id": a.get("id") or ""})
            elif tag == "polygon":
                nums = [float(v) for v in re.findall(r"-?\d*\.?\d+", a.get("points", ""))]
                pts = list(zip(nums[0::2], nums[1::2]))
                fill = (a.get("fill") or "").strip().lstrip("#") or None
                stroke = (a.get("stroke") or "").strip().lstrip("#") or None
                ops.append({"kind": "polygon", "order": order, "points": pts, "fill": fill,
                            "stroke": stroke,
                            "line_w": float(a.get("stroke-width", 1) or 1),
                            "id": a.get("id") or ""})
            elif tag == "path":
                pts = parse_d(a.get("d", ""))
                stroke = (a.get("stroke") or "").strip().lstrip("#")
                ops.append({"kind": "path", "order": order, "points": pts, "color": stroke,
                            "width": float(a.get("stroke-width", 1.7) or 1.7),
                            "dash": bool(a.get("stroke-dasharray")),
                            "arrow": bool((a.get("marker-end") or "").strip()),
                            "id": a.get("id") or ""})
            elif tag == "text":
                lines = text_lines_of(child)
                if not lines:
                    continue
                if any("EDITABLE SVG" in ln for ln in lines):
                    lines = [ln.replace("EDITABLE SVG", "EDITABLE PPTX") for ln in lines]
                family, size, bold, color, classes = class_style(child)
                leading = None
                tspans = [c for c in child if c.tag == NS + "tspan"]
                if len(lines) > 1 and len(tspans) > 1:
                    dys = [float(c.attrib.get("dy", 0) or 0) for c in tspans[1:]]
                    if dys:
                        leading = sum(dys) / len(dys)
                ops.append({"kind": "text", "order": order, "lines": lines, "family": family,
                            "size": size, "bold": bold, "color": color,
                            "align": child.attrib.get("text-anchor", "start"),
                            "x": float(a.get("x", 0)), "y": float(a.get("y", 0)),
                            "leading": leading, "id": a.get("id") or "",
                            "classes": classes})
        return

    walk(root)
    return ops


# ------------------------------------------------------------------ text layout
BREAK = "\u00b7/，、；：＋×≠→|"


def wrap_text(text: str, size: float, max_w: float) -> list[str]:
    if est_width(text, size) <= max_w:
        return [text]
    tokens = re.split(r"(?<=[" + re.escape(BREAK) + r"])", text)
    lines, cur = [], ""
    for tk in tokens:
        if not tk:
            continue
        cand = cur + tk
        if est_width(cand, size) <= max_w:
            cur = cand
            continue
        if cur:
            lines.append(cur.rstrip())
            cur = ""
        if est_width(tk, size) <= max_w:
            cur = tk
            continue
        piece = ""
        for ch in tk:
            if est_width(piece + ch, size) <= max_w:
                piece += ch
            else:
                if piece:
                    lines.append(piece.rstrip())
                piece = ch
        cur = piece
    if cur:
        lines.append(cur.rstrip())
    return [ln for ln in lines if ln] or [text]


def find_parent_rect(op, rects):
    """Smallest card-like rect containing the text baseline point."""
    best = None
    for r in rects:
        if r["h"] < op["size"] * 1.4 or r["w"] < 40:
            continue
        if r["x"] - 2 <= op["x"] <= r["x"] + r["w"] + 2 and r["y"] <= op["y"] <= r["y"] + r["h"] + 6:
            area = r["w"] * r["h"]
            if best is None or area < best[0]:
                best = (area, r)
    return best[1] if best else None


def available_width(op, rect):
    pad = 9.0 if rect["h"] < 40 else 15.0
    if op["align"] == "middle":
        return max(rect["w"] - 2 * pad, 12.0), pad, pad
    if op["align"] == "end":
        return max(op["x"] - (rect["x"] + pad), 12.0), pad, pad
    return max((rect["x"] + rect["w"] - pad) - op["x"], 12.0), pad, pad


def layout_block(op, rect, hard_bottom, floor=None):
    """Fit one text block: keep the SVG size when possible, shrink only when needed."""
    avail_w, pad_l, _ = available_width(op, rect)
    floor = floor or MIN_TEXT_SIZE
    size = op["size"]
    paras = op["lines"]
    while True:
        paras = []
        for ln in op["lines"]:
            paras.extend(wrap_text(ln, size, avail_w))
        top = op["y"] - 0.86 * size
        line_h = size * 1.32
        if line_h * len(paras) <= (hard_bottom - top) + 0.6 or size <= floor:
            break
        size -= 0.25
    return size, paras, pad_l


def draw_page(slide, ops, page_name):
    rects = [o for o in ops if o["kind"] == "rect"]

    # Group text blocks that live inside the same card so they stack from the card
    # top in reading order instead of following the SVG's absolute baselines.
    grouped = {}
    loose = []
    for op in ops:
        if op["kind"] != "text":
            continue
        rect = find_parent_rect(op, rects)
        # Pill / chip labels are self-contained: keep them exactly where the source
        # places them instead of pushing them into the card's text flow.
        pill_label = rect is not None and rect["h"] < 40 and "cardtitle" not in op["classes"]
        if rect is None or pill_label:
            loose.append(op)
        else:
            grouped.setdefault(id(rect), (rect, []))[1].append(op)

    placements = {}
    for rect, group in grouped.values():
        group.sort(key=lambda o: (o["y"], o["x"]))
        pad_top = 5.0 if rect["h"] < 40 else (8.0 if rect["h"] < 110 else 13.0)
        pad_bottom = 4.0 if rect["h"] < 110 else 8.0
        hard_bottom = rect["y"] + rect["h"] - pad_bottom
        # A card whose kicker pill is a separate object must start its text flow
        # below that pill, otherwise the title collides with the pill label.
        first_text_y = min(o["y"] for o in group)
        pill_bottom = rect["y"]
        for r in rects:
            if r["h"] < 40 and r is not rect and \
                    rect["x"] - 1 <= r["x"] <= rect["x"] + rect["w"] and \
                    rect["y"] <= r["y"] <= rect["y"] + rect["h"] and \
                    r["y"] + r["h"] <= first_text_y + 1:
                pill_bottom = max(pill_bottom, r["y"] + r["h"])
        cursor = max(rect["y"] + pad_top, pill_bottom + 2.5)
        for op in group:
            avail_w, pad_l, _ = available_width(op, rect)
            if rect["h"] < 40:
                size, paras = op["size"], op["lines"]
                while size > MIN_TEXT_SIZE and (
                        est_width("".join(paras), size) > avail_w or
                        max(est_width(ln, size) for ln in paras) > avail_w):
                    size -= 0.25
                top = cursor
            else:
                later = [o for o in group if o["y"] > op["y"]]
                reserve = sum(7.6 * 1.32 + 3.0 for _ in later)
                limit = max(hard_bottom - reserve, cursor + 8)
                short = rect["h"] < 110
                floor = (9.5 if short else 10.0) if "cardtitle" in op["classes"] \
                    else (6.2 if short else 7.0)
                size = op["size"]
                while True:
                    paras = []
                    for ln in op["lines"]:
                        paras.extend(wrap_text(ln, size, avail_w))
                    if cursor + size * 1.32 * len(paras) <= limit + 0.6 or size <= floor:
                        break
                    size -= 0.25
                top = cursor
            line_h = size * 1.32
            box_h = line_h * len(paras)
            placements[op["order"]] = (top, size, paras, pad_l, box_h)
            cursor += box_h + (1.0 if rect["h"] < 110 else max(2.0, size * 0.16))

    for op in ops:
        kind = op["kind"]
        if kind == "rect":
            add_rect(slide, op["x"], op["y"], op["w"], op["h"], fill=op["fill"],
                     stroke=op["stroke"], line_w=op["line_w"], radius=op["radius"],
                     name=f"{page_name}-{op['id'] or 'card'}")
        elif kind == "polygon":
            add_polygon(slide, op["points"], fill=op["fill"], stroke=op["stroke"],
                        line_w=op["line_w"], name=f"{page_name}-{op['id'] or 'poly'}")
        elif kind == "path":
            pts = op["points"]
            if len(pts) < 2:
                continue
            add_polyline(slide, pts, op["color"], op["width"], op["dash"],
                         name=f"{page_name}-{op['id'] or 'connector'}")
            if op["arrow"]:
                add_arrow_head(slide, pts[-3] if len(pts) > 2 else pts[0], pts[-1],
                               op["color"], 9.0,
                               name=f"{page_name}-{op['id'] or 'connector'}-head")
        elif kind == "text":
            if op["order"] in placements:
                rect = find_parent_rect(op, rects)
                top, size, paras, pad_l, box_h = placements[op["order"]]
                align = {"middle": "center", "end": "right", "start": "left"}[op["align"]]
                # Everything inside a card uses the card's inner width so that left,
                # centre, and right alignment all stay safely inside the frame.
                bx = rect["x"] + pad_l
                box_w = max(rect["w"] - 2 * pad_l, 20.0)
                line_h = size * 1.32
            else:
                size = op["size"]
                paras = op["lines"]
                align = {"middle": "center", "end": "right", "start": "left"}[op["align"]]
                widest = max(est_width(ln, size) for ln in paras)
                box_w = widest * 1.12 + 6
                if align == "center":
                    bx = op["x"] - box_w / 2
                elif align == "right":
                    bx = op["x"] - box_w
                else:
                    bx = op["x"]
                top = op["y"] - 0.86 * size
                line_h = (op["leading"] or size * 1.36)
                box_h = line_h * (len(paras) - 1) + size * 1.35 if len(paras) > 1 else size * 1.4
                # connector labels get an opaque chip so they never collide with cards
                if "rel" in op["classes"]:
                    add_rect(slide, bx - 6, top - 2, box_w + 12, box_h + 4, fill=WHITE,
                             stroke=None, radius=4,
                             name=f"{page_name}-{op['id'] or op['order']}-chip")
            add_text_shape(slide, bx, top, box_w, box_h, "\n".join(paras), op["family"],
                           size * PX2PT, op["color"], op["bold"], align, line_h,
                           name=f"{page_name}-text-{op['id'] or op['order']}")


def build():
    global DOC
    desktop = connect()
    doc = desktop.loadComponentFromURL("private:factory/simpress", "_blank", 0, ())
    DOC = doc
    pages = doc.getDrawPages()
    while pages.getCount() < len(SVG_FILES):
        pages.insertNewByIndex(pages.getCount())

    for idx, svg in enumerate(SVG_FILES):
        ops = collect_ops(svg)
        page = pages.getByIndex(idx)
        page.Width = PAGE_W
        page.Height = PAGE_H
        page.Orientation = PAPER_PORTRAIT
        page.Name = f"{idx + 1:02d} {svg.stem}"
        try:
            page.Background.FillStyle = FILL_SOLID
            page.Background.FillColor = rgb(PAGE_BG)
        except Exception:
            pass
        draw_page(page, ops, f"fig{idx + 1:02d}")
        print(f"page {idx + 1}: {len(ops)} source primitives")

    doc.storeAsURL(uno.systemPathToFileUrl(str(OUT_ODP)), (pv("FilterName", "impress8"),))
    doc.storeToURL(uno.systemPathToFileUrl(str(OUT_PPTX)),
                   (pv("FilterName", "Impress MS PowerPoint 2007 XML"),))
    doc.close(True)
    print(OUT_ODP)
    print(OUT_PPTX)


if __name__ == "__main__":
    build()
