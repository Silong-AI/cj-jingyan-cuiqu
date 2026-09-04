#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_evals.py — CJ·经验萃取 触发评测运行器（对齐 cangjie-skill 的 run_trigger_evals 思想）

用法:
    python run_evals.py --check            # 校验 tests/eval_set.json 结构合法
    python run_evals.py --report <out.md>  # 生成 EVAL_REPORT 模板（含期望值，供人工/模型回填实际）
    python run_evals.py --grade <actual.json>  # 读取实际结果，对比期望，自动判定 PASS/FAIL

--grade 需要 actual.json 格式（每个用例回填 expect_trigger 的实测结果）:
    [{"id": "T1", "actual_trigger": true, "actual_route": "组织模式"}, ...]

每次改版后跑 --grade 记录基线；基线报告存 tests/EVAL_BASELINE.md。
"""
import json
import os
import sys

REQUIRED = ["id", "prompt", "expect_trigger", "expect_route"]


def load_set(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def check(path):
    """校验评测语料结构：10 例、id 唯一、字段齐全、trigger 类型正确。"""
    fails = []
    data = load_set(path)
    tests = data.get("tests", [])
    if not tests:
        return ["tests 为空"]
    ids = [t["id"] for t in tests]
    if len(ids) != len(set(ids)):
        fails.append("存在重复 id")
    if len(tests) < 10:
        fails.append(f"测试例数 {len(tests)} < 10")
    for t in tests:
        for k in REQUIRED:
            if k not in t:
                fails.append(f"{t.get('id','?')} 缺少字段: {k}")
        if not isinstance(t.get("expect_trigger"), bool):
            fails.append(f"{t.get('id','?')} expect_trigger 必须是布尔值")
    # 必须包含正例与负例
    trig = sum(1 for t in tests if t.get("expect_trigger"))
    neg = len(tests) - trig
    if trig == 0 or neg == 0:
        fails.append("必须同时包含正例（触发）与负例（不触发）")
    return fails


def render_report(data, actual=None):
    """生成 EVAL_REPORT.md 内容。actual: {id: {actual_trigger, actual_route}}"""
    lines = ["# EVAL_REPORT — CJ·经验萃取 触发评测",
             "",
             f"> 语料: `tests/eval_set.json`（{len(data['tests'])} 例）· 运行时间: 见脚本输出",
             "",
             "| # | 输入 | 应触发 | 应分流 | 实测触发 | 实测分流 | 判定 |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    all_pass = True
    for t in data["tests"]:
        a = (actual or {}).get(t["id"], {})
        got_t = a.get("actual_trigger")
        got_r = a.get("actual_route", "")
        if got_t is None:
            verdict = "待测"
            all_pass = False
        else:
            ok = (got_t == t["expect_trigger"]) and (
                got_t is False or got_r == t["expect_route"])
            verdict = "✅" if ok else "❌"
            if not ok:
                all_pass = False
        lines.append(
            f"| {t['id']} | {t['prompt'][:22]} | {'✅' if t['expect_trigger'] else '❌'} "
            f"| {t['expect_route']} | {('✅' if got_t else '❌') if got_t is not None else '—'} "
            f"| {got_r or '—'} | {verdict} |")
    summary = "全部通过，可交付" if all_pass else ("存在失败项，需回炉" if any(
        (actual or {}).get(t["id"], {}).get("actual_trigger") is not None for t in data["tests"]) else "待评测")
    lines += ["", f"**结论**: {summary}", ""]
    return "\n".join(lines), all_pass


def grade(actual_path, eval_path):
    """读取实际结果，对比期望，写 EVAL_BASELINE.md。"""
    with open(actual_path, encoding="utf-8") as f:
        actual_list = json.load(f)
    actual = {a["id"]: a for a in actual_list}
    data = load_set(eval_path)
    report, ok = render_report(data, actual)
    base_dir = os.path.dirname(eval_path)
    out = os.path.join(base_dir, "EVAL_BASELINE.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[{'PASS' if ok else 'FAIL'}] 基线已写入 {out}")
    return 0 if ok else 1


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    mode = sys.argv[1]
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    eval_path = os.path.join(base, "tests", "eval_set.json")
    if not os.path.isfile(eval_path):
        print(f"FAIL: 未找到 {eval_path}")
        return 1
    if mode == "--check":
        fails = check(eval_path)
        if fails:
            print("FAIL:")
            for f in fails:
                print("  -", f)
            return 1
        data = load_set(eval_path)
        trig = sum(1 for t in data["tests"] if t["expect_trigger"])
        print(f"[PASS] 语料合法：{len(data['tests'])} 例（正例 {trig} / 负例 {len(data['tests'])-trig}）")
        return 0
    if mode == "--report":
        data = load_set(eval_path)
        report, _ = render_report(data)
        out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(base, "tests", "EVAL_REPORT.md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"[OK] 报告模板已生成: {out}")
        return 0
    if mode == "--grade":
        if len(sys.argv) < 3:
            print("用法: run_evals.py --grade <actual.json>")
            return 2
        return grade(sys.argv[2], eval_path)
    print(f"未知模式: {mode}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
