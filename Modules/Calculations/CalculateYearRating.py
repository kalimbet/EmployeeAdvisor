import datetime
import tkinter as tk


import VariablesHelper



class Child(tk.Toplevel):
    def __init__(self, db):

        self.db = db
        self.start_calculation()
    # Initialization Child window

    def calculation_year_rating(self, listRatingForMonth, listUserFromDate, listUserUntilDate, listSecondsRest, listSecondsWork):
        self.db.c.execute("SELECT name FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultName = self.db.c.fetchall()
        name = resultName[0][0]
        self.db.c.execute("SELECT surname FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultSurname = self.db.c.fetchall()
        surname = resultSurname[0][0]

        if len(listRatingForMonth) > 11:
            ratingForYear = 0
            secondsRestForYear = 0
            secondsWorkForYear = 0

            i = 0
            while i < 12:  # len(listRatingForWeek):
                rat = listRatingForMonth[i]
                secRest = listSecondsRest[i]
                secWork = listSecondsWork[i]

                ratingForYear += rat
                secondsRestForYear += secRest
                secondsWorkForYear += secWork

                if i == 0:
                    fromDate = listUserUntilDate[i]

                if i % 11 == 0:
                    untilDate = listUserFromDate[i]

                i += 1

            self.db.c.execute(
                'INSERT INTO usersTimeForYear (idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (VariablesHelper.userId, name, surname, untilDate, fromDate, secondsRestForYear, secondsWorkForYear,
                 ratingForYear))
            self.db.connection.commit()

        else:
            print("error")

    def start_calculation(self):
        self.db.c.execute("SELECT ratingForMonth FROM userstimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultRatingForMonth = self.db.c.fetchall()

        self.db.c.execute("SELECT fromDate FROM userstimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultUserFromDate = self.db.c.fetchall()

        self.db.c.execute("SELECT untilDate FROM userstimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultUserUntilDate = self.db.c.fetchall()

        self.db.c.execute("SELECT timeSecondsRest FROM userstimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultSecondsRest = self.db.c.fetchall()

        self.db.c.execute("SELECT timeSecondsWork FROM userstimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC;", (VariablesHelper.userId,))
        resultSecondsWork = self.db.c.fetchall()
        self.convert_data(resultUserFromDate, resultUserUntilDate, resultSecondsRest, resultSecondsWork, resultRatingForMonth )

    def convert_data(self, resultUserFromDate, resultUserUntilDate, resultSecondsRest, resultSecondsWork, resultRatingForMonth ):
        listRatingForMonth = []
        listUserFromDate = []
        listUserUntilDate = []
        listSecondsRest = []
        listSecondsWork = []

        i = 0
        while i < len(resultRatingForMonth):
            listRatingForMonth.append(int(resultRatingForMonth[i][0]))
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

        self.calculation_year_rating(listRatingForMonth, listUserFromDate, listUserUntilDate, listSecondsRest, listSecondsWork)

