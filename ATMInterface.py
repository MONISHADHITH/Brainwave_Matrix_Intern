import datetime


class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append({
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "Withdrawal",
                "amount": amount
            })
            print(f"Withdrawal successful. Your new balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "Deposit",
            "amount": amount
        })
        print(f"Deposit successful. Your new balance is: ${self.balance}")

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction['date']} - {transaction['type']}: ${transaction['amount']}")


class ATM:
    def __init__(self):
        self.accounts = {
            "12345": Account("12345", "1234", 100000),
            "67890": Account("67890", "5678", 500000),
            "34567": Account("34567", "9012", 200000)
        }
        self.current_account = None

    def login(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            self.current_account = self.accounts[account_number]
            print("Login successful!")
        else:
            print("Invalid account number or PIN.")

    def main_menu(self):
        while True:
            print("\nATM Main Menu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transaction History")
            print("5. Logout")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if self.current_account:
                if choice == "1":
                    self.current_account.check_balance()
                elif choice == "2":
                    try:
                        amount = float(input("Enter amount to withdraw: $"))
                        self.current_account.withdraw(amount)
                    except ValueError:
                        print("Invalid amount. Please try again.")
                elif choice == "3":
                    try:
                        amount = float(input("Enter amount to deposit: $"))
                        self.current_account.deposit(amount)
                    except ValueError:
                        print("Invalid amount. Please try again.")
                elif choice == "4":
                    self.current_account.display_transaction_history()
                elif choice == "5":
                    self.current_account = None
                    print("You have been logged out.")
                elif choice == "6":
                    print("Thank you for using our ATM!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Please login first.")
                self.login()


def main():
    atm = ATM()
    while True:
        print("\nWelcome to our ATM!")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            atm.login()
            atm.main_menu()
        elif choice == "2":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
