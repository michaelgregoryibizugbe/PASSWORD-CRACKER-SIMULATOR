def interactive_menu():
    while True:
        print("Interactive Password Strength Testing Menu:")
        print("1. Test Password Strength")
        print("2. Hash Password")
        print("3. Conduct Dictionary Attack")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            password = input("Enter a password to test its strength: ")
            test_password_strength(password)
        elif choice == '2':
            password = input("Enter a password to hash: ")
            hash_password(password)
        elif choice == '3':
            password = input("Enter a short password for dictionary attack: ")
            conduct_dictionary_attack(password)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


def test_password_strength(password):
    # Implement logic for testing the strength of the password
    print(f"Testing strength of '{password}'...")


def hash_password(password):
    # Implement logic for hashing the password
    print(f"Hashing password '{password}'...")


def conduct_dictionary_attack(password):
    # Implement logic for a dictionary attack on the password
    print(f"Conducting dictionary attack on '{password}'...")


if __name__ == '__main__':
    interactive_menu()