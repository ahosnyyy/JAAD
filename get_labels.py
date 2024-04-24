import os
import shutil

def copy_txt_files(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        # Construct the corresponding destination directory path
        relative_path = os.path.relpath(root, source_dir)
        dest_subdir = os.path.join(dest_dir, relative_path)

        # Create the destination directory if it doesn't exist
        os.makedirs(dest_subdir, exist_ok=True)

        for file in files:
            if file.endswith('.png'):
                png_file = os.path.join(root, file)
                txt_file = os.path.join(root.replace('corrupted_jaad10_test/brightness/severity_1', 'labels_bu/labels'), file.replace('.png', '.txt'))

                if os.path.exists(txt_file):
                    shutil.copy(txt_file, dest_subdir)

# Specify the source directory path
source_directory = 'corrupted_jaad10_test/brightness/severity_1'

# Specify the destination directory path
destination_directory = 'temp'

# Call the function to copy the TXT files while maintaining the folder structure
copy_txt_files(source_directory, destination_directory)