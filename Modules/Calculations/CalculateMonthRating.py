import datetime
import tkinter as tk


import VariablesHelper



class Child(tk.Toplevel):
    def __init__(self, db):
        self.db = db
        self.start_calculation()
    # Initialization Child window


    def calculation_month_rating(self, listRatingForWeek, listUserFromDate, listUserUntilDate, listSecondsRest, listSecondsWork):
        self.db.c.execute("SELECT name FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultName = self.db.c.fetchall()
        name = resultName[0][0]
        self.db.c.execute("SELECT surname FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultSurname = self.db.c.fetchall()
        surname = resultSurname[0][0]

        if len(listRatingForWeek) > 3:
            ratingForMonth = 0
            secondsRestForMonth = 0
            secondsWorkForMonth = 0

            i = 0
            while i < 4:  # len(listRatingForWeek):
                rat = listRatingForWeek[i]
                secRest = listSecondsRest[i]
                secWork = listSecondsWork[i]


                ratingForMonth += rat
                secondsRestForMonth += secRest
                secondsWorkForMonth += secWork

                if i == 0:
                    untilDate = listUserUntilDate[i]
                    nameOfMonth = datetime.datetime.strptime(listUserUntilDate[i], "%Y-%m-%d")
                if i % 3 == 0:
                    fromDate = listUserFromDate[i]

                i += 1

            self.db.c.execute(
                'INSERT INTO usersTimeForMonth (idUser, name, surname, fromDate, untilDate, month, timeSecondsRest, timeSecondsWork, ratingForMonth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (VariablesHelper.userId, name, surname, fromDate, untilDate, nameOfMonth.strftime("%B"), secondsRestForMonth, secondsWorkForMonth,
                 ratingForMonth))
            self.db.connection.commit()

        else:
            print("error")

    def start_calculation(self):
        self.db.c.execute("SELECT ratingForWeek FROM userstimeForWeek WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultRatingForMonth = self.db.c.fetchall()

        self.db.c.execute("SELECT fromDate FROM userstimeForWeek WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultUserFromDate = self.db.c.fetchall()

        self.db.c.execute("SELECT untilDate FROM userstimeForWeek WHERE idUser = (%s) ORDER BY untilDate DESC;",
                          (VariablesHelper.userId,))
        resultUserUntilDate = self.db.c.fetchall()

        self.db.c.execute("SELECT timeSecondsRest FROM userstimeForWeek WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultSecondsRest = self.db.c.fetchall()

        self.db.c.execute("SELECT timeSecondsWork FROM userstimeForWeek WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultSecondsWork = self.db.c.fetchall()
        self.convert_data(resultUserFromDate,resultUserUntilDate, resultSecondsRest, resultSecondsWork, resultRatingForMonth )

    def convert_data(self,resultUserFromDate, resultUserUntilDate, resultSecondsRest, resultSecondsWork, resultRatingForMonth ):
        listRatingForWeek = []
        listUserFromDate = []
        listUserUntilDate = []
        listSecondsRest = []
        listSecondsWork = []

        i = 0
        while i < len(resultRatingForMonth):
            listRatingForWeek.append(int(resultRatingForMonth[i][0]))
            i += 1
        i = 0
        while i < len(resultUserFromDate):
            listUserFromDate.append(str(resultUserFromDate[i][0]))
            i += 1
        i = 0
        while i < len(resultUserUntilDate):
            listUserUntilDate.append(str(resultUserUntilDate[i][0]))
            i += 1
        i = 0
        while i < len(resultSecondsRest):
            listSecondsRest.append(int(resultSecondsRest[i][0]))
            i += 1
        i = 0
        while i < len(resultSecondsWork):
            listSecondsWork.append(int(resultSecondsWork[i][0]))
            i += 1

        self.calculation_month_rating(listRatingForWeek, listUserFromDate, listUserUntilDate, listSecondsRest, listSecondsWork)

