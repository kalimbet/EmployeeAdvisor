import mysql

from Modules.Connectors import Connection

connection = Connection.getConnection()
print("Connect 'usersTime' successful!")
def create_table():
    cursor = connection.cursor()
    sql = """
    CREATE TABLE usersTime (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               idUser INTEGER,
               numberRoom INTEGER,
               name text,
               surname text,
               date DATETIME,
               time TIME,
               weekDay INTEGER 
    );
    """
    try:
        cursor.execute(sql)
        print("Table 'userTime' was created!")
    except mysql.connector.errors.ProgrammingError:
        print("Table 'userTime' already exist!")
    connection.close()