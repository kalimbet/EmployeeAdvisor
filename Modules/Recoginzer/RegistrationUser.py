import cv2
import os
import datetime
import VariablesHelper
import tkinter as tk

class Child(tk.Toplevel):
    def __init__(self, db):
        self.init_child()
        self.db = db
        self.start_registration()

    def init_child(self):
        print(1)


    def start_registration(self):
        if not os.path.exists('./dataset'):
            os.makedirs('./dataset')
        nowDateTime = datetime.datetime.utcnow()
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        self.db.c.execute('INSERT INTO users (name, surname,address, email, groupNumber, country, dateRegistration) VALUES (%s, %s, %s, %s, %s, %s, %s)', (VariablesHelper.name, VariablesHelper.surname, VariablesHelper.address, VariablesHelper.email, VariablesHelper.groupNumber, VariablesHelper.country, nowDateTime))
        uid = self.db.c.lastrowid
        sampleNum = 0
        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                sampleNum = sampleNum + 1
                cv2.imwrite("dataset/User." + str(uid) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.waitKey(100)
            cv2.imshow('img', img)
            cv2.waitKey(1);
            if sampleNum > 40:
                break
        cap.release()
        self.db.connection.commit()
        cv2.destroyAllWindows()