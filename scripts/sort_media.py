from media_sorter.iterator import FileIterator

file_paths = FileIterator("C:\Projects\MediaSorting\TestMedia")

for file_path, earliest_date in file_paths:
    print(f"\033[92mProcessing file: {file_path}\033[0m")
    print(file_path, earliest_date)