# YouTube Ad Revenue Analytics

An end-to-end data analysis project exploring YouTube ad revenue trends, 
patterns, and a forward-looking forecast through 2027.  
Built entirely on iPad Air using cloud-based tools.

## Business Questions
- How does ad revenue trend month-over-month and year-over-year?
- What CPM levels correlate with the highest revenue days?
- At what view volume does revenue meaningfully scale?
- What can historical patterns tell us about expected revenue in 2027?

## Status
🚧 In progress — includes 2027 revenue forecast using Excel FORECAST.ETS

## Tools
| Layer | Tool |
|---|---|
| Data cleaning & forecasting | Excel (iPad) |
| SQL analysis | PostgreSQL via Supabase |
| Dashboards & visualization | Looker Studio |
| Version control & portfolio | GitHub |

## Dataset
YouTube Video Performance Metrics (2016–2024) via Opendatabay  
Covers 8+ years of channel-level revenue, CPM, impressions, watch time, and more.  
Includes: AdSense, DoubleClick, YouTube Ads, Watch Page, Premium, and Transaction revenue.

## Key Insights
_Will be filled in on project completion_

## Live Dashboard
_Link will be added once dashboards are complete_

## Project Structure
    youtube-ad-revenue-analytics/
    ├── data/
    │   ├── raw/          ← original Opendatabay CSV
    │   └── clean/        ← cleaned CSV exported from Excel
    ├── sql/
    │   ├── 01_schema.sql
    │   ├── 02_cleaning_queries.sql
    │   └── 03_analysis_queries.sql
    ├── excel/
    │   └── screenshots/  ← formulas, pivot tables, forecast sheet
    └── dashboards/
        ├── screenshots/  ← Looker Studio dashboard exports
        └── LINKS.md      ← live share links

## How to Reproduce
1. Download raw CSV from `data/raw/` (or directly from Opendatabay)
2. Apply Excel cleaning steps — see `excel/screenshots/` for each stage
3. Run `sql/` scripts in order against any PostgreSQL database
4. Connect Looker Studio to your data source and recreate dashboards

## Limitations
- Revenue figures are channel-level estimates, not platform-wide figures
- Data reflects a single channel — findings may not generalise across niches
- 2027 forecast is a statistical projection based on historical trends,  
  not a guarantee — treat as directional, not precise

> 💡 This entire project was completed on iPad Air using only cloud-based tools —  
> no laptop required at any stage.

