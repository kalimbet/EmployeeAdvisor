import os
import statistics
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import VariablesHelper

class Child(tk.Toplevel):
    def __init__(self, db):
        self.db = db
        self.start_create()
    # Initialization Child window

    def start_create(self):
        if os.path.isfile('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg'):
            os.remove('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg')

        self.db.c.execute('SELECT ratingForDay FROM usersTimeForDay WHERE idUser = (%s) ORDER BY date DESC', (VariablesHelper.userId,))
        resultRatingForWeek = self.db.c.fetchall()

        self.convert_data(resultRatingForWeek)

    def convert_data(self, resultRatingForWeek):
        listWithRating = []

        if len(resultRatingForWeek) > 4:
            i = 0
            while i < 5:
                listWithRating.append(int(resultRatingForWeek[i][0]))

                i += 1

            self.create_graph(listWithRating)

    def create_graph(self, listWithRating):

        dif = VariablesHelper.maxRatingForDay - statistics.mean(listWithRating)
        names = dif, statistics.mean(listWithRating),
        size = [dif, statistics.mean(listWithRating)]


        # Create a pieplot
        plt.pie(size, labels=np.round(names, decimals=2), colors=['red', 'green'], textprops={'fontsize': 18})
        plt.title("AVG for week", fontsize=18)
        plt.text(-0.15, -0.2, VariablesHelper.maxRatingForDay, fontsize=60)
        # plt.show()

        # add a circle at the center
        my_circle = plt.Circle((0, 0), 0.6,  color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        if len(listWithRating) > 0:
            self.save_img()
        else:
            if os.path.isfile('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg'):
                os.remove('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg')


    def save_img(self):
        plt.savefig('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg', dpi=50)
        plt.close()
