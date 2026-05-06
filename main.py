# Image Organizer v1.3
# Features: Added GUI folder selection (Browse window)

import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image
import shutil
import sys


# This method returns the selected path as a string
def select_folder():
    root = tk.Tk()
    root.withdraw()  # hide the main window
    root.attributes('-topmost', True)  # bring the window on top of the other windows

    selected_path = filedialog.askdirectory(title="Select Folder")  # returns the path as string
    root.destroy()  # clean root object
    return selected_path


def main():
    try:
        selected_path = select_folder()
        if not selected_path:
            print("Operation cancelled by user!")
            sys.exit()

        # initialize the folder paths:
        source_folder_dir = Path(selected_path)
        horizontal_dir = source_folder_dir / "horizontal"
        vertical_dir = source_folder_dir / "vertical"
        square_dir = source_folder_dir / "square"

        # check if there are any image files in the source folder
        image_extensions = ('.png', '.jpg', '.jpeg', '.webp')
        images = [f for f in source_folder_dir.iterdir() if f.suffix.lower().endswith(image_extensions)]

        if not images:
            print(f"No images found to organize in: {source_folder_dir}")
            sys.exit()

        # create the folders if they do not exist
        for folder in [horizontal_dir, vertical_dir, square_dir]:
            folder.mkdir(parents=True, exist_ok=True)
        print("-" * 40)
        print(f"{len(images)} images found. Starting organization...\n" + "-" * 40)

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
        print("-" * 40)
        print(f"Success: {len(images)} images have been organized!")
    except Exception as ex:
        print(f"Something went wrong: {ex}")


if __name__ == "__main__":
    main()
