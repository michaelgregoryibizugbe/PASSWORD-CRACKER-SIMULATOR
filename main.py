import hashlib
import itertools
import string

class PasswordStrengthAnalyzer:
    def __init__(self, password):
        self.password = password
        self.strength = self.analyze_strength()

    def analyze_strength(self):
        length = len(self.password)
        if length < 6:
            return 'Weak'
        elif length < 12:
            return 'Moderate'
        return 'Strong'

class PasswordHasher:
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class BruteForceAttack:
    def __init__(self, hashed_password):
        self.hashed_password = hashed_password

    def attack(self):
        characters = string.ascii_letters + string.digits
        for length in range(1, 6):
            for guess in itertools.product(characters, repeat=length):
                guess_password = ''.join(guess)
                if PasswordHasher.hash_password(guess_password) == self.hashed_password:
                    return f'Password found: {guess_password}'
        return 'Password not found'

class DictionaryAttack:
    def __init__(self, hashed_password, dictionary_file):
        self.hashed_password = hashed_password
        self.dictionary_file = dictionary_file

    def attack(self):
        with open(self.dictionary_file, 'r') as file:
            for word in file:
                guess_password = word.strip()
                if PasswordHasher.hash_password(guess_password) == self.hashed_password:
                    return f'Password found: {guess_password}'
        return 'Password not found'

if __name__ == '__main__':
    # Example usage
    password = 'test123'
    analyzer = PasswordStrengthAnalyzer(password)
    print(f'Password strength: {analyzer.strength}')
    hashed = PasswordHasher.hash_password(password)
    print(f'Hashed password: {hashed}')
    bf_attack = BruteForceAttack(hashed)
    print(bf_attack.attack())
    # Dictionary attack requires a dictionary file
    # dict_attack = DictionaryAttack(hashed, 'path/to/dictionary.txt')
    # print(dict_attack.attack())