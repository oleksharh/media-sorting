from media_sorter.utils.config import ERROR_LOG_PATH, ERROR_FILES_PATH

def log_error(error_msg, file_path):
    with open(ERROR_LOG_PATH, "a") as error_log:
        error_log.write(f"{error_msg}\n")
    with open(ERROR_FILES_PATH, "a") as error_files:
        error_files.write(f"{file_path}\n")