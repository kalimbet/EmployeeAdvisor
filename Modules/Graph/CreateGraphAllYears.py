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
        if os.path.isfile('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg'):
            os.remove('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg')
        self.db.c.execute('SELECT ratingForYear FROM usersTimeForYear WHERE idUser = (%s) ORDER BY untilDate ASC', (VariablesHelper.userId,))
        resultRatingForAllYears = self.db.c.fetchall()
        self.db.c.execute('SELECT fromDate FROM usersTimeForYear WHERE idUser = (%s) ORDER BY untilDate ASC',
                          (VariablesHelper.userId,))
        resultDate = self.db.c.fetchall()
        self.convert_data(resultRatingForAllYears, resultDate)

    def convert_data(self, resultRatingForAllYears, resultDate):
        listWithRating = []
        listWithDate = []
        if len(resultRatingForAllYears) > 1:
            i = 0
            while i < len(resultRatingForAllYears):
                listWithRating.append(int(resultRatingForAllYears[i][0]))
                listWithDate.append(str(resultDate[i][0]))

                i += 1

        self.create_graph(listWithRating, listWithDate)

    def create_graph(self, listWithRating, listWithDate):
        x = listWithDate
        z1 = listWithRating

        plt.figure()
        plt.bar(x, z1, color=(0.4, 0.4, 0.8, 0.6))
        plt.title('Rating for all years')
        plt.subplots_adjust(bottom=0.3)

        plt.xticks(x, x, rotation=45, fontsize='12',
                   horizontalalignment='right')
        plt.subplots_adjust(bottom=0.3)

        plt.grid(False)
        if len(listWithRating) > 0:
            self.save_img()
        else:
            if os.path.isfile('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg'):
                os.remove('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg')

    def save_img(self):
        plt.savefig('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg', dpi = 95)
        plt.close()
