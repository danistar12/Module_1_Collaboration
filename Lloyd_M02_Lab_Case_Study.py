# Danielle Lloyd
# Module 02 Lab Case Study If Else 
# 8/27/2024
# This App will gather information about a student and 
# decide if they are on the Dean's list or the honor roll
import string
while True:
    last_name=input("Please enter your last name or ZZZ to quit: ")
    last_name=last_name.upper()         # onverts entry to all caps

    if last_name=='ZZZ':
        break                           # break out statement

    first_name=input(f"\nWhat is your first name? ")

    gPa=float(input(f"\nHello {first_name}, what is your current gpa? "))

    if gPa >= 3.5:
        print(f"\nCongratulations {first_name}!! You've made the Dean's List\n")
    elif gPa < 3.5 and gPa >= 3.25:
        print(f"\nGreat Job {first_name}! You've made Honor Roll!\n")
    else:
        print(f"\nKeep working at it {first_name}! You're on the right track\n")