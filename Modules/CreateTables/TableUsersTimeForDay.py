import mysql

from Modules.Connectors import Connection

connection = Connection.getConnection()
print("Connect 'usersTimeForDay' successful!")
def create_table():
    cursor = connection.cursor()
    sql = """
    CREATE TABLE usersTimeForDay (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               idUser INTEGER,
               name text,
               surname text,
               date DATE,
               weekDay INTEGER,
               timeSecondsRest INTEGER,
               timeSecondsWork INTEGER,
               ratingForDay INTEGER 
    );
    """
    try:
        cursor.execute(sql)
        print("Table 'usersTimeForDay' was created!")
    except mysql.connector.errors.ProgrammingError:
        print("Table 'usersTimeForDay' already exist!")
    connection.close()