import cv2
import os
import datetime
import tkinter as tk

class Child(tk.Toplevel):
    def __init__(self, db):
        self.init_child()
        self.db = db
        self.start_camera()

    def init_child(self):
        print(1)

    def start_camera(self):
        # Start child inteface

        fname = "recognizer/trainingData.yml"
        if not os.path.isfile(fname):
            print("Please train the data first")
            exit(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(fname)

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                ids, conf = recognizer.predict(gray[y:y + h, x:x + w])
                self.db.c.execute("SELECT name FROM users WHERE id = (%s);", (ids,))
                resultName = self.db.c.fetchall()
                name = resultName[0][0]
                self.db.c.execute("SELECT surname FROM users WHERE id = (%s);", (ids,))
                resultSurname = self.db.c.fetchall()
                surname = resultSurname[0][0]
                nowDate = datetime.datetime.now()
                nowTime = datetime.datetime.now()
                weekDay = datetime.datetime.now().weekday()
                key = cv2.waitKey(10)
                if key in [27, 1048603]:  # ESC key to abort, close window
                    cv2.destroyAllWindows()
                    break
                if conf < 50:
                    cv2.putText(img, name, (x + 2, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 255, 0), 2)
                    cv2.putText(img, surname, (x + 2, y + h + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 255, 0), 2)
                    self.db.c.execute(
                        'INSERT INTO userstime (idUser, numberRoom, name, surname, date, time, weekDay) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (ids, 1, name, surname, nowDate, nowTime, weekDay))
                    self.db.connection.commit()
                else:
                    cv2.putText(img, 'No Match', (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognizer', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()






