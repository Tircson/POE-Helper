import os

def read_song_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Fehler beim Lesen der Songliste: {e}")
        return []

def compare_and_write_to_file(folder_path, song_list_file, output_file):
    # Durchsuche alle Audiodateien im Ordner
    audio_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp3', '.flac', '.wav'))]

    # Lese die Songliste aus der Textdatei
    song_list = read_song_list(song_list_file)

    # Finde die fehlenden Titel in der Liste
    missing_titles = [title for title in song_list if not any(file.lower().replace(" ","") in title.lower().replace(" ","")  for file in audio_files)]

    # Schreibe die fehlenden Titel in die Ausgabedatei
    with open(output_file, 'w', encoding='utf-8') as file:
        for title in missing_titles:
            file.write(f"{title}\n")

if __name__ == "__main__":
    folder_path = r"G:\Musik\Spotiflyer\Playlists\Meins"  # Passe dies an den tatsächlichen Ordnerpfad an
    song_list_file = "G:\Musik\Spotiflyer\Playlists\playlist_tracks.txt"  # Passe den Pfad zur Textdatei mit der Songliste an
    output_file = "G:\Musik\Spotiflyer\Playlists\missing_titles.txt"  # Passe den Namen der Ausgabedatei an

    compare_and_write_to_file(folder_path, song_list_file, output_file)
    print("Vorgang abgeschlossen.")