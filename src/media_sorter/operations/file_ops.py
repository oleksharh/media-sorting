import shutil
import time
import os

def ensure_dir_exists(path: str):
    os.makedirs(path, exist_ok=True)

def copy_move_file(src: str, dst: str):
    ensure_dir_exists(dst)

    # Append the file name with extension to the destination path
    dst = os.path.join(dst, os.path.basename(src)).replace("\\", "/")

    retries = 5
    for attempt in range(retries):
        try:
            return shutil.copy2(src, dst)
        except PermissionError as e:
            if attempt < retries - 1:
                print(f"File is locked, retrying... ({attempt + 1}/{retries})")
                time.sleep(1)  # Wait before retrying
            else:
                print(f"Error copying file {src} to {dst}: {e}")
                raise