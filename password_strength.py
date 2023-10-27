# password_strength.py

import math
import string

class PasswordStrengthTester:
    def __init__(self, password):
        self.password = password

    def calculate_entropy(self):
        char_set = string.printable
        num_possible_chars = len(char_set)
        entropy = len(self.password) * math.log2(num_possible_chars)
        return entropy

    def check_strength(self):
        entropy = self.calculate_entropy()

        if entropy < 40:
            return "Faible"
        elif entropy >= 40 and entropy < 80:
            return "Moyen"
        else:
            return "Fort"
