#TO DO list 
#Step 1
todo_list=[]
completed_list = []

def add_item():
    item = input("Enter the item to add :")
    todo_list.append(item)
    print(f"Item {item} added to the list")
    
#step 2
def remove_item():
    index = input("Enter the index of the item to remove")
    if index.isdigit() and 1 <= int(index) <= len(todo_list):
        index = int(index) - 1 
        remove_item=todo_list.pop(int(index))
        print(f"Item {remove_item} removed from the list")
    else:
        print("Invalid index")

def display_list(lst, list_name):
    print(f"\n{list_name} :")
    for index, item in enumerate(lst, start=1):
        print(f"{index}. {item}")
    print()
    
#step 3

def mark_item_completed():
    index = input("Enter the index of the item to mark as completed: ")
    if index.isdigit() and 1 <= int(index) <= len(todo_list):
        index = int(index) - 1
        completed_item = todo_list.pop(int(index))
        print("  "+ completed_item+" has been marked as completed")
        completed_list.append(completed_item)
    else:
      print("Invalid index")
      
def main():
    while True:
        print("--------------TO DO List--------------")
        print("-------------------------------------")
        print("1. Add item to the list")
        print("2. Remove item from the list")
        print("3. Mark item as completed")
        print("4. Display the list")
        print("5. Display completed items")
        print("6. Exit")
        
        choice = int(input("Enter Your choice :"))
        
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            mark_item_completed()
        elif choice == 4:
            display_list(todo_list, "To Do List")
        elif choice == 5:
            display_list(completed_list, "Completed Items")
        elif choice == 6:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()