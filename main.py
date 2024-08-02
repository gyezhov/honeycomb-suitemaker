import os
import shutil
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Create Rainmeter skins with background images.")
parser.add_argument('images_dir', type=str, help='Path to the folder containing app icon images.')
parser.add_argument('wallpapers_dir', type=str, help='Path to the folder containing ultra-wide wallpapers.')

# Parse arguments
args = parser.parse_args()
images_dir = args.images_dir
wallpapers_dir = args.wallpapers_dir

# Paths
base_dir = 'GregsHoneycombGGL'

# Ensure the base directory exists
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Get list of PNG files in the images directory
images = [f for f in os.listdir(images_dir) if f.endswith('.png')]
# Get list of JPG wallpapers in the wallpapers directory
wallpapers = {os.path.splitext(f)[0]: f for f in os.listdir(wallpapers_dir) if f.endswith('.jpg')}

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

# Create skins for each app
for image in images:
    app_name = os.path.splitext(image)[0]
    app_dir = os.path.join(base_dir, app_name)
    background_dir = os.path.join(app_dir, 'Background')

    # Create directories if they don't exist
    os.makedirs(background_dir, exist_ok=True)

    # Write background.ini
    background_ini_path = os.path.join(background_dir, 'background.ini')
    with open(background_ini_path, 'w') as f:
        f.write(background_template.format(image_name=f'{app_name}.jpg'))

    # Copy and rename the corresponding wallpaper
    wallpaper_name = wallpapers.get(app_name)
    if wallpaper_name:
        original_wallpaper_path = os.path.join(wallpapers_dir, wallpaper_name)
        new_wallpaper_path = os.path.join(background_dir, f'{app_name}.jpg')
        shutil.copyfile(original_wallpaper_path, new_wallpaper_path)

    # Write app.ini (e.g., chrome.ini)
    app_ini_path = os.path.join(app_dir, f'{app_name}.ini')
    with open(app_ini_path, 'w') as f:
        f.write(app_template.format(app_name=app_name, image_name=image))

print("Skins and wallpapers created successfully!")
