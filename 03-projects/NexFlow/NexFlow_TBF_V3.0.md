# NexFlow V3.0 任务目标基线文件（TBF）

> **版本**：V3.0
> **指令包文件**：`nexflow_v3_0_final.md`
> **创建时间**：2026-04-16
> **最后核查时间**：2026-04-16（SCO 二次核查）

---

## 一、核查清单

### 模块一：人力管理（/hr）

- [x] `HR.tsx` 页面存在，含证件管理/培训记录/排班原则三 Tab | 验证：截图确认 | 状态：已完成
- [ ] `hr_certificates` 表已建立 | 验证：`SHOW TABLES LIKE 'hr_%'` | 状态：❌ 未完成（代码库中未见相关表定义）
- [ ] `hr_trainings` 表已建立 | 验证：`SHOW TABLES LIKE 'hr_%'` | 状态：❌ 未完成（代码库中未见相关表定义）
- [ ] `hr_schedule_principles` 表已建立 | 验证：`SHOW TABLES LIKE 'hr_%'` | 状态：❌ 未完成（代码库中未见相关表定义）
- [ ] `server/routers/hr.ts` 存在且注册至 `routers.ts` | 验证：代码检查 | 状态：❌ 未完成（路由文件不存在）
- [ ] 证件附件上传字段 `attachmentUrl` 存在 | 验证：`schema.ts` | 状态：❌ 未完成
- [ ] 培训证书附件字段 `attachmentUrl` 存在 | 验证：`schema.ts` | 状态：❌ 未完成
- [ ] 证件到期预警（30天内橙色标记）功能正常 | 验证：截图 | 状态：❌ 未完成

### 模块二：日常运营（/daily-ops）

- [x] `DailyOps.tsx` 页面存在，含运营日志/巡检记录/交接班三 Tab | 验证：截图确认 | 状态：已完成
- [ ] `ops_logs` 表已建立 | 验证：`SHOW TABLES LIKE 'ops_%'` | 状态：❌ 未完成（代码库中未见相关表定义）
- [ ] `ops_inspections` 表已建立 | 验证：`SHOW TABLES LIKE 'ops_%'` | 状态：❌ 未完成（代码库中未见相关表定义）
- [ ] `ops_handovers` 表已建立 | 验证：`SHOW TABLES LIKE 'ops_%'` | 状态：❌ 未完成（代码库中未见相关表定义）
- [ ] `server/routers/dailyOps.ts` 存在且注册 | 验证：代码检查 | 状态：❌ 未完成（路由文件不存在）
- [ ] 交接班接班人身份校验功能正常 | 验证：截图 | 状态：❌ 未完成

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
- [ ] 全量测试通过（vitest） | 验证：`pnpm test` | 状态：❌ 未完成（vitest 未安装或未运行成功）

---

## 二、执行框回写记录

**2026-04-16 核查记录**：
经拉取 `carefulxiao-cell/nexflow` 最新代码（commit `884adbc`）核查，发现：
1. **数据库层**：`drizzle/schema.ts` 及迁移文件中均未找到 `hr_`、`ops_`、`files` 相关表定义。
2. **后端层**：`server/routers/` 目录下不存在 `hr.ts`、`dailyOps.ts`、`files.ts`，且 `routers.ts` 中未注册相关路由。
3. **前端层**：`client/src/pages/` 目录下不存在 `HR.tsx`、`DailyOps.tsx`、`FileCenter.tsx`；`NexFlowLayout.tsx` 侧边栏导航项中未见「人力管理」、「日常运营」和「文件中心」；`App.tsx` 中未注册相关路由。
4. **测试层**：执行 `pnpm test` 失败，提示 `vitest: not found`。

**结论**：执行框尚未提交 V3.0 核心功能代码，或代码未推送到 `main` 分支。当前代码库仍停留在 V2.6 状态。

---

## 三、SCO 核查结论（2026-04-16）

**已确认完成**：0项（此前记录的4项在最新代码库中均未找到，状态回退为未完成）
**确认未完成**：20项（全部未完成）

**核查结论**：**V3.0 尚未交付**。
执行框需根据 `nexflow_v3_0_final.md` 和 `nexflow_v3_0_files_patch.md` 重新执行开发任务，并确保代码正确提交并推送到 GitHub 仓库的 `main` 分支。
