def calculate_simple_interest(principal, rate, time):
    """Calculate Simple Interest."""
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n=1):
    """Calculate Compound Interest."""
    amount = principal * (1 + (rate / (n * 100))) ** (n * time)
    return amount - principal

def main():
    print("INTEREST CALCULATOR")
    
    # Input the principal, rate, and time
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    
    # Calculate simple and compound interest
    simple_interest = calculate_simple_interest(principal, rate, time)
    compound_interest = calculate_compound_interest(principal, rate, time)
    
    # Display the results
    print(f"\nSimple Interest: {simple_interest:.2f}")
    print(f"Compound Interest: {compound_interest:.2f}")

if __name__ == "__main__":
    main()
