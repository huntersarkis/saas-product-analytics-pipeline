# Engineering Notes: SaaS Product Analytics Pipeline

## Why I Built This Project

The goal of this project was to simulate how an analytics engineer structures data for a SaaS product. Instead of focusing on dashboards, I focused on building a clean data model that supports business metrics.

---

## Design Approach

I structured the project using a layered approach commonly used in analytics engineering:

- Staging → clean raw data
- Marts → business-ready tables
- Analysis → queries for insights

This separation ensures that transformations are modular and reusable.

---

## Why I Used Fact and Dimension Tables

I implemented fact and dimension tables to mirror real-world data modeling practices.

- Fact tables store measurable events (user activity, revenue)
- Dimension tables store descriptive attributes (user information)

This structure makes it easier to join data and build metrics efficiently.

---

## Key Modeling Decisions

### 1. Separating Events and Revenue

User activity and revenue were modeled in separate fact tables:

- `fct_user_events` for behavior
- `fct_revenue` for monetization

This keeps each table focused and avoids mixing different types of data.

---

### 2. Creating an `is_active` Flag

In the revenue table, I added an `is_active` field based on the subscription end date.

This allows:
- quick filtering of active users
- simple churn analysis

---

### 3. Building a Daily Metrics Table

I created a `daily_metrics` table to aggregate data at the day level.

This was important because:
- raw event data is too granular
- businesses track performance over time

---

### 4. Joining Revenue with Events

In `daily_metrics`, revenue is joined to user activity.

This introduces duplication in some cases (users with multiple events), but was acceptable for this project to simplify the metric calculation.

---

## Challenges and Considerations

- Ensuring joins between tables were correct and consistent
- Deciding how to model revenue and churn
- Understanding the correct level of aggregation for metrics
- Managing query execution and database setup in SQLite

---

## What I Would Improve

- Refine revenue calculations to avoid duplication across events
- Add a date dimension table for more advanced time analysis
- Use a tool like dbt for better model management
- Connect to a cloud data warehouse instead of SQLite

---

## Key Takeaway

This project reinforced how important data modeling is in analytics engineering. The structure of the data directly impacts how easily insights can be generated.