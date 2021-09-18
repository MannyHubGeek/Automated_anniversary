##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
import pandas
import datetime as dt
import random
import smtplib
my_email = "eohue@winfraconsulting.co.uk"
password = "Preach123"

now = dt.datetime.now()
month = now.month
year = now.year
day = now.weekday()
today = (month, day)


# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("automated letters.csv")


anniversay_dict = {}

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:

#Dictionary comprehension template for pandas DataFrame looks like this:
anniversary_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if (today) in anniversary_dict:
    anniversary_person = anniversary_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as let3:
        newText = let3.read().replace('[NAME]', anniversary_person["name"])



    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=anniversary_person["email"],
        msg=f"Subject:Happy Anniversary\n\n{newText}")


# with open("letter_templates/letter_3.txt") as let3:
#     newText = let3.read().replace('birthday', 'Anniversary')
#
# with open("letter_templates/letter_3.txt", "w") as let3:
#     let3.write(newText)

