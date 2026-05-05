# Image Organizer

A lightweight Python utility designed to automatically categorize image files (wallpapers) based on their **aspect ratio**.

## 🚀 Overview
This script scans a specified directory and sorts images into three sub-folders:
*   **Horizontal:** Width > Height
*   **Vertical:** Height > Width
*   **Square:** Width == Height

## 🛠 Tech Stack
*   **Language:** Python 3.x
*   **Libraries:** `Pillow`, `os`, `shutil`

## ⚙️ Key Features
*   **Resource Management:** Implements `with` context managers to ensure file locks are released, preventing `WinError 32`.
*   **Guard Clauses:** Includes directory filtering to skip sub-folders and prevent recursive processing errors.
*   **Format Support:** Handles `.png`, `.jpg`, `.jpeg`, and `.webp`.

## 📖 How to Use
1.  **Install requirements:** `pip install Pillow`
2.  **Configuration:** Update the `source_dir` variable in the script with your local path.
3.  **Run:** `python image_organizer.py`

---
*Developed as a micro-automation utility for efficient asset management.*