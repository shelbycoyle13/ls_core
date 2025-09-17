# Wallet (Part 2)
# Using the code from the previous exercise, modify the code so that when we print the merged_wallet we receive a message Wallet with $80.

# class Wallet: # original code
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Wallet(self.amount + other.amount)

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Wallet): #This is to check the second item's object type is a also Wallet instance to ensure safe addition
            return Wallet(self.amount + other.amount) #Does this calculate the inside of the () first, then create it into a new Wallet object? LS Bot: Yes, the addition is evaluated first, then passes that result to the Wallet constructor to create a new Wallet
        
        return NotImplemented
    
    def __str__(self): #This method is automatically called by the print function
        return f"Wallet with ${self.amount}." #With our print statement, this is checking merged_wallet.amount. 

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.