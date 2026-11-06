# Budget Galaxy

What does the budget say? Every measure in Canada's federal budgets 2022 to 2026, in three
views: the **Map** (how programs connect), **Gravity** (what each budget is made of) and **Priorities** (which themes are
rising up the list or falling off it). Part of [Farhad Panahov's website](https://panahovf.github.io).

## What's here

- `site/` is the web page, published at [panahovf.github.io/budget-galaxy](https://panahovf.github.io/budget-galaxy/).
  - `index.html`: the page.
  - `galaxy.json`: everything the page draws. Written by step 5 below; don't edit it by hand.
  - `og.png`: the preview picture shown when the link is shared: the Map, with the latest budget in colour (made from
    `tools/og.html`, see below).
- The five notebooks at the top, one per step, each saved with its output so its tables and checks can be read without
  running it; `data/` and `checks/` hold what they write, `manual/` the decisions made by hand.
- `.github/workflows/publish.yml` publishes `site/` on every push to `main`.

Budget 2021 is read and categorised too (steps 1 to 3), but the page leaves it out: it is used only for the money side of
Priorities, whose three-budget averages for 2022 and 2023 reach back to it. Step 4 maps Budgets 2022 to 2026 (`YEARS`), and
step 5 shows the same budgets (`SHOW`).

## Run it

With Python 3.9 and the versions pinned in `requirements.txt` (`pip install -r requirements.txt`), from this folder:

```bash
jupyter nbconvert --to notebook --execute --inplace 01_fetch_budgets.ipynb
jupyter nbconvert --to notebook --execute --inplace 02_read_measures.ipynb
jupyter nbconvert --to notebook --execute --inplace 03_categories.ipynb
jupyter nbconvert --to notebook --execute --inplace 04_language.ipynb
jupyter nbconvert --to notebook --execute --inplace 05_chart_data.ipynb
```

Running them again gives the same files: steps 2 to 5 were run twice on 2026-11-05 and every file in `data/` and
`checks/` came out identical.
Step 1 downloads only the pages not yet in `raw/` (set `REFRESH = True` in it to download everything again). The pages
themselves are not in the repository (`.gitignore`); `raw/sources.csv` keeps each page's address, size and fingerprint, so
a page that has changed on budget.canada.ca since shows up.

## The steps

| Notebook | What it does | Writes |
|---|---|---|
| `01_fetch_budgets` | Saves each budget's table of contents and chapter pages from budget.canada.ca | `raw/<year>/*.html`, `raw/sources.csv` |
| `02_read_measures` | Turns the pages into measures (heading, text, words) and places every row of every chapter cost table; checks that each table adds up to its published net fiscal impact | `data/measures.csv`, `data/cost_rows.csv`, `checks/reconciliation.csv`, `checks/matching.csv`, `checks/left_out.csv` |
| `03_categories` | Joins each measure to its category (decided by hand, `manual/categories.csv`) and checks that none is missing or unknown | `data/categorised.csv`, `data/category_list.csv` |
| `04_language` | Budgets 2022 to 2026: how alike the measures are worded (TF-IDF, 100 themes by SVD, cosine similarity), the map (t-SNE), each measure's closest earlier measures and novelty, each category's anchor | `data/language.csv`, `data/category_anchors.csv` |
| `05_chart_data` | Adds it all up the way each chart does (Budget 2021 only in the Priorities averages) | `data/category_year.csv`, `data/gravity.csv`, `data/priorities.csv`, `data/galaxy.json` and `site/galaxy.json` (what the page reads) |

The page calls the categories "themes".

## What is done by hand (`manual/`)

- `categories.csv`: the category of each of the 1,317 measures (Budgets 2021 to 2026), given after reading its full text,
  with a reason, and the category of the earlier policy it undoes, if it undoes one. The rules are in
  `category_guide.md`: a measure aimed only at Indigenous peoples goes to Indigenous; otherwise a measure goes where what
  it is for fits best, not how it is delivered; Taxation and Government hold only the tax system and the running of
  government, plus the money they raise or save; Other only when nothing else fits.
- `cost_matches.csv`: the 27 cost rows placed by hand (the name in the table differs too much from the heading, or the
  row belongs to a whole section or chapter), each with a note.

## Tools

- `tools/reading_files.py <folder>`: one text file per chapter with every measure numbered, its cost and its full text, for
  reading before deciding categories.
- `tools/add_decisions.py <year> <page> <file>`: adds the decisions for one chapter page (`n|CODE|reason`, one line per
  measure) to `manual/categories.csv`.
- `tools/og.html`: the preview picture. After changing it (or the data), render it again and raise the `?v=` number of
  `og:image` in `site/index.html`, so LinkedIn fetches the new picture:

  ```bash
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --allow-file-access-from-files --force-device-scale-factor=2 --window-size=1200,630 --virtual-time-budget=8000 --screenshot="$PWD/site/og.png" "file://$PWD/tools/og.html"
  ```

## Adding a budget

1. Add the year to `YEARS` in `01_fetch_budgets` and `02_read_measures`; run both. Check `checks/reconciliation.csv`; a
   row the matching can't place stops step 2 and goes in `manual/cost_matches.csv`.
2. Write the reading files, read the new budget's measures, and add the decisions page by page. Step 3 lists the measures
   still without a category and stops until there are none.
3. Add the year to `YEARS` in step 4 and `SHOW` in step 5, then run steps 3, 4 and 5. Step 4 draws the map again with the
   new measures, so every dot moves: the map stays the same on re-runs as long as the measures are the same.
4. Commit and push: the workflow publishes the new `site/galaxy.json`.

## Publishing

GitHub publishes the page (Settings → Pages → Source: GitHub Actions) with `.github/workflows/publish.yml`, on every push
to `main` and by hand from the Actions tab. It publishes `site/` as committed: nothing is recomputed online.

## The budgets at a glance

From `data/gravity.csv` (money: net, $ billions, over each cost table's five or six years). Budget 2021, for reference
(not on the page): 318 measures, 277 with a cost, $154.1B of new spending, $11.8B saved or raised, Affordability & social
support 28%.

| Budget | Measures | With a cost | New spending | Savings and money raised | Largest category | Label |
|---|---|---|---|---|---|---|
| 2022 | 203 | 159 | 64.5 | 27.0 | Indigenous, 16% | broad |
| 2023 | 209 | 161 | 73.7 | 27.8 | Health care, 43% | focused |
| 2024 | 292 | 227 | 59.7 | 24.9 | Defence & security, 20% | broad |
| 2025 | 118 | 86 | 143.8 | 54.2 | Defence & security, 43% | focused |
| 2026 | 177 | 141 | 147.7 | 5.6 | Trade, industry & competitiveness, 36% | focused |

Source: Department of Finance Canada, Budgets 2021 to 2026, budget.canada.ca.
