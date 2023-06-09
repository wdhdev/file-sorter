import os
import shutil
import sys

file_extensions = {
    "7z": "Compressed Folders",
    "avi": "Videos",
    "bat": "Programs",
    "c": "Programming",
    "cpp": "Programming",
    "css": "Websites",
    "csv": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "exe": "Programs",
    "gif": "GIFs",
    "gz": "Compressed Folders",
    "h": "Programming",
    "htm": "Websites",
    "html": "Websites",
    "java": "Programming",
    "jpeg": "Images",
    "jpg": "Images",
    "js": "Programming",
    "lnk": "Programs",
    "lua": "Programming",
    "m4a": "Audio",
    "mkv": "Videos",
    "mov": "Videos",
    "mp3": "Audio",
    "mp4": "Videos",
    "msi": "Installers",
    "ogg": "Audio",
    "pdf": "PDFs",
    "php": "Programming",
    "png": "Images",
    "ppt": "Presentations",
    "pptx": "Presentations",
    "py": "Programming",
    "rtf": "Documents",
    "svg": "Images",
    "tar": "Compressed Folders",
    "tiff": "Images",
    "ts": "Programming",
    "txt": "Documents",
    "wav": "Audio",
    "webp": "Images",
    "wma": "Audio",
    "wmv": "Videos",
    "xls": "Documents",
    "xlsb": "Documents",
    "xlsm": "Documents",
    "xlsx": "Documents",
    "xlt": "Templates",
    "xltx": "Templates",
    "xml": "Documents",
    "zip": "Compressed Folders"
}

directory = os.getcwd()
files = os.listdir(directory)

print("Directory:", directory)
print()

confirm = input("Sort files? [y/N]\n>> ")
confirm = confirm.lower()

if confirm == "y" or confirm == "yes":
    print()

    amount = 0

    for file in files:
        destination = directory + "\\Other"

        if not os.path.isfile(file):
            continue

        amount += 1

        for ext in file_extensions:
            if file.endswith("." + ext):
                destination = directory + "\\" + file_extensions[ext]

        if not os.path.isdir(destination):
            os.mkdir(destination)
            print("Created Directory:", destination.rsplit("\\", 1)[1])

        shutil.move(file, destination)
        print("Moved \"" + file + "\" to \"" + destination.rsplit("\\", 1)[1] + "\"")

    if amount == 0:
        print("Error: No files to be sorted.\n")
        os.system("pause")
        sys.exit()

    print()
    os.system("pause")
else:
    print("\nError: Operation cancelled.\n")
    os.system("pause")
    sys.exit()
