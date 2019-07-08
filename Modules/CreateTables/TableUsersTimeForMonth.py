import mysql

from Modules.Connectors import Connection

connection = Connection.getConnection()
print("Connect 'usersTimeForMonth' successful!")
def create_table():
    cursor = connection.cursor()
    sql = """
    CREATE TABLE usersTimeForMonth (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               idUser INTEGER,
               name text,
               surname text,
               fromDate DATE,
               untilDate DATE,
               month text,
               timeSecondsRest INTEGER,
               timeSecondsWork INTEGER,
               ratingForMonth INTEGER 
    );
    """
    try:
        cursor.execute(sql)
        print("Table 'usersTimeForMonth' was created!")
    except mysql.connector.errors.ProgrammingError:
        print("Table 'usersTimeForMonth' already exist!")
    connection.close()
