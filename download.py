from pytube import YouTube
from config import config

def download_audio(url):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(output_path=config["output_path"])
    