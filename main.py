from database.db import initialize_database
from repository.user_repository import UserRepository
from config.logger import Logger

log = Logger("App")

user = UserRepository()

def initApp():
    initialize_database()
    print("app is running.")
    while True:
        print("""
            1 : - create user
            2 : - deactivate user
            3 : - check user
            4 : - get user by name user
            5 : - get user by id user
            6 : - get all users
            7 : - exit
            
        """)
        user_choice = input("Enter you choice (1,2,3,4,5,6) : ")
        if user_choice == "1":
            username = input("enter username :")
            password = input("enter user password:")
            role = input("enter user role :")
            if role != "":
                result = user.create(username  , password , role=role)
                log.success(result)
                
            result = user.create(username , password )
            log.success(result)
            
            
        elif user_choice == "2":
            user_id = input("enter user id :")
            result = user.deactivate(user_id)
            log.success(result)
            
        elif user_choice == "3":
            username = input("enter username :")
            result = user.exists(username)
            log.success(result)
            
        elif user_choice == "4":
            username = input("enter username :")
            result = user.get_by_username(username)
            log.success(result)
            
        elif user_choice == "5":
            id = input("enter id :")
            result = user.get_by_userId(id)
            log.success(result)
            
        elif user_choice == "6":
            records = user.get_all() or {}
            for record in records: # type: ignore
                print(f" user id : {record["id"]} , username : {record["username"]} , role {record["role"]}")
            
        elif user_choice == "7":
            log.success("thanks for using the system.")
            break    
        else:
            log.warning("invalid input please try again!")


if __name__ == "__main__":
    initApp()