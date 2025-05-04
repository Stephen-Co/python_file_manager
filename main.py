import os
import shutil

file_path = os.getcwd()

# create destination folders and check if they already exist
images_dir = "Pictures"
videos_dir = "Videos"
documents_dir ="Word/Excel Documents"
Code_dir = "Coding files"
Misc_dir = "Miscallaneous"

directories_list = [ images_dir, videos_dir, documents_dir, Code_dir, Misc_dir]

 

# Create the directory
for x in directories_list:
        try:
                os.mkdir(x)
                print(f"Directory '{x}' created successfully.")
        except FileExistsError:
                print(f"Directory '{x}' already exists.")
        except PermissionError:
                print(f"Permission denied: Unable to create '{x}'.")
        except Exception as e:
                print(f"An error occurred: {e}")

#define extensions
pic_extensions =["jpeg", "png","heic", "jfif"]
vid_extensions =["mp4", "mp3"]
docx_extensions =["docx", "doc", "xls", "xlsx", "ppt", "pptx", "csv","pdf"]
code_extensions =["c", "py","r", "v"]


#move files to destination