import datetime as dt
import smtplib
import random

my_email = 'jdangelorg@gmail.com'
password = 'uIrb2NO7q#jjvY1SvSumVjzObQpEPv&3pb6FhDlAswiVY&Y9S$wgHj*w*dJZt&KrtM7%9%1z*yuKPmP7Oe$3PtfFrMdbJJUpXLW'
to_email = 'pythontest_michaelsmith100@yahoo.com'
msg = 'Hello'

app_password = 'fgky kaxl sdjh ahsj'

now = dt.datetime.now()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday", "Sunday"]
# print(weekdays[now.weekday()])

if weekdays[now.weekday()] == 'Thursday':
    with open('./quotes.txt') as quotes:
        lines = quotes.readlines()
        quote = random.choice(lines)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Motivational Quote!\n\n{quote}")
