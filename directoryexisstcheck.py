import os

directory_path = r'C:\Users\ROG-ASUS\Musika\Best'

if os.path.exists(directory_path):
    print(f"The directory exists: {directory_path}")
    for filename in os.listdir(directory_path):
        print(filename)
else:
    print(f"The directory does not exist: {directory_path}")
