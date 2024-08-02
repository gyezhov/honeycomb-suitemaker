import os

# Paths
base_dir = 'GregsHoneycombGGL'
images_dir = r'C:\Users\gyezhov\Pictures\Logos\Finished Icons'  # Replace with the actual path to your images folder

# Ensure the base directory exists
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Get list of PNG files in the images directory
images = [f for f in os.listdir(images_dir) if f.endswith('.png')]

# Template for background.ini
background_template = """[Rainmeter]
OnRefreshAction=!ZPos "-2"

[Wallpaper]
Meter = Image
ImageName = {image_name}
"""

# Template for chrome.ini
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
    with open(os.path.join(background_dir, 'background.ini'), 'w') as f:
        f.write(background_template.format(image_name=f'{app_name}.jpg'))

    # Write app.ini (e.g., chrome.ini)
    with open(os.path.join(app_dir, f'{app_name}.ini'), 'w') as f:
        f.write(app_template.format(app_name=app_name, image_name=image))

print("Skins created successfully!")
