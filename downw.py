def hello():
    print("Hello from downw!")


# def downw():
#     print("downw.py is being run directly")
#     hello()

# download and store in current directory
def download_with_youtube_dl(url):
    import youtube_dl
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # name of file
        ydl.download([url])
    return "Downloaded"


def download_with_pytube(url):
    from pytube import YouTube
    yt = YouTube(url)
    print(yt.title)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download()
    print("Downloaded")
    return yt.title


download_with_youtube_dl("https://www.youtube.com/watch?v=9bZkp7q19f0")
