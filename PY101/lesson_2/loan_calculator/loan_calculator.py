# m = p * (j / (1 - (1 + j) ** (-n)))

# m = monthly payment           #monthly_payment
# p = loan amount               #loan_amount
# j = monthly interest rate     #monthly_interest_rate
# n = loan duration in months   #loan_duration_months

#monthly_interest_rate = apr / 12
#loan_duration_months = loan_duration_years * 12
#apr = input()
#loan_duration_years = input()

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_string):
    try:
        return float(number_string) < 0
    except ValueError:
        return True

#Welcome the user
prompt("Welcome to my loan calculator!")

#Ask the user how much is your loan?
while True:
    prompt("How much is your loan? Please use this format: 100000")
    loan_amount = input()

#Validate user input
    while invalid_number(loan_amount):
        prompt("You didn't enter a valid input type. Please try again!")
        loan_amount = input()

#Ask the user what is the annual percentage rate (in this format: 2.5 or 5)?
    prompt("""What is your annual percentage rate?
           Please use this format: 2.5 for 2.5% or 5 for 5%""")
    apr = input()

#Validate user input
    while invalid_number(apr):
        prompt("You didn't enter a valid input type. Please try again!")
        apr = input()

#Ask the user how long does your loan last in years (in this format: 1 or 2.5)?
    prompt("""How long does your loan last in years?
           Please use this format: 2.5 or 5""")
    loan_duration_years = input()

#Validate user input
    while invalid_number(loan_duration_years):
        prompt("You didn't enter a valid input type. Please try again!")
        loan_duration_years = input()

#Coerce our input to floats
    loan_amount = float(loan_amount)
    apr = float(apr)
    loan_duration_years = float(loan_duration_years)

#Output the values of the variables we have so far
    prompt(f"""Okay, so we have a loan in the amount of ${loan_amount:,.2f}
        with an APR of {apr}% and it lasts for {loan_duration_years} years. 
        Let me make my calculations.""")

#Make the calculation and output the result
    loan_duration_months = loan_duration_years * 12

    try:
        if apr == 0:
            prompt("""Oh, I see there is no interest - Nice!
                   Let me adjust for that.""")
            monthly_payment = loan_amount / loan_duration_months
        else:
            monthly_interest_rate = (apr / 100) / 12
            monthly_payment = loan_amount * (
                monthly_interest_rate / (1 - (1 + monthly_interest_rate) **
                 (-loan_duration_months))
                )
    except ZeroDivisionError:
        print("There was an error in the calculation.")
    else:
        prompt(f"""Okay, your monthly payment will be
               ${monthly_payment:,.2f} per month.""")

#Ask the user if they want to calculate again
    prompt("""Would you like to calculate another monthly payment?
           Type Y for Yes and N for No:""")
    preference = input()

#Validate the user preference
    while preference not in ["Y", "y", "N", "n"]:
        prompt("""You didn't select either of the correct options.
               Please try again!""")
        preference = input()

#If they want to end the program
    if preference in ["N", "n"]:
        prompt("Thanks for using my loan calculator!")
        break