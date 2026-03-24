CREATE VIEW fct_revenue AS
SELECT
    s.user_id,
    u.signup_date,
    u.country,
    u.acquisition_channel,
    s.plan,
    s.start_date,
    s.end_date,
    s.monthly_revenue,

    CASE 
        WHEN s.end_date IS NULL OR s.end_date = '' THEN 1
        ELSE 0
    END AS is_active

FROM subscriptions s
LEFT JOIN users u
    ON s.user_id = u.user_id;

SELECT *
FROM fct_revenue
LIMIT 25;