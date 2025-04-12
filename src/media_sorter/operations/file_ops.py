import os
import shutil


def ensure_dir_exists(path: str):
    os.makedirs(path, exist_ok=True)


def copy_move_file(src: str, dst: str):
    ensure_dir_exists(os.path.dirname(dst))
    shutil.copy2(src, dst)
