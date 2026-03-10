# Video Game Sales Analytics (1971–2024)

An end-to-end data analysis project examining more than **50 years of global video game sales**.  
This project explores long-term industry trends including **platform dominance, genre evolution, regional market shifts, and publisher performance**, and includes a **statistical forecast of market trends through 2027**.

The full analysis was conducted using **cloud-based tools and executed entirely on an iPad Air**.

---

# Project Overview

This project analyses historical video game sales data from **1971–2024**, covering over **64,000 titles** across multiple platforms, publishers, and regions.

The goal is to understand how the video game industry has evolved over time and identify patterns that help explain **market growth, platform competition, and consumer preferences**.

The workflow includes:

- Data cleaning and preparation  
- SQL-based exploratory analysis  
- Data visualization through dashboards  
- Time-series forecasting  

---

# Business Questions

This analysis focuses on answering several key questions:

- How have **global video game sales** changed over the past five decades?
- Which **gaming platforms** have dominated the market at different times?
- How has **genre popularity** evolved across console generations?
- Which **regional markets (North America, Japan, Europe)** contribute the most to global sales?
- Which **publishers consistently outperform the market**?
- Based on historical trends, what might the **industry look like through 2027**?

---

# Project Status

🚧 **In Progress**

Current progress:

- Dataset cleaned and structured  
- SQL analysis queries written  
- Early dashboards in development  
- Forecast model created using **Excel FORECAST.ETS**

Final insights and dashboard links will be added when the project is complete.

---

# Tools & Technologies

| Layer | Tool |
|-----|-----|
| Data Cleaning & Forecasting | Excel (iPad) |
| Data Analysis | PostgreSQL (Supabase) |
| Visualization | Looker Studio |
| Version Control | GitHub |

---

# Dataset

**Source:** Maven Analytics – Video Game Sales Dataset  
https://www.mavenanalytics.io/data-playground/video-game-sales

The dataset contains **64,016 video game titles** released between **1971 and 2024**, including information such as:

- Game title
- Console / platform
- Genre
- Publisher
- Developer
- Release date
- Critic score
- Global sales
- Regional sales:
  - North America
  - Japan
  - Europe (PAL region)
  - Other regions

Sales values are recorded in **millions of units sold**.

The original dataset was downloaded from Maven Analytics and then cleaned in Excel before being imported into PostgreSQL for analysis.

---

# Methodology

The analysis was completed in four main stages.

## 1. Data Cleaning

The raw dataset was cleaned using Excel:

- Standardized date formats
- Removed incomplete records
- Checked for duplicate titles
- Verified regional sales totals
- Exported a cleaned dataset for SQL analysis

---

## 2. SQL Analysis

PostgreSQL was used to explore trends across multiple dimensions:

- Global sales by platform
- Genre popularity trends
- Publisher market share
- Regional sales distribution
- Top-selling games of all time

---

## 3. Data Visualization

Interactive dashboards were built in **Looker Studio** to display:

- Global sales trends over time
- Platform market share
- Genre performance
- Regional sales comparisons

---

## 4. Forecasting

A **time-series forecast** was created using Excel’s **FORECAST.ETS** function to estimate **global video game sales trends through 2027**.

---

# Key Insights

*(To be completed once final analysis is finished.)*

Planned insights include:

- Long-term growth trends in global gaming sales
- Platform dominance across different console generations
- Genre popularity shifts over time
- Regional market differences
- Forecasted market trajectory through 2027

---

# Live Dashboard

A public Looker Studio dashboard will be available here:

**Dashboard link coming soon**

The dashboard will include interactive visualizations for:

- Global video game sales trends
- Platform market share
- Regional sales comparisons
- Genre performance over time

---

# Project Structure

```
video-game-sales-analytics/

├── data/
│   ├── raw/          # Original dataset
│   └── clean/        # Cleaned dataset used for analysis

├── sql/
│   ├── 01_schema.sql
│   ├── 02_cleaning_queries.sql
│   └── 03_analysis_queries.sql

├── excel/
│   └── screenshots/  # Data cleaning, pivot tables, forecast model

├── dashboards/
│   ├── screenshots/  # Looker Studio dashboard previews
│   └── LINKS.md      # Dashboard access links
```

---

# How to Reproduce the Analysis

1. Download the raw dataset from `data/raw/` or from Maven Analytics.
2. Follow the Excel data cleaning steps shown in `excel/screenshots/`.
3. Import the cleaned dataset into a PostgreSQL database.
4. Run the SQL scripts in the `sql/` folder in order.
5. Connect Looker Studio to the database and recreate the dashboards.

---

# Industry Context

The video game industry has grown into one of the largest entertainment sectors globally.

Industry reports estimate the **global gaming market was valued at approximately $184 billion in 2023**, with continued growth expected through **2027**, driven by:

- Digital distribution
- Expanding global audiences
- Mobile gaming
- Cross-platform ecosystems

---

# Limitations

- Sales figures represent **reported unit sales** and may not capture all digital purchases.
- Some **indie and smaller titles** may be missing due to limited available data.
- Regional groupings are aggregated and may not represent individual country markets.
- The **2027 forecast** is based on historical trends and statistical modelling, and should be interpreted as a **directional estimate rather than a precise prediction**.

---

# Note

💡 This entire project was completed using **only an iPad Air and cloud-based tools**, demonstrating that a full data analytics workflow can be completed without a traditional laptop or desktop environment.
