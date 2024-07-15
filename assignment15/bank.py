class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs.{amount:.2f} successful.")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs.{amount:.2f} successful.")
        else:
            print("Withdrawal amount should be greater than zero and less than or equal to balance.")

    def get_balance(self):
        return self.balance


# Example usage:
if __name__ == "__main__":
    # Creating an instance of BankAccount
    acc1 = BankAccount("1234567890", "John Doe")

    # Depositing and withdrawing money
    acc1.deposit(1000)
    acc1.withdraw(500)
    
    # Getting the balance
    print(f"Current Balance: Rs.{acc1.get_balance():.2f}")
