"""Centralized configuration loading for environment variables."""
import os
from typing import Optional
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


def _get_env(name: str, *, required: bool = True, default: Optional[str] = None) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        if required and default is None:
            raise RuntimeError(f"Environment variable {name} is required but not set")
        value = default or ""
        logger.warning(f"Environment variable {name} is not set; using default value")
    return value


def _get_int_env(name: str) -> int:
    raw_value = _get_env(name)
    try:
        return int(raw_value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name} must be an integer") from exc


API_ID: int = _get_int_env("API_ID")
API_HASH: str = _get_env("API_HASH")
PHONE: str = _get_env("PHONE")
BOT_TOKEN: str = _get_env("BOT_TOKEN")
CHANNEL_ID: str = _get_env("CHANNEL_ID")
PRODUCT_FILE: str = _get_env("PRODUCT_FILE", required=False, default="product_vacancies.xlsx")
