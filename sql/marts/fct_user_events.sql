SELECT
    e.event_id,
    e.user_id,
    u.signup_date,
    u.country,
    u.acquisition_channel,
    e.event_type,
    e.event_timestamp
FROM events e
LEFT JOIN users u
    ON e.user_id = u.user_id;