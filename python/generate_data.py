from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

NUM_USERS = 1000
NUM_EVENTS = 12000

COUNTRIES = ["United States", "Canada", "United Kingdom", "Germany", "Australia"]
CHANNELS = ["Organic Search", "Paid Search", "LinkedIn", "Referral", "Direct"]
EVENT_TYPES = ["signup", "login", "feature_use", "upgrade_click", "billing_page_view"]
PLANS = ["Basic", "Pro", "Enterprise"]


def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))


def generate_users() -> list[dict]:
    users = []
    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    for user_id in range(1, NUM_USERS + 1):
        signup_date = random_date(start, end)
        users.append(
            {
                "user_id": user_id,
                "signup_date": signup_date.strftime("%Y-%m-%d"),
                "country": random.choice(COUNTRIES),
                "acquisition_channel": random.choice(CHANNELS),
            }
        )
    return users


def generate_events(users: list[dict]) -> list[dict]:
    events = []
    event_start = datetime(2024, 1, 1)
    event_end = datetime(2025, 12, 31)

    for event_id in range(1, NUM_EVENTS + 1):
        user = random.choice(users)
        signup_dt = datetime.strptime(user["signup_date"], "%Y-%m-%d")
        event_time = random_date(max(signup_dt, event_start), event_end)

        events.append(
            {
                "event_id": event_id,
                "user_id": user["user_id"],
                "event_type": random.choice(EVENT_TYPES),
                "event_timestamp": event_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    return events


def generate_subscriptions(users: list[dict]) -> list[dict]:
    subscriptions = []

    for user in users:
        if random.random() < 0.65:
            signup_dt = datetime.strptime(user["signup_date"], "%Y-%m-%d")
            start_date = signup_dt + timedelta(days=random.randint(0, 30))
            plan = random.choices(PLANS, weights=[0.55, 0.35, 0.10], k=1)[0]

            monthly_revenue = {
                "Basic": 29,
                "Pro": 79,
                "Enterprise": 199,
            }[plan]

            churned = random.random() < 0.25
            end_date = (
                (start_date + timedelta(days=random.randint(30, 365))).strftime("%Y-%m-%d")
                if churned
                else ""
            )

            subscriptions.append(
                {
                    "user_id": user["user_id"],
                    "plan": plan,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date,
                    "monthly_revenue": monthly_revenue,
                }
            )

    return subscriptions


def write_csv(filename: str, rows: list[dict]) -> None:
    if not rows:
        return

    filepath = RAW_DIR / filename
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    users = generate_users()
    events = generate_events(users)
    subscriptions = generate_subscriptions(users)

    write_csv("users.csv", users)
    write_csv("events.csv", events)
    write_csv("subscriptions.csv", subscriptions)

    print("Data generated successfully.")
    print(f"users.csv: {len(users)} rows")
    print(f"events.csv: {len(events)} rows")
    print(f"subscriptions.csv: {len(subscriptions)} rows")


if __name__ == "__main__":
    main()