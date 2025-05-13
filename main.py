import os
import shutil

path = os.getcwd()
file_path = os.listdir(path)

# create destination folders and check if they already exist
images_dir = "Pictures"
videos_dir = "Videos"
documents_dir ="Documents"
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



for file in file_path:
        filename = os.fsdecode(file)
        extension = filename.split('.')[-1].lower()


        if extension in pic_extensions:
                shutil.move(filename, images_dir)

        if extension in vid_extensions:
                shutil.move(filename, videos_dir)

        if extension in docx_extensions:
                shutil.move(filename, documents_dir)

        if extension in code_extensions:
                shutil.move(filename, Code_dir)

        else: shutil.move(filename, Misc_dir)
