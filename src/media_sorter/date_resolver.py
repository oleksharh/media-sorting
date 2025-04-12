from datetime import datetime


def get_earliest_date(metadata: dict) -> datetime.date:
    """
    Returns the earliest date in the given metadata
    Args:
        metadata: dict with keys that include date and time

    Returns:
        datetime.date with the earliest date from the given metadata
    """
    if not metadata:
        return None

    dates = []
    date_formats = [
        "%Y:%m:%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S %Z",
        "%Y-%m-%d %H:%M:%S.%f %Z",
        "%Y-%m-%d %H:%M:%S.%f"
    ]

    for value in metadata.values():

        for fmt in date_formats:
            try:
                date = datetime.strptime(value, fmt).date()
                dates.append(date)
            except ValueError:
                continue

    return min(dates) if dates else None
