import os

def iter_media_files(directory, extensions=None):
    """
    Generator that yields file paths matching given extensions.
    :param directory: Path to root media directory
    :param extensions: Optional set/list of file extensions to filter
    """
    for root, _, files in os.walk(directory):
        for name in files:
            if extensions is None or name.lower().endswith(tuple(extensions)):
                yield os.path.join(root, name)
