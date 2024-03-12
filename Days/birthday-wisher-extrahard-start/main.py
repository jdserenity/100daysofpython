import datetime as dt
from random import choice
import pandas
import smtplib
LETTER_PATHS = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']
my_email = 'jdangelorg@gmail.com'
password = 'uIrb2NO7q#jjvY1SvSumVjzObQpEPv&3pb6FhDlAswiVY&Y9S$wgHj*w*dJZt&KrtM7%9%1z*yuKPmP7Oe$3PtfFrMdbJJUpXLW'
app_password = 'fgky kaxl sdjh ahsj'

##################### Extra Hard Starting Project ###################### # noqa E266

now = dt.datetime.now()
current_date = now.day
current_month = now.month

# 1. Update the birthdays.csv ✅

birthdays_dict = pandas.read_csv('./birthdays.csv').to_dict()

# print(birthdays_dict)

# 2. Check if today matches a birthday in the birthdays.csv

birthday_months = birthdays_dict['month']
birthday_dates = birthdays_dict['day']

possible_birthdays = []

# If the current month is one of the birth months, add that person to the list,
# then if the birthday of that person is not the current day, subsequently remove them from the list
# the only people left will be people whose birthday is today
for key, value in birthday_months.items():
    if value == current_month:
        possible_birthdays.append(key)

for key, value in birthday_dates.items():
    if value != current_date:
        if key in possible_birthdays:
            possible_birthdays.remove(key)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

names = birthdays_dict['name']
emails = birthdays_dict['email']

for person in possible_birthdays:
    with open(choice(LETTER_PATHS)) as letter:
        letter_output = letter.read()
        new_letter_output = letter_output.replace('[NAME]', names[person])
        # print(new_letter_output)

    # 4. Send the letter generated in step 3 to that person's email address.

    to_email = emails[person]

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Happy Birthday!!!!\n\n{new_letter_output}")
