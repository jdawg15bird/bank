
import random

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self):
        try:
            amount = float(input("How much would you like to deposit?\n"))

            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount:.2f}")
            else:
                print("Please enter an amount greater than zero.")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    def withdraw(self):
        try:
            amount = float(input("How much would you like to withdraw?\n"))

            if amount <= 0:
                print("Please enter an amount greater than zero.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    def view_account_info(self):
        print(f"Name: {self.name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
