import os
import yt_dlp

# List of songs with YouTube IDs
songs = [
    # ("RETRO PARTY (Fiesta retro en ESPAÑOL / 80s, 90s, 00s / a que te sabes TODAS) | Dj Ricardo Muñoz", "n5V4cyEcYoY"),
    # ("PSY - GANGNAM STYLE(강남스타일) M/V", "9bZkp7q19f0"),
    # ("POP RETRO(Shaggy, Sean Paul, Bruno Mars, Bob Marley, Eminen, Will Smith) RELAX MUSIC 1", "elEukrbtTHE"),
    # ("Banda MS, La Adictiva, La Arrolladora, Banda El Recodo Mix Bandas Románticas ~ Lo Mas Nuevo 2024", "lhttmwSzubU"),
    # ("DJ JOSEMA - BOHEMIA RHAPSODY - ELECTRO MIX 2021", "8ommbqqhtIo")
    # ("SET ALETEO  # 1 | LO NUEVO | Dj Alan Quiñonez", "ID018mrBnqg")
    ("Banda Machos Vs Banda Maguey Quebraditas Mix Dj Scorpio", "OYBIjCMVgCo")
]

# Create a folder to store the downloaded songs
os.makedirs("new_songs", exist_ok=True)


def download_song(song, video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"

    # Define download options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'new_songs/{song}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Download the song
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"Downloaded: {song}")


# Iterate over the list of songs and download each one
for song, video_id in songs:
    try:
        print(f"Downloading: {song}")
        download_song(song, video_id)
    except Exception as e:
        print(f"Failed to download {song}: {e}")

print("All downloads completed!")
