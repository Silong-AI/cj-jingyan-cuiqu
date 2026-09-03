# Jingyan Cuiqu · 经验萃取（Experience Extraction Skill）

An AI skill that turns the tacit knowledge of top performers — sales champions, experts, veterans — into repeatable, trainable, verifiable assets. 把高手"会做但说不清"的经验，变成"看得见、学得会、用得着"的组织资产。

## Who is this for?

**For the people who hold the secret recipes.** 销售冠军、技术专家、老员工、销售团队的 Leader、HR / 培训负责人——你们知道谁能把事做成，但说不清他到底做对了什么。

这份 Skill 帮你把"人会做但说不清"的经验萃取出来：**不是记录故事，而是提炼可复制的干法**。

**You are not trying to write documents. You want the knowledge to leave the expert's head.** 你要的不是一份访谈纪要，而是一套新人照着做就能及格的方法论。

## What you get

- **个人模式**：萃一个人（销冠 / 专家 / 老员工 / 你自己），产出个人方法论、经验手册
- **组织模式**：萃一个团队（如销售），建标准动作库、SOP、课程、案例库，规模化复制
- **访谈问题库**：七段式访谈提纲 + 追问话术 + 深挖工具，直接拿着就能去问高手
- **封装模板**：一句话 SOP、口诀、模型、案例、工具（成果 7 步法）
- **AI 加速**：转写、聚类、建模草稿——让 AI 干重活，人来判断

## How to use

### As a skill

1. 把 `jingyan-cuiqu` 文件夹放到你的 Agent 的 skill 目录（如 `~/.claude/skills/`）
2. 对你的 Agent 说：
   - "帮我萃取这个销冠开发大客户的经验" → 走个人模式
   - "给我们销售团队做一套经验萃取和复制方案" → 走组织模式
   - "给我一份经验萃取访谈问题清单" → 调用访谈问题库
   - "把这段访谈封装成 SOP / 口诀" → 调用成果封装模板

### Trigger phrases

- 萃取经验 / 萃经验 / 高手经验 / 销冠方法论
- 组织经验萃取 / 知识沉淀 / 最佳实践提炼 / 岗位经验
- 把牛人经验变成组织能力 / 经验复制 / 复盘后萃取 / 内萃外取

## Design philosophy

### 经验 = 经历 + 干法 + 被验证

不萃取"我觉得能行"的设想，只萃取"做成过且有效"的经验。没有被验证过的东西，不叫经验。

### 挖细节，不挖观点

高手说不出"为什么成功"，但一定说得出"具体怎么做的"。追问方法 / 动作 / 工具 / 窍门，而不是问"你觉得成功的原因是什么"。

### 鲜活案例自带转化力

用 STAR / SCQA 还原真实场景，案例要有数据、有对标、有金句。案例是经验的载体，不是装饰。

### 萃取必有用，萃取之前必复盘

每次萃取都要回答"给谁用、解决什么问题"。复盘是找到真牛人、牛事、牛招的捷径——不盘不萃不会。

### 目标不是造明星，是让 80% 的人达到 60 分

组织萃取的目的是一群 60 分 > 三两个 90 分。让普通人的产能整体提升，而不是把希望押在个别高手身上。

## Skill structure

```
jingyan-cuiqu/
├── SKILL.md                        # 主流程：定 → 萃 → 用 + 标准四环 + 核心原则
└── references/
    ├── mode-individual.md          # 个人模式：萃一个人的全流程
    ├── mode-organization.md        # 组织模式：萃团队 + 训战复制（销售专项）
    ├── interview-question-bank.md  # 访谈问题库 + 追问话术 + 深挖工具 + 完整示范
    ├── packaging-templates.md      # 成果封装模板（SOP / 口诀 / 模型 / 案例）
    └── ai-assist.md                # AI 辅助萃取（6感模型 / 灵魂三问 / 训战模板）
```

Built by Jie Cai with Claude Code. 方法论框架源自 AACTP「经验萃取」全景案例大会（刘永中 / 叶敬秋 / 曾子亮 / 陈晓燕 / 周珊）。
