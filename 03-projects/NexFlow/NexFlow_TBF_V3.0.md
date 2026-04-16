# NexFlow V3.0 任务目标基线文件（TBF）

> **版本**：V3.0
> **指令包文件**：`nexflow_v3_0_final.md`
> **创建时间**：2026-04-16
> **最后核查时间**：2026-04-16（SCO 首次核查）

---

## 一、核查清单

### 模块一：人力管理（/hr）

- [x] `HR.tsx` 页面存在，含证件管理/培训记录/排班原则三 Tab | 验证：截图确认 | 状态：已完成
- [ ] `hr_certificates` 表已建立 | 验证：`SHOW TABLES LIKE 'hr_%'` | 状态：待核查
- [ ] `hr_trainings` 表已建立 | 验证：`SHOW TABLES LIKE 'hr_%'` | 状态：待核查
- [ ] `hr_schedule_principles` 表已建立 | 验证：`SHOW TABLES LIKE 'hr_%'` | 状态：待核查
- [ ] `server/routers/hr.ts` 存在且注册至 `routers.ts` | 验证：代码检查 | 状态：待核查
- [ ] 证件附件上传字段 `attachmentUrl` 存在 | 验证：`schema.ts` | 状态：待核查
- [ ] 培训证书附件字段 `attachmentUrl` 存在 | 验证：`schema.ts` | 状态：待核查
- [ ] 证件到期预警（30天内橙色标记）功能正常 | 验证：截图 | 状态：待核查

### 模块二：日常运营（/daily-ops）

- [x] `DailyOps.tsx` 页面存在，含运营日志/巡检记录/交接班三 Tab | 验证：截图确认 | 状态：已完成
- [ ] `ops_logs` 表已建立 | 验证：`SHOW TABLES LIKE 'ops_%'` | 状态：待核查
- [ ] `ops_inspections` 表已建立 | 验证：`SHOW TABLES LIKE 'ops_%'` | 状态：待核查
- [ ] `ops_handovers` 表已建立 | 验证：`SHOW TABLES LIKE 'ops_%'` | 状态：待核查
- [ ] `server/routers/dailyOps.ts` 存在且注册 | 验证：代码检查 | 状态：待核查
- [ ] 交接班接班人身份校验功能正常 | 验证：截图 | 状态：待核查

### 模块三：文件中心（/files）

- [ ] 侧边栏「导入导出」已改名为「文件中心」 | 验证：`NexFlowLayout.tsx` 第38行 | 状态：❌ 未完成
- [ ] 路由从 `/import-export` 改为 `/files` | 验证：`App.tsx` | 状态：❌ 未完成
- [ ] `FileCenter.tsx` 页面存在，含五个 Tab | 验证：`pages/` 目录 | 状态：❌ 未完成
- [ ] `server/routers/files.ts` 存在 | 验证：`routers/` 目录 | 状态：❌ 未完成
- [ ] `useFileUpload` hook 存在 | 验证：`hooks/` 目录 | 状态：❌ 未完成
- [ ] 旧路由 `/import-export` 重定向至 `/files` | 验证：`App.tsx` | 状态：❌ 未完成

### 全局

- [x] 侧边栏新增「人力管理」导航项 | 验证：截图确认 | 状态：已完成
- [x] 侧边栏新增「日常运营」导航项 | 验证：截图确认 | 状态：已完成
- [ ] `App.tsx` 注册 `/files` 路由 | 验证：代码检查 | 状态：❌ 未完成
- [ ] 全量测试通过（vitest） | 验证：`pnpm test` | 状态：待执行

---

## 二、执行框回写记录

*(执行框完成后，在此填写实际完成情况和遗漏说明)*

---

## 三、SCO 核查结论（2026-04-16）

**已确认完成**：4项（人力管理页面、日常运营页面、两个侧边栏导航项）
**确认未完成**：6项（文件中心全部相关项）
**待执行框确认**：10项（数据库表、后端路由，因截图显示页面存在但代码未见，需执行框说明实现方式）

**补丁指令**：见指令包文档第一章「高优先级补丁指令」。
