import datetime
import tkinter as tk


import VariablesHelper



class Child(tk.Toplevel):
    def __init__(self, db):
        self.db = db
        self.start_calculation()
    # Initialization Child window

    def get_sec(self, time_str):
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    def clculation_time_on_room(self, lst):
        result = 0
        i = 0
        while i + 1 < len(lst):
            secondElement = lst[i + 1]
            firstElement = lst[i]

            if (firstElement - secondElement) < 3600:
                result += (firstElement - secondElement)
                i += 1
            else:
                i += 2
        return result

    def calculation_rating_for_day(self, timeOnRoomRest, timeOnRoomWork):
        points = 0

        if (timeOnRoomWork >= 14400 and timeOnRoomWork > 0):
            points += 2
        else:
            points += 0
        if (timeOnRoomRest <= 14400 and timeOnRoomRest > 0):
            points += 2
        else:
            points += 0
        if (int(VariablesHelper.taskStatus) == 1):
            points += 3

        return points

    def start_calculation(self):
        self.db.c.execute("SELECT name FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultName = self.db.c.fetchall()
        name = resultName[0][0]
        self.db.c.execute("SELECT surname FROM users WHERE id = (%s);", (VariablesHelper.userId,))
        resultSurname = self.db.c.fetchall()
        surname = resultSurname[0][0]
        nowDate = datetime.datetime.today()
        weekDay = datetime.date.today().weekday()


        timeOnRoomRest = self.clculation_time_on_room(self.convert_data(2)) + self.clculation_time_on_room(self.convert_data(3))
        timeOnRoomWork = self.clculation_time_on_room(self.convert_data(1))
        ratingForDay = self.calculation_rating_for_day(timeOnRoomRest, timeOnRoomWork)
        self.db.c.execute(
            'INSERT INTO usersTimeForDay (idUser, name, surname, date, weekDay, timeSecondsrest, timeSecondsWork, ratingForDay) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)',
            (VariablesHelper.userId, name, surname, nowDate, weekDay, timeOnRoomRest, timeOnRoomWork, ratingForDay))
        self.db.connection.commit()

    def convert_data(self, roomId):
        self.db.c.execute("SELECT time FROM userstime WHERE idUser = (%s) AND numberRoom = (%s) ORDER BY date DESC;", (VariablesHelper.userId, roomId,))
        resultTime = self.db.c.fetchall()

        listString = []
        listSeconds = []

        # Convert tupl time to list[String]
        i = 0
        while i < len(resultTime):
            listString.append(str(resultTime[i][0]))
            i += 1

        # Convert list[String] to seconds
        i = 0
        while i < len(listString):
            listSeconds.append(self.get_sec(listString[i]))
            i += 1
        self.delete_user_time(roomId)
        return listSeconds


    def delete_user_time(self, roomId):
        self.db.c.execute("DELETE FROM userstime WHERE idUser = (%s) AND numberRoom = (%s)", (VariablesHelper.userId, roomId,))
        self.db.connection.commit()