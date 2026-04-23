import sqlite3

from database.db import db
from config.logger import Logger

log = Logger("Repository")

class UserRepository:
    
    def create(self , username , password , role="staff"):
        try:
            cursor = db.get_cursor()
            cursor.execute(
                "INSERT INTO users (username , password , role) VALUES (?,?,?) " ,
                (username , password , role)
                )
            db.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            log.error(f"user creation falied : {e}")
    
    def get_by_username(self, username):
        try:
            cursor = db.get_cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username = ? AND is_Active = 1",
                (username,)
            )
            row = cursor.fetchone()

            return dict(row) if row else None

        except sqlite3.Error as e:
            log.error(f"get user by username failed: {e}")
            return None
    
    def get_by_userId(self , user_id):
        try:
            cursors = db.get_cursor()
            cursors.execute(
                "SELECT * FROM users WHERE id = ? ",
                (user_id,)
            )
            return cursors.fetchone()
        except sqlite3.Error as e:
            log.error(f"user get by id falied : {e}")
        
    def exists(self  , username ):
        try:
            cursors = db.get_cursor()
            cursors.execute(
                "SELECT id FROM users WHERE username = ?",
                (username,)
            )
            return cursors.fetchone() is not None
        except sqlite3.Error as e:
            log.error(f"user check method falied : {e}")
    
    def deactivate(self , user_id):
        try:
            cursors  = db.get_cursor()
            cursors.execute(
                "UPDATE users SET is_Active = 0 WHERE id = ? ",
                (user_id,)
            )
            db.commit()
            return True
        except sqlite3.Error as e:
            log.error(f"user deactivate method falied : {e}")
    
    def get_all(self):
        try:
            cursors = db.get_cursor()
            cursors.execute("SELECT * FROM users")
            rows = cursors.fetchall()
            print(rows[0])
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            log.error(f"get all user method falied : {e}")