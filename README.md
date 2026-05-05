# Image Organizer

A lightweight Python utility designed to automatically categorize image files (wallpapers) based on their **aspect ratio**[cite: 1].

## 🚀 Overview
This script scans a specified directory and sorts images into three sub-folders:
*   **Horizontal:** Width > Height[cite: 1]
*   **Vertical:** Height > Width[cite: 1]
*   **Square:** Width == Height[cite: 1]

## 🛠 Tech Stack
*   **Language:** Python 3.x[cite: 1]
*   **Libraries:** `Pillow`, `os`, `shutil`[cite: 1]

## ⚙️ Key Features
*   **Resource Management:** Implements `with` context managers to ensure file locks are released, preventing `WinError 32`[cite: 1].
*   **Guard Clauses:** Includes directory filtering to skip sub-folders and prevent recursive processing errors[cite: 1].
*   **Format Support:** Handles `.png`, `.jpg`, `.jpeg`, and `.webp`[cite: 1].

## 📖 How to Use
1.  **Install requirements:** `pip install Pillow`[cite: 1]
2.  **Configuration:** Update the `source_dir` variable in the script with your local path[cite: 1].
3.  **Run:** `python image_organizer.py`[cite: 1]

---
*Developed as a micro-automation utility for efficient asset management.*[cite: 1]