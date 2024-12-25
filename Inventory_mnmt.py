# INVENTORY TRACKER APPLICAITON

inventory = {}

def add_item():
    item=input("Enter the idem to be added in the inventory :")
    quantity = int(input("Enter the quantity of " + item + ": "))
    if item in inventory:
        inventory[item]+=quantity
    else:
        inventory[item]=quantity
    print(str(quantity)+" of " + item + " added to the inventory.")

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(item + ": " + str(quantity))
    print()
    
    
#STEP 2

def remove_items():
    item = input("Enter the name of the item to be removed :")
    if item in inventory:
        del inventory[item]
        print(" "+ item+" removed from the inventory.")
    else:
      print(" "+ item + "not found in the inventory")
      
def update_item():
    item = input("Enter the item to be updated: ")
    if item in inventory:
        quantity=int(input("Enter the new quantity of " + item + ": "))
        inventory[item]=quantity
        print("Quantity of " + item + " updated to " + str(quantity) + ".")
    else:
        print(" "+ item + "not found in the inventory")
        
def search_item():
    item = input("Enter the item to be searched: ")
    if item in inventory:
        print("Quantity of " + item + " is " + str(inventory[item]) + " ")
    else:
        print(" "+ item + "not found in the inventory")
        
#STEP 3

def main():
    while True:
        print("---------INVENTORY TRACKER -----------")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Update item quantity")
        print("4. Search item in inventory")
        print("5. Display inventory")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            search_item()
        elif choice == "5":
            print(inventory)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()
     