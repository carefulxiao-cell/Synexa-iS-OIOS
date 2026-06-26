# Synexa 基线文件构建主规范

**文件代号**：BBM（Baseline Builder Master）  
**版本**：V1.2  
**对齐基准**：Synexa_Company_Intro_V3.10  
**适用范围**：所有 Synexa 体系基线文件（L2 项目级 + L3 专项台）  
**文件性质**：机器可执行规范，任何 AI Agent 持此文件即可生产视觉一致的 HTML

---

## ⚡ 强制执行声明（Agent 必读）

**收到本文件即代表当前任务是「生产基线文件」。**

无需等待用户额外确认，无需推断意图，直接按以下规则执行：

**内容识别规则：**
1. 若用户同时上传了源 md 文件 → 直接进入 Step 2（提炼内容），跳过 Step 1
2. 若用户没有上传源 md，只有对话内容 → 直接进入 Step 1（识别类型），从对话提炼
3. 若用户同时上传了 `Baseline_Builder_L2.md` → 按 L2 结构执行
4. 若用户同时上传了 `Baseline_Builder_L3.md` → 按 L3 结构执行

**多文件默认决策（禁止反问）：**
5. 若识别出多个独立专项台（L3）→ **默认分别生成独立文件**，每个专项台一个 md + 一个 HTML，不合并
6. 若识别出多个独立项目（L2）→ **默认分别生成独立文件**，不合并
7. 若内容明显属于同一个文件（章节关系）→ 合并为一个文件

**交付格式默认规则（禁止反问）：**
8. **默认同时生成 md + HTML 两个文件**，这是 BBM 的标准交付格式，无需用户确认
9. 若用户明确说「只要 md」→ 只生成 md，跳过 HTML
10. 完成后直接交付，不询问「你想要什么」「只要 md 还是要 HTML」

**唯一例外**：用户明确说「只看规范」或「不要生产文件」时，才停止执行。

---

## 0. 字体依赖声明（执行前必读）

**本文件必须与 `fonts/` 文件夹同级存放。**

```
Synexa_Company_Intro_V.x/          ← 统一字体根目录（文件夹名可自定义）
├── fonts/                          ← 字体文件夹，永久保留，不随版本更新
│   ├── space-grotesk/
│   ├── dejavu/
│   └── noto/
├── Baseline_Builder_Master.md      ← 本文件
├── Baseline_Builder_L2.md          ← L2 内容结构规范
├── Baseline_Builder_L3.md          ← L3 内容结构规范
├── Synexa_Company_Intro_V3.10.html ← CSS 提取源（必须存在）
└── {其他项目基线文件...}
```

**字体文件不随版本更新**：`fonts/` 内容固定，所有版本 HTML 共用同一套字体，无需重复复制或更新。

---

## 1. 文件层级定义

| 层级 | 类型 | 适用场景 | 结构规范 |
|---|---|---|---|
| L2 | 项目级基线 | 一个完整项目的全量基线（定位、架构、规则、字典、SOP） | `Baseline_Builder_L2.md` |
| L3 | 专项台基线 | 某一专项主题的运营台（任务跟踪、人力管理、餐食运营等） | `Baseline_Builder_L3.md` |

---

## 2. 三形态文件体系

每个基线文件维护三个形态，职责不同，不可混用：

| 形态 | 文件命名 | 用途 | 维护方式 |
|---|---|---|---|
| 机读版 | `{项目名}_machine.md` | AI Agent 载入，纯业务内容，无排版标记 | 每次内容更新后从人读源重新生成 |
| 人读源文件 | `{项目名}_V{版本}.md` | HTML 生成源，含 HTML 结构标记 | SSOT，所有内容更新在此文件 |
| 人读展示层 | `{项目名}_V{版本}.html` | 浏览器打开，视觉展示 | 从人读源一键生成，不手动编辑 |

**PDF 规则**：需要 PDF 时，从 HTML 用 weasyprint 转换，不单独维护 PDF 源文件。

---

## 3. 执行流程（从对话到基线文件）

### Step 1：识别类型

判断当前任务是 L2 还是 L3：
- **L2**：覆盖整个项目，有完整的业务定义、字典、规则体系 → 读取 `Baseline_Builder_L2.md`
- **L3**：聚焦某一专项主题，有任务状态、操作规程、当前进展 → 读取 `Baseline_Builder_L3.md`

### Step 2：提炼内容

从对话内容或上传文件中提炼，按对应结构模板组织：

**提炼原则：**
- 保留所有业务定义、规则、关系、字典、决策结论、数字数据
- 删除所有排版说明、视觉描述、HTML 标签
- 模糊表述转化为结构化字段，不猜测补全，未明确的标注「待确认」
- 对话中的讨论过程只保留结论，不保留过程

### Step 3：生成人读源 md

按结构模板输出 md 文件：
- 文件头加上位引用声明（如适用）
- 章节标题使用 `#` / `##` / `###`，不使用 HTML 标签
- 表格使用标准 Markdown pipe 格式
- 版本号格式：`V0.x`（子业务初版），`V1.x`（正式版）

### Step 4：生成人读 HTML

按本文件 Section 4–12 的排版规范生产 HTML：
- CSS 从 `Synexa_Company_Intro_V3.10.html` 的 `<style>` 块原样提取（不手写，不修改）
- CSS 内联在 `<style>` 块内，不引用外部文件
- 封面区按 Section 7 模板构建
- 章节内容用 python-markdown 转换（extensions: tables, fenced_code, md_in_html, toc, attr_list, nl2br）

**交付物命名规范：**
```
{项目名}_{文件类型}_V{版本号}.md
{项目名}_{文件类型}_V{版本号}.html
```

### Step 5：生成机读精简版（按需）

用户说「加机读版」或需要上传到 Codex Project 时执行：
- 剥离所有 HTML 标签（保留规则说明文字中的标签描述）
- 保留全部业务内容（定义、规则、关系、字典、数据）
- 目标体积比原版压缩 15-25%
- 文件命名：`{项目名}_V{版本号}_machine.md`

---

## 4. 快速触发词

| 用户说 | 执行动作 |
|---|---|
| 整理成基线文件 | 识别类型 → 提炼 → 生成 md + HTML |
| 生产基线文件 | 同上 |
| 只要 md | 跳过 Step 4，只输出 md |
| 加机读版 | 额外执行 Step 5 |
| 更新基线 | 读取已有 md → 合并新内容 → 更新版本号 → 重新生成 HTML |

---

## 5. 字体体系

### 5.1 字体文件路径（相对路径，与 HTML 同级）

```
fonts/
├── space-grotesk/
│   ├── SpaceGrotesk-Regular.ttf
│   ├── SpaceGrotesk-Medium.ttf
│   ├── SpaceGrotesk-SemiBold.ttf
│   └── SpaceGrotesk-Bold.ttf
├── dejavu/
│   ├── JetBrainsMono-Regular.ttf
│   └── JetBrainsMono-Bold.ttf
└── noto/
    ├── NotoSans-Condensed.ttf
    ├── NotoSans-CondensedBold.ttf
    ├── NotoSansCJK-Regular.ttc
    ├── NotoSansCJK-Bold.ttc
    ├── NotoSerifCJK-Regular.ttc
    └── NotoSerifCJK-Bold.ttc
```

### 5.2 字体角色分配

| CSS 变量 | 字体族 | 用途 |
|---|---|---|
| `--font-en-theme` | Space Grotesk | 英文标题、数字、标签、eyebrow |
| `--font-zh-title` | SerifCJK（NotoSerifCJK）| 中文大标题、封面标题、引言 |
| `--font-zh-body` | CJK（NotoSansCJK）| 中文正文、h2/h3 |
| `--font-data` | Mono（JetBrainsMono）| 代码、数据、页脚 |

### 5.3 @font-face 声明（完整，必须原样写入 `<style>` 块）

```css
@font-face { font-family: 'Space Grotesk'; font-weight: 400; src: url('fonts/space-grotesk/SpaceGrotesk-Regular.ttf') format('truetype'); }
@font-face { font-family: 'Space Grotesk'; font-weight: 500; src: url('fonts/space-grotesk/SpaceGrotesk-Medium.ttf') format('truetype'); }
@font-face { font-family: 'Space Grotesk'; font-weight: 600; src: url('fonts/space-grotesk/SpaceGrotesk-SemiBold.ttf') format('truetype'); }
@font-face { font-family: 'Space Grotesk'; font-weight: 700; src: url('fonts/space-grotesk/SpaceGrotesk-Bold.ttf') format('truetype'); }
@font-face { font-family: Mono; src: url('fonts/dejavu/JetBrainsMono-Regular.ttf') format('truetype'); }
@font-face { font-family: Mono; font-weight:700; src: url('fonts/dejavu/JetBrainsMono-Bold.ttf') format('truetype'); }
@font-face { font-family: EnCondensed; src: url('fonts/noto/NotoSans-Condensed.ttf') format('truetype'); }
@font-face { font-family: EnCondensed; font-weight:700; src: url('fonts/noto/NotoSans-CondensedBold.ttf') format('truetype'); }
@font-face { font-family: CJK; src: url('fonts/noto/NotoSansCJK-Regular.ttc') format('collection'); }
@font-face { font-family: CJK; font-weight:700; src: url('fonts/noto/NotoSansCJK-Bold.ttc') format('collection'); }
@font-face { font-family: SerifCJK; src: url('fonts/noto/NotoSerifCJK-Regular.ttc') format('collection'); }
@font-face { font-family: SerifCJK; font-weight:700; src: url('fonts/noto/NotoSerifCJK-Bold.ttc') format('collection'); }
```

### 5.4 L3 台轻量字体方案（零依赖，系统字体降级）

**适用范围**：L3 专项台 HTML（内部工作文件，不依赖 `fonts/` 文件夹）

**原则**：字体接近目标字感即可，不追求完全一致，零存储成本，任何设备打开排版稳定。

```css
:root {
  /* 英文/数字：机械感、几何感（Space Grotesk 方向）*/
  --font-en-theme: 'Space Grotesk', 'DIN Alternate', 'Helvetica Neue', Arial, sans-serif;

  /* 中文主标题：人文化、有衬线（思源宋体方向）*/
  --font-zh-title: 'Noto Serif SC', 'Source Han Serif SC', 'STSong', 'SimSun', Georgia, serif;

  /* 中文正文/h2/h3：人文化、清晰易读（思源黑体方向）*/
  --font-zh-body: 'PingFang SC', 'Noto Sans SC', 'Source Han Sans SC', 'Microsoft YaHei', sans-serif;

  /* 等宽/代码 */
  --font-data: 'JetBrains Mono', 'SF Mono', 'Consolas', 'Courier New', monospace;
}
```

**各平台实际渲染**：

| 用途 | Mac/iOS | Windows | Android |
|---|---|---|---|
| 英文/数字 | Helvetica Neue（接近几何感）| Arial | Roboto |
| 中文主标题 | STSong（有衬线）| SimSun（有衬线）| Noto Serif SC |
| 中文正文 | PingFang SC（最接近思源黑体）| Microsoft YaHei | Noto Sans SC |

**L3 台 HTML 不使用 `@font-face` 声明，不引用 `fonts/` 路径。**

---

## 6. 颜色体系

```css
:root {
  --green:   #28CC83;   /* 主品牌色，强调、边框、eyebrow */
  --purple:  #8B5ACA;   /* 次强调色，callout.core、em、badge */
  --dark:    #1F2933;   /* 主文字色 */
  --mid:     #374151;   /* 次文字色，h2/h3 */
  --muted:   #667085;   /* 辅助文字，封面副标题 */
  --faint:   #98A2B3;   /* 最弱文字，statsub、页脚 */
  --border:  #D9DEE7;   /* 所有边框 */
  --bg-soft: #F7F9FC;   /* 浅背景，表格偶数行、blockquote、callout */
}
```

**禁止规则**：不得在正文中使用 `--green` 或 `--purple` 作为大面积背景色，只用于边框、标签、强调元素。

---

## 7. 封面结构（Cover Section）

### 7.1 HTML 模板

```html
<div class="section cover">

  <div class="topline">
    {品牌标识} · {项目名称} · INTERNAL SSOT
  </div>

  <div class="cover-title">
    {中文大标题}「{文件类型}」
  </div>

  <div class="cover-en">
    {英文项目名} V{版本号}
  </div>

  <div class="cover-sub">
    {一句话英文定位描述}
  </div>

  <div class="quote">
    {核心引言，1-2句}
  </div>

  <div class="statgrid">
    <div class="stat">
      <div class="num">{数字或代号}</div>
      <div class="statlabel">{标签}</div>
      <div class="statsub">{英文说明}</div>
    </div>
    <!-- 固定 4 个 stat 卡片 -->
  </div>

</div>
```

### 7.2 封面字段规则

| 字段 | 规则 |
|---|---|
| topline | 全大写英文，`·` 分隔，字号 10px，颜色 `--muted` |
| cover-title | SerifCJK 字体，36px，中文主标题 + 「文件类型」 |
| cover-en | Space Grotesk，20px，英文项目名 + 版本号 |
| cover-sub | Space Grotesk，11px，颜色 `--muted` |
| quote | SerifCJK，14px，左边框 3px `--green`，背景 `--bg-soft` |
| statgrid | 固定 4 列，每列一个 stat 卡片 |
| num | Space Grotesk Bold，32px，可以是数字或代号（如 CH(-1)）|

---

## 8. 章节容器结构

每个章节必须用以下容器包裹：

```html
<div class="section chapter" id="{章节锚点ID}">
  <div class="eyebrow">{章节分类标签，全大写英文}</div>
  <!-- 章节内容，h1 开头 -->
</div>
```

**eyebrow 规则**：Space Grotesk，10px，颜色 `--green`，字母间距 0.14em，全大写。常用值：`BASELINE PROTOCOL` / `CORE CHAPTER` / `GOVERNANCE` / `APPENDIX` / `VERSION RECORD`

---

## 9. 标题层级

| 标签 | 字体 | 字号 | 颜色 | 用途 |
|---|---|---|---|---|
| h1 | SerifCJK Bold | 24px | `--dark` | 章节主标题，上边框 1px `--border` |
| h2 | CJK Bold | 16px | `--mid` | 小节标题，下边框 1px `--border` |
| h3 | CJK Bold | 14px | `--mid` | 三级标题，无边框 |
| h4 | Space Grotesk Bold | 10px | `--green` | 最小标题，全大写，字母间距 0.12em |

**h1 格式规范**：`CH XX｜{英文标题} {中文副标题}`，中文副标题用 `<span class="subtitle">` 包裹，渲染为 14px `--muted` 颜色。

---

## 10. 组件库

### 10.1 Callout（强调框）

```html
<!-- 默认绿色 -->
<div class="callout note">
  <div class="call-label">NOTE</div>
  {内容}
</div>

<!-- 紫色核心原则 -->
<div class="callout core">
  <div class="call-label">CORE PRINCIPLE</div>
  {内容}
</div>

<!-- 黄色警告 -->
<div class="callout warn">
  <div class="call-label">WARNING</div>
  {内容}
</div>
```

### 10.2 Protocol Grid（2列卡片）

```html
<div class="protocol-grid">
  <div class="protocol-card">
    <div class="pc-title">{标签}</div>
    {内容}
  </div>
  <div class="protocol-card">
    <div class="pc-title">{标签}</div>
    {内容}
  </div>
</div>
```

### 10.3 Summary Grid（2列摘要）

```html
<div class="summary-grid">
  <div class="summary-card">{内容}</div>
  <div class="summary-card">{内容}</div>
</div>
```

### 10.4 Badge（行内标签）

```html
<span class="badge">{标签文字}</span>
```

### 10.5 Blockquote / 引言

```html
<blockquote>
  {引言内容}
</blockquote>
```

左边框 3px `--green`，背景 `--bg-soft`，字号 14px。

---

## 11. 表格规范

- 表头：背景 `#0B1220`（深黑），白色文字，Space Grotesk Bold，11px
- 奇数行：白色背景
- 偶数行：`--bg-soft` 背景
- 单元格：边框 1px `--border`，内边距 7px 10px，顶部对齐
- 字号：13px

**matrix 表格**（代码/数据矩阵）：第一列使用 `class="matrix"`，字体 Mono，颜色 `--purple`。

---

## 12. HTML 文件生成规范

### 12.1 文件结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{文件标题}</title>
<style>
  {完整 CSS，内联，不引用外部文件}
</style>
</head>
<body>
<div class="page-wrap">
  {封面 section.cover}
  {各章节 section.chapter，每章一个 div}
  {页脚 doc-footer}
</div>
</body>
</html>
```

### 12.2 CSS 内联规则

- CSS 必须内联在 `<style>` 块内，不得引用外部 `.css` 文件
- 字体用相对路径 `fonts/` 引用，HTML 与 `fonts/` 文件夹必须同级
- CSS 从已验证 HTML 原样提取，不手写，不修改，确保版本间视觉一致

### 12.3 Python 生成脚本标准流程

```python
# Step 1：从已验证 HTML 原样提取 <style> 块（不手写 CSS）
# Step 2：读取 md 源文件，分离封面区（HTML 原生）和正文（Markdown）
# Step 3：正文用 python-markdown 转换
#         extensions: tables, fenced_code, md_in_html, toc, attr_list, nl2br
# Step 4：组合 HTML = head + style + 封面 + 转换后正文 + 页脚
# Step 5：验证（h1/h2/table 数量、残留 # 行数 = 0）
```

### 12.4 L3 台 HTML 生成规则

**L3 台使用独立的轻量生成脚本**，与 L2 生成流程不同：

| 项目 | L2（Company Intro 级）| L3（专项台）|
|---|---|---|
| 字体方案 | 本地 `fonts/` 文件夹 | 系统字体降级栈（Section 5.4）|
| 封面样式 | 完整封面（topline + title + en + sub + quote + statgrid）| 精简封面（topline + title + en + sub + quote + statgrid，宽度与正文等宽）|
| 正文样式 | L2 section 卡片 | 白底圆角 section 卡片，浅灰 th，`.tag` `.chain` 组件 |
| 生成脚本 | 从已验证 HTML 提取 CSS | `scripts/BBL3_html_generator.py` |

**调用方式**：

```bash
# 在 baseline-builder/ 目录下
python3 scripts/BBL3_html_generator.py <源md文件路径> <输出html文件路径>

# 示例
python3 scripts/BBL3_html_generator.py 番医饭堂·人力管理台_V0.2.md 番医饭堂·人力管理台_V0.2.html
```

**脚本位置**：`carefulxiao-cell/Synexa-iS-OIOS/00-overview/baseline-builder/scripts/BBL3_html_generator.py`

---

## 13. PDF 生成规范

```bash
# 方法一：weasyprint（推荐，中文支持好）
weasyprint input.html output.pdf

# 方法二：浏览器打印
# 浏览器打开 HTML → 打印 → 另存为 PDF → 去掉页眉页脚
```

**注意**：weasyprint 转换时，`fonts/` 路径必须与 HTML 同级，否则字体无法嵌入。

---

## 14. 分发规则

| 场景 | 分发内容 | 说明 |
|---|---|---|
| 内部本地使用 | HTML 文件 | 放入含 `fonts/` 的文件夹，浏览器打开 |
| 对外分享 / 存档 | PDF 文件 | 从 HTML 转换，单文件，无依赖 |
| AI Agent 载入 | `_machine.md` | 纯文本，无排版标记，最小 token 消耗 |
| 内容更新 | 更新人读源 md → 重新生成 HTML → 按需生成 PDF | 三个形态同步更新 |

---

## 15. 版本对齐声明

本标准基于 `Synexa_Company_Intro_V3.10` 的实际 CSS 和 HTML 结构提取，与 V3.10 视觉完全一致。

每次 Company Intro 升级后，检查以下字段是否有变更：
- CSS 颜色变量（Section 6）
- 字体体系（Section 5）
- 封面结构（Section 7）

如有变更，同步更新本文件版本号，并重新生成所有子业务 HTML。

---

---

## 16. COVER 块规范（通用，适用所有层级基线文件）

### 16.1 定义

COVER 块是每个基线文件（L2、L3 及以上）md 文件的**头部声明区**，以 HTML 注释形式写入，不影响 md 正文阅读，由生成脚本解析后渲染为 HTML 封面。

COVER 块只承担**声明性职责**：告知脚本该文件的元信息和 stat 提取意图。**不写执行指令**，不写固定章节号，不写手动统计规则。

### 16.2 COVER 块标准格式

```
<!-- COVER
topline: SYNEXA · [项目代号] · INTERNAL SSOT · [层级标识]
title: [中文主标题]
en: [英文副标题 + 版本号]
sub: [一句话英文描述]
quote: [核心原则/定位语，中文，显示为引言块]
stat_auto: true
stat_override: [函数名] | [章节关键词] | [中文标签] | [英文标签]  ← 可选，例外覆盖
-->
```

### 16.3 字段说明

| 字段 | 必填 | 说明 |
|---|---|---|
| `topline` | ✅ | 全大写英文，`·` 分隔，显示在标题上方 |
| `title` | ✅ | 中文主标题，衬线字体加粗渲染 |
| `en` | ✅ | 英文副标题，含版本号 |
| `sub` | ✅ | 一句话英文描述，显示在副标题下方 |
| `quote` | ✅ | 核心原则，显示为绿色左边框引言块 |
| `stat_auto` | ✅ | 固定写 `true`，触发脚本自动提取核心数字 |
| `stat_override` | 可选 | 例外覆盖，最高优先级，格式见 16.4；用于自动提取无法准确识别的特殊指标 |

> `stat_rule`（旧字段）已废除，不再使用。md 文件作者无需了解统计函数，只需写内容。

### 16.4 stat_override 语法（仅在需要例外覆盖时使用）

**格式**：`stat_override: [函数名] | [章节关键词] | [中文标签] | [英文标签]`

**支持的统计函数**：

| 函数名 | 说明 | 字段数 |
|---|---|---|
| `count_table_rows` | 统计指定章节中第一个表格的数据行数（不含表头）| 4字段：函数 \| 章节关键词 \| 中文标签 \| 英文标签 |
| `count_keyword_rows` | 统计指定章节表格中包含特定关键词的行数 | 5字段：函数 \| 章节关键词 \| 行内关键词 \| 中文标签 \| 英文标签 |
| `count_sections` | 统计 md 中以指定关键词开头的 `##` 章节数 | 4字段 |
| `static` | 固定值，不统计，直接显示 | 4字段：函数 \| 固定值 \| 中文标签 \| 英文标签 |

### 16.5 stat 自动提取原则（P1-P4）

脚本执行 `stat_auto: true` 时，按以下优先级从 md 内容中识别核心数字：

| 优先级 | 类型 | 典型示例 | 识别方式 |
|---|---|---|---|
| **P1 规模类** | 人员数、岗位数、任务数、条目数 | 中台 6 岗、前线 15 岗、25 条精华 | 规则匹配：统计表格行数 |
| **P2 结构类** | 模块数、覆盖域数、层级数 | 职能域 11 个、引擎 9 个 | 规则匹配：统计表格行数或章节数 |
| **P3 缺口/异常类** | 覆盖缺口数、待处理事项数、阻塞数 | 覆盖缺口 1 个、阻塞任务 3 条 | 规则匹配：关键词行统计（缺口/阻塞/待处理） |
| **P4 资产类** | 可迁移精华数、文件资产数、SOP 数 | 可迁移精华 25 条 | 规则匹配：统计表格行数 |

**排除原则**：版本号、日期、百分比、金额、纯文字描述字段不纳入 statgrid。

**数量上限**：每个台最多 6 个 stat 卡片，优先取 P1，依次补充 P2/P3/P4。

### 16.6 融合提取机制（脚本执行流程）

脚本收到 `stat_auto: true` 后，按以下三步执行：

```
Step 1  规则匹配（快速、确定性）
        按 P1-P4 原则，正则扫描 md 全文
        → 输出候选数字列表：[(章节, 数字, 候选标签), ...]

Step 2  LLM 校验 + 补充（语义判断）
        输入：台定位描述（title + sub + quote）+ 候选列表 + P1-P4 原则
        LLM 执行：
          ① 从候选列表选出最重要的 4-6 个
          ② 识别规则匹配遗漏的重要数字（补充）
          ③ 为每项生成准确的中英文标签
        → 输出：最终 stat 列表
        注：LLM 输入仅为候选列表，不读整个 md，token 成本极低

Step 3  stat_override 覆盖（最高优先级）
        若 COVER 块有 stat_override 字段，以人工指定为准，覆盖 Step 2 结果
        → 输出：最终执行的 stat 列表
```

### 16.7 设计原则

- **规范归规范层**：提取原则只在 BBM/BBLx 定义，脚本读规则执行，不内置判断逻辑
- **内容归内容层**：md 只写业务内容和声明，不写执行指令，作者无需懂脚本
- **规则匹配是骨架，LLM 是判断层**：两者职责不重叠，互为补充
- **人工覆盖是最高优先级**：`stat_override` 兜底，保留人工干预出口
- **各层独立演化**：BBLx 新增层级不影响 BBM，脚本升级不影响 md
- `topline` 格式统一：`SYNEXA · [项目代号] · INTERNAL SSOT · [层级]`
- COVER 块放在 md 文件**第一行**，在所有正文内容之前

---

*BBM V1.4 · 2026-06 · SYNEXA INTERNAL SSOT*
