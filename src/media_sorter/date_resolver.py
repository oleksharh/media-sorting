from datetime import datetime

def get_earliest_date(metadata: dict) -> datetime.date:
    dates = []
    
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
                dates.append(date)
            except ValueError:
                continue
        
    print(f"Dates found in {key}: {dates}")
    if dates:
        earliest_date = min(dates)
        print(f"Earliest date found in {key}: {earliest_date}")
        return earliest_date

    print(f"No valid date found in {key} with value: {value}")

