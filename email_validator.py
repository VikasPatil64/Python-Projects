#Email Validator
import re

def is_valid_email(email): #abc@gmail.com
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False
    
def main():
    email = input("Enter your email: ")
    if is_valid_email(email):
        print("Email is valid")
    else:
        print("Email is not valid")
        
if __name__ == "__main__":
    main()