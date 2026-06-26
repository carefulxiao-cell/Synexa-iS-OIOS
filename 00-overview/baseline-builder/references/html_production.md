# HTML 生产规范引用

**文件代号**：HTML-PROD-REF  
**版本**：V1.1  
**上级规范**：BBM V1.3  
**执行脚本**：`BBLx_html_generator.py`（全层级通用）  
**最后更新**：2026-06-26  

本文件为 HTML 生产执行入口说明。L1/L2/L3 全层级统一使用 `BBLx_html_generator.py` 生产 HTML。

## 调用方式

执行 HTML 生产任务时，需要用户提供或 Agent 从 GitHub 读取：

```
Synexa_Baseline_HTML_Production_Standard.md
```

GitHub 路径：`carefulxiao-cell/Synexa-iS-OIOS/00-overview/Synexa_Baseline_HTML_Production_Standard.md`

本地路径：存放于 `Synexa_Company_Intro_V.x/` 文件夹（与 `fonts/` 同级）

## 字体依赖

HTML 生产后，HTML 文件需与 `fonts/` 文件夹同级存放，字体才能正常加载。

`fonts/` 目录结构：
```
fonts/
├── space-grotesk/
├── noto/
└── dejavu/
```

## 快速执行路径

1. 用户提供源 md 文件
2. 用户提供 SBHPS.md（或 Agent 从 GitHub 读取）
3. Agent 按 SBHPS 规范生成 HTML（CSS 内联，无外部依赖）
4. 交付 HTML 文件，用户放入 `Synexa_Company_Intro_V.x/` 文件夹
