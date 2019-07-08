import tkinter as tk
from tkinter import ttk

class Child(tk.Toplevel):
    def __init__(self, window, app):
        super().__init__(window)
        self.init_child()
        self.view = app

    # Initialization Child window
    def init_child(self):
        self.title('Select status of task')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        # Start child inteface
        label_taskStatus = tk.Label(self, text='Has the employee completed the assigned task? ')
        label_taskStatus.place(x=20, y=40)

        label_taskStatus_test = tk.Label(self, text='1 = yes     0 = no ')
        label_taskStatus_test.place(x=20, y=70)

        self.entry_taskStatus = ttk.Entry(self)
        self.entry_taskStatus.place(x=20, y=100)


        btn_cancel = ttk.Button(self, text = 'Close', command = self.destroy)
        btn_cancel.place(x = 100, y = 140)

        self.btn_ok = ttk.Button(self, text = "Ok")
        self.btn_ok.place(x = 20, y = 140)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.tab_first_calculate_rating_for_day(self.entry_taskStatus.get()))




        # End chold interface
        self.grab_set()     # Catch actions
        self.focus_set()
