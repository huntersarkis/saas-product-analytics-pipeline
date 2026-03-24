-- Daily Metrics Analysis --
SELECT *
FROM daily_metrics
ORDER BY event_date;

-- User Acquisition Analysis --
SELECT
    acquisition_channel,
    COUNT(DISTINCT user_id) AS users,
    SUM(monthly_revenue) AS revenue
FROM fct_revenue
GROUP BY acquisition_channel
ORDER BY revenue DESC;

-- Revenue Analysis by Country --
SELECT
    country,
    SUM(monthly_revenue) AS total_revenue
FROM fct_revenue
GROUP BY country
ORDER BY total_revenue DESC;

-- User Engagement Analysis --
SELECT
    event_type,
    COUNT(*) AS total_events
FROM fct_user_events
GROUP BY event_type
ORDER BY total_events DESC;

-- User Retention Analysis --
SELECT
    is_active,
    COUNT(*) AS users
FROM fct_revenue
GROUP BY is_active;
