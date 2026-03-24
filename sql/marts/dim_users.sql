CREATE VIEW dim_users AS
SELECT
    user_id,
    signup_date,
    country,
    acquisition_channel
FROM users;

SELECT *
FROM dim_users
LIMIT 25;