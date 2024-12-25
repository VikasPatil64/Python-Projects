#AGE CALCULATOR
import datetime

def age_calculator(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year 
    if today.month < birthdate.month or (today.month == birthdate.month and today.day==birthdate.day):
        age -= 1
    return age

def main():
    birthdate_str=input("Enter Your birthdate (DD/MM/YYYY): ")
        
    
    