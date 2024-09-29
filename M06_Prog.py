from dateutil import parser
import datetime
file_path = 'today.txt'
with open(file_path, 'r') as file:
    today_string = file.read().strip()
today_date = parser.parse(today_string)
print(f"Date string: {today_string}")
print(f"Parsed date: {today_date}")