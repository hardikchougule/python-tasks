class BankAccount:
    def __init__(self):
        self.balance = 0  

    def deposit(self, amount):
        if amount > 0:  
            self.balance += amount
            return f"Deposited: {amount}, Balance: {self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance: 
            self.balance -= amount
            return f"Withdrew: {amount}, Balance: {self.balance}"
        return "Invalid amount or insufficient balance."

    def get_balance(self):
        return f"Current Balance: {self.balance}"


def main():
    account = BankAccount()
    print("Welcome to the Bank Account System")
    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter deposit amount: "))
                print(account.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 2:
            try:
                amount = float(input("Enter withdrawal amount: "))
                print(account.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 3:
            print(account.get_balance())
        elif choice == 4:
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
