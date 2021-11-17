import pandas
import datetime as dt
import os
import random
import smtplib

# EDIT THESE
LETTERS_DIR = "C:/Absolute/Path/to/birthday-wisher-app/letter_templates"
MY_EMAIL = 'youremailg@gmail.com'
MY_PASSWORD = '123456' 
MY_SMTP = 'smtp.mail.yahoo.com'
# STOP EDIT

today = dt.datetime.now()
today_month = today.month
today_day = today.day

birthdays_df = pandas.read_csv('birthdays.csv')
birthdays_dict = birthdays_df.to_dict('records')

geburtstagskinder = []
geburtstagskind_email = ''
birthday_today = False


def find_out_if_anyone_has_birthday_today():

    for entry in birthdays_dict:

        if entry['month'] == today_month and entry['day'] == today_day:
            geburtstagskinder.append(entry['name'])
            global birthday_today
            global geburtstagskind_email
            geburtstagskind_email = entry['email']
            birthday_today = True
    


find_out_if_anyone_has_birthday_today()


if birthday_today:
    random_letter = random.choice(os.listdir(LETTERS_DIR))
    print(random_letter)
    with open(f'letter_templates/{random_letter}', 'r') as file:
        print(file)
        letter = file.read()
        print(letter)
        custom_letter = letter.replace('[NAME]', geburtstagskinder[0])
        print(custom_letter)

    connection = smtplib.SMTP(MY_SMTP)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=geburtstagskind_email,
        msg=f"Subject:Happy Birthday {geburtstagskinder[0]}!\n\n{custom_letter}")
    connection.close()
