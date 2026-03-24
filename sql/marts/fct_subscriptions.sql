SELECT
    s.user_id,
    u.signup_date,
    u.country,
    u.acquisition_channel,
    s.plan,
    s.start_date,
    s.end_date,
    s.monthly_revenue
FROM subscriptions s
LEFT JOIN users u
    ON s.user_id = u.user_id;