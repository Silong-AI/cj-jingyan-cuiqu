# CJ·Experience Extraction (CJ·经验萃取)

> Turn what "experts can do but can't explain" into reusable, trainable, verifiable assets — for individuals and organizations.

**One-line positioning**: nuwa distills **people**, cangjie distills **books/videos**, darwin evolves skills — **CJ distills "in-house experts"**, turning the tacit playbooks of top salespeople / experts / tenured employees into team skill packs that are **trainable, verifiable, and evolvable**.

![Ecosystem Position](assets/ecosystem-position.svg)

---

## What it is

**CJ·Experience Extraction** is an **Agent Skill** (built on the Agent Skills spec) that uses **dialogue-driven dynamic extraction** to distill expertise:

- **Dialogue-driven probing**: after each answer, present a menu of 2–5 numbered follow-up directions and let the expert choose — the deeper you ask, the deeper you extract.
- **Five-layer state machine**: 基操 (baseline) → 方法 (method) → 牛招 (killer move) → 心法 (mindset) → 边界 (boundary), to identify the moves only this expert has, and to converge.
- **Triple verification gates**: every extracted playbook passes V1 cross-domain replication / V2 predictive power / V3 uniqueness — or it is downgraded/rejected.
- **Validation protocol**: A/B pilots, SOP usability tests (can a newcomer follow it to 60 points?), conflict arbitration, and expertise-expiry detection.
- **Ship-to-use**: organizational extraction directly produces an **installable team skill pack** (playbook library + deliverables + training pack + validation pack + DIGEST).

**Use cases**
- Personal extraction: distill one expert's (or your own) success playbook in a domain → personal methodology / handbook.
- Organizational replication: pick a key business scenario (new-customer development, key-account sales, etc.), batch-extract from multiple top performers → standard action library / training course / team skill pack.

**Not for**: generic experience advice, knowledge Q&A without a specific expert, or celebrity role-play (that's nuwa's job).

---

## Quick Start

Once enabled in your agent, just say:

```
帮我萃一下我们销冠的成功经验          → organization mode
想把老王做单子那套方法整理出来        → individual mode
团队新人上手太慢，怎么办              → fuzzy need → scenario diagnosis
```

The skill then follows **Quick Start**:
1. **Scope**: entry routing → define scenario/person/audience/format + depth (quick/standard/deep)
2. **Extract**: five-layer state machine + probe menus, dig until baseline vs. killer move is clear
3. **Verify + Use**: triple verification gates → package via the "3-question selector" → organizational output becomes a team skill pack

Full flow: `SKILL.md` · Methodology: `references/`

---

## Repository Layout

```
cj-jingyan-cuiqu/
├── SKILL.md                    # Main doc: routing + main flow + quality red lines
├── README.md                   # This file (Chinese) · README.en.md (English)
├── LICENSE                     # MIT
├── CHANGELOG.md                # Version history
├── references/                 # Load-on-demand methodology (14 files)
├── scripts/                    # Engineering tools
│   ├── validate_skill_pack.py  # Skill-pack structure validation (+ JSON Schema)
│   ├── generate_index.py       # Auto-generate playbook index
│   ├── run_evals.py            # Trigger-eval runner (--check / --report / --grade)
│   └── test_validate_schema.py # Schema regression test
├── schemas/
│   └── skill-pack.schema.json
├── tests/
│   ├── eval_set.json           # Trigger-eval corpus (10 cases)
│   └── EVAL_BASELINE.md        # Regression baseline
├── examples/
│   └── demo-新客开发-销冠技能包/ # End-to-end demo (top-sales → team skill pack)
└── archive/                    # Versioned archives (v1.0 ~ current)
```

---

## Verification (benchmark)

Quality red line #7: **run evals before delivery**.

```bash
# 1. Validate skill-pack structure
python scripts/validate_skill_pack.py <skill-pack-dir>

# 2. Auto-generate playbook index
python scripts/generate_index.py <skill-pack-dir>

# 3. Trigger-eval corpus check + regression baseline
python scripts/run_evals.py --check
python scripts/run_evals.py --report
python scripts/run_evals.py --grade <actual_results.json>

# 4. Schema regression test
python scripts/test_validate_schema.py
```

---

## Version History

| Version | Theme | Notes |
| --- | --- | --- |
| v4.0 | Open-source release | LICENSE, bilingual README, ecosystem-position diagram, benchmark demo doc, publishing guide |
| v3.3 | Benchmark-driven polish | SKILL.md ↔ references de-dup (kill "undelegated details" smell), engineering-tool timing table, oral trigger phrases |
| v3.2 | Terminology unification | "干法" → "打法" across files, paths, scripts |
| v3.1 | Engineering (P1) | eval corpus + run_evals.py baseline, root README, version field |
| v3.0 | Structure | third-person description + guardrails, Quick Start, mini extraction example |
| v2.2 | Quality | Voice Check, fallback matrix, JSON Schema, index generation, rework cap, consent red line |
| v2.1 | Eval & ecosystem | trigger evals, ecosystem alignment, validate script, demo skill pack |
| v2.0 | Engineering | entry routing, state machine, triple verification, installable skill pack; renamed CJ·经验萃取 |
| v1.0 | Baseline | original extraction methodology |

Every version is fully archived under `archive/`. Full details in `CHANGELOG.md`.

---

## Ecosystem & Acknowledgements

- **Methodology**: AACTP "Experience Extraction" case conference; international & domestic experience-extraction methodologies.
- **Engineering benchmarks**: Anthropic Agent Skills guide; cangjie-skill (books), nuwa-skill (people), darwin-skill (evolution).
- **Alignment**: Agent Skills frontmatter, darwin eval-case format, installable skill-pack manifest.

## Author & License

**Author**: Jie Cai / 斯泷 — Founder, 青影纪元科技 (Qingying Era Technology); initiator of 青影星球AI community; AI PM / AI trainer.

© 2026 Jie Cai / 斯泷. Released under the **MIT License**. Free to use, modify, and redistribute (please keep the copyright and attribution).

- 公众号 (WeChat): 青影星球AI
- Built with 豆包工作 (Doubao Work)
