import mysql.connector

def getConnection():

    connection = mysql.connector.connect(host='localhost',
                                         database='main',
                                         user='root',
                                         password='1111')

    return connection