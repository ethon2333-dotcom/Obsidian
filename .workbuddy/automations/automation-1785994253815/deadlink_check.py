import os, re, sys

vault = r"C:\Users\Ethon\ObsidianVault\01-笔记"
new_files = [
    r"手机AI智能体\端侧 AI 功耗与散热约束 学习笔记.md",
    r"AI Agent 框架\Agent 可观测性 LLM Observability 学习笔记.md",
    r"知识管理与效率工具\低代码无代码 Agent 搭建平台 学习笔记.md",
    r"安全\端侧模型安全与越狱 学习笔记.md",
]

# gather existing note basenames (without .md)
existing = set()
for root, _, files in os.walk(vault):
    for f in files:
        if f.endswith(".md"):
            existing.add(f[:-3])

link_re = re.compile(r"\[\[([^\]]+?)\]\]")
dead = []
for rel in new_files:
    path = os.path.join(vault, rel)
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    for m in link_re.finditer(txt):
        target = m.group(1).split("|")[0].strip()
        if target not in existing:
            dead.append((rel, target))

if dead:
    print("DEAD LINKS FOUND:")
    for rel, t in dead:
        print(f"  [{rel}] -> [[{t}]]")
    sys.exit(1)
else:
    print("OK: 0 dead links across the 4 new notes.")
    # also count total links for info
    total = 0
    for rel in new_files:
        with open(os.path.join(vault, rel), encoding="utf-8") as fh:
            total += len(link_re.findall(fh.read()))
    print(f"Total wikilinks in new notes: {total}")
