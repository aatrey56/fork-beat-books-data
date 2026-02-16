from pydantic_settings import BaseSettings
from pydantic import field_validator, Field


class Settings(BaseSettings):
    """Centralized configuration for beat-books-data service."""

    # Database
    DATABASE_URL: str

    # Scraping
    SCRAPE_DELAY_SECONDS: int = Field(default=60, gt=0)

    # Odds API (Phase 2)
    ODDS_API_KEY: str = ""
    ODDS_API_BASE_URL: str = "https://api.the-odds-api.com"

    # App
    LOG_LEVEL: str = "INFO"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = Field(default=8001, gt=0, le=65535)

    @field_validator("SCRAPE_DELAY_SECONDS")
    @classmethod
    def validate_scrape_delay(cls, v: int) -> int:
        """Ensure scrape delay is positive to respect rate limits."""
        if v <= 0:
            raise ValueError("SCRAPE_DELAY_SECONDS must be greater than 0")
        return v

    @field_validator("DATABASE_URL")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """Ensure DATABASE_URL is not empty."""
        if not v or not v.strip():
            raise ValueError("DATABASE_URL is required and cannot be empty")
        return v

    model_config = {"env_file": ".env"}


settings = Settings()
