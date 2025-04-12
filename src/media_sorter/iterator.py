import os
from media_sorter.metadata import extract_dates
from media_sorter.date_resolver import get_earliest_date


class FileIterator:
    """
    A class to iterate over files in a directory and process metadata.
    :returns: file_path, earliest_date
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
                    file_path = os.path.join(root, name)
                    metadata = extract_dates(str(file_path))
                    earliest_date = get_earliest_date(metadata)
                    yield file_path, earliest_date
