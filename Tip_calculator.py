#Tip Calculator

def calculate_tip(total_bill, tip_percentage):
    tip_amount = (tip_percentage / 100) * total_bill
    return tip_amount

def calculate_total_bill(total_bill, tip_amount):
    return total_bill + tip_amount

def main():
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
    tip_amount = calculate_tip(total_bill, tip_percentage)
    total_bill_with_tip = calculate_total_bill(total_bill, tip_amount)
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total bill with tip: ${total_bill_with_tip:.2f}")

if __name__ == "__main__":
    main()