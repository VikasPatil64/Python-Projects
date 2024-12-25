import os
from datetime import datetime

def write_entry():
    entry = input("Write your diary entry: ")
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", 'a') as file:
        file.write(f"{timestamp}\n{entry}\n\n")
        
def view_entries():
    if not os.path.exists("diary.txt"):
        print("No diary entries found ")
        return
    with open("diary.txt", "r") as file:
        entries=file.read()
    print("\n-----Diary entries-------")
    print(entries)
    
def main():
    while True:
        print("\n Personal Diary:")
        print("1. Write an entry")
        print("2. View entries")
        print("3. Quit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            write_entry()
        elif choice == 2:
            view_entries()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            
if __name__ == "__main__":
    main()