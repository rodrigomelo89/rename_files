import os

folder_path = 'C:\\Users\\User\\Documents\\codes\\fluencia-NAO\\base_de_dados\\incorretas'  # Specify the folder path where the files are located

# List all files in the folder
files = os.listdir(folder_path)

for filename in files:
    # Construct the old and new file paths
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, 'I' + filename)  # Add a prefix to the new file name

    # Rename the file
    os.rename(old_file_path, new_file_path)

print('File names have been changed successfully.')
