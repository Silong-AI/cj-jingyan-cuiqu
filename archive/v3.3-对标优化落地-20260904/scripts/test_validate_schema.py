# -*- coding: utf-8 -*-
"""回归测试：validate_skill_pack.py 的 Schema 校验应能拦截非法 manifest（负向测试）。
用法: python scripts/test_validate_schema.py
预期: 注入非法 level 后校验输出 FAIL 且含 '不符合 Schema'，否则退出码非 0。"""
import shutil, os, subprocess, sys

base = r'C:\Users\caiji\AppData\Local\DoubaoWork\User Data\Default\.doubaowork\agent_mode\workspace\.user_skills\cj-jingyan-cuiqu'
src = os.path.join(base, 'examples', 'demo-新客开发-销冠技能包')
tmp = os.path.join(base, '_tmp_eval_test')
if os.path.exists(tmp):
    shutil.rmtree(tmp)
shutil.copytree(src, tmp)

# 故意改坏 manifest：level 用非法值 + 缺 entry.description
mp = os.path.join(tmp, 'skill-pack.yaml')
txt = open(mp, encoding='utf-8').read()
txt = txt.replace('level: "牛招"', 'level: "超牛"')
txt = txt.replace('  description: "处理新客开发相关问题：从陌生线索到首次成交的完整打法"', '')
open(mp, 'w', encoding='utf-8').write(txt)
print('已注入错误：非法 level(超牛) + 缺 entry.description')

# 用 anaconda python（有 yaml+jsonschema）运行校验
code = subprocess.run(
    [r'd:\anaconda\python.exe', os.path.join(base, 'scripts', 'validate_skill_pack.py'), tmp],
    capture_output=True, text=True, encoding='utf-8')
print(code.stdout)
print('退出码:', code.returncode)

# 断言：应当 FAIL
if 'FAIL' in code.stdout and '不符合 Schema' in code.stdout:
    print('>>> 反向验证通过：Schema 校验成功拦截了非法 manifest')
    ok = True
else:
    print('>>> 反向验证失败：未按预期拦截')
    ok = False

shutil.rmtree(tmp, ignore_errors=True)
print('临时目录已清理')
sys.exit(0 if ok else 1)
