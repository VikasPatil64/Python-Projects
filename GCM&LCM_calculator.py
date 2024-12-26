# GCM AND LCM CALCULATOR

import math
def calculate_gcd(num1, num2):
    return math.gcd(num1, num2)

def calculate_lcm(num1, num2):
    return abs(num1*num2) // math.gcd(num1, num2)

def main():
    print("GCM AND LCM CALCULATOR")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        gcd = calculate_gcd(num1, num2)
        lcm = calculate_lcm(num1, num2)
         
        print("The GCD is: ", gcd)
        print("The LCM is: ", lcm)
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
if __name__ == "__main__":
    main()
    