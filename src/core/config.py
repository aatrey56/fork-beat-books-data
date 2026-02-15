from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Centralized configuration for beat-books-data service."""

    # Database
    DATABASE_URL: str

    # Scraping
    SCRAPE_DELAY_SECONDS: int = 60

    # Odds API (Phase 2)
    ODDS_API_KEY: str = ""
    ODDS_API_BASE_URL: str = "https://api.the-odds-api.com"

    # App
    LOG_LEVEL: str = "INFO"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8001

    model_config = {"env_file": ".env"}


settings = Settings()
