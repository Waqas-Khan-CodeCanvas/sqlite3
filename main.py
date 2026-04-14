from database.db import db

def initApp():
    print("app is running.")


if __name__ == "__main__":
    db.connect()
    initApp()