from repository.product_repository import ProductRepository
from database.db import db
from config.logger import Logger

product = ProductRepository()
log = Logger("Product-Services")


class ProductServices:

    def create(self, name, price, stock=0):
        if not name or price is None:
            raise Exception("Product name and price are required.")

        if price < 0:
            raise Exception("Price cannot be negative.")

        if stock < 0:
            raise Exception("Stock cannot be negative.")

        try:
            product_id = product.create(name, price, stock)
            db.commit()
            return product_id
        except Exception as e:
            db.rollback()
            log.error(f"Create product failed: {e}")
            raise Exception("Failed to create product.")

    def get_by_id(self, product_id):
        if not product_id:
            raise Exception("Product ID is required.")

        result = product.get_by_id(product_id)
        if not result:
            raise Exception("Product not found.")

        return result

    def get_all(self):
        results = product.get_all()
        if not results:
            raise Exception("No products found.")

        return results

    def update(self, product_id, name=None, price=None, stock=None):
        if not product_id:
            raise Exception("Product ID is required.")

        existing = product.get_by_id(product_id)
        if not existing:
            raise Exception("Product not found.")

        # Keep old values if new ones are not provided
        name = name if name is not None else existing["name"]
        price = price if price is not None else existing["price"]
        stock = stock if stock is not None else existing["stock"]

        if price < 0:
            raise Exception("Price cannot be negative.")

        if stock < 0:
            raise Exception("Stock cannot be negative.")

        try:
            product.update(product_id, name, price, stock)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            log.error(f"Update product failed: {e}")
            raise Exception("Failed to update product.")

    def delete(self, product_id):
        if not product_id:
            raise Exception("Product ID is required.")

        existing = product.get_by_id(product_id)
        if not existing:
            raise Exception("Product not found.")

        try:
            product.delete(product_id)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            log.error(f"Delete product failed: {e}")
            raise Exception("Failed to delete product.")