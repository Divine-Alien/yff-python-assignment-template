from datetime import datetime

def get_time(time_str: str) -> dict:
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    return {
        "year": dt.year,
        "year": dt.year,
        "month": f"{dt.month:02d}",
        "day": f"{dt.day:02d}",
        "hour": f"{dt.hour:02d}",
        "minute": f"{dt.minute:02d}",
        "second": f"{dt.second:02d}"
    }