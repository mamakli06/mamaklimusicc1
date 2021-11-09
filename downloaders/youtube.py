from os import path 
import os
from youtube_dl import YoutubeDL
from pytube import YouTube as YT
from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio",
    "addmetadata": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info['duration'] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"Videos longer than {DURATION_LIMIT} dakikaya(s) izin verilmiyor, sağlanan video is {duration} dakika(s)"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
