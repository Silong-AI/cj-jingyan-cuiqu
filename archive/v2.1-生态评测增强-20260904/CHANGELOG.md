# CJ·经验萃取 · 变更日志（CHANGELOG）

> 版本管理约定：每次迭代把上一版完整复制进 `archive/vX.X-名称-日期/`，再在根目录升级新版。

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
