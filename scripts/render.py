"""Render README.md from data/projects.tsv and data/sections.tsv.

    python3 scripts/render.py
"""
import csv, re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(name):
    with open(ROOT / "data" / name, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def slug(text, seen):
    s = re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")
    n = seen.get(s, 0); seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def stars(n):
    n = int(n)
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


sections = read("sections.tsv")     # area, sub_id, subcategory, intro (in display order)
projects = read("projects.tsv")     # repo, sub_id, stars, created, archived, blurb[, review_note]
review = [p for p in projects if p.get("review_note")]
projects_main = [p for p in projects if not p.get("review_note")]
names = {s["sub_id"]: s["subcategory"] for s in sections}
by_sub = defaultdict(list)
for p in projects_main:
    by_sub[p["sub_id"]].append(p)

areas = []
for s in sections:
    if not areas or areas[-1][0] != s["area"]:
        areas.append((s["area"], []))
    areas[-1][1].append(s)

seen, toc, body = {}, [], []
for area, subs in areas:
    subs = [s for s in subs if by_sub[s["sub_id"]]]
    if not subs:
        continue
    total = sum(len(by_sub[s["sub_id"]]) for s in subs)
    toc.append(f"- [{area}](#{slug(area, seen)}) ({total})")
    body += [f"## {area}", ""]
    for s in subs:
        items = sorted(by_sub[s["sub_id"]], key=lambda p: -int(p["stars"]))
        toc.append(f"  - [{s['subcategory']}](#{slug(s['subcategory'], seen)}) ({len(items)})")
        body += [f"### {s['subcategory']}", "", s["intro"], "",
                 "| Project | Stars | Created | Description |", "|---|--:|---|---|"]
        for p in items:
            flag = " (archived)" if p["archived"] == "true" else ""
            body.append(f"| [{p['repo']}](https://github.com/{p['repo']}){flag} | {stars(p['stars'])} | {p['created']} | {p['blurb'].replace('|', '/')} |")
        body.append("")

if review:
    toc.append(f"- [Needs review](#{slug('Needs review', seen)}) ({len(review)})")
    body += ["## Needs review", "",
             "Projects I couldn't confidently describe or categorize yet. Each has a best-guess section and the reason it's here.", "",
             "| Project | Stars | Created | Best guess | Description | Why it's here |", "|---|--:|---|---|---|---|"]
    for p in sorted(review, key=lambda p: -int(p["stars"])):
        flag = " (archived)" if p["archived"] == "true" else ""
        body.append(f"| [{p['repo']}](https://github.com/{p['repo']}){flag} | {stars(p['stars'])} | {p['created']} | "
                    f"{names.get(p['sub_id'], p['sub_id'])} | {p['blurb'].replace('|', '/')} | {p['review_note'].replace('|', '/')} |")
    body.append("")

head = [
    "# Awesome AI", "",
    f"A personal, categorized index of {len(projects)} AI projects I've starred: agent frameworks, coding agents, "
    "skills, sandboxes, memory and retrieval, tools, and models. Each section is sorted by GitHub stars.", "",
    f"_Last generated {date.today().isoformat()}. Star counts are a snapshot._", "",
    "## Contents", "", *toc, "",
]
(ROOT / "README.md").write_text("\n".join(head + body))
print(f"README.md: {len(projects)} projects, {sum(1 for a, s in areas for x in s if by_sub[x['sub_id']])} sections")
