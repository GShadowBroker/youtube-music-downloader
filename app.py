import sys
from download import download_audio

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_video_url>")
        sys.exit(1)
    url = sys.argv[1]
    download_audio(url)
