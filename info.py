from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6893463477"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://envs.sh/lP-.jpg")
API_ID = int(getenv("API_ID", "29385418"))
API_HASH = str(getenv("API_HASH", "5737577bcb32ea1aac1ac394b96c4b10"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "deathkingworld") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://towaye6074:A2jR9c7DCr3gX09q@cluster0.g8c3j.mongodb.net/?retryWrites=true&w=majority",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)