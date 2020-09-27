#!/usr/bin/env python

import yagmail 
import pandas as pd
from datetime import date
from datetime import time
from datetime import datetime
import numpy as np


#Just to Make it Fancy. :)
Wishes=['On this day, may your most cherished desires come true; i wish you success in life. Happy birthday!',
        'We prayed to God to give us a special gift. He gave us you.  Dear you are a dream come true. Happy birthday!',
        'You are my happiness. Your memories bring a smile to my face.  Have a wonderful day',
        'Dear Friend, as you move into another year of your life, may the blessings and success follow you always. Happy birthday!',
        'You are a very special person to me. Hope the New Year will not change, but have more memorable moments with you. Happy birthday!',
        'Happy birthday my Love. This is my prayer for you on this special day. May accomplish what you wish and earnestly seek.',
        ' I am blessed to have a friend like you, Loving thoughts and warm wishes on your birthday. Happy birthday!']

#Fetching Data
data=pd.read_csv("Birthdays.csv")
data["Birthdate"]=pd.to_datetime(data["Birthdate"])

#Email Sending
def email_send(content,emails):
    try:
        yag=yagmail.SMTP('UrEmailid','UrPassword')#Insert Your Email Id and Passowrd here.
        yag.send(emails,"happy Birthday duh",content)
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
                print(name)
                contents=("Happy Birthday {},".format(name),'\n',Wishes[np.random.randint(0,6)],yagmail.inline("Images\B.jpg"))
                email_send(contents,email)
                
        f+=1  

if __main__==__name__:
    ch_birth()
