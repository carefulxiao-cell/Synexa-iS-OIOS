#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate three review-only, editable 1200×1900 SVG architecture diagrams.

All visual primitives remain individual SVG text / rect / path objects. The diagrams are
candidate architecture expressions; they are not a system design approval or a business standard.
"""
from __future__ import annotations

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent
W, H = 1200, 1900

C = {
    "bg": "#F7F9FC", "white": "#FFFFFF", "ink": "#161A25", "muted": "#667085",
    "line": "#D9DEE7", "green": "#28CC83", "blue": "#2D8EFF", "purple": "#8B5ACA",
    "gold": "#E8A020", "orange": "#FFB97B", "indigo": "#4F46E5", "red": "#E60012",
    "pale_blue": "#EEF6FF", "pale_green": "#ECFBF4", "pale_purple": "#F5F1FF",
    "pale_gold": "#FFF8E7", "pale_red": "#FFF1F2", "pale_indigo": "#F0F1FF",
}


def esc(s: str) -> str:
    return escape(s, quote=True)


def svg_open(title: str) -> list[str]:
    return [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">{esc(title)}</title>
<desc id="desc">番医项目首批架构表达候选；待业务审核，非系统实施批准依据。</desc>
<defs>
  <marker id="arrow-ink" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{C['ink']}"/></marker>
  <marker id="arrow-blue" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{C['blue']}"/></marker>
  <marker id="arrow-purple" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{C['purple']}"/></marker>
  <marker id="arrow-gold" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{C['gold']}"/></marker>
  <marker id="arrow-red" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{C['red']}"/></marker>
  <style>
    .zh{{font-family:'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif;fill:{C['ink']}}}
    .en{{font-family:'Space Grotesk','Noto Sans',sans-serif;fill:{C['ink']};letter-spacing:.3px}}
    .mono{{font-family:'IBM Plex Mono','Noto Sans Mono',monospace;letter-spacing:.2px}}
    .title{{font-size:30px;font-weight:700}}.sub{{font-size:14px;fill:{C['muted']}}}
    .section{{font-size:16px;font-weight:700}}.cardtitle{{font-size:15px;font-weight:700}}.body{{font-size:12px;fill:{C['muted']}}}
    .small{{font-size:10.8px;fill:{C['muted']}}}.label{{font-size:10px;font-weight:700;letter-spacing:.7px}}
    .rel{{font-size:10px;font-weight:700;fill:{C['muted']};font-family:'IBM Plex Mono','Noto Sans Mono',monospace}}
  </style>
</defs>
<rect x="0" y="0" width="{W}" height="{H}" fill="{C['bg']}"/>
''']


def header(buf: list[str], no: str, title: str, en: str, status: str = "CANDIDATE · REVIEW REQUIRED"):
    buf.append(f'''<g id="header">
<text x="60" y="64" class="mono label" fill="{C['indigo']}">PANYI · DUAL INTELLIGENCE · ARCHITECTURE PACK · V0.1</text>
<text x="60" y="108" class="zh title">{esc(title)}</text>
<text x="60" y="136" class="en sub">{esc(en)}</text>
<rect x="60" y="158" width="1080" height="1" fill="{C['line']}"/>
<rect x="60" y="174" width="100" height="24" rx="12" fill="{C['ink']}"/>
<text x="110" y="190" text-anchor="middle" class="mono label" fill="#FFFFFF">{esc(no)}</text>
<rect x="170" y="174" width="250" height="24" rx="12" fill="{C['pale_purple']}" stroke="{C['purple']}"/>
<text x="295" y="190" text-anchor="middle" class="mono label" fill="{C['purple']}">{esc(status)}</text>
<text x="1140" y="190" text-anchor="end" class="mono small">1200 × 1900 · EDITABLE SVG</text>
</g>''')


def footer(buf: list[str], left: str, right: str = "首批候选｜待业务审核｜非实施批准"):
    buf.append(f'''<g id="footer">
<rect x="60" y="1834" width="1080" height="1" fill="{C['line']}"/>
<text x="60" y="1862" class="mono small">{esc(left)}</text>
<text x="1140" y="1862" text-anchor="end" class="zh small" fill="{C['red']}">{esc(right)}</text>
</g>''')


def section(buf: list[str], y: float, code: str, title: str, note: str = ""):
    buf.append(f'''<g class="section-heading"><rect x="60" y="{y-17}" width="5" height="22" rx="2.5" fill="{C['indigo']}"/>
<text x="78" y="{y}" class="mono label" fill="{C['indigo']}">{esc(code)}</text>
<text x="150" y="{y}" class="zh section">{esc(title)}</text>
<text x="1140" y="{y}" text-anchor="end" class="zh small">{esc(note)}</text></g>''')


def text_lines(x: float, y: float, lines: list[str], css: str = "body", leading: float = 18, anchor: str = "start", fill: str | None = None) -> str:
    spans = []
    for i, line in enumerate(lines):
        attrs = f' x="{x}"' + (f' dy="{leading}"' if i else '')
        spans.append(f'<tspan{attrs}>{esc(line)}</tspan>')
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="zh {css}"{f}>' + "".join(spans) + "</text>"


def card(buf: list[str], ident: str, x: float, y: float, w: float, h: float, kicker: str, title: str,
         body: list[str], color: str = C['blue'], pale: str = C['white'], title_size: str = "cardtitle", body_leading: float = 17):
    buf.append(f'<g id="{ident}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{pale}" stroke="{color}" stroke-width="1.2"/>')
    if kicker:
        tagw = min(w - 28, max(90, 7.4 * len(kicker) + 18))
        buf.append(f'<rect x="{x+14}" y="{y+14}" width="{tagw}" height="20" rx="10" fill="{color}" opacity=".12"/>')
        buf.append(f'<text x="{x+23}" y="{y+28}" class="mono label" fill="{color}">{esc(kicker)}</text>')
        title_y = y + 58
    else:
        title_y = y + 31
    buf.append(f'<text x="{x+16}" y="{title_y}" class="zh {title_size}">{esc(title)}</text>')
    if body:
        buf.append(text_lines(x+16, title_y+23, body, "body", body_leading))
    buf.append('</g>')


def tag(buf: list[str], x: float, y: float, label: str, color: str, pale: str | None = None, w: float | None = None):
    w = w or max(62, len(label) * 7 + 20)
    pale = pale or color
    buf.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="22" rx="11" fill="{pale}" opacity=".16" stroke="{color}" stroke-width=".8"/>'
               f'<text x="{x+w/2}" y="{y+15}" text-anchor="middle" class="mono label" fill="{color}">{esc(label)}</text></g>')


def arrow(buf: list[str], ident: str, x1: float, y1: float, x2: float, y2: float, color: str = C['ink'], marker: str = "arrow-ink", dashed: bool = False, label: str | None = None, lx: float | None = None, ly: float | None = None):
    dash = ' stroke-dasharray="5 5"' if dashed else ''
    buf.append(f'<path id="{ident}" d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="1.7"{dash} marker-end="url(#{marker})"/>')
    if label:
        buf.append(f'<text x="{lx if lx is not None else (x1+x2)/2}" y="{ly if ly is not None else (y1+y2)/2-5}" text-anchor="middle" class="rel">{esc(label)}</text>')


def path_arrow(buf: list[str], ident: str, d: str, color: str, marker: str, dashed: bool = False, label: str | None = None, lx: float = 0, ly: float = 0):
    dash = ' stroke-dasharray="6 5"' if dashed else ''
    buf.append(f'<path id="{ident}" d="{d}" fill="none" stroke="{color}" stroke-width="1.7"{dash} marker-end="url(#{marker})"/>')
    if label:
        buf.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" class="rel" fill="{color}">{esc(label)}</text>')


def note_box(buf: list[str], ident: str, x: float, y: float, w: float, h: float, title: str, body: list[str], color: str = C['gold']):
    card(buf, ident, x, y, w, h, "TO VERIFY", title, body, color, C['pale_gold'], body_leading=16)


def close(buf: list[str]) -> str:
    return "\n".join(buf) + "\n</svg>\n"


def diagram_01() -> str:
    b = svg_open("图01｜番医项目总体生态与系统能力架构")
    header(b, "FIG 01", "总体生态与系统能力架构", "Ecosystem & System Capability Architecture")

    section(b, 238, "01A", "项目边界、责任主体与上位接口", "真实事实进入系统；专业人员保留审核与授权")
    roles = [
        ("项目主基线 / 专项总控", "版本、资产、责任、决策记录", C['indigo'], C['pale_indigo']),
        ("专业人员", "业务事实 / 专业审核 / 授权裁决", C['red'], C['pale_red']),
        ("Kimi", "事实整理 / 母表与口径核验", C['blue'], C['pale_blue']),
        ("ChatGPT", "策略 / 架构 / 分析 / 指令", C['purple'], C['pale_purple']),
        ("Manus", "技术架构 / 系统工程 / MVP", C['green'], C['pale_green']),
    ]
    xs = [60, 280, 500, 720, 940]
    for i,(t,body,col,pale) in enumerate(roles):
        card(b, f"role-{i}", xs[i], 266, 200, 96, "RESPONSIBILITY", t, [body], col, pale, body_leading=15)
    note_box(b, "future-04", 60, 382, 1080, 66, "未来 04 系统专项接口", ["承接经业务审核后的技术架构、数据模型、接口、权限与 MVP 设计；本轮仅预留接口。"], C['gold'])

    section(b, 492, "01B", "双数智引擎与共用业务对象 / 规则体系", "两个引擎协同，不互相替代")
    card(b, "data-engine", 60, 520, 500, 290, "ENGINE A · EXISTING + CANDIDATE", "经营数据数智引擎", ["原始事实采集 → 标准化 → 对账 → 计算与追溯 → 经营分析", "保留：来源、时间、处理批次、责任源、差异原因与数据血缘", "边界：不覆盖原始事实；分析指标不反向充当订单 / 库存 / 批次事实"], C['blue'], C['pale_blue'])
    for i,lab in enumerate(["原始事实", "标准化事实", "对账差异", "计算结果", "经营洞察"]):
        tag(b, 78 + (i%3)*145, 705 + (i//3)*35, lab, C['blue'], C['pale_blue'], 128)
    card(b, "ops-engine", 640, 520, 500, 290, "ENGINE B · CANDIDATE", "菜单与运营数智引擎", ["场景菜单 → 产品组合 → 预测 / 确认需求 → 采购 / 库存 → 生产 / 排工 → 配送 / 反馈", "形成：菜单版本、需求计划、生产计划、MRP、执行任务与履约反馈", "边界：系统规则辅助判断；不替代专业审核、授权或异常裁决"], C['purple'], C['pale_purple'])
    for i,lab in enumerate(["场景菜单", "需求计划", "生产计划", "采购库存", "履约反馈"]):
        tag(b, 658 + (i%3)*145, 705 + (i//3)*35, lab, C['purple'], C['pale_purple'], 128)
    card(b, "shared-core", 365, 828, 470, 112, "SHARED CORE · CANDIDATE", "共用业务对象与规则体系", ["Scene / Menu Slot / Product / Variant / SKU / Recipe / BOM / SOP / Ingredient / Supplier / Plan / Batch / Inventory / PO", "范围配置 · 继承—覆盖—禁用 · 版本 / 生效期 / 审批 / 审计"], C['indigo'], C['pale_indigo'], body_leading=16)
    path_arrow(b, "engine-link", "M560,655 C585,655 615,655 640,655", C['indigo'], "arrow-purple", False, "事实 ↔ 执行实绩", 600, 645)
    arrow(b, "data-to-core", 310, 810, 510, 828, C['blue'], "arrow-blue", True, "标准事实 / 洞察", 420, 812)
    arrow(b, "ops-to-core", 890, 810, 690, 828, C['purple'], "arrow-purple", True, "规则引用 / 版本", 780, 812)

    section(b, 992, "01C", "四大业务域 × 六层系统能力", "业务域贯穿六层能力，不等于独立系统孤岛")
    domains = [("需求与产品", "Scene · 菜单 · 产品 · 组合 · 需求", C['blue'], C['pale_blue']),
               ("采购与生产", "BOM · 库存 · 采购 · 批次 · 排工", C['gold'], C['pale_gold']),
               ("履约与服务", "订单 · 配送 · 标签 · 交接 · 反馈", C['green'], C['pale_green']),
               ("财务与经营", "对账 · 成本 · 损益 · 洞察 · 复盘", C['indigo'], C['pale_indigo'])]
    for i,(t,body,col,pale) in enumerate(domains):
        card(b, f"domain-{i}", 60+i*270, 1022, 250, 112, "BUSINESS DOMAIN", t, [body], col, pale, body_leading=15)
    layers = [("L1", "数据接入", "POS / 订单 / 采购 / 库存 / 生产 / 配送 / 财务"),
              ("L2", "主数据与规则", "对象、版本、范围、专业主源、规则校验"),
              ("L3", "事实与计划", "事实、预测、需求、生产、物料、排班计划"),
              ("L4", "业务执行", "采购、收货、领料、生产、质检、配送、结算"),
              ("L5", "智能分析", "对账、成本、产能、风险、经营洞察、优化候选"),
              ("L6", "人机交互", "任务、审批、例外、看板、告警、反馈、审计")]
    for i,(code,t,body) in enumerate(layers):
        x = 60 + (i%3)*360; y = 1160 + (i//3)*112
        card(b, f"layer-{i}", x, y, 335, 88, code, t, [body], C['ink'], C['white'], body_leading=14)

    section(b, 1405, "01D", "三项横贯能力与人机受控进化", "横贯能力不是外挂模块，而是每个对象和工作节点的约束")
    rails = [("数据治理与血缘", "原始值不可覆盖 · 责任源 · 对账差异 · 可重跑计算", C['blue'], C['pale_blue']),
             ("权限、版本与审计", "审批 / 生效 / 冻结 / 变更 / 作废 · 历史快照 · 审计日志", C['red'], C['pale_red']),
             ("AI 协同与受控学习", "事实整理 / 分析 / 建议 → 优化候选 → 人工审核 → 新版本草稿", C['purple'], C['pale_purple'])]
    for i,(t,body,col,pale) in enumerate(rails):
        card(b, f"rail-{i}", 60, 1435+i*82, 1080, 64, "CROSS-CUTTING", t, [body], col, pale, body_leading=14)

    section(b, 1705, "01E", "关键责任边界", "专业人员与系统的边界必须可审计")
    card(b, "human-boundary", 60, 1732, 520, 72, "HUMAN APPROVAL", "人工必须确认 / 授权", ["专业规则、真实业务事实、例外处置、供应商资格、院方承诺、正式生效。"], C['red'], C['pale_red'], body_leading=14)
    card(b, "ai-boundary", 620, 1732, 520, 72, "AI ASSISTANCE", "智能体可以辅助", ["整理、核验、分析、生成候选、追踪任务、技术实现；不得自行放行。"], C['green'], C['pale_green'], body_leading=14)
    footer(b, "SOURCE · 用户任务书 + 番医总控台 V0.1.16 + 餐食运营台 V0.1.12 + 数据字典 v0.3 + 人力管理台 V0.2")
    return close(b)


def diamond(buf: list[str], ident: str, cx: float, cy: float, w: float, h: float, title: str, color: str = C['red']):
    pts = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    buf.append(f'<g id="{ident}"><polygon points="{pts}" fill="{C["pale_red"]}" stroke="{color}" stroke-width="1.3"/>')
    buf.append(text_lines(cx, cy-6, title.split("\n"), "small", 14, "middle", color))
    buf.append('</g>')


def obj_node(buf: list[str], ident: str, x: float, y: float, w: float, h: float, code: str, title: str, body: str, color: str, pale: str):
    card(buf, ident, x, y, w, h, code, title, [body], color, pale, body_leading=15)


def diagram_02() -> str:
    b = svg_open("图02｜番医核心对象与 SKU 关系架构")
    header(b, "FIG 02", "核心对象与 SKU 关系架构", "Core Objects, SKU & Controlled Relationship Architecture")

    section(b, 238, "02A", "共用对象、范围配置与版本治理", "共享不等于全局可编辑；范围覆盖须留来源和有效期")
    card(b, "governance", 60, 266, 1080, 90, "CONTROL PLANE · CANDIDATE", "受控主数据与规则版本", ["对象版本 · 状态 · 生效期 · 批准信息 · 范围（集团 / 项目 / 院区 / 厨房 / 服务点 / 渠道 / 场景）· 继承—覆盖—禁用 · 历史快照"], C['indigo'], C['pale_indigo'], body_leading=16)
    tag(b, 60, 378, "SHARED CAPABILITY POOL", C['indigo'], C['pale_indigo'], 220)
    tag(b, 840, 378, "SCOPED CONFIGURATION", C['purple'], C['pale_purple'], 210)

    section(b, 432, "02B", "场景、菜单档位与产品链", "场景 ≠ 菜单 ≠ 档位 ≠ 餐次；产品 ≠ 变体 ≠ SKU ≠ 套餐")
    obj_node(b, "scene", 60, 466, 250, 116, "SCENE", "场景配置", "对象 / 地点 / 时段 / 渠道 / 服务与履约规则", C['blue'], C['pale_blue'])
    obj_node(b, "slot", 370, 466, 250, 116, "MENU SLOT", "菜单结构点 / 档位", "餐次、菜序、窗口、排序、必选性、容量", C['blue'], C['pale_blue'])
    obj_node(b, "menu", 680, 466, 250, 116, "MENU VERSION", "菜单版本与可售项", "范围 + 有效期下的编排；非生产指令", C['purple'], C['pale_purple'])
    obj_node(b, "product", 60, 650, 205, 118, "PRODUCT", "标准产品", "产品家族 / 共用能力池", C['green'], C['pale_green'])
    obj_node(b, "variant", 315, 650, 205, 118, "VARIANT", "产品变体", "口味、规格、人群、工艺或营养差异", C['green'], C['pale_green'])
    obj_node(b, "sku", 570, 650, 205, 118, "SALES SKU", "售卖 SKU", "包装、份量、渠道、定价、履约差异", C['green'], C['pale_green'])
    obj_node(b, "setmeal", 825, 650, 315, 118, "SET MEAL", "组合套餐", "组成 SKU × 数量 / 可选 / 替换组 / 加价 / 生效期", C['green'], C['pale_green'])
    arrow(b, "scene-slot", 310, 524, 370, 524, C['blue'], "arrow-blue", False, "M:N · 场景化档位配置", 340, 512)
    arrow(b, "slot-menu", 620, 524, 680, 524, C['purple'], "arrow-purple", False, "编排", 650, 512)
    arrow(b, "product-variant", 265, 709, 315, 709, C['green'], "arrow-ink", False, "1:N", 290, 697)
    arrow(b, "variant-sku", 520, 709, 570, 709, C['green'], "arrow-ink", False, "1:N 候选", 545, 697)
    arrow(b, "sku-set", 775, 709, 825, 709, C['green'], "arrow-ink", False, "M:N", 800, 697)
    path_arrow(b, "menu-sku", "M805,582 C805,615 680,620 670,650", C['purple'], "arrow-purple", True, "档位上架 / 可售范围", 770, 620)

    section(b, 830, "02C", "配方、BOM、SOP、质量与采购供应链", "受控规则独立版本化；采购交易对象不可代替营养 / 配方对象")
    obj_node(b, "recipe", 60, 866, 205, 112, "RECIPE", "配方版本", "适用关系：范围 / 优先级 / 生效期", C['purple'], C['pale_purple'])
    obj_node(b, "bom", 315, 866, 205, 112, "BOM LINE", "BOM 明细", "用量 / 单位 / 损耗 / 替代规则", C['purple'], C['pale_purple'])
    obj_node(b, "sop", 570, 866, 205, 112, "SOP", "工艺 SOP", "工序 / 设备 / 节点 / 标签 / 温控", C['purple'], C['pale_purple'])
    obj_node(b, "quality", 825, 866, 315, 112, "QUALITY", "质量放行标准", "验收 / 质检 / 不合格处置；不与 SOP 混用", C['red'], C['pale_red'])
    obj_node(b, "ingredient", 60, 1030, 205, 112, "INGREDIENT", "标准食材", "营养 / 过敏原 / 分类 / 标准计量", C['gold'], C['pale_gold'])
    obj_node(b, "procsku", 315, 1030, 205, 112, "PROCUREMENT SKU", "采购 SKU", "品牌 / 包装 / 规格 / 外部交易编码", C['gold'], C['pale_gold'])
    obj_node(b, "supplier", 570, 1030, 205, 112, "SUPPLIER OFFER", "供应商供货项", "报价 / MOQ / 交期 / 合同 / 有效期", C['gold'], C['pale_gold'])
    obj_node(b, "channel", 825, 1030, 315, 112, "PROCUREMENT CHANNEL", "采购通道", "直供 / 平台 / 框架协议；不等同供应商", C['gold'], C['pale_gold'])
    arrow(b, "variant-recipe", 417, 768, 162, 866, C['purple'], "arrow-purple", True, "M:N · 适用配方", 260, 824)
    arrow(b, "recipe-bom", 265, 922, 315, 922, C['purple'], "arrow-purple", False, "1:N", 290, 910)
    arrow(b, "recipe-sop", 265, 946, 570, 946, C['purple'], "arrow-purple", True, "引用受控版本", 418, 963)
    arrow(b, "recipe-quality", 265, 970, 825, 970, C['red'], "arrow-red", True, "引用放行标准", 545, 988)
    arrow(b, "bom-ingredient", 417, 978, 162, 1030, C['gold'], "arrow-gold", False, "投入 / 用量", 290, 1010)
    arrow(b, "ingredient-procsku", 265, 1086, 315, 1086, C['gold'], "arrow-gold", False, "M:N · 转换", 290, 1074)
    arrow(b, "procsku-supplier", 520, 1086, 570, 1086, C['gold'], "arrow-gold", False, "M:N", 545, 1074)
    arrow(b, "supplier-channel", 775, 1086, 825, 1086, C['gold'], "arrow-gold", False, "M:N", 800, 1074)

    section(b, 1202, "02D", "需求、生产、库存、采购与履约事实闭环", "预测、计划、订单、批次、PO、收货与库存均为不同事实")
    obj_node(b, "order", 60, 1236, 205, 108, "MEAL ORDER", "餐食订单", "需求事实 / 履约承诺；不等于预测", C['blue'], C['pale_blue'])
    obj_node(b, "demand", 315, 1236, 205, 108, "DEMAND PLAN", "需求计划", "预测 / 确认 / 冻结；按场景、餐次、对象归集", C['blue'], C['pale_blue'])
    obj_node(b, "batch", 570, 1236, 205, 108, "PRODUCTION BATCH", "生产批次", "计划分配、领料、产出、质检与版本快照", C['green'], C['pale_green'])
    obj_node(b, "inventory", 825, 1236, 315, 108, "INVENTORY BATCH", "库存批次 / 台账事件", "地点 / 批次 / 效期 / 质量状态 / 可用量", C['gold'], C['pale_gold'])
    obj_node(b, "po", 60, 1410, 270, 108, "SUPPLIER PO", "供应商采购订单", "PO 头 / 行；请购、下达、确认、收货、关闭", C['gold'], C['pale_gold'])
    obj_node(b, "receipt", 405, 1410, 270, 108, "RECEIVING", "收货、验收与入库", "收货 ≠ 验收 ≠ 入库；不合格 / 退货可追溯", C['gold'], C['pale_gold'])
    obj_node(b, "delivery", 750, 1410, 390, 108, "DELIVERY & FEEDBACK", "配送 / 交付 / 反馈", "订单行 / 路线 / 批次可追溯；反馈指向发生对象", C['green'], C['pale_green'])
    arrow(b, "order-demand", 265, 1290, 315, 1290, C['blue'], "arrow-blue", False, "M:N · 需求归集", 290, 1278)
    arrow(b, "demand-batch", 520, 1290, 570, 1290, C['green'], "arrow-ink", False, "M:N · 生产分配", 545, 1278)
    arrow(b, "batch-inventory", 775, 1290, 825, 1290, C['gold'], "arrow-gold", False, "M:N · 领料 / 产出", 800, 1278)
    arrow(b, "po-receipt", 330, 1464, 405, 1464, C['gold'], "arrow-gold", False, "PO 行", 367, 1452)
    arrow(b, "receipt-inventory", 675, 1464, 900, 1344, C['gold'], "arrow-gold", True, "入库批次", 790, 1410)
    arrow(b, "batch-delivery", 672, 1344, 945, 1410, C['green'], "arrow-ink", True, "出品 / 交付", 820, 1380)
    arrow(b, "order-delivery", 162, 1344, 850, 1410, C['blue'], "arrow-blue", True, "履约 / 反馈", 520, 1392)

    section(b, 1590, "02E", "继承与审核约束", "专项餐基于通用能力池继承规则，不预设独立产品库")
    card(b, "inherit", 60, 1620, 515, 130, "INHERITANCE · CANDIDATE", "通用能力池 → 专项 / 场景配置", ["控糖餐、月子餐、专家餐、围餐等：继承 Product / Ingredient / Recipe / SOP 的适用版本；再按专业与场景规则做范围配置。", "任何覆盖须记录来源、理由、生效期、审核与责任人。"], C['indigo'], C['pale_indigo'], body_leading=16)
    card(b, "verify-count", 625, 1620, 515, 130, "TO VERIFY · KIMI", "104 结构点 / 141 产品 SKU", ["仅作为待核验母表事实；本轮不重编、不固化为正式编号或现行规模。", "应先核对：对象层级、名称、状态、价格、映射关系、源版本与责任源。"], C['gold'], C['pale_gold'], body_leading=16)
    footer(b, "SOURCE · 用户任务书 + 番医总控台 V0.1.16 + 餐食运营台 V0.1.12 + 数据字典 v0.3")
    return close(b)


def flow_box(buf: list[str], ident: str, x: float, y: float, w: float, h: float, index: str, title: str, lines: list[str], color: str, pale: str, body_leading: float = 15):
    card(buf, ident, x, y, w, h, index, title, lines, color, pale, body_leading=body_leading)


def diagram_03() -> str:
    b = svg_open("图03｜番医业务工作链与受控进化流程")
    header(b, "FIG 03", "业务工作链与受控进化流程", "Operational Work Chain & Controlled Evolution Flow")

    section(b, 238, "03A", "入口与四类受控版本", "发布菜单不等于生产指令；只有确认需求和批准生产计划可驱动执行")
    card(b, "weekly-package", 60, 266, 1080, 80, "INPUT PACKAGE · CANDIDATE", "每周全部启用场景的菜单计划包", ["覆盖常规场景与临时场景；包含适用范围、菜单候选、专业规则引用、历史事实与待核事项。"], C['indigo'], C['pale_indigo'], body_leading=15)
    versions = [("菜单版本", "草稿 → 待审核 → 已批准 → 已发布 / 生效", C['purple'], C['pale_purple']),
                ("需求版本", "预测 → 待确认 → 已确认 → 已冻结", C['blue'], C['pale_blue']),
                ("生产版本", "草拟 → 审核 → 已批准 → 已冻结 → 放行", C['green'], C['pale_green']),
                ("采购 / 库存执行", "请购 → PO → 收货验收 → 入库 / 领料 / 对账", C['gold'], C['pale_gold'])]
    for i,(t,body,col,pale) in enumerate(versions):
        card(b, f"version-{i}", 60+i*270, 376, 250, 100, "CONTROLLED VERSION", t, [body], col, pale, body_leading=15)

    section(b, 526, "03B", "阶段 1｜菜单形成与需求确认", "菜单候选可发布；确认需求才进入执行驱动")
    flow_box(b, "f1", 60, 558, 220, 126, "01", "菜单生成", ["常规与临时场景", "产品 / 结构点 / 专业规则引用"], C['purple'], C['pale_purple'])
    diamond(b, "g1", 360, 621, 118, 90, "专业审核\nHUMAN")
    flow_box(b, "f2", 500, 558, 220, 126, "02", "菜单发布", ["可供选择菜单 / 备选池", "锁定菜单版本与适用范围"], C['purple'], C['pale_purple'])
    flow_box(b, "f3", 780, 558, 300, 126, "03", "需求合并与预测", ["订单 / 预约 / 历史实绩 / 临时需求", "预测值、确认值与差异原因分开保存"], C['blue'], C['pale_blue'])
    arrow(b, "f1-g1", 280, 621, 301, 621, C['purple'], "arrow-purple")
    arrow(b, "g1-f2", 419, 621, 500, 621, C['red'], "arrow-red", False, "通过 / 退回", 458, 607)
    arrow(b, "f2-f3", 720, 621, 780, 621, C['blue'], "arrow-blue", False, "可选菜单", 750, 607)
    diamond(b, "g2", 960, 738, 118, 90, "确认需求\nHUMAN")
    arrow(b, "f3-g2", 930, 684, 960, 693, C['blue'], "arrow-blue", False, "确认", 935, 720)
    tag(b, 60, 710, "备选菜单 ≠ 生产指令", C['gold'], C['pale_gold'], 215)
    tag(b, 300, 710, "已确认需求 = 下游唯一合法输入", C['green'], C['pale_green'], 310)
    tag(b, 650, 710, "冻结前可调整 / 冻结后走异常变更", C['red'], C['pale_red'], 330)

    section(b, 840, "03C", "阶段 2｜生产、物料与采购计划", "共享采购合并净需求；专项采购独立标识、授权与成本归集")
    flow_box(b, "f4", 60, 872, 220, 126, "04", "生产计划", ["产量、批次、产线、工时、出品时点", "需求冻结点与临时变更窗口"], C['green'], C['pale_green'])
    flow_box(b, "f5", 340, 872, 220, 126, "05", "物料需求 / MRP", ["BOM、损耗、单位换算、可用库存、在途、替代规则"], C['gold'], C['pale_gold'])
    diamond(b, "g3", 640, 935, 118, 90, "物料复核\nHUMAN")
    flow_box(b, "f6", 780, 872, 300, 126, "06", "采购下单", ["共享采购：多场景净需求合并", "专项采购：专用标识 / 独立授权 / 预算与供货规则"], C['gold'], C['pale_gold'])
    path_arrow(b, "g2-f4", "M1019,783 C1019,835 280,835 280,872", C['green'], "arrow-ink", False, "已确认需求", 650, 830)
    arrow(b, "f4-f5", 280, 935, 340, 935, C['green'], "arrow-ink")
    arrow(b, "f5-g3", 560, 935, 581, 935, C['gold'], "arrow-gold")
    arrow(b, "g3-f6", 699, 935, 780, 935, C['red'], "arrow-red", False, "批准后下单", 740, 920)

    section(b, 1050, "03D", "阶段 3｜供应、生产、履约与结算", "实际事件要回写事实；收货、验收、入库、领料、生产、交付与成本不可合并为单状态")
    flow_box(b, "f7", 810, 1082, 195, 132, "07", "验收入库", ["数量 / 批次 / 效期 / 温控 / 质检", "合格入库 / 不合格退货 / 待处置"], C['gold'], C['pale_gold'])
    flow_box(b, "f8", 560, 1082, 195, 132, "08", "领料与排产排工", ["冻结生产版本领料", "岗位资质 / 产能 / 工时 / 时段覆盖"], C['green'], C['pale_green'])
    flow_box(b, "f9", 310, 1082, 195, 132, "09", "生产检查", ["实际投料 / 产出 / 留样 / 温控 / 质检", "放行 / 返工 / 报废"], C['green'], C['pale_green'])
    flow_box(b, "f10", 60, 1082, 195, 132, "10", "配送销售", ["路线批次 / 交接 / 签收 / 实发", "订单行与生产批次可追溯"], C['blue'], C['pale_blue'])
    flow_box(b, "f11", 400, 1262, 400, 118, "11", "结算成本与经营事实", ["采购价、收货、领用、损耗、报废、销量、退餐、餐补 / 结算口径分层对账；成本回写菜单、场景与餐次。"], C['indigo'], C['pale_indigo'], body_leading=16)
    arrow(b, "f6-f7", 930, 998, 907, 1082, C['gold'], "arrow-gold", False, "到货", 950, 1052)
    arrow(b, "f7-f8", 810, 1148, 755, 1148, C['gold'], "arrow-gold")
    arrow(b, "f8-f9", 560, 1148, 505, 1148, C['green'], "arrow-ink")
    arrow(b, "f9-f10", 310, 1148, 255, 1148, C['green'], "arrow-ink")
    path_arrow(b, "delivery-to-fin", "M158,1214 C175,1260 350,1320 400,1320", C['indigo'], "arrow-ink", False, "实绩 / 销售 / 交付", 270, 1280)
    path_arrow(b, "batch-to-fin", "M407,1214 C410,1240 500,1250 500,1262", C['indigo'], "arrow-ink", False, "消耗 / 产出 / 质量", 600, 1245)

    section(b, 1434, "03E", "阶段 4｜复盘、候选与人工受控进化", "实绩不能自动改写规则；先候选，后审核，再进入新版本草稿")
    flow_box(b, "f12", 60, 1466, 260, 126, "12", "复盘优化", ["销量、成本、浪费、质量、体验、异常、交付时效", "规则 / 专业主源 / 经营指标双向校验"], C['indigo'], C['pale_indigo'])
    flow_box(b, "candidate", 410, 1466, 260, 126, "CANDIDATE", "优化候选池", ["候选规则、菜单、配方、采购或排班修改", "保留证据、影响范围与差异说明"], C['purple'], C['pale_purple'])
    diamond(b, "g4", 780, 1529, 130, 96, "人工审核\n与授权")
    flow_box(b, "newdraft", 960, 1466, 180, 126, "NEXT VERSION", "新版本草稿", ["重新进入菜单 / 需求 / 生产受控链"], C['red'], C['pale_red'])
    arrow(b, "fin-review", 600, 1380, 190, 1466, C['indigo'], "arrow-ink", False, "经营事实", 360, 1430)
    arrow(b, "review-candidate", 320, 1529, 410, 1529, C['purple'], "arrow-purple")
    arrow(b, "candidate-g4", 670, 1529, 715, 1529, C['purple'], "arrow-purple")
    arrow(b, "g4-newdraft", 845, 1529, 960, 1529, C['red'], "arrow-red", False, "采纳 / 退回", 900, 1515)
    path_arrow(b, "next-to-menu", "M1050,1466 C1120,1395 1120,520 500,520", C['red'], "arrow-red", True, "经批准后形成后续菜单草稿", 1090, 1000)

    section(b, 1650, "03F", "变更与异常受控通道", "单场景修改必须重算全局影响；不得以线下消息绕开审计")
    card(b, "change", 60, 1682, 515, 112, "CHANGE CONTROL · CANDIDATE", "变更影响引擎", ["菜单 / 人数 / BOM / 供应库存 / 生产资源变更 → 影响订单、总需求、共享/专用食材、产能、工时、路线、预算与成本差异 → 重新审批或升级。"], C['gold'], C['pale_gold'], body_leading=16)
    card(b, "exception", 625, 1682, 515, 112, "EXCEPTION CONTROL · HUMAN", "异常受控通道", ["临时加餐、断供、验收不合格、库存不足、饮食变更、设备/人员故障：异常编号、影响评估、临时授权、补救动作、事后复盘。"], C['red'], C['pale_red'], body_leading=16)
    footer(b, "SOURCE · 用户任务书 + 番医总控台 V0.1.16 + 餐食运营台 V0.1.12 + 数据字典 v0.3")
    return close(b)


def main() -> None:
    diagrams = {
        "番医项目_图01_总体生态与系统能力架构_V0.1.svg": diagram_01(),
        "番医项目_图02_核心对象与SKU关系架构_V0.1.svg": diagram_02(),
        "番医项目_图03_业务工作链与受控进化流程_V0.1.svg": diagram_03(),
    }
    for name, content in diagrams.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print(name)


if __name__ == "__main__":
    main()
