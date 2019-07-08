import datetime

from Modules.CreateTables import TableUsersTime, TableUsers, TableUsersTimeForDay, TableUsersTimeForWeek, TableUsersTimeForMonth, TableUsersTimeForYear

from Modules.Connectors import Connection


class dataBase:
    def __init__(self):
        TableUsers.create_table()
        TableUsersTime.create_table()
        TableUsersTimeForDay.create_table()
        TableUsersTimeForWeek.create_table()
        TableUsersTimeForMonth.create_table()
        TableUsersTimeForYear.create_table()
        self.connection = Connection.getConnection()
        self.c = self.connection.cursor()



    def insert_data_for_rating_day(self, idUser, date, timeSecondsRest, timeSecondsWork, ratingForDay):
        self.c.execute("SELECT name FROM users WHERE id = (%s);", (idUser,))
        resultName = self.c.fetchall()
        name = resultName[0][0]
        self.c.execute("SELECT surname FROM users WHERE id = (%s);", (idUser,))
        resultSurname = self.c.fetchall()
        surname = resultSurname[0][0]

        year, month, day = (int(x) for x in date.split('-'))
        weekDay = datetime.date(year, month, day).weekday()
        self.c.execute(
            'INSERT INTO usersTimeForDay (idUser, name, surname, date, weekDay, timeSecondsrest, timeSecondsWork, ratingForDay) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (idUser, name, surname, date, weekDay, timeSecondsRest, timeSecondsWork, ratingForDay))
        self.connection.commit()


    def insert_data_for_rating_week(self, idUser, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek):
        self.c.execute("SELECT name FROM users WHERE id = (%s);", (idUser,))
        resultName = self.c.fetchall()
        name = resultName[0][0]
        self.c.execute("SELECT surname FROM users WHERE id = (%s);", (idUser,))
        resultSurname = self.c.fetchall()
        surname = resultSurname[0][0]
        self.c.execute(
            'INSERT INTO usersTimeForWeek (idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek))
        self.connection.commit()

    def insert_data_for_rating_month(self, idUser, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForMonth):
        self.c.execute("SELECT name FROM users WHERE id = (%s);", (idUser,))
        resultName = self.c.fetchall()
        name = resultName[0][0]
        self.c.execute("SELECT surname FROM users WHERE id = (%s);", (idUser,))
        resultSurname = self.c.fetchall()
        surname = resultSurname[0][0]
        nameOfMonth = datetime.datetime.strptime(fromDate, "%Y-%m-%d")
        self.c.execute(
            'INSERT INTO usersTimeForMonth (idUser, name, surname, fromDate, untilDate, month, timeSecondsRest, timeSecondsWork, ratingForMonth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (idUser, name, surname, fromDate, untilDate, nameOfMonth.strftime("%B"), timeSecondsRest, timeSecondsWork, ratingForMonth))
        self.connection.commit()

    def insert_data_for_rating_year(self, idUser, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear):
        self.c.execute("SELECT name FROM users WHERE id = (%s);", (idUser,))
        resultName = self.c.fetchall()
        name = resultName[0][0]
        self.c.execute("SELECT surname FROM users WHERE id = (%s);", (idUser,))
        resultSurname = self.c.fetchall()
        surname = resultSurname[0][0]
        self.c.execute(
            'INSERT INTO usersTimeForYear (idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear))
        self.connection.commit()