import os

# directory = r'D:/Downloads/Victor drive/'
# files = os.listdir(directory)
# # print(files)

# folder_name = ['Video', 'Audio', 'document', 'excutable', 'zoom transcript']

# for i in folder_name:
#     if not os.path.exists(directory + i):
#         os.makedirs(directory + i)
#         print(files)

# for file in files:
#     if ".pdf" in directory and not os.path.exists(directory + "document/"):
#         os.rename(directory, directory + "document/")


# version 2

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

print(directory)

# subfolders if they don't exist
for folder in folder_name:
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# files sorting to respective folders
files = os.listdir(directory)
for file in files:
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):  # Ensure it's a file
        file_extension = os.path.splitext(file)[1].lower()
        for folder, extensions in folder_name.items():
            if file_extension in extensions:
                destination = os.path.join(directory, folder, file)
                os.rename(file_path, destination)
                print(f"Moved: {file} -> {folder}")
                break
            else:
                print( 'unknown extension' )