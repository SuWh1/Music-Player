import os
import pygame

def remove_corrupted_mp3(folder_path):
    pygame.mixer.init()

    files = os.listdir(folder_path)

    for file_name in files:
        if file_name.lower().endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            try:
                pygame.mixer.music.load(file_path)
            except pygame.error as e:
                print(f"Error loading {file_name}: {e}. Removing...")
                os.remove(file_path)
                print(f"{file_name} removed.")

# Example usage
folder_path = r"C:\Users\ROG-ASUS\Musika\MyMusicPlayer"
remove_corrupted_mp3(folder_path)
