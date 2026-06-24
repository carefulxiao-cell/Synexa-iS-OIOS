# Synexa 基线文件构建主规范

**文件代号**：BBM（Baseline Builder Master）  
**版本**：V1.0  
**对齐基准**：Synexa_Company_Intro_V3.10  
**适用范围**：所有 Synexa 体系基线文件（L2 项目级 + L3 专项台）  
**文件性质**：机器可执行规范，任何 AI Agent 持此文件 + 对应结构规范，即可从对话内容直接生产视觉一致的基线文件（md + HTML）

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

*BBM V1.0 · 2026-06 · SYNEXA INTERNAL SSOT*
