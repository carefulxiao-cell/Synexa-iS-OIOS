# Synexa 基线文件 HTML 排版生产标准

**文件代号**：SBHPS  
**版本**：V1.0  
**对齐基准**：Synexa_Company_Intro_V3.10  
**适用范围**：所有 Synexa 体系基线文件（L1 Company Intro + L2 子业务基线）  
**文件性质**：机器可执行生产规范，任何 AI Agent 持此文件即可生产视觉一致的 HTML

---

## 1. 文件体系定义

每个基线文件维护三个形态，职责不同，不可混用：

| 形态 | 文件命名 | 用途 | 维护方式 |
|---|---|---|---|
| 机读版 | `{项目名}_machine.md` | AI Agent 载入，业务内容，无排版标记 | SSOT，每次内容更新后重新生成 |
| 人读源文件 | `{项目名}_V{版本}.md` | HTML 生成源，含 HTML 结构标记 | SSOT，内容更新在此文件 |
| 人读展示层 | `{项目名}_V{版本}.html` | 浏览器打开，视觉展示 | 从人读源文件一键生成，不手动编辑 |

**PDF 规则**：需要 PDF 时，从 HTML 用 weasyprint 转换，不单独维护 PDF 源文件。

---

## 2. 字体体系

### 2.1 字体文件路径（相对路径，与 HTML 同级）

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

### 2.2 字体角色分配

| CSS 变量 | 字体族 | 用途 |
|---|---|---|
| `--font-en-theme` | Space Grotesk | 英文标题、数字、标签、eyebrow |
| `--font-zh-title` | SerifCJK（NotoSerifCJK）| 中文大标题、封面标题、引言 |
| `--font-zh-body` | CJK（NotoSansCJK）| 中文正文、h2/h3 |
| `--font-data` | Mono（JetBrainsMono）| 代码、数据、页脚 |

### 2.3 @font-face 声明（完整，必须原样写入 `<style>` 块）

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

## 3. 颜色体系

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

## 4. 页面布局

```css
.page-wrap {
  max-width: 960px;
  margin: 0 auto;
  padding: 48px 48px 80px;
}
```

所有内容必须包裹在 `<div class="page-wrap">` 内，不得直接写在 `<body>` 下。

---

## 5. 封面结构（Cover Section）

### 5.1 HTML 模板

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
    <!-- 重复 4 个 stat，固定 4 列 -->
  </div>

</div>
```

### 5.2 封面字段规则

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

## 6. 章节容器结构

每个章节必须用以下容器包裹：

```html
<div class="section chapter" id="{章节锚点ID}">
  <div class="eyebrow">{章节分类标签，全大写英文}</div>
  <!-- 章节内容，h1 开头 -->
</div>
```

**eyebrow 规则**：Space Grotesk，10px，颜色 `--green`，字母间距 0.14em，全大写。常用值：`BASELINE PROTOCOL` / `CORE CHAPTER` / `GOVERNANCE` / `APPENDIX` / `VERSION RECORD`

---

## 7. 标题层级

| 标签 | 字体 | 字号 | 颜色 | 用途 |
|---|---|---|---|---|
| h1 | SerifCJK Bold | 24px | `--dark` | 章节主标题，上边框 1px `--border` |
| h2 | CJK Bold | 16px | `--mid` | 小节标题，下边框 1px `--border` |
| h3 | CJK Bold | 14px | `--mid` | 三级标题，无边框 |
| h4 | Space Grotesk Bold | 10px | `--green` | 最小标题，全大写，字母间距 0.12em |

**h1 格式规范**：`CH XX｜{英文标题} {中文副标题}`，中文副标题用 `<span class="subtitle">` 包裹，渲染为 14px `--muted` 颜色。

---

## 8. 组件库

### 8.1 Callout（强调框）

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

### 8.2 Protocol Grid（2列卡片）

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

### 8.3 Summary Grid（2列摘要）

```html
<div class="summary-grid">
  <div class="summary-card">{内容}</div>
  <div class="summary-card">{内容}</div>
</div>
```

### 8.4 Badge（行内标签）

```html
<span class="badge">{标签文字}</span>
```

### 8.5 Blockquote / 引言

```html
<blockquote>
  {引言内容}
</blockquote>
```

左边框 3px `--green`，背景 `--bg-soft`，字号 14px。

---

## 9. 表格规范

- 表头：背景 `#0B1220`（深黑），白色文字，Space Grotesk Bold，11px
- 奇数行：白色背景
- 偶数行：`--bg-soft` 背景
- 单元格：边框 1px `--border`，内边距 7px 10px，顶部对齐
- 字号：13px

**matrix 表格**（代码/数据矩阵）：第一列使用 `class="matrix"`，字体 Mono，颜色 `--purple`。

---

## 10. 代码块规范

- 行内代码：Mono 字体，12px，背景 `#F0F2F7`，颜色 `--purple`，圆角 3px
- 代码块：背景 `#F0F2F7`，边框 1px `--border`，圆角 6px，内边距 14px 16px

---

## 11. 页脚规范

```html
<div class="doc-footer">
  {文件代号} · {版本号} · {日期} · SYNEXA INTERNAL SSOT
</div>
```

Mono 字体，11px，颜色 `--faint`，居中，上边框 1px `--border`，距正文 64px。

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
- 不得修改 CSS 内容，以保持全局视觉一致性

### 12.3 Python 生成脚本标准流程

```python
# Step 1：从已验证 HTML 原样提取 <style> 块（不手写 CSS）
# Step 2：读取 md 源文件，分离封面区（HTML 原生）和正文（Markdown）
# Step 3：正文用 python-markdown 转换（extensions: tables, fenced_code, md_in_html, toc, attr_list, nl2br）
# Step 4：组合 HTML = head + style + 封面 + 转换后正文 + 页脚
# Step 5：验证（h1/h2/table 数量、残留 # 行数 = 0）
```

**关键规则**：CSS 永远从已验证 HTML 提取，不手写，不修改，确保版本间视觉一致。

---

## 13. PDF 生成规范

从 HTML 转 PDF，保持视觉完全一致：

```bash
# 方法一：weasyprint（推荐，中文支持好）
weasyprint input.html output.pdf

# 方法二：浏览器打印
# 浏览器打开 HTML → 打印 → 另存为 PDF → 去掉页眉页脚
```

**注意**：weasyprint 转换时，`fonts/` 路径必须是绝对路径或与 HTML 同级相对路径，否则字体无法嵌入。

---

## 14. 分发规则

| 场景 | 分发内容 | 说明 |
|---|---|---|
| 内部本地使用 | HTML 文件 | 放入含 `fonts/` 的文件夹，浏览器打开 |
| 对外分享 / 存档 | PDF 文件 | 从 HTML 转换，单文件，无依赖 |
| AI Agent 载入 | `_machine.md` | 纯文本，无排版标记，最小 token 消耗 |
| 内容更新 | 更新人读源 md → 重新生成 HTML → 重新生成 PDF | 三个形态同步更新 |

---

## 15. 版本对齐声明

本标准基于 `Synexa_Company_Intro_V3.10` 的实际 CSS 和 HTML 结构提取，与 V3.10 视觉完全一致。

每次 Company Intro 升级后，检查以下字段是否有变更：
- CSS 颜色变量（Section 3）
- 字体体系（Section 2）
- 封面结构（Section 5）

如有变更，同步更新本文件版本号，并重新生成所有子业务 HTML。

---

*SBHPS V1.0 · 2026-06 · SYNEXA INTERNAL SSOT*
