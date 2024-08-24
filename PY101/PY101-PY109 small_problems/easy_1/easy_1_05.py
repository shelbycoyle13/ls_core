# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

bill_amount = float(input("What is the bill amount? "))
tip_percentage = float(input("What is the tip percentage? "))

def calculate_tip_and_bill(bill_amount, tip_percentage):
    tip_decimal = tip_percentage / 100
    tip_amount = bill_amount * tip_decimal
    total_bill = bill_amount + tip_amount

    print(f"The tip is {tip_amount:.2f}")
    print(f"The total is {total_bill:.2f}")

calculate_tip_and_bill(bill_amount, tip_percentage)
