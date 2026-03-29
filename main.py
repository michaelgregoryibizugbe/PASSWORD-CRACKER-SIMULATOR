import hashlib
import itertools
import string
import time

# Password Strength Analysis

def password_strength(password):
    if len(password) < 8:
        return 'Weak: Password is too short.'
    elif (any(c.isdigit() for c in password) and
del any(c.isupper() for c in password) and  
        any(c.islower() for c in password)):
        return 'Strong'
    return 'Moderate: Mix of characters needed.'

# SHA-256 Hashing

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary Attack

def dictionary_attack(password, wordlist):
    for word in wordlist:
        if hash_password(word) == hash_password(password):
            return True
    return False

# Brute Force Attack

def brute_force_attack(password):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, len(password) + 1):
        for guess in itertools.product(characters, repeat=length):
            if ''.join(guess) == password:
                return True
    return False

# Main Menu

def main_menu():
    while True:
        print("\nPassword Cracker Simulator")
        print("1. Password Strength Analysis")
        print("2. Dictionary Attack")
        print("3. Brute Force Attack")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            password = input("Enter password to check strength: ")
            print(password_strength(password))

        elif choice == '2':
            password = input("Enter password to crack: ")
            wordlist = input("Enter path to wordlist: ").split()  # Assuming space-separated list
            start_time = time.time()
            if dictionary_attack(password, wordlist):
                print("Password cracked using dictionary attack!")
            else:
                print("Password not found in dictionary.")
            print(f'Time taken: {time.time() - start_time:.2f} seconds')

        elif choice == '3':
            password = input("Enter password to crack: ")
            start_time = time.time()
            if brute_force_attack(password):
                print("Password cracked using brute force attack!")
            else:
                print("Password could not be cracked.")
            print(f'Time taken: {time.time() - start_time:.2f} seconds')

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == '__main__':
    main_menu()