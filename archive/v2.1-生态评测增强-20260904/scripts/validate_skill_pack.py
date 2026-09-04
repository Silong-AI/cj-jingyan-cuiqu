#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_skill_pack.py — CJ·经验萃取 技能包结构校验器
对标 cangjie-skill 的 validate_skill_pack.py：交付前自动检查技能包结构是否合规。

用法:
    python validate_skill_pack.py <技能包目录>

检查项:
    1. 必要文件齐全: README.md / skill-pack.yaml / DIGEST.md / test-prompts.json / 干法库/
    2. skill-pack.yaml 为有效 YAML 且含 pack_id / capabilities
    3. 干法库每张卡含: capability_id / level / 一句话SOP / 适用 / 验证
    4. test-prompts.json 为有效 JSON 且 tests 非空
    5. manifest 中声明的干法文件实际存在
输出: PASS / FAIL 逐项报告，任一 FAIL 返回非 0 退出码。
"""
import json
import os
import re
import sys

REQUIRED_FILES = ["README.md", "skill-pack.yaml", "DIGEST.md", "test-prompts.json"]
CARD_REQUIRED = ["一句话", "适用", "不适用", "验证", "capability_id", "level"]


def check_required_files(root):
    fails = []
    for f in REQUIRED_FILES:
        if not os.path.isfile(os.path.join(root, f)):
            fails.append(f"缺少必要文件: {f}")
    dry = os.path.join(root, "干法库")
    if not os.path.isdir(dry):
        fails.append("缺少干法库/ 目录")
    return fails


def check_yaml(root):
    fails = []
    yp = os.path.join(root, "skill-pack.yaml")
    if not os.path.isfile(yp):
        return ["skill-pack.yaml 不存在"]
    txt = open(yp, encoding="utf-8").read()
    if "pack_id:" not in txt or "capabilities:" not in txt:
        fails.append("skill-pack.yaml 缺少 pack_id 或 capabilities 字段")
    # 尝试用 yaml 库深度校验
    try:
        import yaml
        data = yaml.safe_load(txt)
        if not data.get("pack_id"):
            fails.append("pack_id 为空")
        caps = data.get("capabilities") or []
        if not isinstance(caps, list) or not caps:
            fails.append("capabilities 为空")
        else:
            for c in caps:
                if not c.get("id") or not c.get("file"):
                    fails.append("存在缺少 id 或 file 的干法声明")
                elif not os.path.isfile(os.path.join(root, c["file"])):
                    fails.append(f"manifest 声明的干法文件不存在: {c['file']}")
    except ImportError:
        # 无 yaml 库时仅做基础存在性检查
        print("[info] PyYAML 未安装，跳过 manifest 深度校验（结构字段已检查）")
    except Exception as e:
        fails.append(f"skill-pack.yaml 解析失败: {e}")
    return fails


def check_cards(root):
    fails = []
    dry = os.path.join(root, "干法库")
    if not os.path.isdir(dry):
        return ["干法库/ 目录不存在"]
    md_files = [f for f in os.listdir(dry) if f.endswith(".md")]
    if not md_files:
        return ["干法库/ 为空"]
    for f in md_files:
        txt = open(os.path.join(dry, f), encoding="utf-8").read()
        for kw in CARD_REQUIRED:
            if kw not in txt:
                fails.append(f"干法卡 {f} 缺少: {kw}")
    return fails


def check_json(root):
    fails = []
    jp = os.path.join(root, "test-prompts.json")
    if not os.path.isfile(jp):
        return ["test-prompts.json 不存在"]
    try:
        data = json.load(open(jp, encoding="utf-8"))
        if not data.get("tests"):
            fails.append("test-prompts.json 的 tests 为空")
    except Exception as e:
        fails.append(f"test-prompts.json 解析失败: {e}")
    return fails


def main():
    if len(sys.argv) < 2:
        print("用法: python validate_skill_pack.py <技能包目录>")
        return 2
    root = sys.argv[1]
    if not os.path.isdir(root):
        print(f"FAIL: 目录不存在 {root}")
        return 1

    checks = {
        "必要文件": check_required_files(root),
        "manifest": check_yaml(root),
        "干法卡": check_cards(root),
        "评测用例": check_json(root),
    }
    ok = True
    print(f"=== 技能包校验: {os.path.basename(root)} ===")
    for name, fails in checks.items():
        if fails:
            ok = False
            print(f"[FAIL] {name}:")
            for f in fails:
                print(f"       - {f}")
        else:
            print(f"[PASS] {name}")
    print("=== 结果:", "PASS 可交付" if ok else "FAIL 需回炉", "===")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
