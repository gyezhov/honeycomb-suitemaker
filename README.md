# Greg's Honeycomb GGL Rainmeter Skins

## Project Overview

This project automates the creation and management of Rainmeter skins, specifically designed for a skin set called "Greg's Honeycomb GGL." The project involves organizing icon images and background wallpapers, configuring the appropriate Rainmeter `.ini` files, and ensuring a clean structure for easy deployment and customization.

## Directory Structure

```
GregsHoneycombGGL/
│
├── @Resources/
│   └── Images/
│       └── *.png            # Icon images for applications
│
├── {AppName}/
│   ├── {AppName}.ini        # Main configuration file for the skin
│   ├── Background/
│   │   ├── background.ini   # Configuration file for the background
│   │   └── {AppName}.jpg    # Background wallpaper for the skin
│   └── ...                  # Additional skins for the same app, if any
│
└── ...
```


## Project Components

1. **@Resources/Images**:
   - Contains all the icon images for the applications, stored as PNG files. These images are referenced in the `.ini` configuration files for each skin.

2. **{AppName} Folders**:
   - Each application has its own folder named after the application (e.g., "Chrome").
   - Inside each folder:
     - `{AppName}.ini`: The main configuration file for the application skin.
     - `Background`: A folder containing the `background.ini` and the associated background wallpaper (`.jpg`).

## Functionality

- **Icon Image Handling**:
  - All icon images are collected from a specified source directory and moved to the `@Resources/Images` directory.

- **Skin Copying and Updating**:
  - Skins from an existing directory, "Honeycomb + GGL," are copied to `GregsHoneycombGGL`. This includes ensuring that backgrounds and additional skins are also copied over.
  - The script updates the image paths in the `.ini` files to reference the new location in `@Resources/Images`.

- **Background Management**:
  - Background wallpapers are stored in the `Background` folder for each application. The script moves corresponding `.jpg` wallpapers to these folders, creating new skins if they don't exist.

## Usage Instructions

1. **Setup**:
   - Place all icon images in a designated folder (specified by `images_dir` in the script).
   - Place all background wallpapers in a designated folder (specified by `wallpapers_dir` in the script).
   - Ensure the existing skins are available in the "Honeycomb + GGL" directory.

2. **Execution**:
   - Run the provided script to automatically organize and set up the skins in the `GregsHoneycombGGL` directory.

3. **Customization**:
   - You can customize each skin by modifying the `.ini` files. The icon and background image paths are already correctly set up to point to the `@Resources/Images` and the respective `Background` folders.

## Output Report

After the script runs, a summary report is generated, detailing the following for each skin:
- **App Name**: The name of the application/skin.
- **Has Background**: Indicates whether a background image is present.
- **Has Icon Image**: Indicates whether an icon image is present and correctly referenced.

This report helps in verifying that all necessary assets are in place and correctly configured.

## Contributions

Contributions are welcome! If you have any suggestions for improvement or additional features, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This project was created to streamline the management of Rainmeter skins, making it easier to customize and deploy a visually appealing desktop experience. Happy customizing!
