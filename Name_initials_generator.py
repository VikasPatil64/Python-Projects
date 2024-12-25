# NAME INITIALS GENERATOR

def generate_initials(full_name):
    """Generate initials from a full name."""
    name_parts=full_name.strip().split()
    initials = ''.join([part[0].upper() for part in name_parts])
    return initials

def main():
    while True:
        print("Name Initials generator")
        print("1. Generate Initials ")
        print("2. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            full_name = input("Enter your full name: ")
            print("Your initials are: ", generate_initials(full_name))
        elif choice == 2:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
        