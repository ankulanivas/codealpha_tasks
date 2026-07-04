import os
import shutil

source_folder = "test_folder2"
destination_folder = "test_folder1"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files=os.listdir(source_folder)

for file in files:
    
    if file.endswith(".jpg"):
        if(file.endswith(".pdf") or file.endswith(".jpeg") or file.endswith(".Docx")):
            continue
        
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"{file} moved successfully!")

print("Task completed.")