# Adds the category decisions for one chapter page to manual/categories.csv (one row per measure, keyed by its id).
#
#   python tools/add_decisions.py <year> <page> <decisions file>        (run from the top of the repository)
#   e.g. python tools/add_decisions.py 2026 chap3-en.html decisions_2026_chap3.txt
#
# The decisions file has one line per measure of the page, numbered as in tools/reading_files.py:
#   n|CODE|reason              e.g.  4|CLI|heat pump rebates and deep building retrofits
#   n|CODE|reason|CODE2        a measure that reverses an earlier policy; CODE2 is the category of the policy it undoes
# Every measure of the page must be decided; a measure decided before is overwritten. Codes are below.
import csv
import os
import sys

import pandas as pd

CODES = {"HOU": "Housing", "AFF": "Affordability & social support", "HEA": "Health care",
         "TRD": "Trade, industry & competitiveness", "JOB": "Jobs, skills & immigration", "INF": "Infrastructure",
         "RES": "Research, AI & technology", "CUL": "Culture & communities", "NAT": "Nature & environment",
         "CLI": "Clean energy & climate", "TAX": "Taxation", "GOV": "Government", "DEF": "Defence & security",
         "IND": "Indigenous", "OTH": "Other"}
year, page, decisions = int(sys.argv[1]), sys.argv[2], sys.argv[3]
M = pd.read_csv("data/measures.csv")
x = M[(M["year"] == year) & (M["page"] == page)].reset_index(drop=True)
assert len(x), f"no measures for {year} {page}"
path = "manual/categories.csv"
cols = ["id", "year", "page", "heading", "money_b", "category", "reason", "reverses"]
rows = {r["id"]: r for r in csv.DictReader(open(path, encoding="utf-8"))} if os.path.exists(path) else {}
seen = set()
for line in open(decisions, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = [p.strip() for p in line.split("|")]
    n, code, reason = int(parts[0]), parts[1], parts[2]
    rev = parts[3] if len(parts) > 3 else ""
    assert code in CODES, f"unknown code {code}: {line}"
    assert not rev or rev in CODES, f"unknown reverses code {rev}: {line}"
    assert reason, f"no reason: {line}"
    r = x.iloc[n]
    rows[r["id"]] = {"id": r["id"], "year": year, "page": page, "heading": r["heading"],
                     "money_b": "" if pd.isna(r["money_b"]) else r["money_b"], "category": CODES[code], "reason": reason,
                     "reverses": CODES[rev] if rev else ""}
    seen.add(n)
missing = sorted(set(range(len(x))) - seen)
assert not missing, f"{year} {page}: no decision for measures {missing}"
order = {mid: i for i, mid in enumerate(M["id"])}                 # keep the file in step 2's order
out = sorted(rows.values(), key=lambda r: order.get(r["id"], 10 ** 9))
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(out)
print(f"{year} {page}: {len(seen)} decisions saved; {len(out)} rows in {path}")
