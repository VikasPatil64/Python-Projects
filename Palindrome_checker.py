def main():
    while True:
        print("Palindrome checker")
        print("1. Check if a string is a palindrome")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            s = input("Enter a string: ")
            if s == s[::-1]:
                print("The string is a palindrome")
            else:
                print("The string is not a palindrome")
        elif choice == 2:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            
if __name__ == "__main__":
    main()
    