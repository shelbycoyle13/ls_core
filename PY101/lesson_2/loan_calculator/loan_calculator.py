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

#Clears the screen and gets valid loan amount
def get_loan_amount():
    clean_screen()
    prompt("ask_loan_amount")
    input_loan_amount = input()

    #Validate user input for loan
    while invalid_number(input_loan_amount):
        prompt("invalid_number")
        input_loan_amount = input()

    while invalid_amount_time(input_loan_amount):
        prompt("no_zeros")
        input_loan_amount = input()

    input_loan_amount = float(input_loan_amount)
    return input_loan_amount

#Asks and validates apr in _% format
def get_apr():
    prompt("ask_apr")
    input_apr = input()

    while invalid_number(input_apr):
        prompt("invalid_number")
        input_apr = input()

    input_apr = float(input_apr)
    return input_apr

#Ask and validate duration (whole numbers only)
def get_loan_duration_years():
    prompt("ask_year")
    input_loan_duration_years = input()

    while invalid_number(input_loan_duration_years):
        prompt("invalid_number")
        input_loan_duration_years = input()

    while invalid_amount_time(input_loan_duration_years):
        prompt("no_zeros")
        input_loan_duration_years = input()
    input_loan_duration_years = int(input_loan_duration_years)
    return input_loan_duration_years

def get_loan_duration_months():
    prompt("ask_months")
    input_loan_duration_months = input()

    while invalid_number(input_loan_duration_months):
        prompt("invalid_number")
        input_loan_duration_months = input()

    input_loan_duration_months = int(input_loan_duration_months)
    return input_loan_duration_months

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
        return num <= 0
    except ValueError:
        return True

def calc_monthly_payment(
        input_loan_amount, input_apr, input_loan_duration_months_total
        ):
    if input_apr == 0:
        prompt("no_interest")
        input_monthly_payment = (input_loan_amount /
                                 input_loan_duration_months_total)
    else:
        monthly_interest_rate = (input_apr / 100) / 12
        input_monthly_payment = input_loan_amount * (
                monthly_interest_rate / (1 - (1 + monthly_interest_rate) **
                 (-input_loan_duration_months_total))
                )
    return input_monthly_payment

def calculate_again():
    prompt("another_calculation")
    user_preference = input()

    while user_preference not in ["Y", "y", "N", "n"]:
        prompt("preference_choice")
        user_preference = input()
    if user_preference in ["Y", "y"]:
        return True
    return False

#Welcome the user

prompt("welcome")

while True:
    loan_amount = get_loan_amount()
    apr = get_apr()
    loan_duration_years = get_loan_duration_years()
    loan_duration_months = get_loan_duration_months()

#Output the values of the variables we have so far
    prompt(
        "state_numbers", loan_amount=loan_amount, apr=apr, 
        loan_duration_years=loan_duration_years,
        loan_duration_months=loan_duration_months
        )

#Make the calculation and output the result
    loan_duration_months_total = (
        loan_duration_years * 12) + loan_duration_months

    try:
        monthly_payment = calc_monthly_payment(
            loan_amount, apr, loan_duration_months_total)
    except ZeroDivisionError:
        print("calc_error")
    else:
        prompt("result", monthly_payment=monthly_payment)

    preference = calculate_again()

    if not preference:
        prompt("end_of_program")
        break