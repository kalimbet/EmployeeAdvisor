import tkinter as tk
from tkinter import ttk

class Child(tk.Toplevel):
    def __init__(self, window, app):
        super().__init__(window)
        self.init_child()
        self.view = app

    # Initialization Child window
    def init_child(self):
        self.title('Update week data')
        self.geometry('400x400+400+300')
        self.resizable(False, False)

        # Start child inteface

        label_from_date = tk.Label(self, text='From date (Year-Mouth-Day) ')
        label_from_date.place(x=50, y=50)

        label_until_date = tk.Label(self, text='Until date (Year-Mouth-Day) ')
        label_until_date.place(x=50, y=80)

        label_timeSecondsRest = tk.Label(self, text='Time on rest ')
        label_timeSecondsRest.place(x=50, y=110)

        label_timeSecondsWork = tk.Label(self, text='Time on work ')
        label_timeSecondsWork.place(x=50, y=140)

        label_ratingForWeek = tk.Label(self, text='Rating for week ')
        label_ratingForWeek.place(x=50, y=170)


        self.entry_from_date = ttk.Entry(self)
        self.entry_from_date.place(x=200, y=50)


        self.entry_until_date = ttk.Entry(self)
        self.entry_until_date.place(x=200, y=80)


        self.entry_time_seconds_rest = ttk.Entry(self)
        self.entry_time_seconds_rest.place(x=200, y=110)

        self.entry_time_seconds_work = ttk.Entry(self)
        self.entry_time_seconds_work.place(x=200, y=140)

        self.entry_rating_for_week = ttk.Entry(self)
        self.entry_rating_for_week.place(x=200, y=170)

        btn_cancel = ttk.Button(self, text = 'Close', command = self.destroy)
        btn_cancel.place(x = 300, y = 340)

        self.btn_ok = ttk.Button(self, text = "Update")
        self.btn_ok.place(x = 220, y = 340)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.tab_third_update_record(self.entry_from_date.get(),
                                                                                      self.entry_until_date.get(),
                                                                                      self.entry_time_seconds_rest.get(),
                                                                                      self.entry_time_seconds_work.get(),
                                                                                      self.entry_rating_for_week.get()))



        # End chold interface
        self.grab_set()     # Catch actions
        self.focus_set()
