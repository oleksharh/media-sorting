from datetime import datetime

def get_earliest_date(metadata: dict) -> datetime.date:
    for key, value in metadata.items():
        date_formats = [
            "%Y:%m:%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S %Z",
            "%Y-%m-%d %H:%M:%S.%f %Z",
            "%Y-%m-%d %H:%M:%S.%f"
        ]
        for fmt in date_formats:
            try:
                date = datetime.strptime(value, fmt).date()
                print(f"Parsed date from {key}: {date}")
                return date
            except ValueError:
                continue
        print(f"ValueError: {value} does not match any known date format")

# TODO: IMPLEMENT Comparisons to get the earliest date