from app import download_audio_single, download_audio_multiple

DOWNLOAD_SINGLE = True
DOWNLOAD_DIRECTORY = "downloads"
EXAMPLE_URLS = [
    "https://www.youtube.com/watch?v=qod03PVTLqk",
    "https://www.youtube.com/watch?v=qod03PVTLqk"
]

if __name__=="__main__":
    if DOWNLOAD_SINGLE:
        downloaded_file = download_audio_single(EXAMPLE_URLS[-1], download_dir=DOWNLOAD_DIRECTORY)
        print(downloaded_file)
    else:
        download_audio_multiple(EXAMPLE_URLS, download_dir=DOWNLOAD_DIRECTORY)