import sqlite3

class UserDatabase:
    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )"""
            )

    def add_user(self, user_id, name):
        with self.conn:
            self.conn.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, name))

    def get_user(self, user_id):
        cursor = self.conn.execute("SELECT name FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return row[0] if row else None

    def get_all_users(self):
        cursor = self.conn.execute("SELECT * FROM users")
        return cursor.fetchall()
