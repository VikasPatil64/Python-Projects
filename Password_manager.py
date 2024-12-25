import os
from cryptography.fernet import Fernet

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    """Load the encryption key from the file."""
    return open("secret.key", "rb").read()

def encrypt_message(msg):
    """Encrypt a message using the encryption key."""
    key = load_key()
    f = Fernet(key)
    return f.encrypt(msg.encode())

def decrypt_message(encrypted_msg):
    """Decrypt a message using the encryption key."""
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_msg.encode()).decode()

def main():
    if not os.path.exists("secret.key"):
        generate_key()

    passwords = {}

    if os.path.exists("passwords.txt"):
        # Load existing passwords from the file
        with open("passwords.txt", "r") as f:
            for line in f:
                line = line.strip()
                if " : " in line:  # Check for valid format
                    website, encrypted_password = line.split(" : ")
                    passwords[website] = encrypted_password

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve a Password")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == 1:
            website = input("Enter Website: ")
            password = input("Enter Your Password: ")
            encrypted_password = encrypt_message(password).decode()

            passwords[website] = encrypted_password

            with open("passwords.txt", "a") as f:
                f.write(website + " : " + encrypted_password + "\n")

            print("Password added successfully for", website)

        elif choice == 2:
            website = input("Enter Website name to retrieve the password: ")

            if website in passwords:
                try:
                    print("Password for", website, "is:", decrypt_message(passwords[website]))
                except Exception as e:
                    print("Error decrypting the password:", e)
            else:
                print("Password not found for", website)

        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
