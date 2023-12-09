import os
import shutil

def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            file_extension = filename.split('.')[-1].lower()
            destination_path = os.path.join(destination_folder, file_extension)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            shutil.move(source_path, os.path.join(destination_path, filename))

if __name__ == "__main__":
    # Specify the source and destination folders
    source_folder = "path/to/source/folder"
    destination_folder = "path/to/destination/folder"

    organize_files(source_folder, destination_folder)
    print("File organization completed.")
