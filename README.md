# Video Game Sales Analytics (1971–2024)

An end-to-end data analysis project exploring 50+ years of global video game sales trends, platform dominance shifts, genre evolution, and a forward-looking forecast through 2027. Built entirely on iPad Air using cloud-based tools.

---

## Business Questions

1. How have global video game sales trended across five decades — and where did the peaks and declines occur?
2. Which genres dominated which eras, and which have declined as player preferences shifted?
3. How has regional market share (NA, Japan, EU) shifted since the 1980s — and when did NA pull decisively ahead?
4. Which publishers have consistently outperformed the market across multiple console generations?
5. What do 50+ years of sales patterns predict for the global market through 2027?

---

## Status

🚧 **In progress** — SQL analysis and Looker Studio dashboards underway

> Screenshots for Excel cleaning stages and dashboard exports will be added as each phase completes.

---

## Tools

| Layer | Tool |
|---|---|
| Data cleaning & forecasting | Excel (iPad) |
| SQL analysis | PostgreSQL via Supabase |
| Dashboards & visualization | Looker Studio |
| Version control & portfolio | GitHub |

---

## Dataset

**Video Game Sales 1971–2024** via [Maven Analytics](https://www.mavenanalytics.io/) (free)

64,016 titles across platforms, genres, publishers, and regional sales figures. Includes: NA, Japan, EU, and other regional sales, critic scores, and release years.

---

## Key Insights

> *Full insights will be finalized on project completion. Early findings below are directional and subject to revision.*

- **NA dominated global sales** throughout the 1990s–2000s, with Japan's market share declining steadily post-2010 as mobile gaming reshaped its domestic market
- **Action and Shooter genres** account for a disproportionate share of top-selling titles, particularly from 2005 onward — coinciding with the rise of online multiplayer
- **A small number of publishers** (Activision, EA, Rockstar, Nintendo) appear repeatedly in high-sales rankings across multiple decades and platforms, suggesting brand and franchise power outweighs novelty
- **Sales forecast through 2027** projects continued global growth, consistent with the broader market trajectory (the global gaming market was valued at ~$184B in 2023)

---

## Forecast Methodology

The 2027 sales projection uses **Excel's FORECAST.ETS function**, which applies exponential triple smoothing (ETS) to historical annual sales totals. This method accounts for trends and seasonal patterns in time series data. Inputs are aggregated yearly global sales figures from the cleaned dataset (1971–2024), with the model extrapolating forward three years.

> This is a statistical projection based on historical patterns — treat it as directional, not prescriptive.

---

## Live Dashboard

*Link will be added once dashboards are complete.*

---

## Project Structure

```
video-game-sales-analytics/
├── data/
│   ├── raw/          ← original Maven Analytics CSV
│   └── clean/        ← cleaned CSV exported from Excel
├── sql/
│   ├── 01_schema.sql
│   ├── 02_cleaning_queries.sql
│   └── 03_analysis_queries.sql
├── excel/
│   └── screenshots/  ← formulas, pivot tables, forecast sheet (coming soon)
└── dashboards/
    ├── screenshots/  ← Looker Studio dashboard exports (coming soon)
    └── LINKS.md      ← live share links
```

---

## How to Reproduce

1. Download raw CSV from `data/raw/` (or directly from Maven Analytics)
2. Apply Excel cleaning steps — see `excel/screenshots/` for each stage
3. Run `sql/` scripts in order against any PostgreSQL database
4. Connect Looker Studio to your data source and recreate dashboards

---

## Challenges & What I Learned

Completing this project entirely on iPad Air forced creative problem-solving at every layer. Supabase's browser-based SQL editor replaced a desktop client entirely. Excel on iPad handled 64k rows of cleaning and forecasting without issue, though pivot table workflows required adapting to a touch-first interface. Looker Studio's web app connected seamlessly.

The biggest challenge was managing a multi-tool workflow — cleaning in Excel, analyzing in SQL, visualizing in Looker Studio — with no desktop to act as a central hub. That constraint pushed better discipline around file naming, version control via GitHub, and keeping each layer of the project cleanly separated.

The takeaway: cloud-first tooling has matured enough that a laptop is no longer a prerequisite for serious data work.

---

## Macro Context

Channel-level sales projections are directionally validated against publicly reported gaming industry revenue figures. The global video game market was valued at approximately $184 billion in 2023 and is projected to grow consistently through 2027.

---

## Limitations

- Sales figures represent physical and digital reported units — not all digital sales are captured in this dataset
- Data reflects titles with documented sales records — indie and smaller releases may be underrepresented
- 2027 forecast is a statistical projection based on historical trends, not a guarantee — treat as directional, not precise

---

💡 *This entire project was completed on iPad Air using only cloud-based tools — no laptop required at any stage.*
