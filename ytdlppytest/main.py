import re
import yt_dlp

from urllib.parse import urlparse, parse_qs


YOUTUBE_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def clean_youtube_url(url: str) -> str:
    url = url.strip()

    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")

    video_id = None

    if host in ("youtube.com", "m.youtube.com"):
        query = parse_qs(parsed.query)
        video_id = query.get("v", [None])[0]

    elif host == "youtu.be":
        video_id = parsed.path.strip("/").split("/")[0]

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    if not YOUTUBE_ID_PATTERN.fullmatch(video_id):
        raise ValueError("Invalid YouTube video ID")

    return f"https://www.youtube.com/watch?v={video_id}"


def download_audio(url: str):
    clean_url = clean_youtube_url(url)

    print("Clean URL:", clean_url)

    options = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(clean_url, download=True)

    return info


url = input("Enter YouTube URL: ")

try:
    info = download_audio(url)

    print()
    print("Done!")
    print("Title:", info["title"])
    print("Video ID:", info["id"])

except Exception as e:
    print("Error:", e)