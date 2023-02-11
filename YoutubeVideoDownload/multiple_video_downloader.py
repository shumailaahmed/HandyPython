import os
from pytube import YouTube

video_urls = [ "https://www.youtube.com/watch?v=6ZfuNTqbHE8",   
              "https://www.youtube.com/watch?v=8UEE2XEKc4s",
              "https://www.youtube.com/watch?v=r-lGjNc1NX0"]

for url in video_urls:
    yt = YouTube(url)
    video = yt.streams.first()
    video.download("/path/to/downloads")
    print("Downloaded", yt.title)
