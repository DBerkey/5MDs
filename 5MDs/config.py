import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def _to_int(value, name):
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Environment variable {name} must be an integer.") from exc


def get_env(name, default=None, required=False, cast=str):
    value = os.getenv(name, default)
    if required and (value is None or value == ""):
        raise ValueError(f"Environment variable {name} is required.")
    if value is None:
        return None
    if cast is int:
        return _to_int(value, name)
    return cast(value)


def get_id_set(name):
    value = os.getenv(name, "")
    if not value.strip():
        return set()
    return {int(item.strip()) for item in value.split(",") if item.strip()}


def data_path(filename):
    return DATA_DIR / filename


DISCORD_BOT_TOKEN = get_env("DISCORD_BOT_TOKEN", required=True)
MONGODB_URI = get_env("MONGODB_URI", required=True)
DEFAULT_PREFIX = get_env("DEFAULT_PREFIX", default="5")
OWN_BOT_ID = get_env("OWN_BOT_ID", default="1012793992359972977", cast=int)
TARGET_BOT_ID = get_env("TARGET_BOT_ID", default="571027211407196161", cast=int)

ADMIN_IDS = get_id_set("ADMIN_IDS")
RAID_GUIDE_EDITOR_IDS = get_id_set("RAID_GUIDE_EDITOR_IDS")

DAILY_WATCH_CHANNEL_ID_SHOP_VIEW = get_env("DAILY_WATCH_CHANNEL_ID_SHOP_VIEW", default="1376249740748128256", cast=int)
DAILY_WATCH_MESSAGE_ID_SHOP_VIEW = get_env("DAILY_WATCH_MESSAGE_ID_SHOP_VIEW", default="1376530332676784288", cast=int)
DAILY_WATCH_CHANNEL_ID_SHOP_PING = get_env("DAILY_WATCH_CHANNEL_ID_SHOP_PING", default="1376249501400043620", cast=int)

GOOGLE_SHEETS_CREDENTIALS_FILE = get_env("GOOGLE_SHEETS_CREDENTIALS_FILE", default=str(data_path("google_api_login.json")))
RAID_SHEET_NAME = get_env("RAID_SHEET_NAME", default="")
FLOOR_SHEET_NAME = get_env("FLOOR_SHEET_NAME", default="")
