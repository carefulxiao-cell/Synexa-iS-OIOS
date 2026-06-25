#!/usr/bin/env python3
"""
BBL3_html_generator.py
Synexa iS · L3 专项台 HTML 生成器
版本：V1.0
用法：python3 BBL3_html_generator.py <源md文件路径> <输出html文件路径>

规范依据：
- BBM Section 5.4（L3 台轻量字体方案）
- BBM Section 12.4（L3 台 HTML 生成规则）
- BBL3 references/L3_structure.md（HTML 生成规范节）
"""

import sys
import re
import markdown
from pathlib import Path
from datetime import datetime

# ─────────────────────────────────────────────
# CSS：L3 台轻量排版标准（系统字体降级，零依赖）
# ─────────────────────────────────────────────
CSS = """
:root {
  --green:   #28CC83;
  --purple:  #8B5ACA;
  --dark:    #1F2933;
  --mid:     #374151;
  --muted:   #667085;
  --faint:   #98A2B3;
  --border:  #D9DEE7;
  --bg-soft: #F7F9FC;

  /* L3 台系统字体降级栈（BBM Section 5.4）*/
  --font-en-theme: 'Space Grotesk', 'DIN Alternate', 'Helvetica Neue', Arial, sans-serif;
  --font-zh-title: 'Noto Serif SC', 'Source Han Serif SC', 'STSong', 'SimSun', Georgia, serif;
  --font-zh-body:  'PingFang SC', 'Noto Sans SC', 'Source Han Sans SC', 'Microsoft YaHei', sans-serif;
  --font-data:     'JetBrains Mono', 'SF Mono', 'Consolas', 'Courier New', monospace;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg-soft);
  color: var(--dark);
  font-family: var(--font-zh-body);
  font-size: 14px;
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}

/* ── 页面容器 ── */
.page-wrap {
  max-width: min(1280px, calc(100% - 48px));
  margin: 0 auto;
  padding: 40px 0 80px;
}

/* ── 封面区域 ── */
.cover {
  background: #fff;
  border-radius: 12px;
  padding: 56px 64px 48px;
  margin-bottom: 32px;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
}

.topline {
  font-family: var(--font-en-theme);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.14em;
  color: var(--muted);
  text-transform: uppercase;
  margin-bottom: 24px;
}

.cover-title {
  font-family: var(--font-zh-title);
  font-size: 36px;
  font-weight: 700;
  color: var(--dark);
  line-height: 1.25;
  margin-bottom: 12px;
}

.cover-en {
  font-family: var(--font-en-theme);
  font-size: 20px;
  font-weight: 600;
  color: var(--mid);
  margin-bottom: 8px;
}

.cover-sub {
  font-family: var(--font-en-theme);
  font-size: 11px;
  color: var(--muted);
  margin-bottom: 28px;
}

.cover-quote {
  border-left: 3px solid var(--green);
  background: var(--bg-soft);
  padding: 14px 20px;
  font-family: var(--font-zh-body);
  font-size: 14px;
  color: var(--mid);
  border-radius: 0 6px 6px 0;
  margin-bottom: 32px;
  line-height: 1.8;
}

.statgrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 16px;
  margin-top: 8px;
}

.stat {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 20px 16px;
  background: #fff;
}

.stat .num {
  font-family: var(--font-en-theme);
  font-size: 32px;
  font-weight: 700;
  color: var(--dark);
  line-height: 1;
  margin-bottom: 8px;
}

.stat .statlabel {
  font-family: var(--font-zh-body);
  font-size: 13px;
  color: var(--mid);
  margin-bottom: 4px;
}

.stat .statsub {
  font-family: var(--font-en-theme);
  font-size: 10px;
  color: var(--faint);
}

/* ── 章节卡片 ── */
.chapter {
  background: #fff;
  border-radius: 8px;
  padding: 40px 48px;
  margin-bottom: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,.05);
}

.eyebrow {
  font-family: var(--font-en-theme);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.14em;
  color: var(--green);
  text-transform: uppercase;
  margin-bottom: 16px;
}

/* ── 标题层级 ── */
h1 {
  font-family: var(--font-zh-title);
  font-size: 24px;
  font-weight: 700;
  color: var(--dark);
  border-top: 1px solid var(--border);
  padding-top: 20px;
  margin-bottom: 24px;
  line-height: 1.4;
}

h2 {
  font-family: var(--font-zh-body);
  font-size: 16px;
  font-weight: 700;
  color: var(--mid);
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
  margin: 28px 0 14px;
}

h3 {
  font-family: var(--font-zh-body);
  font-size: 14px;
  font-weight: 700;
  color: var(--mid);
  margin: 20px 0 10px;
}

h4 {
  font-family: var(--font-en-theme);
  font-size: 10px;
  font-weight: 700;
  color: var(--green);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin: 16px 0 8px;
}

/* ── 表格 ── */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 13px;
}

th {
  background: #F0F2F5;
  color: var(--dark);
  font-family: var(--font-zh-body);
  font-weight: 700;
  font-size: 12px;
  padding: 9px 12px;
  text-align: left;
  border: 1px solid var(--border);
}

td {
  padding: 8px 12px;
  border: 1px solid var(--border);
  vertical-align: top;
  line-height: 1.6;
}

tr:nth-child(even) td { background: var(--bg-soft); }

/* ── 标签组件 ── */
.tag {
  display: inline-block;
  background: rgba(40,204,131,.12);
  color: #1a9e63;
  border: 1px solid rgba(40,204,131,.3);
  border-radius: 4px;
  padding: 2px 8px;
  font-family: var(--font-en-theme);
  font-size: 11px;
  font-weight: 600;
  margin: 2px 3px 2px 0;
}

.chain {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 8px 0;
}

/* ── 引言/blockquote ── */
blockquote {
  border-left: 3px solid var(--green);
  background: var(--bg-soft);
  padding: 12px 18px;
  margin: 16px 0;
  border-radius: 0 6px 6px 0;
  font-size: 14px;
  color: var(--mid);
}

/* ── 代码 ── */
code {
  font-family: var(--font-data);
  font-size: 12px;
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: 3px;
  padding: 1px 5px;
  color: var(--purple);
}

pre {
  background: #0B1220;
  border-radius: 6px;
  padding: 20px;
  overflow-x: auto;
  margin: 16px 0;
}

pre code {
  font-family: var(--font-data);
  font-size: 12px;
  color: #e2e8f0;
  background: none;
  border: none;
  padding: 0;
}

/* ── 段落/列表 ── */
p { margin: 10px 0; }
ul, ol { padding-left: 22px; margin: 10px 0; }
li { margin: 4px 0; line-height: 1.7; }

strong { font-weight: 700; color: var(--dark); }
em { color: var(--purple); font-style: normal; font-weight: 600; }

/* ── 分隔线 ── */
hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 28px 0;
}

/* ── 页脚 ── */
.doc-footer {
  text-align: center;
  font-family: var(--font-en-theme);
  font-size: 10px;
  color: var(--faint);
  letter-spacing: 0.1em;
  padding: 32px 0 0;
  border-top: 1px solid var(--border);
  margin-top: 40px;
}
"""

# ─────────────────────────────────────────────
# 封面解析：从 md 文件头部提取封面字段
# ─────────────────────────────────────────────
def extract_cover_fields(text):
    """从 md 文本中提取封面字段（<!-- COVER ... --> 注释块）"""
    cover = {
        "topline": "SYNEXA · INTERNAL SSOT · L3 STATION",
        "title": "",
        "en": "",
        "sub": "",
        "quote": "",
        "stats": []
    }

    # 尝试解析 <!-- COVER --> 注释块
    cover_match = re.search(r'<!--\s*COVER\s*\n(.*?)\n-->', text, re.DOTALL)
    if cover_match:
        block = cover_match.group(1)
        for line in block.strip().split('\n'):
            if ':' in line:
                key, _, val = line.partition(':')
                key = key.strip().lower()
                val = val.strip()
                if key == 'topline': cover['topline'] = val
                elif key == 'title': cover['title'] = val
                elif key == 'en': cover['en'] = val
                elif key == 'sub': cover['sub'] = val
                elif key == 'quote': cover['quote'] = val
                elif key == 'stat':
                    # 格式：stat: 数字 | 标签 | 英文说明
                    parts = [p.strip() for p in val.split('|')]
                    if len(parts) >= 2:
                        cover['stats'].append({
                            'num': parts[0],
                            'label': parts[1],
                            'sub': parts[2] if len(parts) > 2 else ''
                        })
    else:
        # 回退：从 h1 提取标题
        h1_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        if h1_match:
            cover['title'] = h1_match.group(1).strip()

    return cover


def build_cover_html(cover):
    """构建封面 HTML"""
    stats_html = ""
    for s in cover['stats']:
        stats_html += f"""
      <div class="stat">
        <div class="num">{s['num']}</div>
        <div class="statlabel">{s['label']}</div>
        <div class="statsub">{s['sub']}</div>
      </div>"""

    statgrid = f'<div class="statgrid">{stats_html}\n    </div>' if stats_html else ''
    quote_html = f'<div class="cover-quote">{cover["quote"]}</div>' if cover['quote'] else ''

    return f"""
  <div class="cover">
    <div class="topline">{cover['topline']}</div>
    <div class="cover-title">{cover['title']}</div>
    <div class="cover-en">{cover['en']}</div>
    <div class="cover-sub">{cover['sub']}</div>
    {quote_html}
    {statgrid}
  </div>
"""


# ─────────────────────────────────────────────
# 正文解析：按 ## 章节分割，每章一个 section 卡片
# ─────────────────────────────────────────────
def build_body_html(text):
    """将 md 正文转换为章节卡片 HTML"""
    # 移除 COVER 注释块
    text = re.sub(r'<!--\s*COVER\s*\n.*?\n-->', '', text, flags=re.DOTALL)

    # 按 # 开头的标题分割章节
    # 每个 h1（#）或 h2（##）开头视为新章节
    chapters = re.split(r'\n(?=#{1,2} )', text.strip())

    md_ext = ['tables', 'fenced_code', 'toc', 'attr_list', 'nl2br']

    body_html = ""
    for chapter in chapters:
        chapter = chapter.strip()
        if not chapter:
            continue

        # 确定 eyebrow 标签
        eyebrow = "CORE CHAPTER"
        if re.match(r'^# CH\(-1\)', chapter): eyebrow = "GOVERNANCE"
        elif re.match(r'^# CH00', chapter): eyebrow = "BASELINE PROTOCOL"
        elif re.match(r'^# CH\d+.*版本', chapter): eyebrow = "VERSION RECORD"
        elif re.match(r'^# CH\d+.*快速恢复', chapter): eyebrow = "RECOVERY PROTOCOL"
        elif re.match(r'^# CH\d+.*附录', chapter): eyebrow = "APPENDIX"
        elif re.match(r'^# 台定位', chapter): eyebrow = "STATION SCOPE"
        elif re.match(r'^# Executive', chapter): eyebrow = "EXECUTIVE SUMMARY"

        # 转换 markdown
        html_content = markdown.markdown(chapter, extensions=md_ext)

        body_html += f"""
  <div class="chapter">
    <div class="eyebrow">{eyebrow}</div>
    {html_content}
  </div>
"""

    return body_html


# ─────────────────────────────────────────────
# 主函数
# ─────────────────────────────────────────────
def generate(md_path: str, html_path: str):
    src = Path(md_path)
    if not src.exists():
        print(f"❌ 源文件不存在：{md_path}")
        sys.exit(1)

    text = src.read_text(encoding='utf-8')

    # 提取文件标题（用于 <title>）
    title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    page_title = title_match.group(1).strip() if title_match else src.stem

    # 构建封面
    cover_fields = extract_cover_fields(text)
    if not cover_fields['title']:
        cover_fields['title'] = page_title
    cover_html = build_cover_html(cover_fields)

    # 构建正文
    body_html = build_body_html(text)

    # 页脚
    today = datetime.now().strftime('%Y-%m-%d')
    footer_html = f"""
  <div class="doc-footer">
    SYNEXA · INTERNAL SSOT · GENERATED {today} · BBL3_HTML_GENERATOR V1.0
  </div>
"""

    # 组合完整 HTML
    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="page-wrap">
{cover_html}
{body_html}
{footer_html}
</div>
</body>
</html>"""

    Path(html_path).write_text(full_html, encoding='utf-8')

    # 验证
    h1_count = full_html.count('<h1>')
    table_count = full_html.count('<table>')
    stray_md = len(re.findall(r'\n#{1,4} ', full_html))
    size_kb = len(full_html.encode('utf-8')) / 1024

    print(f"✅ 生成完成：{html_path}")
    print(f"   h1={h1_count} | tables={table_count} | 残留md标题={stray_md} | 大小={size_kb:.1f}KB")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法：python3 BBL3_html_generator.py <源md文件路径> <输出html文件路径>")
        sys.exit(1)
    generate(sys.argv[1], sys.argv[2])
