#!/usr/bin/env python

import yagmail 
import pandas as pd
from datetime import date
from datetime import time
from datetime import datetime
import numpy as np
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import csv
import os

HEIGHT=500
WIDTH=700
root = Tk()

#save 3 input in csv file
def get_text(entry1, entry2, entry3):
    with open("database.csv", newline='', mode="a") as database2:
        Name = entry1
        Data = entry2
        Email = entry3
        csv_writer = csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Name,Data,Email])

#open the desire csv file and send birthday greetings according to dates in opend csv
def open_csv():
    my_csv = filedialog.askopenfilename()
    os.system(my_csv)
    
    #Fetching Data
    data=pd.read_csv(my_csv)
    data["Birthdate"]=pd.to_datetime(data["Birthdate"])

    #Email Sending
    def email_send(content,emails):
        try:
            yag=yagmail.SMTP('USERNAME','PASSWORD')#Insert Your Email Id and Passowrd here.
            yag.send(emails,"Happy Birthday duh",content)
            print("Email Has been sent")
        except:
            print("Nah")  

    #Main Program
    def ch_birth():
        x=date.today()
        f=0
        for e in data["Birthdate"]:
            name=()
            if e.month==x.month:
                if e.day==x.day:
                    name=(data['Name'][f])
                    email=(data['email_id'][f])
                    contents=("Happy Birthday {},".format(name),'\n',Wishes[np.random.randint(0,6)],yagmail.inline("./Stuff/B.jpg"))
                    email_send(contents,email)
                    f+=1  

    ch_birth()


canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg="#80cbe0")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Birthday Mail", fg='red')
label.pack()

L1 = Label(frame, text = "Name")
L1.place(relx=0.17, rely=0.1)

entry1 = Entry(frame, bd=5)
entry1.place(relx=0.1, rely=0.16)

#input date format: mm-dd-yyyy
L2 = Label(frame, text = "Date")
L2.place(relx=0.45, rely=0.1)

entry2 = Entry(frame, bd=5)
entry2.place(relx=0.37, rely=0.16)

L3 = Label(frame, text = "Email")
L3.place(relx=0.70, rely=0.1)

entry3 = Entry(frame, bd=5)
entry3.place(relx=0.64, rely=0.16)

#submit 3 inputs in database.csv
submit_button = Button(frame, text='Submit', command=lambda: get_text(entry1.get(), entry2.get(), entry3.get()))
submit_button.place(relx=0.70, rely=0.30)

csv_button = Button(frame, text="Open CSV and send Email", command=open_csv)
csv_button.place(relx=0.7, rely=0.9)


#Just to Make it Fancy. :)
Wishes=['On this day, may your most cherished desires come true; i wish you success in life. Happy birthday!',
        'We prayed to God to give us a special gift. He gave us you.  Dear you are a dream come true. Happy birthday!',
        'You are my happiness. Your memories bring a smile to my face.  Have a wonderful day',
        'Dear Friend, as you move into another year of your life, may the blessings and success follow you always. Happy birthday!',
        'You are a very special person to me. Hope the New Year will not change, but have more memorable moments with you. Happy birthday!',
        'Happy birthday my Love. This is my prayer for you on this special day. May accomplish what you wish and earnestly seek.',
        ' I am blessed to have a friend like you, Loving thoughts and warm wishes on your birthday. Happy birthday!']

root.mainloop()