import os
from shutil import move

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

file_mappings = {
    'pdf': 'PDFs',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'pptx': 'Documents',
    'docx': 'Documents',
    'xlsx': 'Documents',
    'exe': 'Applications',
    'enw': 'References',
    'zip': 'Compressed',
}


default_folder = 'Miscellaneous'

def sort_files(downloads_folder):
    for filename in os.listdir(downloads_folder):
        
        file_path = os.path.join(downloads_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine the destination folder based on the file extension
        file_extension = filename.split('.')[-1].lower()
        dest_folder_name = file_mappings.get(file_extension, default_folder)
        dest_folder_path = os.path.join(downloads_folder, dest_folder_name)
        
        # Create the destination folder if it doesn't exist
        if not os.path.exists(dest_folder_path):
            os.mkdir(dest_folder_path)
        
        # Construct the destination file path
        dest_file_path = os.path.join(dest_folder_path, filename)

        # Handle potential filename conflicts
        counter = 1
        base_filename, extension = os.path.splitext(filename)
        while os.path.exists(dest_file_path):
            dest_file_path = os.path.join(dest_folder_path, f"{base_filename}_{counter}{extension}")
            counter += 1
        
        # Move the file to the destination folder
        move(file_path, dest_file_path)
        print(f'Moved {filename} to {dest_file_path}')

def main():
    sort_files(downloads_path)
    print('Downloads sorted.')

if __name__ == "__main__":
    main()
