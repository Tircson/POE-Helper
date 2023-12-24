import os
import mutagen

def rename_music_files(folder_path):
    # Durchsuche alle Audiodateien im Ordner
    audio_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp3', '.flac', '.wav','m4a'))]

    for file_name in audio_files:
        file_path = os.path.join(folder_path, file_name)

        try:
            # Lese die Metadaten der Datei
            mp3 = mutagen.File(file_path)
            title = mp3.get("TIT2")
            album = mp3.get("TALB")
            album = str(album).replace(':','')
            album = str(album).replace("'", '')
            album = str(album).replace("?", '')
            album = str(album).replace("/", '')

            title = str(title).replace(':','')
            title = str(title).replace("'", '')
            title = str(title).replace("?", '')
            title = str(title).replace("/", '')
            title = str(title).replace('"', '')

            # Erstelle den neuen Dateinamen
            new_file_name = f"{title} -_- {str(album).replace('/','').replace(':','').replace('?','')}.mp3"

            # Erstelle den neuen Dateipfad
            new_file_path = os.path.join(folder_path, new_file_name)

            # Überprüfe, ob der neue Dateiname bereits existiert
            if not os.path.exists(new_file_path):
                os.rename(file_path, new_file_path)
                print(f"Erfolgreich umbenannt: {new_file_name}")
            else:
                print(f"Datei existiert bereits: {new_file_name}")

        except Exception as e:
            print(f"Fehler beim Bearbeiten von {file_name}: {e}")

if __name__ == "__main__":
    folder_path = r"G:\Musik\Spotiflyer\Playlists\Neuer Ordner"  # Passe dies an den tatsächlichen Ordnerpfad an
    rename_music_files(folder_path)
    print("Umbenennung abgeschlossen.")