from mutagen.easyid3 import EasyID3

def get_artist_name(file_path):
    try:
        audio = EasyID3(file_path)
        artist = audio["artist"][0]
        return artist
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
file_path = r"C:\Users\ROG-ASUS\Musika\Best\7 Days.mp3"
artist_name = get_artist_name(file_path)
if artist_name:
    print(f"The artist is: {artist_name}")
else:
    print("Unable to retrieve artist information.")