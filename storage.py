
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "devquest.db"


def initialize_database():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS player_progress (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                xp INTEGER NOT NULL DEFAULT 0,
                completed_quests TEXT NOT NULL DEFAULT '',
                accepted_quests TEXT NOT NULL DEFAULT ''
            )
        """)

        columns = {
            row[1] for row in connection.execute(
                "PRAGMA table_info(player_progress)"
            ).fetchall()
        }

        if "accepted_quests" not in columns:
            connection.execute("""
                ALTER TABLE player_progress
                ADD COLUMN accepted_quests TEXT NOT NULL DEFAULT ''
            """)

        connection.execute("""
            INSERT OR IGNORE INTO player_progress
                (id, xp, completed_quests, accepted_quests)
            VALUES (1, 0, '', '')
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS leaderboard (
                username TEXT PRIMARY KEY COLLATE NOCASE,
                xp INTEGER NOT NULL DEFAULT 0,
                completed_count INTEGER NOT NULL DEFAULT 0
            )
        """)


def load_progress():
    initialize_database()

    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute("""
            SELECT xp, completed_quests, accepted_quests
            FROM player_progress
            WHERE id = 1
        """).fetchone()

    return {
        "xp": row[0],
        "completed_quests": [
            item for item in row[1].split(",") if item
        ],
        "accepted_quests": [
            item for item in row[2].split(",") if item
        ],
    }


def save_progress(xp, completed_quests, accepted_quests):
    initialize_database()

    completed = ",".join(sorted(set(completed_quests)))
    accepted = ",".join(sorted(set(accepted_quests)))

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            UPDATE player_progress
            SET xp = ?, completed_quests = ?, accepted_quests = ?
            WHERE id = 1
        """, (int(xp), completed, accepted))


def save_player_score(username, xp, completed_count):
    username = username.strip()

    if not username:
        return

    initialize_database()

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            INSERT INTO leaderboard (username, xp, completed_count)
            VALUES (?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET
                xp = excluded.xp,
                completed_count = excluded.completed_count
        """, (username, int(xp), int(completed_count)))


def get_leaderboard(limit=10):
    initialize_database()

    with sqlite3.connect(DB_PATH) as connection:
        rows = connection.execute("""
            SELECT username, xp, completed_count
            FROM leaderboard
            ORDER BY xp DESC, completed_count DESC, username COLLATE NOCASE
            LIMIT ?
        """, (int(limit),)).fetchall()

    return [
        {
            "username": row[0],
            "xp": row[1],
            "completed_count": row[2],
        }
        for row in rows
    ]
