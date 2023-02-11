import os
import re
from pytube import YouTube
from pytube import Playlist

playlist_url = input("Enter the playlist URL: ")
download_path = "."

playlist = Playlist(playlist_url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print("Total videos in the playlist: ", len(playlist.video_urls))

for url in playlist.video_urls:
    try:
        yt = YouTube(url)
    except Exception as e:
        print(f"{url} is not a valid YouTube URL: {e}")
        continue
    try:
        video = yt.streams.first()
        video_title = yt.title
        file_name = f"{video_title}.mp4"
        file_path = os.path.join(download_path, file_name)
        if not os.path.exists(file_path):
            video.download(download_path)
            print("Downloaded", video_title)
        else:
            print(f"{video_title} already exists.")
    except:
        print("VideoUnavailable")
