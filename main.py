# Image Organizer v1.2
# The folder must be on Desktop located!

from pathlib import Path
from PIL import Image
import shutil

# initialize the folder paths:
desktop_dir = Path.home() / "Desktop"
user_input_folder_name = input("Enter the image folder name: ").lower()
source_folder_dir = desktop_dir / user_input_folder_name

horizontal_dir = source_folder_dir / "horizontal"
vertical_dir = source_folder_dir / "vertical"
square_dir = source_folder_dir / "square"

# check if there are any image files in the source folder
try:
    image_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    images = [f for f in source_folder_dir.iterdir() if f.suffix.lower().endswith(image_extensions)]

    if not images:
        print(f"There are no images to be organized in <{source_folder_dir}>!")
        exit()
    else:
        # create the folders if they do not exist
        for folder in [horizontal_dir, vertical_dir, square_dir]:
            folder.mkdir(parents=True, exist_ok=True)
        print("------------------- o -------------------")
        print(f"{len(images)} images found. Starting organization...\n------------------- o -------------------")

        for file_path in images:
            # if it's a folder, skip
            if file_path.is_dir():
                continue

            try:
                # open the file and get the resolution
                with Image.open(file_path) as img:
                    width, height = img.size

                # sort the files based on their resolutions
                if width > height:
                    target_path = horizontal_dir / file_path.name
                elif height > width:
                    target_path = vertical_dir / file_path.name
                else:
                    target_path = square_dir / file_path.name

                # move the files to the target folders
                shutil.move(file_path, target_path)
                print(f"Moved: {file_path.name}")

            except Exception as e:
                print(f"Something went wrong when moving '{file_path.name}': {e}")
        print(f"------------------- o -------------------\nSuccess: {len(images)} Images have been organized!")
except FileNotFoundError:
    print(f"'{user_input_folder_name}' was not found in '{source_folder_dir}'")



