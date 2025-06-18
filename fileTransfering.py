import os
import shutil

source_path_folder = r"Your originate path folder"
destination_path_folder = r"Your destination path folder"
file_name = "Your target file"

#Join of the folder and file path
full_source_path = os.path.join(source_path_folder, file_name)

#Conditional statement if the folder is not created before taking an action of file transfering
if not os.path.exists(source_path_folder):
    os.makedirs(source_path_folder)
    print(f"Source folder {source_path_folder} created.")
    shutil.move(full_source_path, destination_path_folder)
    print(f"File {file_name} moved to {destination_path_folder}")
else:
    shutil.move(full_source_path, destination_path_folder)
    print(f"File {file_name} moved to {destination_path_folder}")
