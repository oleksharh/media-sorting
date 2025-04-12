from PIL import Image
from PIL.ExifTags import TAGS
from pymediainfo import MediaInfo
from media_sorter.utils.logger import log_error


def extract_dates(file_path):
    """
    Extracts metadata from a media file using pymediainfo.
    Args:
        file_path (str): Path to the media file.
    Returns:
        dict: Dates extracted from Metadata
    """
    metadata = {}

    # For images
    # Extract metadata using PIL and ExifTags
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)

                    # there are attrs ("DateTime", "DateTimeOriginal", "DateTimeDigitized")
                    if "DateTime" in tag:
                        metadata[tag] = value

            if metadata:
                return metadata

    except Exception as e:
        pass  # Fallthrough to MediaInfo parser

    # For videos or JPGs
    # Extract metadata using pymediainfo
    try:
        media_info = MediaInfo.parse(file_path)
        for track in media_info.tracks:
            if track:
                for key, value in track.to_data().items():
                    if "date" in key.lower():
                        metadata[key] = value
            else:
                pass # ignore other track types

        return metadata if metadata else None

    except Exception as e:
        log_error(f"Error extracting metadata from {file_path}: {e}\n", file_path)
        return None


# Example usage
if __name__ == "__main__":
    # Example usage
    file_paths = [
                r"C:\Projects\MediaSorting\IphoneMediaFiles/BBAX3224.MP4",
                r"C:\Projects\MediaSorting\IphoneMediaFiles/AIBHE7480.JPG"
              ]

    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        metadata = extract_dates(file_path)
        if metadata:
            print("Extracted Metadata:")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print("No metadata extracted.")
