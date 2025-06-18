import os
import shutil

source_path_folder = r"C:\Users\215MArcedas\Desktop\fileFolder"
destination_path_folder = r"C:\Users\215MArcedas\Desktop\destinationFolder"
file_name = "sample.txt"

full_source_path = os.path.join(source_path_folder, file_name)

if not os.path.exists(source_path_folder):
    os.makedirs(source_path_folder)
    print(f"Source folder {source_path_folder} created.")
else:
    shutil.move(full_source_path, destination_path_folder)
    print(f"File {file_name} moved to {destination_path_folder}")