import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("5894848388", None))
API_HASH = getenv("9881b1317590d1afd10879ca3632e4cf", None)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7849762569:AAFng-G1P5bI2vVSI_X7POIRUSPYn7Q", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
MUSIC_BOT_NAME = getenv("MusicXsweet", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002547815290", None))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value Telegram id
OWNER_ID = int(getenv("OWNER_ID", "5894848388"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/plhannakabakj/music1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+0069jm2JvsVmYzhl")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Ksm09ePOR4lmNTll")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session
STRING1 = getenv("BQFxWksASA2APaTa5vhbVseQ0YFNxvVhGTvCFrmsUHMmuLu8482bqD5GSd-z0_XeGwUKEDyieGIPtVmQ5cfdogevLWJatZ1oVbCNdvRZSrW9VoQJDnbNHO5zvjGgXvAiuPMAqQfzEk_O5wEnQykh3mCTP_F02XjrisdhQlQ6Mgzfpb5iryaK2Se71yTG1EUnAPWRRHzpMIjy7GFYUU-QpHrYzmXekDZ_PaqlU-dGaZRqb76DnqrmAK6RvXaax1NGjZE2liFvaYIyPcWss5AqXPEmAFMCAfEcNtmnqivsOgJw8X-1YUnsAYmv5n5lbzt7KKTO7CAJj3cZr23MYFThuNvRArDgTgAAAAHb6bh7AA",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/fda47677514501a9ca8d3-66a909f303ede65807.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/88fefe83d17a2b1a7ce67-ef9559767e2a8b5504.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/ec8b5b562ef863c0b2653-dac3e054ce90b65b85.jpg"
STATS_IMG_URL = "https://graph.org/file/2d908747d20eeed234494-4f677a746aa5ceebbd.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/afc3c99a5c5952506d01a-c79a879a231500e9cc.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/52f68c96ab69c57a985a1-ef96ee18120203a381.jpg"
STREAM_IMG_URL = "https://graph.org/file/fbdbc52e4415e6b868c78-f62caffb45ce4d5719.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/82d82317c91683685af83-29900a5f43877fe205.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/569066df814066dcdaca3-79c3f4684f51f8b184.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5e8f6602b58f190664f82-56e5059bbe886d5e23.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/ae902feb90d8b992cd0ec-7bbe43c44299635de5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/9670a4bf312b4981a2ac9-da95b29227340264d8.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
