import os
import sys
import yt_dlp
from pytube import Search

# List of songs
songs = [
    "Flans - Bazar",
    "Timbiriche - Tu y Yo Somos Uno Mismo",
    "Magneto - Vuela Vuela",
    "Pandora - Cómo Te Va Mi Amor",
    "Luis Miguel - La Incondicional",
    "Yuri - Maldita Primavera",
    "Emmanuel - Toda La Vida",
    "Mijares - Bella",
    "Miguel Bosé - Amante Bandido",
    "Alejandra Guzmán - Hacer El Amor Con Otro",
    "Gloria Trevi - Dr. Psiquiatra",
    "Maná - Rayando El Sol",
    "Caifanes - La Negra Tomasa",
    "Madonna - Like a Virgin",
    "Michael Jackson - Billie Jean",
    "Cyndi Lauper - Girls Just Want to Have Fun",
    "Queen - Another One Bites the Dust",
    "Depeche Mode - Just Can't Get Enough",
    "Rick Astley - Never Gonna Give You Up",
    "Whitney Houston - I Wanna Dance with Somebody",
    "Duran Duran - Hungry Like the Wolf",
    "Prince - 1999",
    "The Human League - Don't You Want Me",
    "Eurythmics - Sweet Dreams (Are Made of This)",
    "Billy Idol - Dancing with Myself",
    "Bonnie Tyler - Total Eclipse of the Heart",
    "Boney M - Rasputin",
    "A-ha - Take On Me",
    "Tears for Fears - Everybody Wants to Rule the World",
    "Culture Club - Karma Chameleon",
    "Lionel Richie - All Night Long",
    "Wham! - Wake Me Up Before You Go-Go",
    "Chaka Khan - I Feel for You",
    "Kool & The Gang - Celebration",
    "INXS - Need You Tonight",
    "Men at Work - Down Under",
    "Pet Shop Boys - West End Girls",
    "New Order - Blue Monday",
    "Soft Cell - Tainted Love",
    "Falco - Rock Me Amadeus",
    "George Michael - Faith",
    "Toto - Africa",
    "Simple Minds - Don't You (Forget About Me)",
    "Hall & Oates - Maneater",
    "Phil Collins - You Can't Hurry Love",
    "Genesis - Invisible Touch",
    "The Bangles - Walk Like an Egyptian",
    "Erasure - A Little Respect",
    "Dead or Alive - You Spin Me Round (Like a Record)",
    "Baltimora - Tarzan Boy",
    "Modern Talking - Brother Louie",
    "Spandau Ballet - True",
    "Roxette - The Look",
    "Fine Young Cannibals - She Drives Me Crazy",
    "Pointer Sisters - I'm So Excited",
    "Cameo - Word Up!",
    "Kim Wilde - Kids in America",
    "Pat Benatar - Love Is a Battlefield",
    "Blondie - Call Me",
    "The Police - Every Breath You Take",
    "R.E.M. - It's the End of the World as We Know It",
    "ABC - The Look of Love",
    "The Clash - Should I Stay or Should I Go",
    "Dexys Midnight Runners - Come On Eileen",
    "Laura Branigan - Gloria",
    "Belinda Carlisle - Heaven Is a Place on Earth",
    "Bryan Adams - Summer of '69",
    "Cyndi Lauper - Time After Time",
    "Alphaville - Big in Japan",
    "Thompson Twins - Hold Me Now",
    "Wang Chung - Dance Hall Days",
    "The B-52's - Love Shack",
    "Tina Turner - What's Love Got to Do with It",
    "Frankie Goes to Hollywood - Relax",
    "Talking Heads - Burning Down the House",
    "Sade - Smooth Operator",
    "Steve Winwood - Higher Love",
    "Peter Gabriel - Sledgehammer",
    "Belouis Some - Imagination",
    "Van Halen - Jump",
    "Europe - The Final Countdown",
    "U2 - With or Without You",
    "John Farnham - You're the Voice",
    "The Cure - Just Like Heaven",
    "The Smiths - There Is a Light That Never Goes Out",
    "Devo - Whip It",
    "Simple Minds - Alive and Kicking",
    "The Cars - Drive",
    "Kajagoogoo - Too Shy",
    "Thompson Twins - Doctor! Doctor!",
    "Rick Springfield - Jessie's Girl",
    "OMD - If You Leave",
    "Robert Palmer - Addicted to Love",
    "Starship - We Built This City",
    "Bruce Springsteen - Dancing in the Dark",
    "The Rolling Stones - Start Me Up",
    "Nena - 99 Luftballons",
    "Katrina and the Waves - Walking on Sunshine",
    "Bon Jovi - Livin' on a Prayer",
    "Foreigner - I Want to Know What Love Is"
]

# Create a folder to store the downloaded songs
os.makedirs("songs", exist_ok=True)


def download_song(song):
    # Search for the song on YouTube
    search = Search(song)
    video = search.results[0]
    url = video.watch_url

    # Define download options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'songs/{song}.%(ext)s',
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
for song in songs:
    try:
        print(f"Downloading: {song}")
        download_song(song)
    except Exception as e:
        print(f"Failed to download {song}: {e}")
