from pydantic_settings import BaseSettings
from pydantic import field_validator, Field
from typing import List


class Settings(BaseSettings):
    """Centralized configuration for beat-books-data service."""

    # Database
    DATABASE_URL: str

    # Scraping
    SCRAPE_DELAY_SECONDS: int = Field(default=60, gt=0)
    SCRAPE_REQUEST_TIMEOUT: int = 30  # seconds
    SCRAPE_MAX_RETRIES: int = 3
    SCRAPE_RETRY_DELAYS: List[int] = [
        30,
        60,
        120,
    ]  # exponential backoff delays in seconds

    # User-Agent rotation pool (10+ browser-like user agents)
    SCRAPE_USER_AGENTS: List[str] = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    ]

    # Proxy rotation (optional)
    SCRAPE_USE_PROXY: bool = False
    SCRAPE_PROXY_LIST: List[str] = (
        []
    )  # Format: ["http://proxy1:port", "http://proxy2:port"]

    # Odds API (Phase 2)
    ODDS_API_KEY: str = ""
    ODDS_API_BASE_URL: str = "https://api.the-odds-api.com"

    # App
    LOG_LEVEL: str = "INFO"
    API_HOST: str = "0.0.0.0"  # nosec B104
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
