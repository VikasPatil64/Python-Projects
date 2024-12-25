#AGE CALCULATOR
from datetime import datetime

def age_calculator(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year 
    if today.month < birthdate.month or (today.month == birthdate.month and today.day==birthdate.day):
        age -= 1
    return age

def main():
    birthdate_str=input("Enter Your birthdate (DD/MM/YYYY): ")
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y").date()
    age=age_calculator(birthdate)
    print(f"Your age is {age}")
    
if __name__ == "__main__":
    main()
        
