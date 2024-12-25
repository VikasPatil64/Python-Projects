def main():
    income = float(input("Enter your total income : "))
    expenses = {}
    while True:
        expense_name = input("Enter your expenses name (or 'done' to finish) :")
        if expense_name.lower() == 'done':
            break
        expense_amt = float(input("Enter the amount for " + expense_name +":"))
        expenses[expense_name] = expense_amt
        
    total_expenses = sum(expenses.values())
    surplus_or_deficit = income - total_expenses
    print("\n Budget Summary:")
    print("-----------------")
    print("Total Income: ", income)
    print("Total Expenses: ", total_expenses)
    print("\n Expenses Breakdown")
    for expense, amount in expenses.items():
        print(" " + expense + ": $"  + str(round(amount, 2)) )
    print("\n Surplus/Deficit: $" + str(round(surplus_or_deficit , 2 )))

if __name__ == "__main__":
    main()
        
        