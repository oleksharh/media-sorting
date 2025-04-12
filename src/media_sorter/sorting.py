from media_sorter.operations.file_ops import copy_move_file


def sort_move_file(base_path: str, file_obj):
    """
    Create sorted directories based on the earliest date of files.
    """
    file_path = file_obj[0]
    file_date = file_obj[1]

    year = file_date.year
    month = file_date.month
    quarter = (month - 1) // 3 + 1

    # Create directory structure
    sorted_dir = f"{base_path}/{year}/{quarter}"
    return copy_move_file(file_path, sorted_dir)
