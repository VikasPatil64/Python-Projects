import string

def password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)

    strength = {
        "length": length_criteria,
        "uppercase": upper_criteria,
        "lowercase": lower_criteria,
        "digits": digit_criteria,
        "special_char": special_criteria
    }

    met_criteria_count = sum(strength.values())  # Count the number of True criteria

    if met_criteria_count == 5:
        return "Strong Password", strength
    elif met_criteria_count >= 3:
        return "Moderate Password", strength
    else:
        return "Weak Password", strength

def main():
    print("Welcome to Password Strength Checker")
    while True:
        print("----------------------")
        password = input("Enter a password to check its strength (or 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        strength_text, strength_dict = password_strength(password)
        print("Password Strength:", strength_text)
        print("Criteria Met:")
        
        for criteria, met in strength_dict.items():
            print("-", criteria.capitalize(), ":", "Yes" if met else "No")

if __name__ == "__main__":
    main()
