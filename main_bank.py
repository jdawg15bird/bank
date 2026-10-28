
from bank_account import BankAccount

def main():
    print("Welcome to the Bank of Spencer!")

    name = input("Please enter your name:\n")
    account = BankAccount(name)

    while True:
        print("\nPlease choose an option:")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. View account information")
        print("4. Quit")

        choice = input()

        if choice == "1":
            account.deposit()

        elif choice == "2":
            account.withdraw()

        elif choice == "3":
            account.view_account_info()

        elif choice == "4":
            print("Thank you for your business!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
