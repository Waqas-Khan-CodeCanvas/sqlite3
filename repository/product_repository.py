import sqlite3

from database.db import db
from config.logger import Logger

log = Logger("Product-Repository")


class ProductRepository:

    def create(self, name, price, stock):
        try:
            cursor = db.get_cursor()
            cursor.execute(
                "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
                (name, price, stock)
            )
            db.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            log.error(f"Product creation failed: {e}")

    def get_by_id(self, product_id):
        try:
            cursor = db.get_cursor()
            cursor.execute(
                "SELECT * FROM products WHERE id = ?",
                (product_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
        except sqlite3.Error as e:
            log.error(f"Get product by id failed: {e}")
            return None

    