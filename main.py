import youtube_dl
import os


def get_download_path(download_dir: str) -> os.path:
    """  
    Checks whether a particular directory exists, if not create one in current directory and return the path
    """
    download_path = os.path.join(os.getcwd(), download_dir)
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    return download_path


def download_audio_single(url: str, filename: str = None, download_dir: str = None):
    """  
    Download the audio from a specified URL and save it locally
    """
    file_data = youtube_dl.YoutubeDL().extract_info(url, download=False)
    if filename is None:
        title = file_data["title"]
        filename = f"{title}.mp3"
    if download_dir is None:
        download_dir = "downloads"
    download_path = get_download_path(download_dir)
    download_options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": os.path.join(download_path, filename)
    }
    with youtube_dl.YoutubeDL(download_options) as downloader:
        downloader.download(url_list=[url])


def download_audio_multiple(url_list: list[str], filename_list: list[str] = None, download_dir: str = None):
    """  
    Iterates over a list of audio URLs and downloads each title
    """
    if filename_list is None:
        filename_list = [None]*len(url_list)
    for url_id, url, filename in enumerate(zip(url_list, filename_list)):
        try:
            download_audio_single(url, download_dir, filename)
        except youtube_dl.DownloadError as download_exception:
            print(f"Encountered an exception while attempting to download URL: {url_id}:{url} - {download_exception}")
            continue
        

if __name__=="__main__":
    EXAMPLE_URL = "https://www.youtube.com/watch?v=qod03PVTLqk"
    # EXAMPLE_URLS = [
    #     "https://www.youtube.com/watch?v=qod03PVTLqk",
    #     "https://www.youtube.com/watch?v=qod03PVTLqk"
    # ]
    download_audio_single(EXAMPLE_URL, "download")


# def download_audio_multiple(url_list: list[str]) -> list[Song]:
#     pass


#     try:
#         with youtube_dl.YoutubeDL(download_options) as downloader:
#             downloader.download([video_info["webpage_url"]])
#         return f"{video_info['title']}.mp3"
#     except youtube_dl.utils.DownloadError:
#         print(f"Encountered an error while trying to retrieve audio from: {url}")
#         return None


# if __name__ == "__main__":
#     # Load script configuration file
#     with open("config.json", "r") as config_file:
#         config = json.load(config_file)

#     # Read urls from the text file
#     with open(config["dataFile"], "r") as data_file:
#         urls = data_file.read().splitlines()

#     # Loop over all urls contained in the text file
#     for url in urls:
#         downloaded_filename = download_audio(url, download_dir=config["downloadDir"])
#         if downloaded_filename is not None:
#             # If the file is downloaded succesfully, check if the converted file dir exists, and use ffmpeg to convert to mp3 from m4a
#             downloaded_filepath = os.path.join(
#                 config["downloadDir"], downloaded_filename
#             )
#             if not os.path.exists(config["convertedDir"]):
#                 os.mkdir(config["convertedDir"])
#             converted_filepath = os.path.join(
#                 config["convertedDir"], downloaded_filename
#             )
#             os.system(
#                 f"ffmpeg -i '{downloaded_filepath}' -c:v copy -c:a libmp3lame -q:a 4 '{converted_filepath}'"
#             )
