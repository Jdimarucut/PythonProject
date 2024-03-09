import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Create a key for the hash table using the website and username
        key = (website, username)

        # Add the hashed password to the hash table
        self.passwords[key] = hashed_password

        print("Password Added Successfully")

    def retrieve_password(self):
        if not self.passwords:
            print("No passwords stored.")
            return

        print("Stored Passwords:")
        for key, hashed_password in self.passwords.items():
            website, username = key
            print(f"{website} - {username}")

        website = input("Enter the website: ")
        username = input("Enter the username: ")

        key = (website, username)
        hashed_password = self.passwords.get(key)

        if hashed_password:
            print(f"Password for {username} on {website}: {hashed_password}")
        else:
            print("Password not found")

    def delete_password(self):
        if not self.passwords:
            print("No passwords stored.")
            return

        print("Stored Passwords:")
        for key, hashed_password in self.passwords.items():
            website, username = key
            print(f"{website} - {username}")

        website = input("Enter the website: ")
        username = input("Enter the username: ")

        key = (website, username)
        if key in self.passwords:
            del self.passwords[key]
            print("Successful Password Deletion")
            self.retrieve_password()
        else:
            print("Password not found")

# Example Usage
password_manager = PasswordManager()

while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        website = input("Enter the website: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        password_manager.add_password(website, username, password)
    elif choice == "2":
        password_manager.retrieve_password()
    elif choice == "3":
        password_manager.delete_password()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")