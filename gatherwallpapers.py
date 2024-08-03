import os
import shutil

# Define the path to the Honeycomb + GGL directory and the destination Wallpapers directory
honeycomb_path = r'C:\Users\gyezhov\Documents\Rainmeter\Skins\Honeycomb + GGL'
wallpapers_path = r'C:\Users\gyezhov\Pictures\Wallpapers'

# Ensure the Wallpapers directory exists
os.makedirs(wallpapers_path, exist_ok=True)

def copy_jpg_files(source_dir, dest_dir):
    # Create the destination directory if it does not exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(dest_dir, file)
                # Copy the jpg file to the destination directory
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} to {destination_file}")


copy_jpg_files(honeycomb_path, wallpapers_path)