# L3 专项台基线文件结构规范

适用于：某一专项主题的运营台（任务跟踪台、人力管理台、餐食运营台、采购台等）

---

## 文件命名规范

```
{品牌简称}_{专项名称}_{台类型}_V{版本号}.md
例：番医饭堂·餐食运营推进工作台_V1.0.md
    番医饭堂·任务跟踪台_V1.0.md
    番医饭堂·人力管理台_V1.0.md
```

---

## 必选章节（所有 L3 文件必须包含）

### 文件头声明区

```markdown
上位参考：{所属 L2 基线文件名}
文件层级：L3 · 专项台
专项类型：{任务跟踪 / 运营推进 / 人力管理 / 采购管理 / 其他}
当前版本：V{版本号}
最后更新：{日期}
```

### 台定位（3 行以内）

- 本台覆盖范围（一句话）
- 本台不覆盖什么（边界）
- 与其他专项台的关系（如有交叉）

### 当前状态总览

格式：任务/主题编号 + 名称 + 当前状态 + 最近动作

```markdown
| 编号 | 主题 | 状态 | 最近动作 | 下一步 |
|---|---|---|---|---|
| T1 | ... | 进行中 | ... | ... |
```

状态枚举：`待启动` / `进行中` / `暂停` / `已完成` / `已归档`

---

## 按专项类型的扩展章节

### 任务跟踪台（专项类型 = 任务跟踪）

**必选扩展章节：**

- **任务清单**：T0-Tn 完整列表，每项包含：编号、名称、负责人、截止日期、状态、阻塞原因（如有）
- **暂停与阻塞记录**：当前所有暂停项的原因和恢复条件
- **已完成归档**：已完成任务的简要记录（不删除，归档保留）
- **下一步优先动作**：最多 5 条，按优先级排序

### 运营推进台（专项类型 = 运营推进）

**必选扩展章节：**

- **当期推进主题**：本阶段聚焦的 3-5 个主题
- **关键决策记录**：每次推进产生的关键结论，格式：日期 + 结论 + 影响范围
- **规则变更记录**：运营规则的每次变更，格式：变更前 → 变更后 + 原因
- **待解决问题池**：未解决的问题清单，格式：问题描述 + 优先级 + 负责人

### 人力管理台（专项类型 = 人力管理）

**必选扩展章节：**

- **当前人员清单**：姓名、岗位、状态（在职/离职/待入职）、入职日期
- **岗位职责详述**：每个岗位的详细职责、权限、考核标准
- **排班规则**：当前排班逻辑、轮班周期、特殊情况处理
- **薪酬结构**：基本工资 + 绩效结构（不含具体数字，只含结构）
- **问题与待处理事项**：人力相关的待解决问题

### 采购管理台（专项类型 = 采购管理）

**必选扩展章节：**

- **供应商清单**：名称、品类、状态、联系方式
- **当期采购计划**：品类 + 数量 + 预计到货日期
- **采购规则**：触发条件、审批流程、验收标准
- **价格基准**：关键食材的基准价格和波动范围
- **异常记录**：采购异常、缺货、替代方案记录

---

## 通用附录章节（可选）

- **附录 A：关键数据表**（SKU 清单、价格表、人员表等）
- **附录 B：SOP 摘要**（完整 SOP 的精简版，完整版存于独立文件）
- **附录 C：历史记录归档**（超过 30 条的旧记录归档区）

---

## 体积控制规则

| 规则 | 标准 |
|---|---|
| 单台体积上限 | ≤ 300 行 |
| 历史记录超出 | 超过 30 条后，旧记录移入附录 C |
| 决策记录保留 | 最近 20 条保留在主体，更早的归档 |
| 文件超过 300 行 | 拆分为主台 + 历史归档台两个文件 |

---

## 内容提炼指引

从对话中提炼 L3 内容时：

1. **状态类信息**：直接录入当前状态总览表，精确到"最近动作"和"下一步"
2. **规则类信息**：录入对应规则章节，标注生效日期
3. **问题与阻塞**：录入待解决问题池或暂停记录，不丢失
4. **数字与数据**：原样保留，不做推断或估算
5. **未明确的信息**：标注「待确认」，不猜测补全
6. **对话中的讨论过程**：只保留结论，不保留讨论过程

---

## HTML 生成规范（L3 台专属）

### 调用脚本

```bash
python3 scripts/BBL3_html_generator.py <源md文件路径> <输出html文件路径>
```

脚本位置：`baseline-builder/scripts/BBL3_html_generator.py`

### 字体方案

L3 台使用系统字体降级栈（BBM Section 5.4），零依赖，不需要 `fonts/` 文件夹。

| 用途 | 字体栈 |
|---|---|
| 英文/数字（机械感）| `'Space Grotesk', 'DIN Alternate', 'Helvetica Neue', Arial, sans-serif` |
| 中文主标题（人文化衬线）| `'Noto Serif SC', 'Source Han Serif SC', 'STSong', 'SimSun', serif` |
| 中文正文（人文化无衬线）| `'PingFang SC', 'Noto Sans SC', 'Source Han Sans SC', 'Microsoft YaHei', sans-serif` |
| 等宽/代码 | `'JetBrains Mono', 'SF Mono', 'Consolas', monospace` |

### 封面样式规则

- 封面与正文等宽：`min(1280px, calc(100% - 48px))`，居中
- topline：全大写英文，`·` 分隔，10px，颜色 `--muted`
- 中文主标题：系统衬线字体，36px，font-weight 700
- 英文副标题：几何感字体，20px，font-weight 600
- quote 引言：左边框 3px `--green`，背景 `--bg-soft`
- statgrid：4-6 列等宽卡片，数字 32px 几何感字体

### 正文样式规则

- 每个章节用白底圆角卡片包裹（`border-radius: 8px`，`box-shadow` 轻阴影）
- 表格 `th`：浅灰背景 `#F0F2F5`，深色文字，非深黑底
- 支持 `.tag`（绿色胶囊标签）和 `.chain`（链式标签组）组件
- 页面背景：`#F7F9FC`（浅灰），卡片背景：白色


---

## L3 台 COVER 块 stat_rule 示例

> stat_rule 语法规范详见 BBM Section 16。以下为各类 L3 专项台的推荐配置，按台类型选用。

### 人力管理台

```
stat_rule: count_table_rows | CH03 | 中台岗位 | Mid-tier Roles
stat_rule: count_table_rows | CH04 | 前线岗位 | Front-line Roles
stat_rule: count_table_rows | CH05 | 职能域 | Function Domains
stat_rule: count_keyword_rows | CH05 | 缺口 | 覆盖缺口 | Coverage Gaps
stat_rule: count_table_rows | CH06 | 数智引擎 | Active Engines
stat_rule: count_table_rows | CH09 | 可迁移精华 | Transferable Insights
```

### 任务跟踪台

```
stat_rule: count_keyword_rows | CH03 | 进行中 | 进行中任务 | Active Tasks
stat_rule: count_keyword_rows | CH03 | 阻塞 | 阻塞任务 | Blocked Tasks
stat_rule: count_keyword_rows | CH03 | 已完成 | 已完成任务 | Completed Tasks
stat_rule: count_table_rows | CH04 | 两周清单 | Sprint Items
stat_rule: static | 5 | 任务分类 | Task Categories
```

### 运营推进台

```
stat_rule: count_table_rows | CH03 | 工作流 | Workflows
stat_rule: count_table_rows | CH04 | 文档体系 | Document Types
stat_rule: count_table_rows | CH05 | SOP | SOPs
stat_rule: count_keyword_rows | CH06 | P0 | 最高级异常 | P0 Incidents
stat_rule: count_table_rows | CH07 | 补充模块 | Add-on Modules
```

### 通用原则

- 每个台的 `stat_rule` 应体现该台**最核心的量化指标**，让封面一眼看出台的健康状态
- 建议 4-6 个 statgrid 卡片，不超过 6 个
- 优先选择**动态变化**的指标（任务数、岗位数），而非静态说明性字段
- `static` 函数用于版本号、固定配置数等不需要统计的字段
