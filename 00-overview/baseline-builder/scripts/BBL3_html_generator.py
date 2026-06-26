#!/usr/bin/env python3
"""
BBL3_html_generator.py
Synexa iS · L3 专项台 HTML 生成器
版本：V1.3
用法：python3 BBL3_html_generator.py <源md文件路径> <输出html文件路径>

规范依据：
- BBM Section 5.4（L3 台轻量字体方案）
- BBM Section 12.4（L3 台 HTML 生成规则）
- BBM Section 16（COVER 块规范 + stat_auto/stat_override 语法）
- BBL3 references/L3_structure.md（HTML 生成规范节）

V1.3 升级说明：
  - 新增 stat_auto 支持：三步融合提取（规则匹配 → LLM 校验 → stat_override 覆盖）
  - 新增 stat_override 支持：人工覆盖，最高优先级
  - stat_rule（旧字段）保留向后兼容，不再推荐
  - 提取原则定义详见 BBM Section 16.5（P1-P4）
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
# stat_rule 自动统计函数（BBM Section 16）
# ─────────────────────────────────────────────
def find_chapter_text(full_text, chapter_keyword):
    """从 md 全文中提取包含指定关键词的章节内容
    
    修复说明（V1.2）：原正则在 DOTALL 模式下 lookahead 的 ^ 无法正常锚定行首，
    改用 re.split 按章节分割后逐章匹配，彻底解决章节截取失败问题。
    """
    # 在文本开头加 \n，确保第一个章节也能被 split 正确切割
    # 支持 # ## ### 三级标题（包括子章节如 CH05.1）
    text_with_prefix = '\n' + full_text
    chapters = re.split(r'\n(?=#{1,3} )', text_with_prefix)
    for chapter in chapters:
        if re.match(r'^#{1,3} [^\n]*' + re.escape(chapter_keyword), chapter, re.IGNORECASE):
            return chapter
    return ""


def count_table_rows(full_text, chapter_keyword):
    """统计指定章节中表格的数据行数（不含表头和分隔行）
    
    修复说明（V1.2）：原逻辑把分隔行当成了第二行（header_passed=True），
    导致数据行永远无法被计数。修复为：先判断是否是分隔行，再决定是表头还是数据行。
    """
    chapter_text = find_chapter_text(full_text, chapter_keyword)
    if not chapter_text:
        return 0
    count = 0
    in_table = False
    header_passed = False
    sep_passed = False
    for line in chapter_text.split('\n'):
        stripped = line.strip()
        if not stripped:
            if in_table:
                in_table = False
                header_passed = False
                sep_passed = False
            continue
        if stripped.startswith('|'):
            # 先判断是否是分隔行（只含 - : 空格 |）
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                if in_table and header_passed and not sep_passed:
                    sep_passed = True
            elif not in_table:
                # 第一行：表头
                in_table = True
                header_passed = True
                sep_passed = False
            elif header_passed and sep_passed:
                # 数据行
                count += 1
        else:
            if in_table:
                in_table = False
                header_passed = False
                sep_passed = False
    return count


def count_keyword_rows(full_text, chapter_keyword, keyword):
    """统计指定章节中包含特定关键词的表格行数"""
    chapter_text = find_chapter_text(full_text, chapter_keyword)
    if not chapter_text:
        return 0
    count = 0
    for line in chapter_text.split('\n'):
        if line.startswith('|') and keyword in line:
            # 排除表头和分隔行
            if not re.match(r'^\|[-:\s|]+\|$', line.strip()):
                count += 1
    return count


def resolve_stat_rules(full_text, stat_rules):
    """解析 stat_rule 列表，返回 stats 列表"""
    stats = []
    for rule in stat_rules:
        parts = [p.strip() for p in rule.split('|')]
        if not parts:
            continue
        func = parts[0].strip().lower()

        if func == 'static':
            # static | 固定值 | 中文标签 | 英文标签
            num = parts[1] if len(parts) > 1 else '—'
            label = parts[2] if len(parts) > 2 else ''
            sub = parts[3] if len(parts) > 3 else ''
            stats.append({'num': num, 'label': label, 'sub': sub})

        elif func == 'count_table_rows':
            # count_table_rows | 章节关键词 | 中文标签 | 英文标签
            chapter_kw = parts[1] if len(parts) > 1 else ''
            label = parts[2] if len(parts) > 2 else chapter_kw
            sub = parts[3] if len(parts) > 3 else ''
            num = count_table_rows(full_text, chapter_kw)
            stats.append({'num': str(num), 'label': label, 'sub': sub})

        elif func == 'count_keyword_rows':
            # count_keyword_rows | 章节关键词 | 关键词 | 中文标签 | 英文标签
            chapter_kw = parts[1] if len(parts) > 1 else ''
            keyword = parts[2] if len(parts) > 2 else ''
            label = parts[3] if len(parts) > 3 else keyword
            sub = parts[4] if len(parts) > 4 else ''
            num = count_keyword_rows(full_text, chapter_kw, keyword)
            stats.append({'num': str(num), 'label': label, 'sub': sub})

    return stats


# ─────────────────────────────────────────────
# stat 自动提取：三步融合机制（BBM Section 16.6）
# ─────────────────────────────────────────────
def auto_extract_stats(full_text, cover_meta, stat_overrides=None):
    """
    三步融合提取（BBM Section 16.6）：
    Step 1  规则匹配：按 P1-P4 原则正则扫描 md，生成候选列表
    Step 2  LLM 校验：传入台定位 + 候选列表，返回最终 stat 列表
    Step 3  stat_override 覆盖：人工指定优先级最高
    """
    # Step 1: 规则匹配，按 P1-P4 原则扫描候选数字
    candidates = _rule_match_candidates(full_text)

    # Step 2: LLM 校验 + 补充
    stats = _llm_validate_stats(candidates, cover_meta, full_text)

    # Step 3: stat_override 覆盖（最高优先级）
    if stat_overrides:
        override_stats = resolve_stat_rules(full_text, stat_overrides)
        if override_stats:
            stats = override_stats

    return stats


def _rule_match_candidates(full_text):
    """
    Step 1: 规则匹配——按 P1-P4 原则扫描 md，返回候选数字列表
    返回格式：[{‘chapter’: str, ‘count’: int, ‘type’: str, ‘keyword’: str}, ...]
    """
    candidates = []
    text_with_prefix = '\n' + full_text
    chapters = re.split(r'\n(?=#{1,3} )', text_with_prefix)

    # P3 关键词：缺口/阻塞/待处理/异常
    P3_KEYWORDS = ['缺口', '阻塞', '待处理', '异常', '待解决', 'P0']

    for chapter in chapters:
        chapter = chapter.strip()
        if not chapter:
            continue
        # 提取章节标题
        title_match = re.match(r'^(#{1,3})\s+(.+)', chapter)
        if not title_match:
            continue
        chapter_title = title_match.group(2).strip()

        # 统计表格行数（P1/P2/P4）
        row_count = _count_rows_in_chapter(chapter)
        if row_count > 0:
            # 根据章节标题关键词判断类型
            stat_type = _classify_chapter(chapter_title)
            candidates.append({
                'chapter': chapter_title,
                'count': row_count,
                'type': stat_type,
                'keyword': None
            })

        # P3: 关键词行统计
        for kw in P3_KEYWORDS:
            kw_count = _count_keyword_in_chapter(chapter, kw)
            if kw_count > 0:
                candidates.append({
                    'chapter': chapter_title,
                    'count': kw_count,
                    'type': 'P3',
                    'keyword': kw
                })

    return candidates


def _count_rows_in_chapter(chapter_text):
    """统计章节内第一个表格的数据行数"""
    count = 0
    in_table = False
    header_passed = False
    sep_passed = False
    for line in chapter_text.split('\n'):
        stripped = line.strip()
        if not stripped:
            if in_table:
                in_table = False
                header_passed = False
                sep_passed = False
            continue
        if stripped.startswith('|'):
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                if in_table and header_passed and not sep_passed:
                    sep_passed = True
            elif not in_table:
                in_table = True
                header_passed = True
                sep_passed = False
            elif header_passed and sep_passed:
                count += 1
        else:
            if in_table:
                in_table = False
                header_passed = False
                sep_passed = False
    return count


def _count_keyword_in_chapter(chapter_text, keyword):
    """统计章节内包含关键词的表格行数"""
    count = 0
    for line in chapter_text.split('\n'):
        if line.startswith('|') and keyword in line:
            if not re.match(r'^\|[-:\s|]+\|$', line.strip()):
                count += 1
    return count


def _classify_chapter(chapter_title):
    """根据章节标题关键词判断 P1-P4 类型"""
    P1_KEYWORDS = ['岗位', '人员', '任务', '条目', '数量', '清单', '名单']
    P2_KEYWORDS = ['模块', '域', '层级', '引擎', '类型', '结构', '分类']
    P3_KEYWORDS = ['缺口', '阻塞', '待处理', '异常', '待解决']
    P4_KEYWORDS = ['精华', '资产', 'SOP', '文件', '规则', '基准', '定义']
    for kw in P1_KEYWORDS:
        if kw in chapter_title: return 'P1'
    for kw in P2_KEYWORDS:
        if kw in chapter_title: return 'P2'
    for kw in P3_KEYWORDS:
        if kw in chapter_title: return 'P3'
    for kw in P4_KEYWORDS:
        if kw in chapter_title: return 'P4'
    return 'P2'  # 默认归入 P2


def _llm_validate_stats(candidates, cover_meta, full_text):
    """
    Step 2: LLM 校验 + 补充
    输入：候选列表 + 台定位描述（title + sub + quote）
    输出：最终 stat 列表，最多 6 个，优先 P1
    """
    import os
    import json

    # 如果没有候选，直接返回空
    if not candidates:
        return []

    # 尝试调用 LLM
    api_key = os.environ.get('OPENAI_API_KEY')
    api_base = os.environ.get('OPENAI_API_BASE', 'https://api.openai.com/v1')

    if not api_key:
        # 无 API Key，降级为规则优先排序
        print('⚠️  未配置 OPENAI_API_KEY，降级为规则匹配模式')
        return _fallback_sort_candidates(candidates)

    # 构建输入（仅传候选列表，不读整个 md）
    station_context = (
        f"台名称：{cover_meta.get('title', '')}"
        f"。台定位：{cover_meta.get('sub', '')}"
        f"。核心原则：{cover_meta.get('quote', '')}"
    )
    candidates_text = json.dumps(candidates, ensure_ascii=False, indent=2)

    prompt = f"""你是一个业务分析専家。以下是一个运营管理台的定位和候选数字列表。

台定位：{station_context}

候选数字（规则匹配结果）：
{candidates_text}

请从中选出最重要的 4-6 个指标，要求：
1. 优先选 P1（规模类），依次补充 P2/P3/P4
2. 不超过 6 个
3. 为每个指标生成简洁的中英文标签（中文不超过 6 字，英文不超过 4 词）
4. 排除版本号、日期、百分比、金额类数字

以 JSON 数组返回，格式：
[
  {{"num": "数字", "label": "中文标签", "sub": "英文标签"}},
  ...
]
只返回 JSON，不要其他内容。"""

    try:
        import urllib.request
        payload = json.dumps({
            'model': 'gpt-4.1-mini',
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0.1,
            'max_tokens': 500
        }).encode('utf-8')
        req = urllib.request.Request(
            f'{api_base}/chat/completions',
            data=payload,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            }
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            content = result['choices'][0]['message']['content'].strip()
            # 提取 JSON 数组
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                stats = json.loads(json_match.group())
                # 确保格式正确
                return [{
                    'num': str(s.get('num', '?')),
                    'label': s.get('label', ''),
                    'sub': s.get('sub', '')
                } for s in stats if isinstance(s, dict)]
    except Exception as e:
        print(f'⚠️  LLM 校验失败，降级为规则匹配模式：{e}')

    return _fallback_sort_candidates(candidates)


def _fallback_sort_candidates(candidates):
    """降级模式：按 P1>P2>P3>P4 排序，取前 6 个，生成 stat 列表"""
    priority = {'P1': 0, 'P2': 1, 'P3': 2, 'P4': 3}
    sorted_candidates = sorted(candidates, key=lambda x: priority.get(x['type'], 9))
    stats = []
    # 去重：同一章节的表格行统计只保留一条
    seen_chapters = set()
    for c in sorted_candidates:
        if len(stats) >= 6:
            break
        kw = c.get('keyword')
        chapter_key = c['chapter'] + (kw or '')
        if chapter_key in seen_chapters:
            continue
        seen_chapters.add(chapter_key)
        if kw:
            label = f"{kw}数"
            sub = f"{kw} Count"
        else:
            # 从章节标题中提取有意义的关键词作为标签
            title = c['chapter']
            # 移除 CH数字、全角竖线、编号前缀
            clean = re.sub(r'^CH\d+[\.\d]*[｜|\s]+', '', title)
            clean = re.sub(r'^#+\s*', '', clean)
            # 取前 5 个字作为标签
            label = clean[:5] if len(clean) > 5 else clean
            # 英文标签：提取章节标题中的英文单词
            en_words = re.findall(r'[A-Za-z]+', title)
            sub = ' '.join(en_words[:3]) if en_words else label
        stats.append({
            'num': str(c['count']),
            'label': label,
            'sub': sub
        })
    return stats


# ─────────────────────────────────────────────
# 封面解析：从 md 文件头部提取封面字段
# ─────────────────────────────────────────────
def extract_cover_fields(text):
    """从 md 文本中提取封面字段（<!-- COVER ... --> 注释块）
    
    V1.3 新增支持：
    - stat_auto: true  → 触发三步融合自动提取
    - stat_override: ... → 人工覆盖，最高优先级
    - stat_rule: ...（旧字段）→ 向后兼容，仍可使用
    """
    cover = {
        "topline": "SYNEXA · INTERNAL SSOT · L3 STATION",
        "title": "",
        "en": "",
        "sub": "",
        "quote": "",
        "stats": [],
        "stat_rules": [],
        "stat_auto": False,
        "stat_overrides": []
    }

    # 尝试解析 <!-- COVER --> 注释块
    cover_match = re.search(r'<!--\s*COVER\s*\n(.*?)\n-->', text, re.DOTALL)
    if cover_match:
        block = cover_match.group(1)
        for line in block.strip().split('\n'):
            if ':' not in line:
                continue
            key, _, val = line.partition(':')
            key = key.strip().lower()
            val = val.strip()
            if key == 'topline':
                cover['topline'] = val
            elif key == 'title':
                cover['title'] = val
            elif key == 'en':
                cover['en'] = val
            elif key == 'sub':
                cover['sub'] = val
            elif key == 'quote':
                cover['quote'] = val
            elif key == 'stat_auto':
                cover['stat_auto'] = val.lower() == 'true'
            elif key == 'stat_override':
                cover['stat_overrides'].append(val)
            elif key == 'stat':
                # 兼容旧格式：stat: 数字 | 标签 | 英文说明
                parts = [p.strip() for p in val.split('|')]
                if len(parts) >= 2:
                    cover['stats'].append({
                        'num': parts[0],
                        'label': parts[1],
                        'sub': parts[2] if len(parts) > 2 else ''
                    })
            elif key == 'stat_rule':
                # 旧字段，向后兼容
                cover['stat_rules'].append(val)
    else:
        # 回退：从 h1 提取标题
        h1_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        if h1_match:
            cover['title'] = h1_match.group(1).strip()

    # 优先级：stat_auto（三步融合）> stat_rule（旧字段）> 静态 stat
    if cover['stat_auto']:
        # 新机制：三步融合提取
        cover_meta = {
            'title': cover['title'],
            'sub': cover['sub'],
            'quote': cover['quote']
        }
        cover['stats'] = auto_extract_stats(
            text,
            cover_meta,
            stat_overrides=cover['stat_overrides'] if cover['stat_overrides'] else None
        )
    elif cover['stat_rules']:
        # 旧机制：手写 stat_rule（向后兼容）
        cover['stats'] = resolve_stat_rules(text, cover['stat_rules'])

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
# 正文解析：按章节分割，每章一个 section 卡片
# ─────────────────────────────────────────────
def build_body_html(text):
    """将 md 正文转换为章节卡片 HTML"""
    # 移除 COVER 注释块
    text = re.sub(r'<!--\s*COVER\s*\n.*?\n-->', '', text, flags=re.DOTALL)

    # 按 # 开头的标题分割章节
    chapters = re.split(r'\n(?=#{1,2} )', text.strip())

    md_ext = ['tables', 'fenced_code', 'toc', 'attr_list', 'nl2br']

    body_html = ""
    for chapter in chapters:
        chapter = chapter.strip()
        if not chapter:
            continue

        # 确定 eyebrow 标签
        eyebrow = "CORE CHAPTER"
        if re.match(r'^# CH\(-1\)', chapter):   eyebrow = "GOVERNANCE"
        elif re.match(r'^# CH00', chapter):      eyebrow = "BASELINE PROTOCOL"
        elif re.match(r'^# CH\d+.*版本', chapter): eyebrow = "VERSION RECORD"
        elif re.match(r'^# CH\d+.*快速恢复', chapter): eyebrow = "RECOVERY PROTOCOL"
        elif re.match(r'^# CH\d+.*附录', chapter): eyebrow = "APPENDIX"
        elif re.match(r'^# 台定位', chapter):    eyebrow = "STATION SCOPE"
        elif re.match(r'^# Executive', chapter): eyebrow = "EXECUTIVE SUMMARY"
        elif re.match(r'^# CH\d+.*数智', chapter): eyebrow = "DIGITAL INTELLIGENCE"
        elif re.match(r'^# CH\d+.*岗位', chapter): eyebrow = "ROLES & RESPONSIBILITIES"
        elif re.match(r'^# CH\d+.*任务', chapter): eyebrow = "TASK MANAGEMENT"
        elif re.match(r'^# CH\d+.*工作流', chapter): eyebrow = "WORKFLOW"
        elif re.match(r'^# CH\d+.*台账', chapter): eyebrow = "RECORDS & REPORTS"

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
    SYNEXA · INTERNAL SSOT · GENERATED {today} · BBL3_HTML_GENERATOR V1.3
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
