from repository.user_repository import UserRepository
from database.db import db
from config.logger import Logger
from utils.security import hash_password , verify_password

user = UserRepository()
log = Logger("Auth-Services")

class UserAuthService:
    
    def register(self , username , password , role="staff"):
        
        if not username or not password:
            raise Exception("Username and password required")
        if user.exists(username):
            raise Exception("Username already exists")
        if len(password) < 6 :
            raise Exception("Username already existsPassword must be at least 6 characters")
        
        hashed_password = hash_password(password)
        try:
            user_id = user.create(username , hashed_password , role )
            db.commit()
            return user_id
        
        except Exception as e:
            raise Exception(f"Registration failed: {e}")
        
