# Function to add a customer
def add_customer():
    id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    addr = input("Enter Customer Address: ")
    phone = input("Enter Customer Phone Number: ")

    row = id + "\t" + name + "\t" + addr + "\t" + phone + "\n"

    with open("customer.txt", "a") as f:
        f.write(row)
    print("Customer added successfully!")


# Function to delete a customer
def delete_customer():
    id = input("Enter the Customer ID to delete: ")
    flag = False

    with open("customer.txt", "r") as f:
        lines = f.readlines()

    with open("customer.txt", "w") as f:
        for line in lines:
            if line.startswith(id + "\t"):
                flag = True
            else:
                f.write(line)

    if flag:
        print("Customer record deleted successfully!")
    else:
        print("No record found with the given ID.")


# Function to display all customers
def show_all_customers():
    try:
        with open("customer.txt", "r") as f:
            data = f.read()
            if data.strip():
                print("\nCustomer Records:")
                print("ID\tName\tAddress\tPhone")
                print(data)
            else:
                print("No customer records found.")
    except FileNotFoundError:
        print("No customer records found.")


# Function to search for a customer
def search_customer():
    query = input("Enter Customer ID or Name to search: ").lower()
    found = False

    try:
        with open("customer.txt", "r") as f:
            for line in f:
                if query in line.lower():
                    print("\nMatching Customer Record:")
                    print("ID\tName\tAddress\tPhone")
                    print(line)
                    found = True
                    break

        if not found:
            print("No matching customer record found.")
    except FileNotFoundError:
        print("No customer records found.")


# Function to update a customer
def update_customer():
    id = input("Enter the Customer ID to update: ")
    updated = False

    with open("customer.txt", "r") as f:
        lines = f.readlines()

    with open("customer.txt", "w") as f:
        for line in lines:
            if line.startswith(id + "\t"):
                name = input("Enter new Customer Name: ")
                addr = input("Enter new Customer Address: ")
                phone = input("Enter new Customer Phone Number: ")

                updated_row = id + "\t" + name + "\t" + addr + "\t" + phone + "\n"
                f.write(updated_row)
                updated = True
            else:
                f.write(line)

    if updated:
        print("Customer record updated successfully!")
    else:
        print("No record found with the given ID.")


# Main menu
def main():
    print("Welcome to the Customer Portal:")
    print("--------------------------------")

    while True:
        print("\n1. Add Customer")
        print("2. Delete Customer")
        print("3. Update Customer")
        print("4. Search Customer")
        print("5. Show All Customers")
        print("6. Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if ch == 1:
            add_customer()
        elif ch == 2:
            delete_customer()
        elif ch == 3:
            update_customer()
        elif ch == 4:
            search_customer()
        elif ch == 5:
            show_all_customers()
        elif ch == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()