import os
from shutil import move
from datetime import datetime

# Define the paths
desktop_path = r"C:\Users\sabar\OneDrive\Desktop"
archive_root_path = r"C:\Users\sabar\Documents\Snaps"
# Exclude list
exclude = ['obsidian.lnk']

# Create a timestamped folder for the archived files
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
archive_folder_path = os.path.join(archive_root_path, f"Desktop_{timestamp}")

if not os.path.exists(archive_folder_path):
    os.makedirs(archive_folder_path)

print(f"Archiving items to {archive_folder_path}")

# Move files and folders from the desktop to the archive folder, excluding specified
for item in os.listdir(desktop_path):
    if item.lower() not in [name.lower() for name in exclude]:
        source_path = os.path.join(desktop_path, item)
        dest_path = os.path.join(archive_folder_path, item)
        
        print(f"Moving {source_path} to {dest_path}")
        move(source_path, dest_path)
        print(f"Moved {item} to {archive_folder_path}")

print('All items on the Desktop have been archived.')