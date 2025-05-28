class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

if __name__ == "__main__":
    accounts = {}

    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Display Account Info\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                print("Account already exists.")
                continue
            holder = input("Enter account holder name: ")
            try:
                initial = float(input("Enter initial deposit (or 0): "))
                accounts[acc_num] = BankAccount(acc_num, holder, initial)
                print("Account created successfully.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = accounts.get(acc_num)
            if account:
                try:
                    amt = float(input("Enter deposit amount: "))
                    account.deposit(amt)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            account = accounts.get(acc_num)
            if account:
                try:
                    amt = float(input("Enter withdrawal amount: "))
                    account.withdraw(amt)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")
        elif choice == "4":
            acc_num = input("Enter account number: ")
            account = accounts.get(acc_num)
            if account:
                print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = accounts.get(acc_num)
            if account:
                print(account)
            else:
                print("Account not found.")
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")