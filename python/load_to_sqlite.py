import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
DB_PATH = BASE_DIR / "saas_analytics.db"

def main():
    conn = sqlite3.connect(DB_PATH)

    users = pd.read_csv(RAW_DIR / "users.csv")
    events = pd.read_csv(RAW_DIR / "events.csv")
    subscriptions = pd.read_csv(RAW_DIR / "subscriptions.csv")

    users.to_sql("users", conn, if_exists="replace", index=False)
    events.to_sql("events", conn, if_exists="replace", index=False)
    subscriptions.to_sql("subscriptions", conn, if_exists="replace", index=False)

    conn.close()
    print("Loaded users, events, and subscriptions into saas_analytics.db")

if __name__ == "__main__":
    main()