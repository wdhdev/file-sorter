import os, shutil, sys

file_extensions = {
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
    "tiff": "Images",
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

print("[44m DIRECTORY [0m", directory)
print()

confirm = input("Are you sure you want to sort these files? [y/N]\n>> ")
confirm = confirm.lower()

if confirm == "y" or confirm == "yes":
    print()

    amount = 0

    for file in files:
        destination = directory + "\\Other"

        if file == __file__.rsplit("\\", 1)[1] or not os.path.isfile(file):
            continue

        amount += 1

        for ext in file_extensions:
            if file.endswith("." + ext):
                destination = directory + "\\" + file_extensions[ext]

        if not os.path.isdir(destination):
            os.mkdir(destination)
            print("[35mDirectory Created:[0m", destination.rsplit("\\", 1)[1])

        shutil.move(file, destination)
        print("[34mFile Moved[0m: \"" + file + "\" to \"" + destination.rsplit("\\", 1)[1] + "\"")

    if amount == 0:
        print("[41m ERROR [0m No files to be sorted.\n")
        os.system("pause")
        sys.exit()

    print()
    os.system("pause")
else:
    os.system("pause")
    sys.exit()
