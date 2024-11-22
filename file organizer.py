import os
import time


# the directory containing files
directory = r'D:/Downloads/Victor drive/'

# folder categories
folder_name = {
    'Video': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav', '.m4a'],
    'Document': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Executable': ['.exe', '.msi', '.dmg'],
    'Zoom Transcript': ['.vtt', '.srt', '.ics']
}

# track processed files
processed_files = set()

# function to organize files
def organize_files():
    global processed_files
    current_files = set(os.listdir(directory))
    new_files = current_files - processed_files # get files not yet sorted
    for file in new_files:
        file_path = os.path.join(directory,file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            for folder, extension in folder_name.items():
                if file_extension in extension:
                    destination_folder = os.path.join(directory, folder)
                    destination_path = os.path.join(destination_folder,file)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    os.rename(file_path, destination_path)
                    print(f"moved: {file} -> {folder}")
                    break


    # Update the sorted files set
    processed_files = current_files

# Polling loop
try:
    print(f"Monitoring folder: {directory}")
    while True:
        organize_files()
        time.sleep(5)  # Check every 5 seconds
except KeyboardInterrupt:
    print("Stopped monitoring.")