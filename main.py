import os
import json
import youtube_dl


def download_audio(url: str, download_dir: str = None):
    video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
    filename = "{download_dir}/{title}.mp3".format_map(
        {
            "download_dir": download_dir,
            "title": video_info["title"],
        }
    )
    download_options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": filename,
    }
    try:
        with youtube_dl.YoutubeDL(download_options) as downloader:
            downloader.download([video_info["webpage_url"]])
        return f"{video_info['title']}.mp3"
    except youtube_dl.utils.DownloadError:
        print(f"Encountered an error while trying to retrieve audio from: {url}")
        return None


if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    with open(config["dataFile"], "r") as data_file:
        urls = data_file.read().splitlines()

    for url in urls:
        downloaded_filename = download_audio(url, download_dir=config["downloadDir"])
        if downloaded_filename is not None:
            downloaded_filepath = os.path.join(
                config["downloadDir"], downloaded_filename
            )
            if not os.path.exists(config["convertedDir"]):
                os.mkdir(config["convertedDir"])
            converted_filepath = os.path.join(
                config["convertedDir"], downloaded_filename
            )
            os.system(
                f"ffmpeg -i '{downloaded_filepath}' -c:v copy -c:a libmp3lame -q:a 4 '{converted_filepath}'"
            )
