import os
import shutil

# Paths
base_dir = r'GregsHoneycombGGL'
images_dir = r'C:\Users\gyezhov\Pictures\Logos\Finished Icons'  # Replace with the actual path to your images folder
honeycomb_ggl_dir = r'C:\Users\gyezhov\Documents\Rainmeter\Skins\Honeycomb + GGL'
wallpapers_dir = r'C:\Users\gyezhov\Pictures\Wallpapers'  # Replace with the actual path to your wallpapers folder

# Template for background.ini
background_template = """[Rainmeter]
OnRefreshAction=!ZPos "-2"

[Wallpaper]
Meter = Image
ImageName = {image_name}
"""

# Template for app.ini
app_template = """[{app_name}]
Meter=Image
ImageName=#@#Images\\{image_name}
H=90
MouseOverAction=[!ActivateConfig "GregsHoneycombGGL\\{app_name}\\Background" "background.ini"]
MouseLeaveAction=[!DeactivateConfig "GregsHoneycombGGL\\{app_name}\\Background" "background.ini"]
LeftMouseUpAction=[]
"""

# Create @Resources/Images directory
resources_images_dir = os.path.join(base_dir, '@Resources', 'Images')
os.makedirs(resources_images_dir, exist_ok=True)

# Move all images from images_dir to @Resources/Images
for image in os.listdir(images_dir):
    if image.endswith('.png'):
        shutil.move(os.path.join(images_dir, image), os.path.join(resources_images_dir, image))

# Function to copy skins and ensure they exist in GregsHoneycombGGL
def copy_skins(src, dest):
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith('.ini'):
                src_file = os.path.join(root, file)
                relative_path = os.path.relpath(src_file, src)
                dest_file = os.path.join(dest, relative_path)
                dest_dir = os.path.dirname(dest_file)

                # Ensure the destination directory exists
                os.makedirs(dest_dir, exist_ok=True)

                # Copy the .ini file if it doesn't exist in the destination or if it's a new skin
                if not os.path.exists(dest_file):
                    shutil.copy2(src_file, dest_file)

                # Check for and move background wallpapers
                if 'Background' in dest_dir:
                    wallpaper_path = os.path.join(root, 'background.ini')
                    if os.path.exists(wallpaper_path):
                        shutil.copy2(wallpaper_path, os.path.join(dest_dir, 'background.ini'))

# Copy skins from Honeycomb + GGL to GregsHoneycombGGL
copy_skins(honeycomb_ggl_dir, base_dir)

# Move images from Honeycomb + GGL skins to @Resources/Images
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.ini'):
            ini_file = os.path.join(root, file)
            with open(ini_file, 'r') as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                if 'ImageName=' in line:
                    image_path = line.split('=')[1].strip()
                    image_name = os.path.basename(image_path)
                    # Move image to @Resources/Images
                    src_image_path = os.path.join(honeycomb_ggl_dir, image_path.replace('#@#', '@Resources'))
                    dest_image_path = os.path.join(resources_images_dir, image_name)
                    if os.path.exists(src_image_path):
                        shutil.move(src_image_path, dest_image_path)
                        new_line = line.replace(image_path, '#@#Images\\' + image_name)
                    else:
                        new_line = line
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
            # Write the updated ini file
            with open(ini_file, 'w') as f:
                f.writelines(new_lines)

# Move jpg wallpapers to their respective Background folders and create skins if necessary
for wallpaper in os.listdir(wallpapers_dir):
    if wallpaper.endswith('.jpg'):
        app_name = os.path.splitext(wallpaper)[0]
        wallpaper_path = os.path.join(wallpapers_dir, wallpaper)
        background_dir = os.path.join(base_dir, app_name, 'Background')

        # Ensure the Background directory exists
        os.makedirs(background_dir, exist_ok=True)

        # Move the wallpaper to the Background directory
        shutil.move(wallpaper_path, os.path.join(background_dir, wallpaper))

        # Check if an app-specific .ini file exists, create one if it doesn't
        app_ini_file = os.path.join(base_dir, app_name, f'{app_name}.ini')
        if not os.path.exists(app_ini_file):
            with open(app_ini_file, 'w') as f:
                f.write(app_template.format(app_name=app_name, image_name=f'{app_name}.png'))

print("Skins and resources have been successfully set up!")