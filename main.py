from app import download_audio_single, download_audio_multiple

DOWNLOAD_SINGLE = True
DOWNLOAD_DIRECTORY = "downloads"
EXAMPLE_URLS = [
    "https://www.youtube.com/watch?v=qod03PVTLqk",
    "https://www.youtube.com/watch?v=qod03PVTLqk"
]

if __name__=="__main__":
    if DOWNLOAD_SINGLE:
        download_audio_single(EXAMPLE_URLS[-1], download_dir=DOWNLOAD_DIRECTORY)
    else:
        download_audio_multiple(EXAMPLE_URLS, download_dir=DOWNLOAD_DIRECTORY)


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
