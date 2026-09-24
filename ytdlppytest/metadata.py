import json
import os
import re

import yt_dlp

from urllib.parse import urlparse, parse_qs


YOUTUBE_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def clean_youtube_url(url: str) -> str:
    url = url.strip()

    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")

    video_id = None

    # https://www.youtube.com/watch?v=VIDEO_ID&...
    if host in ("youtube.com", "m.youtube.com"):
        query = parse_qs(parsed.query)
        video_id = query.get("v", [None])[0]

    # https://youtu.be/VIDEO_ID?...
    elif host == "youtu.be":
        video_id = parsed.path.strip("/").split("/")[0]

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    if not YOUTUBE_ID_PATTERN.fullmatch(video_id):
        raise ValueError("Invalid YouTube video ID")

    return f"https://www.youtube.com/watch?v={video_id}"


def extract_metadata(url: str):
    clean_url = clean_youtube_url(url)

    options = {
        # We only want information.
        # Nothing will be downloaded.
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(
            clean_url,
            download=False
        )

    metadata = {
        "id": info.get("id"),
        "title": info.get("title"),
        "description": info.get("description"),

        "channel": info.get("channel"),
        "channel_id": info.get("channel_id"),
        "channel_url": info.get("channel_url"),

        "uploader": info.get("uploader"),
        "uploader_id": info.get("uploader_id"),
        "uploader_url": info.get("uploader_url"),

        "upload_date": info.get("upload_date"),
        "timestamp": info.get("timestamp"),

        "duration": info.get("duration"),
        "duration_string": info.get("duration_string"),

        "thumbnail": info.get("thumbnail"),

        "view_count": info.get("view_count"),
        "like_count": info.get("like_count"),
        "comment_count": info.get("comment_count"),

        "categories": info.get("categories"),
        "tags": info.get("tags"),

        "chapters": info.get("chapters"),

        "language": info.get("language"),
        "age_limit": info.get("age_limit"),

        "webpage_url": info.get("webpage_url"),
    }

    return metadata


def save_metadata(metadata: dict):
    os.makedirs("metadata", exist_ok=True)

    video_id = metadata["id"]

    filename = f"metadata/{video_id}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            metadata,
            file,
            indent=4,
            ensure_ascii=False
        )

    return filename


if __name__ == "__main__":

    url = input("Enter YouTube URL: ")

    try:
        metadata = extract_metadata(url)

        json_file = save_metadata(metadata)

        print()
        print("Metadata extracted successfully!")
        print("Video ID:", metadata["id"])
        print("Title:", metadata["title"])
        print("JSON:", json_file)

    except Exception as e:
        print()
        print("Error:", e)