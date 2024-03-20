import datetime as dt; import smtplib, random; import confidential

my_email = confidential.MY_EMAIL
to_email = confidential.YAHOO_TEST_EMAIL
msg = 'Hello'

app_password = confidential.APP_PASSWORD

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
