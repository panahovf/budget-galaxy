# Writes one plain-text file per budget chapter with every measure numbered, its section, cost, word count and full text:
# the files used to read each measure before giving it a category (step 3).
#
#   python tools/reading_files.py <folder for the files>        (run from the top of the repository)
#
# A file is named <year>_<page>.txt (e.g. 2026_chap3.txt); measure [n] is the n-th measure of that page in data/measures.csv,
# the number tools/add_decisions.py expects.
import os
import sys

import pandas as pd

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
M = pd.read_csv("data/measures.csv")
for (year, page), x in M.groupby(["year", "page"], sort=False):
    lines = [f"##### {year} {page} — {x['chapter'].iloc[0]} ({len(x)} measures, {int(x['words'].sum()):,} words)"]
    for n, r in enumerate(x.itertuples()):
        money = "no cost row" if pd.isna(r.money_b) else f"${r.money_b:,.3f}B"
        section = r.section if isinstance(r.section, str) else ""
        flags = ("  |  TABLE-ONLY" if r.source == "table" else "") + ("  |  box" if r.box else "")
        lines.append(f"\n[{n}] {r.heading}  |  {section}  |  {money}  |  {r.words} words{flags}")
        lines.append(r.text if isinstance(r.text, str) else "(no text)")
    with open(os.path.join(out, f"{year}_{page.replace('-en.html', '')}.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
print(f"{len(M):,} measures in {M.groupby(['year', 'page']).ngroups} files, in {out}")
