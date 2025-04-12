import os

class FileIterator:
    """
    A class to iterate over files in a directory.
    """

    def __init__(self, directory, extensions=None):
        """
        Initialize the iterator with a directory and optional extensions.
        :param directory: Path to root media directory
        :param extensions: Optional set/list of file extensions to filter
        """
        self.directory = directory
        self.extensions = extensions

    def __iter__(self):
        """
        Make the class iterable.
        """
        for root, _, files in os.walk(self.directory):
            for name in files:
                if self.extensions is None or name.lower().endswith(tuple(self.extensions)):
                    yield os.path.join(root, name)
