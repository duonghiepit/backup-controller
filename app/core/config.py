from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # --- App ---
    APP_NAME: str = "Backup Controller"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    # --- Database ---
    DATABASE_URL: str

    # --- Security ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # --- Checker timing (seconds) ---
    CHECK_T1: int = 60      # Agent unhealthy nếu không ping sau T1s
    CHECK_T2: int = 120     # Task fail nếu không update sau T2s
    CHECK_T3: int = 30      # Task overdue nếu next_run + T3 < now

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()