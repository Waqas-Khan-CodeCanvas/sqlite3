import sqlite3
from utils.constants import DATABASE_NAME
from database.schemas import create_tables
from config.logger import Logger

log = Logger("DB")

class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(DATABASE_NAME)
            self.conn.execute("PRAGMA foreign_keys = ON;")
            self.conn.row_factory = sqlite3.Row
            log.success("Database connected successfully.")
            return self.conn
        except sqlite3.Error as e:
            log.error(f"Database connection failed : {e}")

    def get_cursor(self):
        if not self.conn:
            self.connect()
        return self.conn.cursor() # type: ignore

    def commit(self):
        if self.conn:
            self.conn.commit()

    def rollback(self):
        if self.conn:
            self.conn.rollback()
    
    def close(self):
        if self.conn:
            self.conn.close()

db  = Database()

def initialize_database():
    db.connect()
    create_tables(db.get_cursor())
    
    