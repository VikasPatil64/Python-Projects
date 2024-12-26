#GREETING MESSAGE GENERATOR
#=====================================

from datetime import datetime 
def get_time_of_day():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Morning"
    elif 12 <= current_hour < 18:
        return "Afternoon"
    else:
        return "Evening"
    
def generate_greeting(name, occassion=None):
    time_of_day = get_time_of_day()
    if occassion:
        return f"Good {time_of_day}, {name}! Wishing you a wonderful {occassion}"
    else:
        return f"Good {time_of_day}, {name} ! Hope you have a good day"

def main():
    print("Welcome to Greeting message generator")
    name = input("Enter your name: ")
    occassion = input("Enter the occassion (optional): ")
    if not name:
        print("Please enter your name")
        return
    greetings = generate_greeting(name, occassion)
    print(greetings)
    
if __name__ == "__main__":
    main()
        
    