# NUMBER BASE CONVERTOR

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

def decimal_to_octal(decimal_num):
    return oct(decimal_num).replace("0o", "")

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num).replace("0x", "")

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

def binary_to_octal(binary_num):
    return oct(int(binary_num, 2)).replace("0o", "")

def binary_to_hexadecimal(binary_num):
    return hex(int(binary_num, 2)).replace("0x", "")

def octal_to_decimal(octal_num):
    return int(octal_num, 8)

def octal_to_binary(octal_num):
    return bin(int(octal_num, 8)).replace("0b", "")

def octal_to_hexadecimal(octal_num):
    return hex(int(octal_num, 8)).replace("0x", "")

def hexadecimal_to_decimal(hexadecimal_num):
    return int(hexadecimal_num, 16)

def hexadecimal_to_binary(hexadecimal_num):
    return bin(int(hexadecimal_num, 16)).replace("0b", "")

def hexadecimal_to_octal(hexadecimal_num):
    return oct(int(hexadecimal_num, 16)).replace("0o", "")

def main():
    while True:
        print("NUMBER BASE CONVERTOR")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Binary to Octal")
        print("6. Binary to Hexadecimal")
        print("7. Octal to Decimal")
        print("8. Octal to Binary")
        print("9. Octal to Hexadecimal")
        print("10. Hexadecimal to Decimal")
        print("11. Hexadecimal to Binary")
        print("12. Hexadecimal to Octal")
        print("13. Exit")
        
        ch = int(input("Enter Your choice : "))
        if ch == 1:
            decimal_num = int(input("Enter a decimal number: "))
            binary_num = bin(decimal_num).replace("0b", "")
            print("Binary: ", binary_num)
            
        elif ch == 2:
            decimal_num = int(input("Enter a decimal number: "))
            octal_num = oct(decimal_num).replace("0o", "")
            print("Octal: ", octal_num)
        
        elif ch == 3:
            decimal_num = int(input("Enter a decimal number: "))
            hexadecimal_num = hex(decimal_num).replace("0x", "")
            print("Hexadecimal: ", hexadecimal_num)
        
        elif ch == 4:
            binary_num = input("Enter a binary number: ")
            decimal_num = int(binary_num, 2)
            print("Decimal: ", decimal_num)
            
        elif ch == 5:
            binary_num = input("Enter a binary number: ")
            octal_num = oct(int(binary_num, 2)).replace("0o", "")
            print("Octal: ", octal_num)
            
        elif ch == 6:
            binary_num = input("Enter a binary number: ")
            hexadecimal_num = hex(int(binary_num, 2)).replace("0x", "")
            print("Hexadecimal: ", hexadecimal_num)
            
        elif ch == 7:
            octal_num = input("Enter an octal number: ")
            decimal_num = int(octal_num, 8)
            print("Decimal: ", decimal_num)
            
        elif ch == 8:
            octal_num = input("Enter an octal number: ")
            binary_num = bin(int(octal_num, 8)).replace("0b", "")
            print("Binary: ", binary_num)
            
        elif ch == 9:
            octal_num = input("Enter an octal number: ")
            hexadecimal_num = hex(int(octal_num, 8)).replace("0x", "")
            print("Hexadecimal: ", hexadecimal_num)
            
        elif ch == 10:
            hexadecimal_num = input("Enter a hexadecimal number: ")
            decimal_num = int(hexadecimal_num, 16)
            print("Decimal: ", decimal_num)
            
        elif ch == 11:
            hexadecimal_num = input("Enter a hexadecimal number: ")
            binary_num = bin(int(hexadecimal_num, 16)).replace("0b", "")
            print("Binary: ", binary_num)
            
        elif ch == 12:
            hexadecimal_num = input("Enter a hexadecimal number: ")
            octal_num = oct(int(hexadecimal_num, 16)).replace("0o", "")
            print("Octal: ", octal_num)
        
        elif ch == 13:
            print("Exiting the program ...")
            break
            
        else:
            print("Invalid choice. Please choose a valid option.")
            
if __name__ == "__main__":
    main()
    
            
        
    
    
    