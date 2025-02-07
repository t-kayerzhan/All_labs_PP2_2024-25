class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = int(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Current balance:", self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
        
        print("Current balance:", self.balance)

owner_name = input("Enter an owner name: ")
initial_balance = input("Enter an initial balance: ")

account1 = Account(owner_name, initial_balance)
command = input("Enter command deposit/withdraw: ")
if command == "deposit":
    amount = int(input("Enter the amount: "))
    account1.deposit(amount)
elif command == "withdraw":
    amount = int(input("Enter the amount: "))
    account1.withdraw(amount)
else:
    print("Incorrect request, try again.")
