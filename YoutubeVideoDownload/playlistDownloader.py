from pytube import YouTube
from pytube import Playlist
import re
playlist_url = input("Enter the playlist URL: ")

playlist = Playlist(playlist_url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print("Total videos in the playlist: ", len(playlist.video_urls))

for url in playlist.video_urls:
    yt = YouTube(url)
    yt.streams.first().download()
    print("Downloaded", yt.title)
