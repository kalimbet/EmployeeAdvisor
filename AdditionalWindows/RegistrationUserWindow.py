import tkinter as tk
from tkinter import ttk

class Child(tk.Toplevel):
    def __init__(self, window, app):
        super().__init__(window)
        self.init_child()
        self.view = app

    # Initialization Child window
    def init_child(self):
        self.title('User registration')
        self.geometry('400x500+400+300')
        self.resizable(False, False)

        # Start child inteface
        label_name = tk.Label(self, text='Name: ')
        label_name.place(x=20, y=70)

        label_surname = tk.Label(self, text='Surname: ')
        label_surname.place(x=20, y=110)

        label_address = tk.Label(self, text='Address: ')
        label_address.place(x=20, y=150)

        label_email = tk.Label(self, text='Email: ')
        label_email.place(x=20, y=190)

        label_groupNumber = tk.Label(self, text='Number of group: ')
        label_groupNumber.place(x=20, y=230)

        label_country = tk.Label(self, text='Country: ')
        label_country.place(x=20, y=270)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=70)

        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=200, y=110)

        self.entry_address = ttk.Entry(self)
        self.entry_address.place(x=200, y=150)

        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=200, y=190)

        self.entry_groupNumber = ttk.Entry(self)
        self.entry_groupNumber.place(x=200, y=230)

        self.entry_country = ttk.Entry(self)
        self.entry_country.place(x=200, y=270)


        btn_cancel = ttk.Button(self, text = 'Close', command = self.destroy)
        btn_cancel.place(x = 300, y = 400)

        self.btn_ok = ttk.Button(self, text = "Enter")
        self.btn_ok.place(x = 200, y = 400)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.tab_last_registration_user(self.entry_name.get(),
                                                                                         self.entry_surname.get(),
                                                                                         self.entry_address.get(),
                                                                                         self.entry_email.get(),
                                                                                         self.entry_groupNumber.get(),
                                                                                         self.entry_country.get()))




        # End chold interface
        self.grab_set()     # Catch actions
        self.focus_set()
