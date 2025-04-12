## General Logic and Steps of Sorting

1. **Extract File Metadata**  
    Retrieve the file's metadata and return a dictionary containing data tags.

2. **Process Metadata for Dates**  
    Analyze the metadata dictionary to identify the earliest date.

3. **Generate Destination Folder Path**  
    Create a folder path based on the earliest date in the format:  
    `year/quarter`, where `quarter` is determined as follows:  
    - Q1: January - March  
    - Q2: April - June  
    - Q3: July - September  
    - Q4: October - December  

4. **Move or Copy the File**  
    Use the generated folder path to move or copy the media file to the destination.