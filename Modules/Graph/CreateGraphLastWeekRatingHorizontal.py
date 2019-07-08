import tkinter as tk
import matplotlib.pyplot as plt

import VariablesHelper

class Child(tk.Toplevel):
    def __init__(self, db):
        self.db = db
        self.start_create()
    # Initialization Child window


    def start_create(self):
        self.db.c.execute('SELECT ratingForDay FROM usersTimeForDay WHERE idUser = (%s) ORDER BY date DESC', (VariablesHelper.userId,))
        resultRatingForWeek = self.db.c.fetchall()
        self.db.c.execute('SELECT weekDay FROM usersTimeForDay WHERE idUser = (%s) ORDER BY date DESC',
                          (VariablesHelper.userId,))
        resultDateForWeek = self.db.c.fetchall()
        self.convert_data(resultRatingForWeek, resultDateForWeek)

    def convert_data(self, resultRatingForWeek, resultDateForWeek):
        listWithRating = []
        listWithDate = []
        if len(resultRatingForWeek) > 4:
            i = 0
            while i < 5:
                listWithRating.append(int(resultRatingForWeek[i][0]))
                listWithDate.append(int(resultDateForWeek[i][0]))
                i += 1
            self.name_of_day(listWithRating, listWithDate)


    def name_of_day(self, listWithRating, listWithDate):
        listNameOfDay = []
        test = {
            0: 'Mon',
            1: 'Tue',
            2: 'Wed',
            3: 'Thu',
            4: 'Fri',
            5: 'Sat',
            6: 'Sun',
        }
        i = 0
        while i < len(listWithDate):
            listNameOfDay.append(test.get(listWithDate[i]))
            i += 1
        self.create_graph(listWithRating, listNameOfDay)

    def create_graph(self, listWithRating, listNameOfDay):
        x = listNameOfDay
        z1 = listWithRating

        plt.figure()
        plt.barh(x, z1, color=(0.2, 0.4, 0.6, 0.6))
        plt.title('Rating for last 5 days')
        plt.grid(False)

        self.save_img()

    def save_img(self):
        plt.savefig('pictures/tabFirstGraph/rating_for_week.' + str(VariablesHelper.userId) + '.jpg', dpi = 75)
        plt.close()
