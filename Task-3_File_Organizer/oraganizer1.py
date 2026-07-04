import os
import shutil

source_folder="test_folder2"
destination_folder="test_folder1"

if os.path.exists(destination_folder):
    print("The Destination folder is already exists")
else:
    os.makedirs(destination_folder)

count=0
files=os.listdir(source_folder)

for file in files:

    if file.lower().endswith(".jpg"):
        
        source_path=os.path.join(source_folder,file)
        destination_path=os.path.join(destination_folder,file)

        shutil.move(source_path,destination_path) 
        count+=1

    print(f"{file} moved succesfully!")   

print(f"Task Completed,Total files moved {count} out of {len(files)}")
