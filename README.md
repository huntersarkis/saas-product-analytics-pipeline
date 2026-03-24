# SaaS Product Analytics Pipeline

## Overview
This project simulates an end-to-end analytics engineering workflow for a SaaS company. The goal is to transform raw user, event, and subscription data into analytics-ready models that support business insights such as user engagement, retention, and revenue.

The pipeline follows a structured approach using staging and mart layers to create clean, reusable datasets for reporting and analysis.

---

## Tech Stack
- Python (data generation and ingestion)
- SQL (data transformation and modeling)
- SQLite (local database)
- Git & GitHub (version control)
- VS Code (development environment)

---

## Data Sources
The project uses three core datasets:

- **users**: user signups and attributes (country, acquisition channel)
- **events**: user activity (logins, feature usage, interactions)
- **subscriptions**: subscription plans, revenue, and churn information

All data is programmatically generated using Python to simulate real-world SaaS data.

---

## Data Model

### Staging Layer
- `stg_users`
- `stg_events`
- `stg_subscriptions`

These models represent cleaned versions of the raw data.

### Fact Tables
- `fct_user_events`: captures user activity and behavior
- `fct_revenue`: captures subscription revenue and active status

### Dimension Tables
- `dim_users`: user attributes used for analysis

### Metrics Layer
- `daily_metrics`: aggregated daily KPIs including:
  - total events
  - daily active users (DAU)
  - total revenue from active subscriptions

---

## Key Metrics

- **Daily Active Users (DAU)**: number of unique users generating events per day  
- **Total Events**: total number of tracked user actions  
- **Revenue**: total monthly revenue from active subscriptions  
- **Active vs Churned Users**: determined using subscription end dates  

---

## Example Use Cases

This data model can support:
- user engagement analysis by country or acquisition channel  
- revenue analysis across subscription plans  
- tracking growth trends over time  
- identifying high-value user segments  

---

## Project Structure


```text
saas-product-analytics-pipeline/
│
├── data/
│   └── raw/
│       ├── users.csv
│       ├── events.csv
│       └── subscriptions.csv
│
├── sql/
│   ├── staging/
│   │   ├── stg1_users.sql
│   │   ├── stg2_events.sql
│   │   └── stg3_subscriptions.sql
│   │
│   ├── marts/
│   │   ├── fct_user_events.sql
│   │   ├── fct_revenue.sql
│   │   ├── dim_users.sql
│   │   └── daily_metrics.sql
│   │
│   └── analysis/
│       └── analysis_queries.sql
│
├── python/
│   ├── generate_data.py
│   └── load_to_sqlite.py
│
├── dashboards/
├── saas_analytics.db
└── README.md
```


---

## AI Assistance Disclosure

Parts of this project, including initial data generation scripts, were developed with the assistance of AI tools (ChatGPT). All code was reviewed, modified, and validated to ensure accuracy and understanding.

---

## Findings

Analysis of the modeled SaaS data revealed several key business insights:

- **Referral was the top acquisition channel by revenue**, generating 9,731 in total revenue, slightly outperforming organic search.
- **Germany produced the highest total revenue** (9,020), followed by Australia and the United Kingdom, indicating stronger monetization in those regions.
- **User activity was evenly distributed across event types**, with signups and logins leading total engagement, suggesting consistent interaction across the product.
- **Active subscriptions significantly outnumbered churned users** (482 active vs 162 churned), indicating relatively strong retention in the dataset.
- **Daily KPI modeling revealed fluctuations in user activity and revenue over time**, demonstrating how the pipeline supports ongoing performance tracking.

---
## Example Analysis Queries

Sample queries used to generate insights can be found in:

`sql/analysis/analysis_queries.sql`

---

## Summary

This project demonstrates core analytics engineering skills, including:
- building data pipelines
- designing data models (fact and dimension tables)
- transforming raw data into business-ready datasets
- defining and calculating key business metrics