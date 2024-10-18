import pygame
import tkinter as tk
from tkinter import filedialog
import os
import random   
from mutagen.easyid3 import EasyID3


pygame.init()
pygame.display.init()
pygame.display.set_mode((1, 1))
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, music_folder, label):
        self.playlist = []
        self.current_index = 0
        self.label = label
        self.load_music_files(music_folder)
        
        if self.playlist:
            self.load_music(self.playlist[self.current_index])

        pygame.mixer.music.set_endevent(pygame.USEREVENT)

    def load_music_files(self, music_folder):
        for file_name in os.listdir(music_folder):
            if file_name.endswith(('.mp3', '.wav', '.ogg')):
                file_path = os.path.join(music_folder, file_name)
                self.playlist.append(file_path)
        random.shuffle(self.playlist)

    def load_music(self, file_path):
        pygame.mixer.music.load(file_path)
        self.update_label(file_path)

    def play_music(self):
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def next_music(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.load_music(self.playlist[self.current_index])
            self.play_music()

    def back_music(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.load_music(self.playlist[self.current_index])
            self.play_music()

    def choose_song(self):
        file_path = filedialog.askopenfilename(filetypes=(("Audio Files", "*.mp3;*.wav;*.ogg"),))
        if file_path:
            if file_path in self.playlist:
                self.playlist.remove(file_path)
            
            self.playlist.insert(self.current_index + 1, file_path)
            self.current_index += 1
            self.load_music(file_path)
            self.play_music()
            
    def get_artist_name(self, file_path):
        try:
            audio = EasyID3(file_path)
            artist = audio["artist"][0]
            return artist
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def update_label(self, file_path):
        song_name = os.path.basename(file_path)
        artist_name = self.get_artist_name(file_path)
        self.label.config(text = f"Now playing: {artist_name} - {song_name[:-4]}")
        
root = tk.Tk()
root.title("Simple Music Player")
root.geometry("400x300")

song_label = tk.Label(root, text="No song playing", bg="black", fg="white", font=("Helvetica", 10))
song_label.grid(pady=20)

music_folder = os.path.expanduser("~/.vscode/MusicPlayer/Best")
player = MusicPlayer(music_folder, song_label)

# Create buttons
play_button = tk.Button(root, text="Play", command=player.play_music, bg="blue", fg="white", font=("Arial", 12))
pause_button = tk.Button(root, text="Pause", command=player.pause_music, bg="yellow", fg="black", font=("Arial", 12))
unpause_button = tk.Button(root, text="Unpause", command=player.unpause_music, bg="green", fg="white", font=("Arial", 12))
next_button = tk.Button(root, text="Next", command=player.next_music, bg="purple", fg="white", font=("Arial", 12))
back_button = tk.Button(root, text="Back", command=player.back_music, bg="red", fg="white", font=("Arial", 12))
choose_button = tk.Button(root, text="Choose Song", command=player.choose_song, bg="gray", fg="black", font=("Arial", 12))

# Arrange buttons using grid layout
play_button.grid(row=1, column=0, padx=10, pady=10)
pause_button.grid(row=1, column=1, padx=10, pady=10)
unpause_button.grid(row=1, column=2, padx=10, pady=10)
next_button.grid(row=2, column=0, padx=10, pady=10)
back_button.grid(row=2, column=1, padx=10, pady=10)
choose_button.grid(row=2, column=2, padx=10, pady=10)

def handle_music_end():
    player.next_music()

def event_loop():
    root.update() 
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            handle_music_end()
    root.after(100, event_loop)

event_loop()
root.mainloop()
