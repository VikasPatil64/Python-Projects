# EXPENSE SPLITTER

def add_expense(expenses, payers):
    payer= input("Enter payer name :")
    amount = float(input("Enter amount :"))
    description = input("Enter the description :")
    
    expenses.append({
        "payer": payer,
        "amount": amount,
        "description": description
    })    
    
    if payer not in payers:
        payers[payer] = 0
        payers[payer] += amount
        
    print(f"Expense '{description}' added : {amount} by {payer}")
    
def calculate_splits(expenses, payers):
    total_amount = 