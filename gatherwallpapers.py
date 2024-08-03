import os
import shutil

# Define the path to the Honeycomb + GGL directory and the destination Wallpapers directory
honeycomb_path = 'path_to_Honeycomb_GGL_directory'
wallpapers_path = 'path_to_Wallpapers_directory'

# Ensure the Wallpapers directory exists
os.makedirs(wallpapers_path, exist_ok=True)

# Loop through each skin directory in the Honeycomb + GGL directory
for skin in os.listdir(honeycomb_path):
    skin_path = os.path.join(honeycomb_path, skin)
    background_path = os.path.join(skin_path, 'Background')
    background_ini_path = os.path.join(background_path, 'background.ini')

    # Check if the Background directory and background.ini file exist
    if os.path.exists(background_path) and os.path.exists(background_ini_path):
        # Read the background.ini file to find the ImageName
        with open(background_ini_path, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            if 'ImageName' in line:
                image_name = line.split('=')[1].strip().replace('"', '')
                image_path = os.path.join(background_path, image_name)
                
                # Check if the image file exists and copy it to the Wallpapers directory
                if os.path.exists(image_path):
                    destination = os.path.join(wallpapers_path, os.path.basename(image_path))
                    shutil.copyfile(image_path, destination)
                    print(f"Copied {image_path} to {destination}")
                break