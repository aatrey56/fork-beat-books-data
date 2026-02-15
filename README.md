# beat-books-data

NFL data ingestion, storage, and retrieval service for the BeatTheBooks platform.

## What This Does

- **Scrapes** NFL statistics from Pro-Football-Reference (Selenium + BeautifulSoup)
- **Stores** data in PostgreSQL (Neon.tech) via SQLAlchemy
- **Serves** data retrieval API for other BeatTheBooks services
- **Owns** the database schema and all migrations

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL (Neon.tech)
- Selenium + BeautifulSoup + Pandas

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your DATABASE_URL

# Run the service
uvicorn src.main:app --reload --port 8001
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/scrape/{team}/{year}` | Scrape single team stats |
| GET | `/scrape/{year}` | Scrape team offense stats |
| POST | `/scrape/excel` | Batch scrape from Excel URLs |

## Database

14+ tables covering team and player statistics, games, and standings. See `Tables.sql` for the full schema.

## Related Repos

- [beat-books-model](https://github.com/Kame4201/beat-books-model) — ML predictions & strategy
- [beat-books-api](https://github.com/Kame4201/beat-books-api) — API gateway
- [beat-books-infra](https://github.com/Kame4201/beat-books-infra) — CI/CD, docs, Docker
