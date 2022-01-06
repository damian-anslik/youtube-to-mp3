import youtube_dl
import os


def get_download_path(download_dir: str) -> os.path:
    """  
    Get the path for the download dir, create dir if one doesnt exist
    """
    download_path = os.getcwd().join([download_dir]) 
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    return download_path


def download_audio_single(url: str, download_dir: str = None) -> str:
    """
    Download the audio from a specified URL and save it locally, return the path of the download
    """
    file_data = youtube_dl.YoutubeDL().extract_info(url, download=False)
    if download_dir is None or len(download_dir)==0:
        download_dir = "downloads"
    title = file_data["title"]
    filename = f"{title}.mp3"
    download_path = get_download_path(download_dir)
    full_download_path = os.path.join(download_path, filename)
    download_options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": full_download_path
    }
    with youtube_dl.YoutubeDL(download_options) as downloader:
        downloader.download(url_list=[url])
    return str(full_download_path)


def download_audio_multiple(url_list: list[str], download_dir: str = None) -> list[str]:
    """  
    Iterates over a list of audio URLs and downloads each title
    """
    downloaded_filepaths = []
    for url in enumerate(url_list):
        try:
            downloaded_filename = download_audio_single(url, download_dir)
            downloaded_filepaths.append(downloaded_filename)
        except youtube_dl.DownloadError as download_exception:
            print(f"SKIPPING: Encountered an exception while attempting to download URL: {url} - {download_exception}")
            continue
    return downloaded_filepaths