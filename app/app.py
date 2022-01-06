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


def download_audio_single(url: str, filename: str = None, download_dir: str = None):
    """  
    Download the audio from a specified URL and save it locally
    """
    file_data = youtube_dl.YoutubeDL().extract_info(url, download=False)
    if filename is None:
        title = file_data["title"]
        filename = f"{title}.mp3"
    else:
        filename = f"{filename}.mp3"
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
    return filename


def download_audio_multiple(url_list: list[str], filename_list: list[str] = None, download_dir: str = None) -> list[str]:
    """  
    Iterates over a list of audio URLs and downloads each title
    """
    downloaded_files = []
    if filename_list is None:
        filename_list = [None]*len(url_list)
    for url, filename in zip(url_list, filename_list):
        try:
            downloaded_filename = download_audio_single(url, filename, download_dir)
            downloaded_files.append(downloaded_filename)
        except youtube_dl.DownloadError as download_exception:
            print(f"Encountered an exception while attempting to download URL: {url} - {download_exception}")
            continue
    return downloaded_files