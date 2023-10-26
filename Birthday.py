
#!/usr/bin/env python

import yagmail
import pandas as pd
from datetime import date
import random
import os

# Load sensitive data from a config file
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')  # Create a 'config.ini' file with your email and password

Wishes = ['On this day, may your most cherished desires come true; I wish you success in life. Happy birthday!',
          'May your life be filled with joy, laughter, and love. Happy birthday!',
          # Add more wishes here...
         ]

# Fetching the Data
data = pd.read_csv("Birthdays.csv")
data["Birthdate"] = pd.to_datetime(data["Birthdate"])

# Sending Emails
def email_send(name, email, content):
    try:
        yag = yagmail.SMTP(config.get('Email', 'username'), config.get('Email', 'password'))
        yag.send(email, "Happy Birthday!", content)
        print(f"Email has been sent to {name}")
    except Exception as e:
        print(f"Failed to send email to {name}: {str(e)}")

# Main Program
def send_birthday_emails():
    today = date.today()
    for _, row in data.iterrows():
        name = row['Name']
        email = row['email_id']
        birthdate = row['Birthdate']

        if birthdate.month == today.month and birthdate.day == today.day:
            random_wish = random.choice(Wishes)
            email_content = (f"Happy Birthday, {name}!\n\n{random_wish}")
            
            # Add a random image from a directory or use a default image
            image_folder = 'birthday_images'
            if os.path.exists(image_folder):
                image_files = os.listdir(image_folder)
                random_image = os.path.join(image_folder, random.choice(image_files))
                email_content += yagmail.inline(random_image)

            email_send(name, email, email_content)

if __name__ == "__main__":
    send_birthday_emails()