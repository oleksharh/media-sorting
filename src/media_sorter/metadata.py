from PIL import Image
from PIL.ExifTags import TAGS
from pymediainfo import MediaInfo

# path to error logs
error_log_path = "error.txt"
# files with errors will be logged here
error_files_path = "error_files.txt"

# image extensions
# image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.heic', '.heif', '.tiff', '.bmp', '.webp']
#  video extensions
# video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.mpeg', '.mpg', '.3gp']

def extract_dates(file_path):
    """
    Extract metadata from a media file using pymediainfo.
    
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
                    if "DateTime" in tag: # there are attrs ("DateTime", "DateTimeOriginal", "DateTimeDigitized")
                        metadata[tag] = value

            if not metadata:
                pass
            else:
                return metadata
        
    # Error Logging and Handling
    except Exception as e:
        pass # it will be handled in the video section

    
    # For videos
    # Extract metadata using pymediainfo
    try:
        media_info = MediaInfo.parse(file_path)
        for track in media_info.tracks:
            if track.track_type == "General":
                for key, value in track.to_data().items():
                    if "date" in key.lower():
                        metadata[key] = value
            else:
                print(f"\033[92mTrack type: {track.track_type}\033[0m")
                print(f"\033[92mKey: {key}, Value: {value}\033[0m")
                return None
                

            return metadata
        
    # Error Logging and Handling
    except Exception as e:
        with open(error_log_path, "a") as error_log:
            error_log.write(f"Error extracting metadata from {file_path}: {e}\n")
        with open(error_files_path, "a") as error_files:
            error_files.write(f"{file_path}\n")
        print(f"Video metadata extraction failed: {e}")

        return None

def extract_metadata(file_path):
    """
    Extract metadata from a media file using pymediainfo.
    
    Args:
        file_path (str): Path to the media file.
        
    Returns:
        dict: Metadata extracted from the file.
    """
    metadata = {}

    # Extract metadata using pymediainfo
    try:
        media_info = MediaInfo.parse(file_path)
        for track in media_info.tracks:
            if track.track_type == "General":
                for key, value in track.to_data().items():
                    metadata[key] = value
            else:
                return None

            return metadata
        
    # Error Logging and Handling
    except Exception as e:
        with open(error_log_path, "a") as error_log:
            error_log.write(f"Error extracting metadata from {file_path}: {e}\n")
        with open(error_files_path, "a") as error_files:
            error_files.write(f"{file_path}\n")
        print(f"Metadata extraction failed: {e}")

        return None



# Example usage
if __name__ == "__main__":
    # Example usage
    file_paths = ["IphoneMediaFiles/BBAX3224.MP4", "IphoneMediaFiles/AIBHE7480.JPG"]

    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        metadata = extract_dates(file_path)
        if metadata:
            print("Extracted Metadata:")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print("No metadata extracted.")
