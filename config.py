import os

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
HEROKU_API = os.getenv("HEROKU_API")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
PY_SESSION = os.getenv("PYROGRAM_SESSION")
TE_SESSION = os.getenv("TELETHON_SESSION")
PREFIX = os.environ.get("PREFIX", ".")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
ALIVE_PIC = os.environ.get("ALIVE_IMAGE", "https://telegra.ph/file/f9f1d48988f2a98f2b510.jpg")
PM_IMG = os.environ.get("PM_IMAGE", "https://telegra.ph/file/f9f1d48988f2a98f2b510.jpg")
