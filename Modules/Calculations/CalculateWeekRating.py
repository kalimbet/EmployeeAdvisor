import tkinter as tk


import VariablesHelper



class Child(tk.Toplevel):
    def __init__(self, db):
        self.db = db
        self.start_calculation()
    # Initialization Child window

    def calculation_week_rating(self, listRatingForDay, listUserDate, listSecondsRest, listSecondsWork):
        self.db.c.execute("SELECT name FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultName = self.db.c.fetchall()
        name = resultName[0][0]
        self.db.c.execute("SELECT surname FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultSurname = self.db.c.fetchall()
        surname = resultSurname[0][0]

        ratingForWeek = 0
        secondsRestForWeek = 0
        secondsWorkForWeek = 0

        if len(listRatingForDay) > 4:

            i = 0
            while i < 5:  # len(listRatingForDay):
                rat = listRatingForDay[i]
                secRest = listSecondsRest[i]
                secWork = listSecondsWork[i]

                ratingForWeek += rat
                secondsRestForWeek += secRest
                secondsWorkForWeek += secWork
                if i == 0:
                    fromDate = listUserDate[i]


                if i % 4 == 0:
                    untilDate = listUserDate[i]

                i += 1

            self.db.c.execute(
                'INSERT INTO usersTimeForWeek (idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (VariablesHelper.userId, name, surname, untilDate, fromDate, secondsRestForWeek, secondsWorkForWeek,
                 ratingForWeek))
            self.db.connection.commit()

        else:
            print("error")

    def start_calculation(self):
        self.db.c.execute("SELECT ratingForDay FROM userstimeForDay WHERE idUser = (%s) ORDER BY date DESC;", (VariablesHelper.userId,))
        resultRatingForDay = self.db.c.fetchall()

        self.db.c.execute("SELECT date FROM userstimeForDay WHERE idUser = (%s) ORDER BY date DESC;", (VariablesHelper.userId,))
        resultUserDate = self.db.c.fetchall()

        self.db.c.execute("SELECT timeSecondsRest FROM userstimeForDay WHERE idUser = (%s) ORDER BY date DESC;", (VariablesHelper.userId,))
        resultSecondsRest = self.db.c.fetchall()

        self.db.c.execute("SELECT timeSecondsWork FROM userstimeForDay WHERE idUser = (%s) ORDER BY date DESC;", (VariablesHelper.userId,))
        resultSecondsWork = self.db.c.fetchall()
        self.convert_data(resultUserDate, resultSecondsRest, resultSecondsWork, resultRatingForDay, )

    def convert_data(self,resultUserDate, resultSecondsRest, resultSecondsWork, resultRatingForDay, ):
        listRatingForDay = []
        listUserDate = []
        listSecondsRest = []
        listSecondsWork = []

        i = 0
        while i < len(resultRatingForDay):
            listRatingForDay.append(int(resultRatingForDay[i][0]))
            i += 1
        i = 0
        while i < len(resultUserDate):
            listUserDate.append(str(resultUserDate[i][0]))
            i += 1
        i = 0
        while i < len(resultSecondsRest):
            listSecondsRest.append(int(resultSecondsRest[i][0]))
            i += 1
        i = 0
        while i < len(resultSecondsWork):
            listSecondsWork.append(int(resultSecondsWork[i][0]))
            i += 1

        self.calculation_week_rating(listRatingForDay, listUserDate, listSecondsRest, listSecondsWork)

