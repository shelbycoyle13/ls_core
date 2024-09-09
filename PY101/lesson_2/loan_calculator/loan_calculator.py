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

import json

LANGUAGE = "en"

with open('loan_calc_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def messages(message, lang="en"):
    return MESSAGES[lang][message]

def prompt(key, **kwargs):
    message = messages(key, LANGUAGE)

    if kwargs:
        message = message.format(**kwargs)

    print(f"==> {message}")

def invalid_number(number_string):
    try:
        return float(number_string) < 0
    except ValueError:
        return True

#Welcome the user
prompt("welcome")

#Ask the user how much is your loan?
while True:
    prompt("ask_loan_amount")
    loan_amount = input()

#Validate user input
    while invalid_number(loan_amount):
        prompt("invalid_number")
        loan_amount = input()

#Ask the user what is the annual percentage rate (in this format: 2.5 or 5)?
    prompt("ask_apr")
    apr = input()

#Validate user input
    while invalid_number(apr):
        prompt("invalid_number")
        apr = input()

#Ask the user how long does your loan last in years (in this format: 1 or 2.5)?
    prompt("ask_time")
    loan_duration_years = input()

#Validate user input
    while invalid_number(loan_duration_years):
        prompt("invalid_number")
        loan_duration_years = input()

#Coerce our input to floats
    loan_amount = float(loan_amount)
    apr = float(apr)
    loan_duration_years = float(loan_duration_years)

#Output the values of the variables we have so far
    prompt(
        "state_numbers", loan_amount=loan_amount, apr=apr, 
        loan_duration_years=loan_duration_years)

#Make the calculation and output the result
    loan_duration_months = loan_duration_years * 12

    try:
        if apr == 0:
            prompt("no_interest")
            monthly_payment = loan_amount / loan_duration_months
        else:
            monthly_interest_rate = (apr / 100) / 12
            monthly_payment = loan_amount * (
                monthly_interest_rate / (1 - (1 + monthly_interest_rate) **
                 (-loan_duration_months))
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