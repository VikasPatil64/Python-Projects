import matplotlib.pyplot as plt

def main():
    expenses = {}
    while True:
        expense_name = input("Enter the name of the expense (or 'done' to finish): ")
        if expense_name.lower() == 'done':
            break
        try:
            expense_amount = float(input(f"Enter the amount for {expense_name}: "))
            expenses[expense_name] = expense_amount
        except ValueError:
            print("Please enter a valid number for the amount.")

    plot_expenses(expenses)

def plot_expenses(expenses):
    if not expenses:
        print("No expenses to plot.")
        return

    labels = list(expenses.keys())
    values = list(expenses.values())

    plt.figure(figsize=(8, 8))  # Set the size of the figure
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)  # Create a pie chart
    plt.title("Expense Distribution")  # Title of the chart
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.show()

if __name__ == "__main__":
    main()
