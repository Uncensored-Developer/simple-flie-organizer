import os
from pathlib import Path

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                   ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Texts": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "Python": [".py"],
    "XML": [".xml"],
    "Executable": [".exe"],
    "Shell": [".sh"]
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

    # if file extension not present in the dictionary than create a folder name "Others"
    try:
        os.mkdir("Others")
    except PermissionError:
        print('Failed to obtain permission')
    except:
        pass

    for item in os.scandir():
        try:
            if item.is_dir():
                os.rmdir(item)
            else:
                os.rename(os.getcwd() + '/' + str(Path(item)), os.getcwd() + '/Others/' + str(Path(item)))
        except PermissionError:
            print('Failed to obtain permission')
        except:
            pass


if __name__ == "__main__":
    organize()
