

def create_tables():
    sql_query = """
        CREATE TABLE USER(
            username char(30) NOT NULL UNIQUE,
            password char(30) NOT NULL,
            role char(20) ,
            isActive char(5) )
        """
    