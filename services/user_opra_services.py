

from repository.user_repository import UserRepository
from config.logger import Logger
from database.db import db

log = Logger("User-Services")
User = UserRepository()

class UserServices:
    
    def get_by_username(self , username):    
        if not username:
            raise Exception("username required.")
        
        user = User.get_by_username(username)
        if not user:
            raise Exception("user not found.")
    
        return user   
    
    def get_by_userId(self, id):
        if not id:
            raise Exception("username required.")
        
        user = User.get_by_userId(id)
        if not user:
            raise Exception("user not found.")
        
        return user 
  