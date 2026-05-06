import os
from pathlib import Path
from PIL import Image
import shutil

# initialize the folder paths:
# base directory
base_dir = Path.home() # C/Users/[pc-name]

# folder to get the images from
source_dir = base_dir / "Desktop/organizer"

# folders to sort the images
horizontal_dir = source_dir / "horizontal"
vertical_dir = source_dir / "vertical"
square_dir = source_dir / "square"

# check if there is any image file in the source folder
images = [f for f in os.listdir(source_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

if not images:
    print(f"There is no images to be organized in <{source_dir}>!")
    exit()
else:
    # create the folders if not exist
    for folder in [horizontal_dir, vertical_dir, square_dir]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            file_path = os.path.join(source_dir, filename)

            # if it's a folder, skip
            if os.path.isdir(file_path):
                continue

            try:
                # open the file and get the resolution
                with Image.open(file_path) as img:
                    width, height = img.size

                # sort the files based on their resolutions
                if width > height:
                    target_path = horizontal_dir / filename
                elif height > width:
                    target_path = vertical_dir / filename
                else:
                    target_path = square_dir / filename

                # move the files to the target folders
                shutil.move(file_path, target_path)
                print(f"Moved: {filename}")

            except Exception as e:
                print(f"Something went wrong when moving '{filename}': {e}")

    print("Images have been organized!")
