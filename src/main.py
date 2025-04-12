from media_sorter.metadata import extract_dates
from media_sorter.date_resolver import get_earliest_date

file_paths = ["IphoneMediaFiles/BBAX3224.MP4", "IphoneMediaFiles/AIBHE7480.JPG"]

for file_path in file_paths:
    print(f"Processing file: {file_path}")
    metadata = extract_dates(file_path)
    if metadata:
        print("Extracted Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("No metadata extracted.")

    print("Earliest Date:")
    earliest_date = get_earliest_date(metadata)
    print(earliest_date)