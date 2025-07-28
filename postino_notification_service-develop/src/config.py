import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# ---------------------------------------------------------------------------
load_dotenv()


# ---------------------------------------------------------------------------
class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    ENVIRONMENT: str
    LOG_LEVEL: str

    # SMS Provider
    SMS_PROVIDER_API_KEY: str
    SMS_PROVIDER_OTP_TEMPLATE_ID: int


# ---------------------------------------------------------------------------
class DevSettings(Settings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env.dev")


# ---------------------------------------------------------------------------
class ProdSettings(Settings):
    model_config = SettingsConfigDict()


# ---------------------------------------------------------------------------
@lru_cache
def get_settings() -> Settings:
    configs = {"dev": DevSettings, "prod": ProdSettings}
    get_config = configs.get(os.environ.get("APP_ENV", "dev"))
    return get_config()


# ---------------------------------------------------------------------------
settings = get_settings()
