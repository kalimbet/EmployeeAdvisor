import mysql

from Modules.Connectors import Connection

connection = Connection.getConnection()
print("Connect 'users' successful!")

def create_table():
    cursor = connection.cursor()
    sql = """
    CREATE TABLE users (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               name text,
               surname text,
               address text,
               email text,
               groupNumber text,
               country text,
               dateRegistration  DATETIME
    );
    """
    try:
        cursor.execute(sql)
        print("Table 'users' was created!")
    except mysql.connector.errors.ProgrammingError:
        print("Table 'users' already exist!")
    connection.close()
