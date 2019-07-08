import os
import tkinter as tk
import matplotlib.pyplot as plt

import VariablesHelper

class Child(tk.Toplevel):
    def __init__(self, db):
        self.db = db
        self.start_create()
    # Initialization Child window

    def start_create(self):
        if os.path.isfile('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg'):
            os.remove('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg')
        self.db.c.execute('SELECT ratingForMonth FROM usersTimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC', (VariablesHelper.userId,))
        resultRatingForMonth = self.db.c.fetchall()
        self.db.c.execute('SELECT month FROM usersTimeForMonth WHERE idUser = (%s) ORDER BY untilDate DESC',
                          (VariablesHelper.userId,))
        resultMonth = self.db.c.fetchall()
        self.convert_data(resultRatingForMonth, resultMonth)

    def convert_data(self, resultRatingForMonth, resultMonth):
        listWithRating = []
        listWithDate = []
        if len(resultRatingForMonth) > 11:
            i = 0
            while i < 12:
                listWithRating.append(int(resultRatingForMonth[i][0]))
                listWithDate.append(str(resultMonth[i][0]))

                i += 1

        self.create_graph(listWithRating, listWithDate)

    def create_graph(self, listWithRating, listNameOfDay):
        x = listNameOfDay
        z1 = listWithRating

        plt.figure()
        plt.bar(x, z1, color=(0.4, 0.7, 0.4, 0.6))
        plt.title('Rating for last 12 month')
        plt.xticks(x, x,  rotation=45, fontsize='14',
                   horizontalalignment='right')
        plt.subplots_adjust(bottom=0.3)

        plt.grid(False)
        if len(listWithRating) > 0:
            self.save_img()
        else:
            if os.path.isfile('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg'):
                os.remove('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg')

    def save_img(self):
        plt.savefig('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg', dpi = 95)
        plt.close()
