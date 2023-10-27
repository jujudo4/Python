# password_generator.py

import random
import string

class PasswordGenerator:
    def generate_password(self, length, num_lower, num_upper, num_digits, num_special):
        char_set = ""
        char_set += string.ascii_lowercase * num_lower
        char_set += string.ascii_uppercase * num_upper
        char_set += string.digits * num_digits
        char_set += string.punctuation * num_special
        if len(char_set) < length:
            raise ValueError("Impossible de générer un mot de passe avec ces critères.")
        password = ''.join(random.choice(char_set) for _ in range(length))
        return password
