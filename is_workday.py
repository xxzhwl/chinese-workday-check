#!/usr/bin/env python3
"""Check if today is a Chinese statutory workday using NateScarlet/holiday-cn data."""
import json
import sys
from datetime import date, datetime
from urllib.request import urlopen

def is_workday(d: date) -> tuple[bool, str]:
    """Returns (is_workday, reason)."""
    url = f"https://raw.githubusercontent.com/NateScarlet/holiday-cn/master/{d.year}.json"
    try:
        resp = urlopen(url, timeout=10)
        data = json.loads(resp.read())
    except Exception as e:
        # Fallback: if we can't fetch data, just check Mon-Fri
        is_weekday = d.weekday() < 5
        return (is_weekday, f"fallback: {e}")

    date_str = d.isoformat()
    for entry in data.get("days", []):
        if entry["date"] == date_str:
            name = entry["name"]
            if entry["isOffDay"]:
                return (False, f"holiday: {name}")
            else:
                return (True, f"makeup workday: {name}")

    # Not in special list: normal Mon-Fri is workday, weekend is off
    is_weekday = d.weekday() < 5
    if is_weekday:
        return (True, "normal weekday")
    else:
        return (False, "normal weekend")

if __name__ == "__main__":
    target_date = date.today()
    if len(sys.argv) > 1:
        try:
            target_date = datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
        except ValueError:
            pass

    workday, reason = is_workday(target_date)
    print(f"{target_date.isoformat()} workday={workday} reason={reason}")
    sys.exit(0 if workday else 1)
