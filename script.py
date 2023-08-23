import os
import shutil
import platform
import locale
extensions_to_organize = [
    ".txt", ".jpg", ".png",".pdf",".jpeg",".xls",".ppt",".zip",".rar",".7z",".exe",".msi",".iso",".mp3",".mp4",".avi",".mkv",".mov",".wav",".flac",".m4a",".aac",".wma",".ogg",".bmp",".gif",".svg",".ico",".psd",".ai",".tif",".tiff",".eps",".raw",".cr2",".nef",".orf",".sr2",".webp",".heic",".3gp",".3g2",".asf",".wmv",".flv",".swf",".avchd",".mkv",".webm",".html",".css",".js",".json",".php",".c",".cpp",".py",".java",".class",".cs",".vb",".go",".swift",".rb",".pl",".sql",".xml",".csv",".dat",".key",".odp",".pps",".ppt",".pptx",".ods",".xls",".xlsx",".doc",".docx",".odt",".pdf",".rtf",".tex",".wks",".wps",".wpd"
]
folder_map = {
        ".txt": "TextFiles",
        ".jpg": "ImageFiles",
        ".png": "ImageFiles",
        ".pdf": "PDFFiles",
        ".jpeg": "ImageFiles",
        ".docx": "WordFiles",
        ".doc": "WordFiles",
        ".xlsx": "ExcelFiles",
        ".xls": "ExcelFiles",
        ".pptx": "PowerPointFiles",
        ".ppt": "PowerPointFiles",
}
def get_desktop_path():
    user_language, _ = locale.getdefaultlocale()

    if "pt" in user_language:  # Assuming "pt" corresponds to Portuguese language
        system = platform.system()
        if system == "Linux":
            return os.path.expanduser("~/Área de Trabalho")
        elif system == "Darwin":  # macOS
            return os.path.expanduser("~/Área de Trabalho")
        elif system == "Windows":
            return os.path.join(os.path.expanduser("~"), "Área de Trabalho")
    else:
        # Default to the English name "Desktop"
        return os.path.expanduser("~/Desktop")

def organize_desktop():
    desktop_path = get_desktop_path()
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path) and not item.startswith("."):  # Check if it's a file and not hidden
            extension = os.path.splitext(item)[1]
            if extension in extensions_to_organize:
                move_file(desktop_path, item, extension)

def move_file(desktop_path, filename, extension):
    default_folder_name = "OtherFiles"
    
    folder_name = folder_map.get(extension, default_folder_name)
    folder_path = os.path.join(desktop_path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(desktop_path, filename)
    new_file_path = os.path.join(folder_path, filename)
    
    shutil.move(file_path, new_file_path)
    print(f"Moved {filename} to {folder_path}")

organize_desktop()
