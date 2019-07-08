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
        if os.path.isfile('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg'):
            os.remove('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg')
        self.db.c.execute('SELECT ratingForWeek FROM usersTimeForWeek WHERE idUser = (%s) ORDER BY untilDate DESC', (VariablesHelper.userId,))
        resultRatingForWeek = self.db.c.fetchall()
        self.convert_data(resultRatingForWeek)

    def convert_data(self, resultRatingForWeek, ):
        listWithRating = []
        listWithDate = []
        if len(resultRatingForWeek) > 3:
            i = 0
            while i < 4:
                listWithRating.append(int(resultRatingForWeek[i][0]))
                listWithDate.append(str(i+1))

                i += 1

        self.create_graph(listWithRating, listWithDate)

    def create_graph(self, listWithRating, listNameOfDay):

        x = listNameOfDay
        z1 = listWithRating

        plt.figure()
        plt.bar(x, z1, color=(0.7, 0.4, 0.4, 0.6))
        plt.title('Rating for last 4 week')
        plt.grid(False)

        if len(listWithRating) > 0:
            self.save_img()
        else:
            if os.path.isfile('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg'):
                os.remove('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg')

    def save_img(self):
        plt.savefig('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg', dpi = 95)
        plt.close()
