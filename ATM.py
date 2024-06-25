#MY ATM Machine 

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Successful. New balance: Rs{self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal Successful. New balance: Rs{self.balance:.2f}")

    def check_balance(self):
        print(f"Account balance: Rs{self.balance:.2f}")


def main():
    account = Account("3549939392", "1215", 1000)

    while True:
        print("Welcome to MY ATM Machine")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            pin = input("Enter your PIN: ")
            if account.check_pin(pin):
                account.withdraw(amount)
            else:
                print("Invalid PIN")
        elif choice == "3":
            pin = input("Enter your PIN: ")
            if account.check_pin(pin):
                account.check_balance()
            else:
                print("Invalid PIN")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()