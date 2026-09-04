#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_index.py — CJ·经验萃取 打法库索引自动生成器
扫描技能包的 打法库/*.md，读取每张打法卡 frontmatter 注释与标题，
自动生成"打法索引.md"总览表（ID | 打法名 | 层级 | 验证 | 一句话）。

用法:
    python generate_index.py <技能包目录>

输出:
    写入 <技能包目录>/打法库/打法索引.md（若已存在则覆盖更新）
"""
import os
import re
import sys


def parse_card(path):
    """从打法卡提取: id / level / verification / 标题 / 一句话"""
    try:
        txt = open(path, encoding="utf-8").read()
    except Exception as e:
        return None, f"读取失败: {e}"

    def grab(pat):
        m = re.search(pat, txt)
        return m.group(1).strip() if m else ""

    cid = grab(r"capability_id:\s*([\w\-]+)")
    level = grab(r"level:\s*([\w]+)")
    ver = grab(r"verification:\s*([\w\s✓✗]+)")
    title = grab(r"^#\s*(.+)$", ) if False else ""
    m = re.search(r"^#\s*(.+)$", txt, re.M)
    title = m.group(1).strip() if m else os.path.basename(path)
    one = ""
    m2 = re.search(r"\*\*一句话(?:\（一句话SOP\）)?\*\*\s*[:：]?\s*(.+)", txt)
    if m2:
        one = m2.group(1).strip()
    return {"id": cid, "level": level, "ver": ver, "title": title, "one": one}, None


def main():
    if len(sys.argv) < 2:
        print("用法: python generate_index.py <技能包目录>")
        return 2
    root = sys.argv[1]
    dry = os.path.join(root, "打法库")
    if not os.path.isdir(dry):
        print(f"FAIL: 未找到打法库目录 {dry}")
        return 1

    cards = []
    for f in sorted(os.listdir(dry)):
        if not f.endswith(".md") or f == "打法索引.md":
            continue
        info, err = parse_card(os.path.join(dry, f))
        if err:
            print(f"[warn] {f}: {err}")
            continue
        cards.append((f, info))

    lines = ["# 打法索引（自动生成）", "",
             "> 本表由 `scripts/generate_index.py` 自动生成，请勿手改。",
             "", "| ID | 打法 | 层级 | 验证 | 一句话 |", "| --- | --- | --- | --- | --- |"]
    for f, c in cards:
        lines.append(
            f"| {c['id'] or '—'} | {c['title']} | {c['level'] or '—'} "
            f"| {c['ver'] or '—'} | {c['one'][:50] or '—'} |"
        )
    out = os.path.join(dry, "打法索引.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"[OK] 已生成 {out}（{len(cards)} 张打法卡）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
