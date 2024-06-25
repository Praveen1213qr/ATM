import sys

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")
        else:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient funds. Please enter a lesser amount.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, pin, balance=0):
        account = Account(account_number, pin, balance)
        self.accounts[account_number] = account

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def start(self):
        print("Welcome to the ATM Machine") 
        
        while True:
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            account = self.authenticate(account_number, pin)
            
            if account:
                print("Authentication successful!")
                self.account_menu(account)
            else:
                print("Authentication failed. Please try again.")

    def account_menu(self, account):
        while True:
            print("\nATM Menu")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            
            choice = input("Please choose an option: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

def main():
    atm = ATM()
    # Adding some accounts for testing purposes
    atm.add_account("123456789", "1234", 1000)
    atm.add_account("987654321", "4321", 500)
    
    atm.start()

if __name__ == "__main__":
    main()
