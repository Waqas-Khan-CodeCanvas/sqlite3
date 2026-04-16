from database.db import initialize_database

def initApp():
    initialize_database()
    print("app is running.")

if __name__ == "__main__":
    initApp()