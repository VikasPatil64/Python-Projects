class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
        self.transactions = []  # List to store the transactions
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance is ${self.balance}")
            self.transactions.append({"type": "deposit", "amount": amount})
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance is ${self.balance}")
            self.transactions.append({"type": "withdrawal", "amount": amount})
        else:
            print("Invalid withdrawal amount. Please enter a positive number less than or equal to your current balance")
            
    def get_balance(self):
        print("Current Balance :", self.balance)   
        
    def get_transactions(self):
        print("Transaction History")
        if not self.transactions:
            print("No transactions made")
        for transaction in self.transactions:
            print(transaction)
                
def main():
    initial_bal = float(input("Enter the initial balance :"))
    acc = BankAccount(initial_bal)
    while True:
        print("\n Choose an Option : ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")                    
        
        ch = int(input("Enter Your Choice :"))
        if ch == 1:
            amount = float(input("Enter the amount to deposit:"))
            acc.deposit(amount)
        elif ch == 2:
            amount=float(input("Enter the amount to withdraw:"))
            acc.withdraw(amount)
            
        elif ch == 3:
            acc.get_balance()
        
        elif ch == 4:
            acc.get_transactions()

        elif ch == 5:
            print("Exiting the bank account manager")
            break
        else:
            print("Invalid choice. Please choose a valid option")
            
if __name__ == "__main__":
    main()
            