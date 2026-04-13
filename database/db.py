import sqlite3

DATABASE_NAME = "example.db"

class Database:
    def __init__(self) -> None:
        self.conn = None
        self.cursor = None
    
    def connect(self):
            try:
                self.conn = sqlite3.connect(DATABASE_NAME)
                self.cursor = self.conn.cursor()
            except sqlite3.Error as e:
                print(f"[DB ERROR] connection failed : {e}") 
                
    def close(self):
        if self.conn :
            self.conn.close()

db = Database()

    