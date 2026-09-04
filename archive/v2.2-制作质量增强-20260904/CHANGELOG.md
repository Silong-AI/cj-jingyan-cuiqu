# CJ·经验萃取 · 变更日志（CHANGELOG）

> 版本管理约定：每次迭代把上一版完整复制进 `archive/vX.X-名称-日期/`，再在根目录升级新版。

## v2.2（制作质量增强）— 2026-09-04

基于制作质量维度的竞品对比（vs cangjie / nuwa），补齐 5 个差距 + 1 个隐藏隐患。v2.1 完整归档于 `archive/v2.1-生态评测增强-20260904/`。

**新增**
- `references/fallback-matrix.md`：失败降级表——对话式萃取 11 个高频卡壳场景的"触发条件→一线修复→仍失败兜底"预案（对标 nuwa 的失败降级表）。
- `schemas/skill-pack.schema.json`：`skill-pack.yaml` 的 JSON Schema 深度校验规范（level 枚举 / capabilities 必填 / pack_id 格式）。
- `scripts/generate_index.py`：干法库索引自动生成脚本（读干法卡 frontmatter 汇总为"干法索引.md"）。
- `scripts/test_validate_schema.py`：Schema 校验回归测试（负向验证：非法 manifest 必须被拦截）。
- `references/trigger-evals.md` 新增 **1.2 萃取师 Voice Check**：对话质量 6 项验证（追问自然度/对抗认知闭合/菜单设计/话术具体性/挖掘推进/金句保留），检验"追问像不像专业萃取师"。

**增强**
- `SKILL.md`：**精简 frontmatter description**（约 600→200 字，降每 session token 消耗、防长尾关键词误触发，触发词收敛到核心）；质量红线新增第 8 条（**回炉上限**：每技能包最多回炉 2 次，不无限打磨）、第 9 条（**知情同意与数据安全**：当事人授权 / 脱敏 / 发布过审）；何时使用新增 fallback-matrix、Voice Check、generate_index 引用。
- `scripts/validate_skill_pack.py`：新增 **JSON Schema 深度校验**（jsonschema 缺失时降级为基础字段检查并提示）。
- `references/ai-assist.md`：注意事项补"知情同意"条目。
- `references/skill-pack-template.md`：v2.2 工程化校验说明（Schema / 索引自动生成 / 回归测试）。
- `references/ecosystem-alignment.md`：manifest 深度校验 + 干法索引自动生成小节。

**验证**
- `generate_index.py` 在 demo 技能包实测：生成 3 张干法卡的索引 ✓
- `validate_skill_pack.py`（含 Schema）在 demo 技能包实测：四项全 PASS ✓
- `test_validate_schema.py` 负向测试实测：注入非法 level 被 Schema 拦截 → FAIL ✓

## v2.1（生态与评测增强）— 2026-09-04

**新增**
- `references/trigger-evals.md`：触发评测协议（10 例触发测试集 + 流程评测点 + 干法卡 10 分制 + 技能包 7 项清单 + 回炉规则），把质量红线落地为可执行评测。
- `references/ecosystem-alignment.md`：生态对齐规范（`skill-pack.yaml` manifest、稳定 `capability_id`、Agent Skills frontmatter、`test-prompts.json` darwin 兼容），让技能包被 Claude Code / Codex / npx / darwin 识别。
- `scripts/validate_skill_pack.py`：技能包结构自动校验脚本（必要文件 / manifest / 干法卡 / 评测用例，PASS-FAIL 报告）。
- `examples/demo-新客开发-销冠技能包/`：完整案例 demo（示例数据）——B2B 销冠「新客开发」经验 → 团队技能包，演示 v2.1 全流程（分流→定向→萃→验→用 + 生态对齐）。

**增强**
- `references/skill-pack-template.md`：技能包结构加入 `skill-pack.yaml` 与 `test-prompts.json`。
- `SKILL.md`：何时使用新增 4 条引用；质量红线新增第 7 条"交付前必须跑评测"；版本历史更新。

## v2.0（CJ·经验萃取）— 2026-09-04

基于竞品对比分析（cangjie「仓颉」/ nuwa「女娲」），吸收"工程化、验证门禁、产品化体验、可演示产物"思路，完整保留 v1.0 方法论。主流程升级为 **定→萃→验→用**。

**新增**
- `references/entry-routing.md`：入口分流 / 场景诊断 / 档位管理 / 4 个检查点 / 断点续跑。
- `references/extraction-state-machine.md`：五层状态机（基操→方法→牛招→心法→边界）、牛招 5 判据、追问判停条件、对抗认知闭合自动触发。
- `references/verification-gates.md`：三重验证门禁（V1/V2/V3）、成果校验清单、落地验证协议（A/B 对照、SOP 可用性测试、冲突仲裁、经验过期检测）。
- `references/skill-pack-template.md`：可安装团队技能包（干法库 + 成果物 + 训练包 + 验证包 + DIGEST）。

**命名**：`jingyan-cuiqu` → `cj-jingyan-cuiqu`（CJ·经验萃取）。

## v1.0（基础版）— 原始版

完整归档于 `archive/v1.0-基础版-20260904/`。
