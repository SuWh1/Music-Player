import os
import zipfile

def remove_specific_string_from_filename(directory_path, string_to_remove):
    for filename in os.listdir(directory_path):
        old_file_path = os.path.join(directory_path, filename)
        if os.path.isfile(old_file_path) and filename.endswith('.mp3'):
            new_filename = filename.replace(string_to_remove, '')
            new_file_path = os.path.join(directory_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed file: {old_file_path} to {new_file_path}")

directory_path = ""

zip_path = r"C:\Users\ROG-ASUS\Musika\Best.zip"
directory_path = r"C:\Users\ROG-ASUS\Musika\Best"

if os.path.isfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(directory_path)
    print(f"Extracted the contents of '{zip_path}' to '{directory_path}'.")
else:
    print(f"The file '{zip_path}' does not exist.")
    
# Define the specific string to remove
string_to_remove = '[SPOTIFY-DOWNLOADER.COM] '

# Rename files in the directory
remove_specific_string_from_filename(directory_path, string_to_remove)

print("Processing complete!")
