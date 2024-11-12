import os
import shutil

# Define the source directory to organize (e.g., "Downloads")
source_dir = "/path/to/your/Downloads"

# Define folder categories and corresponding file extensions
file_categories = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".xls", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".dmg"],
    "Others": []  # Catch-all for uncategorized files
}

# Function to create directories if they don't exist
def create_directories():
    for folder_name in file_categories.keys():
        folder_path = os.path.join(source_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to categorize and move files
def organize_files():
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move file to corresponding folder
        moved = False
        for folder_name, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination = os.path.join(source_dir, folder_name, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename} -> {folder_name}")
                moved = True
                break

        # Move uncategorized files to "Others" folder
        if not moved:
            destination = os.path.join(source_dir, "Others", filename)
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> Others")

# Main function to execute the organizer
def main():
    create_directories()
    organize_files()
    print("File organization completed.")

# Run the script
if __name__ == "__main__":
    main()
