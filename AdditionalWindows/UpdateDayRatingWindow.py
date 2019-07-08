import tkinter as tk
from tkinter import ttk

class Child(tk.Toplevel):
    def __init__(self, window, app):
        super().__init__(window)
        self.init_child()
        self.view = app

    # Initialization Child window
    def init_child(self):
        self.title('Update day data')
        self.geometry('400x400+400+300')
        self.resizable(False, False)

        # Start child inteface


        label_date = tk.Label(self, text='Date (Year-Mouth-Day) ')
        label_date.place(x=50, y=20)

        label_timeSecondsRest = tk.Label(self, text='Time on rest ')
        label_timeSecondsRest.place(x=50, y=50)

        label_timeSecondsWork = tk.Label(self, text='Time on work ')
        label_timeSecondsWork.place(x=50, y=80)

        label_ratingForDay = tk.Label(self, text='Rating for day ')
        label_ratingForDay.place(x=50, y=110)



        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=200, y=20)

        self.entry_timeSecondsRest = ttk.Entry(self)
        self.entry_timeSecondsRest.place(x=200, y=50)

        self.entry_timeSecondsWork = ttk.Entry(self)
        self.entry_timeSecondsWork.place(x=200, y=80)

        self.entry_ratingForDay = ttk.Entry(self)
        self.entry_ratingForDay.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text = 'Close', command = self.destroy)
        btn_cancel.place(x = 300, y = 340)

        self.btn_ok = ttk.Button(self, text = "Update")
        self.btn_ok.place(x = 220, y = 340)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.tab_second_update_record(self.entry_date.get(),
                                                                                          self.entry_timeSecondsRest.get(),
                                                                                          self.entry_timeSecondsWork.get(),
                                                                                          self.entry_ratingForDay.get()))




        # End chold interface
        self.grab_set()     # Catch actions
        self.focus_set()
