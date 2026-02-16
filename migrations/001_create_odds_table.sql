-- Migration: Create odds table for storing betting lines and odds data
-- Date: 2026-02-15
-- Description: Adds odds table to track opening/closing lines and line movements from multiple sportsbooks

CREATE TABLE IF NOT EXISTS odds (
    id SERIAL PRIMARY KEY,
    season INTEGER NOT NULL,
    week INTEGER NOT NULL,
    game_date DATE NOT NULL,

    home_team VARCHAR(64) NOT NULL,
    away_team VARCHAR(64) NOT NULL,
    sportsbook VARCHAR(64) NOT NULL,

    -- Spread (point spread for each team)
    spread_home NUMERIC(5, 2),
    spread_away NUMERIC(5, 2),

    -- Moneyline (American odds format, e.g., -150, +130)
    moneyline_home INTEGER,
    moneyline_away INTEGER,

    -- Over/Under total points
    over_under NUMERIC(5, 2),

    -- Timestamp when this line was recorded
    timestamp TIMESTAMP NOT NULL,

    -- Track opening vs closing lines
    is_opening BOOLEAN DEFAULT FALSE,
    is_closing BOOLEAN DEFAULT FALSE,

    -- Ensure uniqueness per game/sportsbook/timestamp
    CONSTRAINT uq_odds_game_sportsbook_timestamp
        UNIQUE (season, week, home_team, sportsbook, timestamp)
);

-- Create indexes for common queries
CREATE INDEX idx_odds_season_week ON odds(season, week);
CREATE INDEX idx_odds_home_team ON odds(home_team);
CREATE INDEX idx_odds_away_team ON odds(away_team);
CREATE INDEX idx_odds_sportsbook ON odds(sportsbook);
CREATE INDEX idx_odds_game_date ON odds(game_date);
CREATE INDEX idx_odds_closing ON odds(is_closing) WHERE is_closing = TRUE;
CREATE INDEX idx_odds_opening ON odds(is_opening) WHERE is_opening = TRUE;

-- Add comments for documentation
COMMENT ON TABLE odds IS 'Stores betting odds and lines from various sportsbooks for NFL games';
COMMENT ON COLUMN odds.spread_home IS 'Point spread for home team (negative means favored)';
COMMENT ON COLUMN odds.spread_away IS 'Point spread for away team (positive means underdog)';
COMMENT ON COLUMN odds.moneyline_home IS 'Moneyline odds for home team in American format';
COMMENT ON COLUMN odds.moneyline_away IS 'Moneyline odds for away team in American format';
COMMENT ON COLUMN odds.over_under IS 'Total points over/under line';
COMMENT ON COLUMN odds.is_opening IS 'True if this is the opening line for this game/sportsbook';
COMMENT ON COLUMN odds.is_closing IS 'True if this is the closing line for this game/sportsbook';
