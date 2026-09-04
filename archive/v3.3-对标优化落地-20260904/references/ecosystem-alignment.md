# 生态对齐规范（Ecosystem Alignment）—— CJ·经验萃取 v2.2

让 CJ 萃取产出的"团队技能包"**能被社区生态识别、调用、进化**，而不是孤立的文档。对齐对象：Agent Skills 开放规范（Claude Code / Codex 等）、nuwa-skill（人物 Skill 规范）、cangjie-skill / darwin-skill（能力卡 + 评测用例规范）。

## 一、核心原则

1. **机器可读**：每个技能包必须有一份 `skill-pack.yaml`（结构化清单），让工具/脚本能解析。
2. **稳定标识**：每条打法有固定 `capability_id`，跨版本不变（改名只增新 ID，不删旧 ID）。
3. **前端可触发**：每个"打法卡"或"入口"的 SKILL.md 必须遵循 Agent Skills frontmatter 规范（`name` + `description` 触发词）。
4. **可进化**：技能包附带 `test-prompts.json` 评测用例，可喂给 darwin 类工具自动进化。

## 二、技能包 manifest（skill-pack.yaml）

每个团队技能包根目录放一份 `skill-pack.yaml`：

```yaml
# skill-pack.yaml
schema_version: "1.0"
pack_id: "xj-sp-20260904-xinkehai"        # 稳定包 ID（品牌+年份+场景）
name: "新客开发"                           # 技能包名称
type: "team-skill-pack"                    # 类型标识（团队技能包）
industry: "B2B销售"                        # 适用行业
generated_by: "CJ·经验萃取 v2.1"           # 生成工具
generated_at: "2026-09-04"

# 触发入口（供 Agent 识别）
entry:
  name: "xinkehai-entry"
  description: "处理新客开发相关问题：从陌生客户到首次成交的完整打法"

# 打法清单（每条一个 capability_id）
capabilities:
  - id: "xkh-001-seed"
    name: "种子陪建法"
    level: "牛招"                          # 基操/方法/牛招/心法/边界
    trigger: "如何让客户愿意深度参与"
  - id: "xkh-002-probe"
    name: "需求探针三问"
    level: "方法"
    trigger: "如何挖出客户真实需求"

# 验证状态
verification:
  v1_cross_domain: true
  v2_predictive: true
  v3_unique: true

# 生态兼容
compatible_with:
  - "claude-code"
  - "codex"
  - "npx-skills"
  - "darwin-skill"
```

> **★v2.2 manifest 深度校验**：`skill-pack.yaml` 须通过 `schemas/skill-pack.schema.json`（JSON Schema）校验——`level` 只能是"基操/方法/牛招/心法/边界"，`capabilities` 每项必含 `id`/`file` 且对应文件存在，`pack_id` 必须小写连字符。校验由 `scripts/validate_skill_pack.py` 执行（缺 jsonschema 库时降级为基础字段检查并提示）。回归测试：`scripts/test_validate_schema.py`。

## 二·五、打法索引自动生成（★v2.2）

打法库的"打法索引.md"不手写，由 `scripts/generate_index.py` 自动生成：扫描 `打法库/*.md`，读取每张卡的 frontmatter 注释（`capability_id` / `level`）与"一句话"，汇总成总览表。每次新增/修改打法卡后重跑一次即可，保证索引与卡片不脱节。

## 三、打法卡 → 能力卡（对齐 cangjie 的 RIA 卡）

每张打法卡建议对齐社区"能力卡"结构，让第三方可识别其意图与边界：

```markdown
# 打法：种子陪建法
<!-- capability_id: xkh-001-seed -->
<!-- level: 牛招 -->

## 一句话（一句话SOP）
如果（要冷启动新客）…切忌（把客户当"捧场"的）…那么就（邀约当"联创"深度参与）…避开（被动等待）…从而（获得种子客户）

## 适用 / 边界
- 适用：新客开发早期 / 种子用户获取
- 不适用：成熟期放量阶段

## 可执行步骤（E）
1. ...（动作级）
2. ...

## 边界与反例（B）
- 失效条件：...
- 反例：...

## 验证（Evidence）
- 指标：... | 来源：...

## 评测用例（对齐 darwin）
```json
{"id":"xkh-001","prompt":"客户说'我再考虑考虑'，如何推进","expect":"...","type":"trigger"}
```
```

## 四、评测用例格式（对齐 darwin-skill）

在技能包根目录放 `test-prompts.json`，格式对齐 darwin / cangjie 评测：

```json
{
  "pack_id": "xj-sp-20260904-xinkehai",
  "tests": [
    {
      "id": "xkh-t01",
      "type": "trigger",
      "prompt": "客户说要考虑一下，怎么推进成交？",
      "expect_trigger": "xkh-001-seed",
      "expect_keywords": ["预约具体时间", "留钩子"]
    },
    {
      "id": "xkh-t02",
      "type": "boundary",
      "prompt": "这个种子陪建法在放量阶段还适用吗？",
      "expect_trigger": "xkh-002-probe",
      "expect_boundary": "不适用，应切换放量打法"
    }
  ]
}
```

## 五、安装与分发（对齐 npx 生态）

- 技能包目录 = 一个可整体复制/分发的单元（**自包含**：不依赖外部文件，复制整个目录即独立可用）。
- 建议提供一键安装说明（README 内）：如何放入 Claude Code 的 `~/.claude/skills/`、Codex 的 skills 目录，或通过 `npx skills add` 发布。
- 每个打法卡的 frontmatter 遵循 Agent Skills 规范：`name` + `description`（含明确触发词 + "不在一般性问题上自动触发"防呆）。

## 六、与社区三件套的分工定位（README 叙事用）

| 生态工具 | 蒸馏对象 | CJ 的对齐点 |
| --- | --- | --- |
| nuwa-skill | 人的思维 | CJ 产出的人物经验手册可对齐其 perspective Skill 结构 |
| cangjie-skill | 书/视频的方法论 | CJ 的打法卡对齐其 RIA 能力卡 + verified 清单 |
| darwin-skill | 进化任意 skill | CJ 技能包附 test-prompts.json，可直接喂 darwin 进化 |
| **CJ·经验萃取** | **组织内高手的打法** | **产出：团队技能包（给组织用）** |

> 一句话定位：nuwa 蒸人、cangjie 蒸书、darwin 进化，**CJ 蒸组织内的高手，把经验变成团队可训练、可验证、可进化的资产**。
