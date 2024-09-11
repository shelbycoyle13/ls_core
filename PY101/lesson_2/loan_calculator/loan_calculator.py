# m = p * (j / (1 - (1 + j) ** (-n)))

# m = monthly payment           #monthly_payment
# p = loan amount               #loan_amount
# j = monthly interest rate     #monthly_interest_rate
# n = loan duration in months   #loan_duration_months

#monthly_interest_rate = apr / 12
#loan_duration_months = loan_duration_years * 12
#apr = input()
#loan_duration_years = input()

"""Loan calculator that calculates the dollar amount 
for the monthly payments"""

import os
import math
import json

LANGUAGE = "en"

with open('loan_calc_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def messages(message, lang="en"):
    return MESSAGES[lang][message]

def prompt(key, **kwargs):
    message = messages(key, LANGUAGE)

    if kwargs:
        message = message.format(**kwargs)

    print(f"==> {message}")

def invalid_number(number_string):
    try:
        num = float(number_string)
        if math.isnan(num) or math.isinf(num):
            return True
        return num < 0
    except ValueError:
        return True

def invalid_amount_time(number_string):
    try:
        num = float(number_string)
        if math.isnan(num) or math.isinf(num):
            return True
        return float(number_string) == 0
    except ValueError:
        return True

#Welcome the user

prompt("welcome")

#Clear the screen and Ask the user how much is your loan?
while True:
    clean_screen()
    prompt("ask_loan_amount")
    loan_amount = input()

#Validate user input for loan
    while invalid_number(loan_amount):
        prompt("invalid_number")
        loan_amount = input()

    while invalid_amount_time(loan_amount):
        prompt("no_zeros")
        loan_amount = input()

#Ask the user what is the annual percentage rate (in this format: 2.5 or 5)?
    prompt("ask_apr")
    apr = input()

#Validate user input for apr
    while invalid_number(apr):
        prompt("invalid_number")
        apr = input()

#Ask the user how long does your loan last in years and months (whole numbers only, enter year first)
    prompt("ask_year")
    loan_duration_years = input()

#Validate user input for years
    while invalid_number(loan_duration_years):
        prompt("invalid_number")
        loan_duration_years = input()

    while invalid_amount_time(loan_duration_years):
        prompt("no_zeros")
        loan_duration_years = input()

#Ask how many months?
    prompt("ask_months")
    loan_duration_months = input()

#Validate user input for months
    while invalid_number(loan_duration_months):
        prompt("invalid_number")
        loan_duration_months = input()

#Coerce our input to floats
    loan_amount = float(loan_amount)
    apr = float(apr)
    loan_duration_years = int(loan_duration_years)
    loan_duration_months = int(loan_duration_months)

#Output the values of the variables we have so far
    prompt(
        "state_numbers", loan_amount=loan_amount, apr=apr, 
        loan_duration_years=loan_duration_years, loan_duration_months=loan_duration_months)

#Make the calculation and output the result
    loan_duration_months_total = (loan_duration_years * 12) + loan_duration_months

    try:
        if apr == 0:
            prompt("no_interest")
            monthly_payment = loan_amount / loan_duration_months_total
        else:
            monthly_interest_rate = (apr / 100) / 12
            monthly_payment = loan_amount * (
                monthly_interest_rate / (1 - (1 + monthly_interest_rate) **
                 (-loan_duration_months_total))
                )
    except ZeroDivisionError:
        print("calc_error")
    else:
        prompt("result", monthly_payment=monthly_payment)

#Ask the user if they want to calculate again
    prompt("another_calculation")
    preference = input()

#Validate the user preference
    while preference not in ["Y", "y", "N", "n"]:
        prompt("preference_choice")
        preference = input()

#If they want to end the program
    if preference in ["N", "n"]:
        prompt("end_of_program")
        break