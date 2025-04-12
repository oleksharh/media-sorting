from media_sorter.iterator import FileIterator
from media_sorter.sorting import sort_move_file
from media_sorter.operations.file_ops import copy_move_file

file_paths = FileIterator("C:/Projects/MediaSorting/IphoneMediaFiles/Private")
dest_path = "C:/Users/Alex/Pictures/IphoneSorted"

for el in file_paths:
    print(f"\033[92mProcessing file: {el[0]}\033[0m")
    print(el[0], el[1])
    print("Moved to: " + sort_move_file(dest_path, el))
