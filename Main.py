import datetime
import os
import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import ConfigurationWindow, DataBase, VariablesHelper

from AdditionalWindows import TaskStatusWindow, AddDayRatingWindow, AddWeekRatingWindow, AddMonthRatingWindow, AddYearRatingWindow, RegistrationUserWindow, UpdateDayRatingWindow, UpdateWeekRatingWindow, UpdateMonthRatingWindow, UpdateYearRatingWindow
from Modules.Cameras import CameraKitchen, CameraWorkplace, CameraGym
from Modules.Calculations import CalculateRatingForDay, CalculateWeekRating, CalculateMonthRating, CalculateYearRating
from Modules.Recoginzer import RegistrationUser, TrainRecognizer
from Modules.Graph import CreateGraphLastWeekRating, CreateGraphLastWeekRatingHorizontal, CreateGraphLastMonthRating, CreateGraphLastYearRating, CreateGraphAvgWeek, CreateGraphAvgMonth, CreateGraphAvgYear, CreateGraphAllYears

class Main(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.db = db

        self.tab_first()
        self.tab_second()
        self.tab_third()
        self.tab_fourth()
        self.tab_fifth()
        self.tab_last()
        self.tab_first_view_records()
        self.tab_second_view_records()
        self.tab_third_view_records()
        self.tab_fourth_view_records()
        self.tab_fifth_view_records()
        self.tab_last_view_records()
        # Workplace


    def tab_first(self):
        test = tk.Text(lab1, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test.insert(1.0, "")
        test.place(x=410, y=250)

        test1 = tk.Text(lab1, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test1.insert(1.0, "")
        test1.place(x=0, y=0)


        test2 = tk.Text(lab1, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test2.insert(1.0, "")
        test2.place(x=0, y=824)

        canvasUserAvatar.image = ImageTk.PhotoImage(imageUserAvatar)
        canvasUserAvatar.create_image(0, 0, image=canvasUserAvatar.image, anchor='nw')


        self.tab_first_change_user_img = tk.PhotoImage(file='icons/128x128/user.png')
        btn_open_dialog_user_info = tk.Button(lab1, text='Change user', command=self.tab_first_change_user,
                                              compound=tk.BOTTOM, image=self.tab_first_change_user_img)
        btn_open_dialog_user_info.place(x=30, y=260)

        calculationData = tk.Text(lab1, width=53, height=1, bg="black", fg='white', wrap=tk.WORD)
        calculationData.insert(1.0, "Select calculation!")
        calculationData.configure(state=tk.DISABLED)
        calculationData.place(x=0, y=430)

        btn_calc_user_rating_for_day = tk.Button(lab1, text='Rating for day', command=self.tab_first_calc_rating_open,
                                              compound=tk.BOTTOM)
        btn_calc_user_rating_for_day.place(x=12, y=460)

        btn_calc_user_rating_for_week = tk.Button(lab1, text='Rating for week',
                                                 command=self.tab_first_calculate_user_rating_for_week,
                                                 compound=tk.BOTTOM)
        btn_calc_user_rating_for_week.place(x=107, y=460)

        btn_calc_user_rating_for_month = tk.Button(lab1, text='Rating for month',
                                                  command=self.tab_first_calculate_user_rating_for_month,
                                                  compound=tk.BOTTOM)
        btn_calc_user_rating_for_month.place(x=207, y=460)

        btn_calc_user_rating_for_year = tk.Button(lab1, text='Rating for year',
                                                   command=self.tab_first_calculate_user_rating_for_year,
                                                   compound=tk.BOTTOM)
        btn_calc_user_rating_for_year.place(x=317, y=460)


        self.first_name_table = ttk.Treeview(lab1, columns=(
            'name'), height=1, show='headings', style="mystyle.Treeview")
        self.first_name_table.column('name', width=200, anchor=tk.CENTER)
        self.first_name_table.heading('name', text='Name')
        self.first_name_table.place(x=200, y=20)

        self.first_surname_table = ttk.Treeview(lab1, columns=(
            'surname'), height=1, show='headings', style="mystyle.Treeview")
        self.first_surname_table.column('surname', width=200, anchor=tk.CENTER)
        self.first_surname_table.heading('surname', text='Surname')
        self.first_surname_table.place(x=200, y=75)

        self.first_address_table = ttk.Treeview(lab1, columns=(
            'address'), height=1, show='headings', style="mystyle.Treeview")
        self.first_address_table.column('address', width=200, anchor=tk.CENTER)
        self.first_address_table.heading('address', text='Address')
        self.first_address_table.place(x=200, y=135)

        self.first_email_table = ttk.Treeview(lab1, columns=(
            'email'), height=1, show='headings', style="mystyle.Treeview")
        self.first_email_table.column('email', width=200, anchor=tk.CENTER)
        self.first_email_table.heading('email', text='Email')
        self.first_email_table.place(x=200, y=195)

        self.first_group_table = ttk.Treeview(lab1, columns=(
            'group'), height=1, show='headings', style="mystyle.Treeview")
        self.first_group_table.column('group', width=200, anchor=tk.CENTER)
        self.first_group_table.heading('group', text='Group')
        self.first_group_table.place(x=200, y=255)

        self.first_country_table = ttk.Treeview(lab1, columns=(
            'country'), height=1, show='headings', style="mystyle.Treeview")
        self.first_country_table.column('country', width=200, anchor=tk.CENTER)
        self.first_country_table.heading('country', text='Country')
        self.first_country_table.place(x=200, y=310)

        self.first_date_registration_table = ttk.Treeview(lab1, columns=(
            'date_registration'), height=1, show='headings', style="mystyle.Treeview")
        self.first_date_registration_table.column('date_registration', width=200, anchor=tk.CENTER)
        self.first_date_registration_table.heading('date_registration', text='Date registration')
        self.first_date_registration_table.place(x=200, y=370)

        userTable = tk.Text(lab1, width=53, height=1, bg="black", fg='white', wrap=tk.WORD)
        userTable.insert(1.0, "All users in the system!")
        userTable.configure(state=tk.DISABLED)
        userTable.place(x=0, y=520)

        self.first_info_about_users_table = ttk.Treeview(lab1, columns=(
            'id', 'name', 'surname', 'dateReg'), height=13, show='headings', style="mystyle.Treeview")
        self.first_info_about_users_table.column('id', width=50, anchor=tk.CENTER)
        self.first_info_about_users_table.column('name', width=120, anchor=tk.CENTER)
        self.first_info_about_users_table.column('surname', width=120, anchor=tk.CENTER)
        self.first_info_about_users_table.column('dateReg', width=140, anchor=tk.CENTER)

        self.first_info_about_users_table.heading('id', text='id')
        self.first_info_about_users_table.heading('name', text='Name')
        self.first_info_about_users_table.heading('surname', text='Surname')
        self.first_info_about_users_table.heading('dateReg', text='Date registration')
        self.first_info_about_users_table.place(x=0, y=540)


    def tab_first_change_user(self):
        VariablesHelper.userId = self.first_info_about_users_table.set(self.first_info_about_users_table.selection()[0], '#1')
        self.tab_first_change_user_records()

    def tab_first_change_user_records(self):
        self.tab_first_view_records()
        self.tab_second_view_records()
        self.tab_third_view_records()
        self.tab_fourth_view_records()
        self.tab_fifth_view_records()
        self.tab_last_view_records()
        self.tab_first_change_user_avatar()





        self.tab_first_change_user_rating_for_week_circle()
        self.tab_first_change_user_rating_for_month_circle()
        self.tab_first_change_user_rating_for_year_circle()
        self.tab_second_change_user_rating_for_week()
        self.tab_third_change_user_rating_for_month()
        self.tab_fourth_change_user_rating_for_year()
        self.tab_fifth_change_user_rating_for_all_years()


    def tab_first_create_graph_bar_for_week(self):
        CreateGraphLastWeekRating.Child(db)
        if os.path.isfile('pictures/tabFirstGraph/rating_for_week.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_second_change_user_rating_for_week()

    def tab_first_create_graph_circle_for_week(self):
        CreateGraphAvgWeek.Child(db)
        if os.path.isfile('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_first_change_user_rating_for_week_circle()

    def tab_first_create_graph_circle_for_month(self):
        CreateGraphAvgMonth.Child(db)
        if os.path.isfile('pictures/tabFirstGraph/rating_for_month_circle.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_first_change_user_rating_for_month_circle()

    def tab_first_create_graph_circle_for_year(self):
        CreateGraphAvgYear.Child(db)
        if os.path.isfile('pictures/tabFirstGraph/rating_for_year_circle.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_first_change_user_rating_for_year_circle()


    def tab_first_view_records(self):
        self.db.c.execute(
            "SELECT name FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_name_table.delete(i) for i in self.first_name_table.get_children()]
        [self.first_name_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT surname FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_surname_table.delete(i) for i in self.first_surname_table.get_children()]
        [self.first_surname_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT address FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_address_table.delete(i) for i in self.first_address_table.get_children()]
        [self.first_address_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT email FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_email_table.delete(i) for i in self.first_email_table.get_children()]
        [self.first_email_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT groupNumber FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_group_table.delete(i) for i in self.first_group_table.get_children()]
        [self.first_group_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT country FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_country_table.delete(i) for i in self.first_country_table.get_children()]
        [self.first_country_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT dateRegistration FROM users WHERE id = (%s)", (VariablesHelper.userId,))
        [self.first_date_registration_table.delete(i) for i in self.first_date_registration_table.get_children()]
        [self.first_date_registration_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.db.c.execute(
            "SELECT id, name, surname,dateRegistration FROM users ")
        [self.first_info_about_users_table.delete(i) for i in self.first_info_about_users_table.get_children()]
        [self.first_info_about_users_table.insert('', 'end', values=row) for row in self.db.c.fetchall()]

        self.tab_first_change_user_avatar()

        self.tab_first_create_graph_circle_for_week()
        self.tab_first_create_graph_circle_for_month()
        self.tab_first_create_graph_circle_for_year()

    def tab_first_change_user_avatar(self):
        im2 = Image.open('dataset/User.' + str(VariablesHelper.userId) + '.2.jpg')
        canvasUserAvatar.image = ImageTk.PhotoImage(im2)
        canvasUserAvatar.create_image(0, 0, image=canvasUserAvatar.image, anchor='nw')

    def tab_first_change_user_rating_for_week_circle(self):

        if os.path.isfile('pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForLastWeekCircle2 = Image.open(
                'pictures/tabFirstGraph/rating_for_week_circle.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForLastWeekCircle.image = ImageTk.PhotoImage(imageUserRatingForLastWeekCircle2)
            canvasUserRatingForLastWeekCircle.create_image(0, 0, image=canvasUserRatingForLastWeekCircle.image, anchor='nw')
        else:
            imageUserRatingForLastWeekCircle2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForLastWeekCircle.image = ImageTk.PhotoImage(imageUserRatingForLastWeekCircle2)
            canvasUserRatingForLastWeekCircle.create_image(0, 0, image=canvasUserRatingForLastWeekCircle.image,
                                                           anchor='nw')

    def tab_first_change_user_rating_for_month_circle(self):

        if os.path.isfile('pictures/tabFirstGraph/rating_for_month_circle.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForLastMonthCircle2 = Image.open(
                'pictures/tabFirstGraph/rating_for_month_circle.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForLastMonthCircle.image = ImageTk.PhotoImage(imageUserRatingForLastMonthCircle2)
            canvasUserRatingForLastMonthCircle.create_image(0, 0, image=canvasUserRatingForLastMonthCircle.image, anchor='nw')
        else:
            imageUserRatingForLastMonthCircle2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForLastMonthCircle.image = ImageTk.PhotoImage(imageUserRatingForLastMonthCircle2)
            canvasUserRatingForLastMonthCircle.create_image(0, 0, image=canvasUserRatingForLastMonthCircle.image,
                                                           anchor='nw')

    def tab_first_change_user_rating_for_year_circle(self):

        if os.path.isfile('pictures/tabFirstGraph/rating_for_year_circle.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForLastYearCircle2 = Image.open(
                'pictures/tabFirstGraph/rating_for_year_circle.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForLastYearCircle.image = ImageTk.PhotoImage(imageUserRatingForLastYearCircle2)
            canvasUserRatingForLastYearCircle.create_image(0, 0, image=canvasUserRatingForLastYearCircle.image,
                                                            anchor='nw')
        else:
            imageUserRatingForLastYearCircle2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForLastYearCircle.image = ImageTk.PhotoImage(imageUserRatingForLastYearCircle2)
            canvasUserRatingForLastYearCircle.create_image(0, 0, image=canvasUserRatingForLastYearCircle.image,
                                                            anchor='nw')

    def tab_first_calc_rating_open(self):
        TaskStatusWindow.Child(window, app)

    def tab_first_calculate_rating_for_day(self, taskStatus):
        VariablesHelper.taskStatus = taskStatus
        CalculateRatingForDay.Child(db)
        self.tab_second_view_records()

    def tab_first_calculate_user_rating_for_week(self):
        CalculateWeekRating.Child(db)
        self.tab_third_view_records()

    def tab_first_calculate_user_rating_for_month(self):
        CalculateMonthRating.Child(db)
        self.tab_fourth_view_records()

    def tab_first_calculate_user_rating_for_year(self):
        CalculateYearRating.Child(db)
        self.tab_fifth_view_records()




    def tab_second(self):

        test1 = tk.Text(lab2, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test1.insert(1.0, "")
        test1.place(x=0, y=0)

        test2 = tk.Text(lab2, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test2.insert(1.0, "")
        test2.place(x=0, y=824)

        self.tab_second_add_img = tk.PhotoImage(file='icons/128x128/folderAdd.png')
        btn_open_dialog = tk.Button(lab2, text='Add data', command=self.tab_second_open_dialog,
                                    compound=tk.BOTTOM, image=self.tab_second_add_img)
        btn_open_dialog.place(x=10, y=20)

        self.tab_second_update_img = tk.PhotoImage(file='icons/128x128/folderUpl.png')
        btn_open_dialog_info = tk.Button(lab2, text='Update info', command=self.tab_second_open_dialog_update,
                                         compound=tk.BOTTOM, image=self.tab_second_update_img)
        btn_open_dialog_info.place(x=10, y=182)

        self.tab_second_delete_img = tk.PhotoImage(file='icons/128x128/folderDel.png')
        btn_open_dialog_info = tk.Button(lab2, text='Delete info', command=self.tab_second_delete_record,
                                         compound=tk.BOTTOM, image=self.tab_second_delete_img)
        btn_open_dialog_info.place(x=10, y=344)


        self.ratingForDay = ttk.Treeview(lab2, columns=('id','idUser', 'name', 'surname', 'date', 'weekDay', 'timeSecondsRest',
                                                        'timeSecondsWork', 'ratingForDay'), height=15, show='headings', style="mystyle.Treeview")
        self.ratingForDay.column('id', width=60, anchor=tk.CENTER)
        self.ratingForDay.column('idUser', width=60, anchor=tk.CENTER)
        self.ratingForDay.column('name', width=100, anchor=tk.CENTER)
        self.ratingForDay.column('surname', width=140, anchor=tk.CENTER)
        self.ratingForDay.column('date', width=100, anchor=tk.CENTER)
        self.ratingForDay.column('weekDay', width=60, anchor=tk.CENTER)
        self.ratingForDay.column('timeSecondsRest', width=130, anchor=tk.CENTER)
        self.ratingForDay.column('timeSecondsWork', width=130, anchor=tk.CENTER)
        self.ratingForDay.column('ratingForDay', width=130, anchor=tk.CENTER)

        self.ratingForDay.heading('id', text='id')
        self.ratingForDay.heading('idUser', text='idUser')
        self.ratingForDay.heading('name', text='Name')
        self.ratingForDay.heading('surname', text='Surname')
        self.ratingForDay.heading('date', text='Date')
        self.ratingForDay.heading('weekDay', text='Day')
        self.ratingForDay.heading('timeSecondsRest', text='Time on rest')
        self.ratingForDay.heading('timeSecondsWork', text='Time on work')
        self.ratingForDay.heading('ratingForDay', text='Rating for day')

        self.ratingForDay.place(x=160, y=20)

        test3 = tk.Text(lab2, width=114, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test3.insert(1.0, "")
        test3.place(x=160, y=350)
    def tab_second_records(self, date, timeSecondsRest, timeSecondsWork, ratingForDay):
        self.db.insert_data_for_rating_day(VariablesHelper.userId, date, timeSecondsRest, timeSecondsWork, ratingForDay)
        self.tab_second_view_records()

    def tab_second_view_records(self):
        self.db.c.execute(
            "SELECT id, idUser, name, surname, date, weekDay, timeSecondsRest, timeSecondsWork, ratingForDay FROM userstimeforday WHERE idUser = (%s) ORDER BY date DESC", (VariablesHelper.userId,))
        [self.ratingForDay.delete(i) for i in self.ratingForDay.get_children()]
        [self.ratingForDay.insert('', 'end', values=row) for row in self.db.c.fetchall()]

        self.tab_second_create_graph_bar_plot_for_week()

    def tab_second_update_record(self, date, timeSecondsRest, timeSecondsWork, ratingForDay):
        year, month, day = (int(x) for x in date.split('-'))
        weekDay = datetime.date(year, month, day).weekday()
        self.db.c.execute("UPDATE usersTimeForDay SET date = (%s), weekDay = (%s), timeSecondsRest = (%s), timeSecondsWork = (%s), ratingForDay = (%s) WHERE id = (%s)", (date, weekDay, timeSecondsRest, timeSecondsWork, ratingForDay, self.ratingForDay.set(self.ratingForDay.selection()[0], '#1')))
        self.db.connection.commit()
        self.tab_second_view_records()

    def tab_second_delete_record(self):
        self.db.c.execute("DELETE FROM usersTimeForDay WHERE id = (%s)", (self.ratingForDay.set(self.ratingForDay.selection()[0], '#1'), ))
        self.db.connection.commit()
        self.tab_second_view_records()

    def tab_second_open_dialog(self):
        AddDayRatingWindow.Child(window, app)

    def tab_second_open_dialog_update(self):
        UpdateDayRatingWindow.Child(window, app)

    def tab_second_create_graph_bar_plot_for_week(self):
        CreateGraphLastWeekRating.Child(db)
        if os.path.isfile('pictures/tabSecondGraph/rating_for_week.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_second_change_user_rating_for_week()

    def tab_second_change_user_rating_for_week(self):

        if os.path.isfile('pictures/tabSecondGraph/rating_for_week.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForLastWeek2 = Image.open(
                'pictures/tabSecondGraph/rating_for_week.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForLastWeek.image = ImageTk.PhotoImage(imageUserRatingForLastWeek2)
            canvasUserRatingForLastWeek.create_image(0, 0, image=canvasUserRatingForLastWeek.image, anchor='nw')
        else:
            imageUserRatingForLastWeek2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForLastWeek.image = ImageTk.PhotoImage(imageUserRatingForLastWeek2)
            canvasUserRatingForLastWeek.create_image(0, 0, image=canvasUserRatingForLastWeek.image,
                                                     anchor='nw')


    def tab_third(self):

        test1 = tk.Text(lab3, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test1.insert(1.0, "")
        test1.place(x=0, y=0)

        test2 = tk.Text(lab3, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test2.insert(1.0, "")
        test2.place(x=0, y=824)


        self.ratingForWeek = ttk.Treeview(lab3, columns=('id',
        'idUser', 'name', 'surname', 'fromDate', 'untilDate', 'timeSecondsRest',
        'timeSecondsWork', 'ratingForWeek'), height=15, show='headings', style="mystyle.Treeview")
        self.ratingForWeek.column('id', width=60, anchor=tk.CENTER)
        self.ratingForWeek.column('idUser', width=70, anchor=tk.CENTER)
        self.ratingForWeek.column('name', width=130, anchor=tk.CENTER)
        self.ratingForWeek.column('surname', width=140, anchor=tk.CENTER)
        self.ratingForWeek.column('fromDate', width=100, anchor=tk.CENTER)
        self.ratingForWeek.column('untilDate', width=100, anchor=tk.CENTER)
        self.ratingForWeek.column('timeSecondsRest', width=100, anchor=tk.CENTER)
        self.ratingForWeek.column('timeSecondsWork', width=100, anchor=tk.CENTER)
        self.ratingForWeek.column('ratingForWeek', width=120, anchor=tk.CENTER)

        self.ratingForWeek.heading('id', text='id')
        self.ratingForWeek.heading('idUser', text='idUser')
        self.ratingForWeek.heading('name', text='Name')
        self.ratingForWeek.heading('surname', text='Surname')
        self.ratingForWeek.heading('fromDate', text='From date')
        self.ratingForWeek.heading('untilDate', text='Until date')
        self.ratingForWeek.heading('timeSecondsRest', text='Time on rest')
        self.ratingForWeek.heading('timeSecondsWork', text='Time on work')
        self.ratingForWeek.heading('ratingForWeek', text='Rating for week')

        self.ratingForWeek.place(x=215, y=20)

        self.tab_third_add_img = tk.PhotoImage(file='icons/128x128/folderAdd.png')
        btn_open_dialog = tk.Button(lab3, text='Add data', command=self.tab_third_open_dialog,
                                    compound=tk.BOTTOM, image=self.tab_second_add_img)
        btn_open_dialog.place(x=1150, y=20)

        self.tab_third_update_img = tk.PhotoImage(file='icons/128x128/folderUpl.png')
        btn_open_dialog_info = tk.Button(lab3, text='Update info', command=self.tab_third_open_dialog_update,
                                         compound=tk.BOTTOM, image=self.tab_third_update_img)
        btn_open_dialog_info.place(x=1150, y=182)

        self.tab_third_delete_img = tk.PhotoImage(file='icons/128x128/folderDel.png')
        btn_open_dialog_info = tk.Button(lab3, text='Delete info', command=self.tab_third_delete_record,
                                         compound=tk.BOTTOM, image=self.tab_third_delete_img)
        btn_open_dialog_info.place(x=1150, y=344)

        test3 = tk.Text(lab3, width=114, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test3.insert(1.0, "")
        test3.place(x=215, y=350)

    def tab_third_records(self, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek):
        self.db.insert_data_for_rating_week(VariablesHelper.userId, fromDate, untilDate, timeSecondsRest, timeSecondsWork,
                                            ratingForWeek)
        self.tab_third_view_records()

    def tab_third_update_record(self, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek):
        self.db.c.execute("UPDATE usersTimeForWeek SET fromDate = (%s), untilDate = (%s), timeSecondsRest = (%s), timeSecondsWork = (%s), ratingForWeek = (%s) WHERE id = (%s)", (fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek, self.ratingForWeek.set(self.ratingForWeek.selection()[0], '#1')))
        self.db.connection.commit()
        self.tab_third_view_records()

    def tab_third_open_dialog_update(self):
        UpdateWeekRatingWindow.Child(window, app)

    def tab_third_delete_record(self):
        self.db.c.execute("DELETE FROM usersTimeForWeek WHERE id = (%s)", (self.ratingForWeek.set(self.ratingForWeek.selection()[0], '#1'), ))
        self.db.connection.commit()
        self.tab_third_view_records()

    def tab_third_view_records(self):
        self.db.c.execute(
            "SELECT id, idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForWeek FROM userstimeforweek WHERE idUser = (%s) ORDER BY untilDate DESC", (VariablesHelper.userId,))
        [self.ratingForWeek.delete(i) for i in self.ratingForWeek.get_children()]
        [self.ratingForWeek.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.tab_third_create_graph_bar_plot_for_month()


    def tab_third_open_dialog(self):
        AddWeekRatingWindow.Child(window, app)

    def tab_third_open_dialog_update(self):
        UpdateWeekRatingWindow.Child(window, app)

    def tab_third_create_graph_bar_plot_for_month(self):
        CreateGraphLastMonthRating.Child(db)
        if os.path.isfile('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_third_change_user_rating_for_month()

    def tab_third_change_user_rating_for_month(self):

        if os.path.isfile('pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForLastMonth2 = Image.open(
                'pictures/tabThirdGraph/rating_for_month.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForLastMonth.image = ImageTk.PhotoImage(imageUserRatingForLastMonth2)
            canvasUserRatingForLastMonth.create_image(0, 0, image=canvasUserRatingForLastMonth.image, anchor='nw')
        else:
            imageUserRatingForLastMonth2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForLastMonth.image = ImageTk.PhotoImage(imageUserRatingForLastMonth2)
            canvasUserRatingForLastMonth.create_image(0, 0, image=canvasUserRatingForLastMonth.image,
                                                     anchor='nw')



    def tab_fourth(self):

        test1 = tk.Text(lab4, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test1.insert(1.0, "")
        test1.place(x=0, y=0)

        test2 = tk.Text(lab4, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test2.insert(1.0, "")
        test2.place(x=0, y=824)


        self.add_info_for_month = tk.PhotoImage(file='icons/128x128/folderAdd.png')
        btn_open_dialog = tk.Button(lab4, text='Add data', command=self.tab_fourth_open_dialog,
                                    compound=tk.BOTTOM, image=self.tab_second_add_img)
        btn_open_dialog.place(x=10, y=20)

        self.tab_fourth_update_img = tk.PhotoImage(file='icons/128x128/folderUpl.png')
        btn_open_dialog_info = tk.Button(lab4, text='Update info', command=self.tab_fourth_open_dialog_update,
                                         compound=tk.BOTTOM, image=self.tab_fourth_update_img)
        btn_open_dialog_info.place(x=10, y=182)

        self.tab_fourth_delete_img = tk.PhotoImage(file='icons/128x128/folderDel.png')
        btn_open_dialog_info = tk.Button(lab4, text='Delete info', command=self.tab_fourth_delete_record,
                                         compound=tk.BOTTOM, image=self.tab_fourth_delete_img)
        btn_open_dialog_info.place(x=10, y=344)

        self.ratingForMonth = ttk.Treeview(lab4, columns=('id',
            'idUser', 'name', 'surname', 'fromDate', 'untilDate', 'month', 'timeSecondsRest',
            'timeSecondsWork', 'ratingForMonth'), height=15, show='headings', style="mystyle.Treeview")
        self.ratingForMonth.column('id', width=60, anchor=tk.CENTER)
        self.ratingForMonth.column('idUser', width=70, anchor=tk.CENTER)
        self.ratingForMonth.column('name', width=120, anchor=tk.CENTER)
        self.ratingForMonth.column('surname', width=140, anchor=tk.CENTER)
        self.ratingForMonth.column('fromDate', width=110, anchor=tk.CENTER)
        self.ratingForMonth.column('untilDate', width=110, anchor=tk.CENTER)
        self.ratingForMonth.column('month', width=100, anchor=tk.CENTER)
        self.ratingForMonth.column('timeSecondsRest', width=100, anchor=tk.CENTER)
        self.ratingForMonth.column('timeSecondsWork', width=100, anchor=tk.CENTER)
        self.ratingForMonth.column('ratingForMonth', width=130, anchor=tk.CENTER)

        self.ratingForMonth.heading('id', text='id')
        self.ratingForMonth.heading('idUser', text='idUser')
        self.ratingForMonth.heading('name', text='Name')
        self.ratingForMonth.heading('surname', text='Surname')
        self.ratingForMonth.heading('fromDate', text='From date')
        self.ratingForMonth.heading('untilDate', text='Until date')
        self.ratingForMonth.heading('month', text='Month')
        self.ratingForMonth.heading('timeSecondsRest', text='Time on rest')
        self.ratingForMonth.heading('timeSecondsWork', text='Time on work')
        self.ratingForMonth.heading('ratingForMonth', text='Rating for month')

        self.ratingForMonth.place(x=160, y=20)

        test3 = tk.Text(lab4, width=130, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test3.insert(1.0, "")
        test3.place(x=160, y=350)


    def tab_fourth_records(self, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForMonth):
        self.db.insert_data_for_rating_month(VariablesHelper.userId, fromDate, untilDate, timeSecondsRest, timeSecondsWork,
                                             ratingForMonth)
        self.tab_fourth_view_records()

    def tab_fourth_view_records(self):
        self.db.c.execute(
            "SELECT id, idUser, name, surname, fromDate, untilDate, month, timeSecondsRest, timeSecondsWork, ratingForMonth FROM userstimeformonth WHERE idUser = (%s) ORDER BY untilDate DESC",
            (VariablesHelper.userId,))
        [self.ratingForMonth.delete(i) for i in self.ratingForMonth.get_children()]
        [self.ratingForMonth.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.tab_fourth_create_graph_bar_plot_for_year()

    def tab_fourth_update_record(self, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForMonth):
        self.db.c.execute("UPDATE usersTimeForMonth SET fromDate = (%s), untilDate = (%s), timeSecondsRest = (%s), timeSecondsWork = (%s), ratingForMonth = (%s) WHERE id = (%s)", (fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForMonth, self.ratingForMonth.set(self.ratingForMonth.selection()[0], '#1')))
        self.db.connection.commit()
        self.tab_fourth_view_records()

    def tab_fourth_delete_record(self):
        self.db.c.execute("DELETE FROM usersTimeForMonth WHERE id = (%s)", (self.ratingForMonth.set(self.ratingForMonth.selection()[0], '#1'), ))
        self.db.connection.commit()
        self.tab_fourth_view_records()

    def tab_fourth_open_dialog(self):
        AddMonthRatingWindow.Child(window, app)

    def tab_fourth_open_dialog_update(self):
        UpdateMonthRatingWindow.Child(window, app)

    def tab_fourth_create_graph_bar_plot_for_year(self):
        CreateGraphLastYearRating.Child(db)
        if os.path.isfile('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_fourth_change_user_rating_for_year()

    def tab_fourth_change_user_rating_for_year(self):

        if os.path.isfile('pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForLastYear2 = Image.open(
                'pictures/tabFourthGraph/rating_for_year.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForLastYear.image = ImageTk.PhotoImage(imageUserRatingForLastYear2)
            canvasUserRatingForLastYear.create_image(0, 0, image=canvasUserRatingForLastYear.image, anchor='nw')
        else:
            imageUserRatingForLastYear2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForLastYear.image = ImageTk.PhotoImage(imageUserRatingForLastYear2)
            canvasUserRatingForLastYear.create_image(0, 0, image=canvasUserRatingForLastYear.image,
                                                     anchor='nw')




    def tab_fifth(self):
        test1 = tk.Text(lab5, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test1.insert(1.0, "")
        test1.place(x=0, y=0)

        test2 = tk.Text(lab5, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test2.insert(1.0, "")
        test2.place(x=0, y=824)


        self.ratingForYear = ttk.Treeview(lab5, columns=('id',
            'idUser', 'name', 'surname', 'fromDate', 'untilDate', 'timeSecondsRest',
            'timeSecondsWork', 'ratingForYear'), height=15, show='headings', style="mystyle.Treeview")
        self.ratingForYear.column('id', width=60, anchor=tk.CENTER)
        self.ratingForYear.column('idUser', width=70, anchor=tk.CENTER)
        self.ratingForYear.column('name', width=130, anchor=tk.CENTER)
        self.ratingForYear.column('surname', width=140, anchor=tk.CENTER)
        self.ratingForYear.column('fromDate', width=110, anchor=tk.CENTER)
        self.ratingForYear.column('untilDate', width=110, anchor=tk.CENTER)
        self.ratingForYear.column('timeSecondsRest', width=100, anchor=tk.CENTER)
        self.ratingForYear.column('timeSecondsWork', width=100, anchor=tk.CENTER)
        self.ratingForYear.column('ratingForYear', width=130, anchor=tk.CENTER)

        self.ratingForYear.heading('id', text='id')
        self.ratingForYear.heading('idUser', text='idUser')
        self.ratingForYear.heading('name', text='Name')
        self.ratingForYear.heading('surname', text='Surname')
        self.ratingForYear.heading('fromDate', text='From date')
        self.ratingForYear.heading('untilDate', text='Until date')
        self.ratingForYear.heading('timeSecondsRest', text='Time on rest')
        self.ratingForYear.heading('timeSecondsWork', text='Time on work')
        self.ratingForYear.heading('ratingForYear', text='Rating for year')

        self.ratingForYear.place(x=180, y=20)


        self.add_info_for_year = tk.PhotoImage(file='icons/128x128/folderAdd.png')
        btn_open_dialog = tk.Button(lab5, text='Add data', command=self.tab_fifth_open_dialog,
                                    compound=tk.BOTTOM, image=self.tab_second_add_img)
        btn_open_dialog.place(x=1150, y=20)

        self.tab_fifth_update_img = tk.PhotoImage(file='icons/128x128/folderUpl.png')
        btn_open_dialog_info = tk.Button(lab5, text='Update info', command=self.tab_fifth_open_dialog_update,
                                         compound=tk.BOTTOM, image=self.tab_fifth_update_img)
        btn_open_dialog_info.place(x=1150, y=182)

        self.tab_fifth_delete_img = tk.PhotoImage(file='icons/128x128/folderDel.png')
        btn_open_dialog_info = tk.Button(lab5, text='Delete info', command=self.tab_fifth_delete_record,
                                         compound=tk.BOTTOM, image=self.tab_fifth_delete_img)
        btn_open_dialog_info.place(x=1150, y=344)

        test3 = tk.Text(lab5, width=119, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test3.insert(1.0, "")
        test3.place(x=180, y=350)

    def tab_fifth_records(self, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear):
        self.db.insert_data_for_rating_year(VariablesHelper.userId, fromDate, untilDate, timeSecondsRest, timeSecondsWork,
                                            ratingForYear)
        self.tab_fifth_view_records()

    def tab_fifth_view_records(self):
        self.db.c.execute(
            "SELECT id, idUser, name, surname, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear FROM userstimeforyear WHERE idUser = (%s) ORDER BY untilDate DESC",
            (VariablesHelper.userId,))
        [self.ratingForYear.delete(i) for i in self.ratingForYear.get_children()]
        [self.ratingForYear.insert('', 'end', values=row) for row in self.db.c.fetchall()]

        self.tab_fifth_create_graph_bar_plot_for_all_years()

    def tab_fifth_update_record(self, fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear):
        self.db.c.execute("UPDATE usersTimeForYear SET fromDate = (%s), untilDate = (%s), timeSecondsRest = (%s), timeSecondsWork = (%s), ratingForYear = (%s) WHERE id = (%s)", (fromDate, untilDate, timeSecondsRest, timeSecondsWork, ratingForYear, self.ratingForYear.set(self.ratingForYear.selection()[0], '#1')))
        self.db.connection.commit()
        self.tab_fifth_view_records()


    def tab_fifth_delete_record(self):
        self.db.c.execute("DELETE FROM usersTimeForYear WHERE id = (%s)", (self.ratingForYear.set(self.ratingForYear.selection()[0], '#1'), ))
        self.db.connection.commit()
        self.tab_fifth_view_records()

    def tab_fifth_open_dialog(self):
        AddYearRatingWindow.Child(window, app)

    def tab_fifth_open_dialog_update(self):
        UpdateYearRatingWindow.Child(window, app)

    def tab_fifth_create_graph_bar_plot_for_all_years(self):
        CreateGraphAllYears.Child(db)
        if os.path.isfile('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg'):
            self.tab_fifth_change_user_rating_for_all_years()

    def tab_fifth_change_user_rating_for_all_years(self):
        if os.path.isfile('pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg'):
            imageUserRatingForAllYears2 = Image.open(
                'pictures/tabFifthGraph/rating_for_all_years.' + str(VariablesHelper.userId) + '.jpg')
            canvasUserRatingForAllYears.image = ImageTk.PhotoImage(imageUserRatingForAllYears2)
            canvasUserRatingForAllYears.create_image(0, 0, image=canvasUserRatingForAllYears.image, anchor='nw')
        else:
            imageUserRatingForAllYears2 = Image.open(
                'icons/128x128/graphIm.png')
            canvasUserRatingForAllYears.image = ImageTk.PhotoImage(imageUserRatingForAllYears2)
            canvasUserRatingForAllYears.create_image(0, 0, image=canvasUserRatingForAllYears.image,
                                                     anchor='nw')

    def tab_last(self):

        test1 = tk.Text(lab6, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test1.insert(1.0, "")
        test1.place(x=0, y=0)

        test2 = tk.Text(lab6, width=200, height=1, bg="black", fg='white', wrap=tk.WORD, state=tk.DISABLED)
        test2.insert(1.0, "")
        test2.place(x=0, y=824)


        bestRatingForAllWeeks = tk.Text(lab6, width=78, height=1, bg="black", fg='white', wrap=tk.WORD)
        bestRatingForAllWeeks.insert(1.0, "Best rating for week!")
        bestRatingForAllWeeks.configure(state=tk.DISABLED)
        bestRatingForAllWeeks.place(x=0, y=70)
        self.topRatingForAllWeeks = ttk.Treeview(lab6, columns=(
                                                         'idUser', 'name', 'surname', 'fromDate', 'untilDate',
                                                         'ratingForWeek'), height=15,
                                                 show='headings', style="mystyle.Treeview")
        self.topRatingForAllWeeks.column('idUser', width=70, anchor=tk.CENTER)
        self.topRatingForAllWeeks.column('name', width=90, anchor=tk.CENTER)
        self.topRatingForAllWeeks.column('surname', width=140, anchor=tk.CENTER)
        self.topRatingForAllWeeks.column('fromDate', width=130, anchor=tk.CENTER)
        self.topRatingForAllWeeks.column('untilDate', width=130, anchor=tk.CENTER)
        self.topRatingForAllWeeks.column('ratingForWeek', width=70, anchor=tk.CENTER)


        self.topRatingForAllWeeks.heading('idUser', text='idUser')
        self.topRatingForAllWeeks.heading('name', text='Name')
        self.topRatingForAllWeeks.heading('surname', text='Surname')
        self.topRatingForAllWeeks.heading('fromDate', text='From date')
        self.topRatingForAllWeeks.heading('untilDate', text='Until date')
        self.topRatingForAllWeeks.heading('ratingForWeek', text='Rating')

        self.topRatingForAllWeeks.place(x=0, y=90)

        selectCamera = tk.Text(lab6, width=78, height=1, bg="black", fg='white', wrap=tk.WORD)
        selectCamera.insert(1.0, "Select camera!")
        selectCamera.configure(state=tk.DISABLED)
        selectCamera.place(x=675, y=70)

        self.cameraWorkspaceImage = tk.PhotoImage(file='icons/128x128/videoCamera.png')
        btn_camera_workplace = tk.Button(lab6, text='Camera in Workplace', command=self.tab_last_open_camera_workplace,
                                         compound=tk.BOTTOM, image=self.cameraWorkspaceImage)
        btn_camera_workplace.place(x=820, y=98)
        self.cameraGymImage = tk.PhotoImage(file='icons/128x128/videoCamera.png')
        btn_camera_gym = tk.Button(lab6, text='Camera in Gym', command=self.tab_last_open_camera_gym,
                                   compound=tk.BOTTOM, image=self.cameraGymImage)
        btn_camera_gym.place(x=1020, y=98)
        self.cameraKitchenImage = tk.PhotoImage(file='icons/128x128/videoCamera.png')
        btn_camera_kitchen = tk.Button(lab6, text='Camera in Kitchen', command=self.tab_last_open_camera_kitchen,
                                       compound=tk.BOTTOM, image=self.cameraKitchenImage)
        btn_camera_kitchen.place(x=1020, y=278)

        selectSystemOperation= tk.Text(lab6, width=78, height=1, bg="black", fg='white', wrap=tk.WORD)
        selectSystemOperation.insert(1.0, "Select an operation in the system!")
        selectSystemOperation.place(x=0, y=460)

        self.registrationUser = tk.PhotoImage(file='icons/128x128/regUser.png')
        btn_registration_user = tk.Button(lab6, text='Register a new user', command=self.tab_last_open_registration_dialog,
                                          compound=tk.BOTTOM, image=self.registrationUser)
        btn_registration_user.place(x=10, y=490)
        self.trainRecognizer = tk.PhotoImage(file='icons/128x128/recognize.png')
        btn_train_recognizer = tk.Button(lab6, text='Train recognizer', command=self.tab_last_open_train_recognizer,
                                         compound=tk.BOTTOM, image=self.trainRecognizer)
        btn_train_recognizer.place(x=180, y=490)

        bestRatingForAllMonth = tk.Text(lab6, width=78, height=1, bg="black", fg='white', wrap=tk.WORD)
        bestRatingForAllMonth.insert(1.0, "Best rating for months!")
        bestRatingForAllMonth.configure(state=tk.DISABLED)
        bestRatingForAllMonth.place(x=675, y=460)


        self.topRatingForAllMonths = ttk.Treeview(lab6, columns=(
                                                         'idUser', 'name', 'surname', 'fromDate', 'untilDate',
                                                         'ratingForMonth'), height=15,
                                                 show='headings', style="mystyle.Treeview")
        self.topRatingForAllMonths.column('idUser', width=70, anchor=tk.CENTER)
        self.topRatingForAllMonths.column('name', width=90, anchor=tk.CENTER)
        self.topRatingForAllMonths.column('surname', width=130, anchor=tk.CENTER)
        self.topRatingForAllMonths.column('fromDate', width=130, anchor=tk.CENTER)
        self.topRatingForAllMonths.column('untilDate', width=130, anchor=tk.CENTER)
        self.topRatingForAllMonths.column('ratingForMonth', width=70, anchor=tk.CENTER)


        self.topRatingForAllMonths.heading('idUser', text='idUser')
        self.topRatingForAllMonths.heading('name', text='Name')
        self.topRatingForAllMonths.heading('surname', text='Surname')
        self.topRatingForAllMonths.heading('fromDate', text='From date')
        self.topRatingForAllMonths.heading('untilDate', text='Until date')
        self.topRatingForAllMonths.heading('ratingForMonth', text='Rating')

        self.topRatingForAllMonths.place(x=675, y=480)

    def tab_last_view_records(self):
        self.db.c.execute(
            "SELECT idUser, name, surname, fromDate, untilDate, ratingForWeek FROM userstimeforweek ORDER BY ratingForWeek DESC")
        [self.topRatingForAllWeeks.delete(i) for i in self.topRatingForAllWeeks.get_children()]
        [self.topRatingForAllWeeks.insert('', 'end', values=row) for row in self.db.c.fetchall()]

        self.db.c.execute(
            "SELECT idUser, name, surname, fromDate, untilDate, ratingForMonth FROM userstimeformonth ORDER BY ratingForMonth DESC")
        [self.topRatingForAllMonths.delete(i) for i in self.topRatingForAllMonths.get_children()]
        [self.topRatingForAllMonths.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def tab_last_open_camera_workplace(self):
        CameraWorkplace.Child(db)

    def tab_last_open_camera_gym(self):
        CameraGym.Child(db)

    def tab_last_open_camera_kitchen(self):
        CameraKitchen.Child(db)

    def tab_last_open_train_recognizer(self):
        TrainRecognizer.init_child()

    def tab_last_open_registration_dialog(self):
        RegistrationUserWindow.Child(window, app)

    def tab_last_registration_user(self, name, surname, address, email, groupNumber, country):
        VariablesHelper.name = name
        VariablesHelper.surname = surname
        VariablesHelper.address = address
        VariablesHelper.email = email
        VariablesHelper.groupNumber = groupNumber
        VariablesHelper.country = country
        RegistrationUser.Child(db)
        self.tab_first_view_records()

# Window
if __name__ == "__main__":
    window = tk.Tk()

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 11,'bold' ))  # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

    style.configure('TButton', font=('calibri', 9), borderwidth='4')

    tabWindow = ttk.Notebook(window)

    lab1 = ttk.Frame(tabWindow)
    lab2 = ttk.Frame(tabWindow)
    lab3 = ttk.Frame(tabWindow)
    lab4 = ttk.Frame(tabWindow)
    lab5 = ttk.Frame(tabWindow)
    lab6 = ttk.Frame(tabWindow)
    tabWindow.add(lab1, text='User ')
    tabWindow.add(lab2, tex='Rating for day')
    tabWindow.add(lab3, tex='Rating for week')
    tabWindow.add(lab4, tex='Rating for month')
    tabWindow.add(lab5, tex='Rating for year')
    tabWindow.add(lab6, text='Admin panel')
    tabWindow.pack(side=tk.TOP, expand=1, fill='both')

    canvasUserAvatar = tkinter.Canvas(lab1, width=200, height=200)
    canvasUserAvatar.place(x=0, y=19)
    imageUserAvatar = Image.open('dataset/User.' + str(VariablesHelper.userId) + '.2.jpg')

    #Tab fist
    canvasUserRatingForLastWeekCircle = tkinter.Canvas(lab1, width=352, height=264)
    canvasUserRatingForLastWeekCircle.place(x=410, y=10)

    canvasUserRatingForLastMonthCircle = tkinter.Canvas(lab1, width=352, height=264)
    canvasUserRatingForLastMonthCircle.place(x=725, y=10)

    canvasUserRatingForLastYearCircle = tkinter.Canvas(lab1, width=352, height=264)
    canvasUserRatingForLastYearCircle.place(x=1025, y=10)

    #Tab second
    canvasUserRatingForLastWeek = tkinter.Canvas(lab2, width=576, height=432)
    canvasUserRatingForLastWeek.place(x=160, y=370)


    #Tab third
    canvasUserRatingForLastMonth = tkinter.Canvas(lab3, width=576, height=432)
    canvasUserRatingForLastMonth.place(x=555, y=370)

    #Tab fourth
    canvasUserRatingForLastYear = tkinter.Canvas(lab4, width=576, height=432)
    canvasUserRatingForLastYear.place(x=160, y=370)

    #Tab fifth
    canvasUserRatingForAllYears = tkinter.Canvas(lab5, width=576, height=432)
    canvasUserRatingForAllYears.place(x=555, y=370)

    mainmenu = tk.Menu(window)
    window.config(menu=mainmenu)

    db = DataBase.dataBase()

    app = Main(window)
    app.pack()
    ConfigurationWindow.confWindow.set_info(window)
    window.mainloop()


