import sqlite3
import logging

DB_NAME = 'weather_bot.db'
logger = logging.getLogger(__name__)


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            city_name TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    logger.info("База данных инициализирована.")


def log_request(user_id, city_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO requests (user_id, city_name) VALUES (?, ?)''', (user_id, city_name))
    conn.commit()
    conn.close()
    logger.info(f"Запрос от пользователя {user_id} для города {city_name} сохранен.")
