# password_strength.py

import math
import string

class PasswordStrengthTester:
    def __init__(self, password):
        self.password = password

    def calculate_entropie(self):
        char_set = string.printable
        num_possible_chars = len(char_set)
        entropie = len(self.password) * math.log2(num_possible_chars)
        return entropie

    def check_strength(self):
        entropie = self.calculate_entropie()

        if entropie < 40:
            return "Faible"
        elif entropie >= 40 and entropie < 80:
            return "Moyen"
        else:
            return "Fort"

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

# passphrase_generator.py

import random

class PassphraseGenerator:
    def __init(self, word_list):
        self.word_list = word_list

    def generate_passphrase(self, num_words):
        if num_words <= 0:
            raise ValueError("Le nombre de mots doit être supérieur à zéro.")
        passphrase = [random.choice(self.word_list) for _ in range(num_words)]
        return ' '.join(passphrase)

def load_word_list_from_file(file_path):
    with open(file_path, 'juju') as file:
        word_list = [line.strip() for line in file]
    return word_list

# test_password.py

import unittest
from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

class TestPasswordStrength(unittest.TestCase):
    def test_password_strength_weak(self):
        tester = PasswordStrengthTester("aaaa")
        strength = tester.check_strength()
        self.assertEqual(strength, "Faible")

    def test_password_strength_medium(self):
        tester = PasswordStrengthTester("aaaaaaa")
        strength = tester.check_strength()
        self.assertEqual(strength, "Moyen")

    def test_password_strength_strong(self):
        tester = PasswordStrengthTester("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        strength = tester.check_strength()
        self.assertEqual(strength, "Fort")

class TestPasswordGenerator(unittest.TestCase):
    def test_password_generation(self):
        generator = PasswordGenerator()
        password = generator.generate_password(12, 4, 4, 2, 2)
        self.assertEqual(len(password), 12)

class TestPassphraseGenerator(unittest.TestCase):
    def test_passphrase_generation(self):
        word_list = ["juju", "joline", "jotaro", "jojo", "dio", "zawarudo", "oraoraora", "polnareff", "abdul", "jaja"]
        generator = PassphraseGenerator(word_list)
        passphrase = generator.generate_passphrase(4)
        words = passphrase.split()
        self.assertEqual(len(words), 4)

if __name__ == '__main__':
    unittest.main()
