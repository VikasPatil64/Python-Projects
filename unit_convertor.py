# UNIT CONVERTOR - LENGTH, WEIGHT, TEMPERATURE, 
def convert_length():
    print("\nLength Conversion:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Feet to Meters")
    print("4. Meters to Feet")

    choice = int(input("Choose an option (1-4): "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        result = value / 1000
        print(f"{value} meters = {result:.4f} kilometers")
    elif choice == 2:
        result = value * 1000
        print(f"{value} kilometers = {result:.4f} meters")
    elif choice == 3:
        result = value * 0.3048
        print(f"{value} feet = {result:.4f} meters")
    elif choice == 4:
        result = value / 0.3048
        print(f"{value} meters = {result:.4f} feet")
    else:
        print("Invalid choice. Please try again.")

def convert_weight():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")

    choice = int(input("Choose an option (1-4): "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        result = value * 2.20462
        print(f"{value} kilograms = {result:.4f} pounds")
    elif choice == 2:
        result = value / 2.20462
        print(f"{value} pounds = {result:.4f} kilograms")
    elif choice == 3:
        result = value / 1000
        print(f"{value} grams = {result:.4f} kilograms")
    elif choice == 4:
        result = value * 1000
        print(f"{value} kilograms = {result:.4f} grams")
    else:
        print("Invalid choice. Please try again.")

def convert_temperature():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Choose an option (1-4): "))
    value = float(input("Enter the temperature to convert: "))

    if choice == 1:
        result = (value * 9/5) + 32
        print(f"{value} °C = {result:.4f} °F")
    elif choice == 2:
        result = (value - 32) * 5/9
        print(f"{value} °F = {result:.4f} °C")
    elif choice == 3:
        result = value + 273.15
        print(f"{value} °C = {result:.4f} K")
    elif choice == 4:
        result = value - 273.15
        print(f"{value} K = {result:.4f} °C")
    else:
        print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Unit Converter!")
    while True:
        print("\nMain Menu:")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Exit")

        choice = int(input("Choose a category (1-4): "))
        if choice == 1:
            convert_length()
        elif choice == 2:
            convert_weight()
        elif choice == 3:
            convert_temperature()
        elif choice == 4:
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
