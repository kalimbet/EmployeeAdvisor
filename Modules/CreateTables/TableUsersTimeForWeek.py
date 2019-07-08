import mysql

from Modules.Connectors import Connection

connection = Connection.getConnection()
print("Connect 'usersTimeForWeek' successful!")
def create_table():
    cursor = connection.cursor()
    sql = """
    CREATE TABLE usersTimeForWeek (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               idUser INTEGER,
               name text,
               surname text,
               fromDate DATE,
               untilDate DATE,
               timeSecondsRest INTEGER,
               timeSecondsWork INTEGER,
               ratingForWeek INTEGER 
    );
    """
    try:
        cursor.execute(sql)
        print("Table 'usersTimeForWeek' was created!")
    except mysql.connector.errors.ProgrammingError:
        print("Table 'usersTimeForWeek' already exist!")
    connection.close()
