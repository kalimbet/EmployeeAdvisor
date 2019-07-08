import mysql

from Modules.Connectors import Connection

connection = Connection.getConnection()
print("Connect 'usersTimeForYear' successful!")
def create_table():
    cursor = connection.cursor()
    sql = """
    CREATE TABLE usersTimeForYear (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               idUser INTEGER,
               name text,
               surname text,
               fromDate DATE,
               untilDate DATE,
               timeSecondsRest INTEGER,
               timeSecondsWork INTEGER,
               ratingForYear INTEGER 
    );
    """
    try:
        cursor.execute(sql)
        print("Table 'usersTimeForYear' was created!")
    except mysql.connector.errors.ProgrammingError:
        print("Table 'usersTimeForYear' already exist!")
    connection.close()
