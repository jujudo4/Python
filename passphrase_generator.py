# passphrase_generator.py

import random

class PassphraseGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_passphrase(self, num_words):
        if num_words <= 0:
            raise ValueError("Le nombre de mots doit être supérieur à zéro.")
        passphrase = [random.choice(self.word_list) for _ in range(num_words)]
        return ' '.join(passphrase)

def load_word_list_from_file(file_path):
    with open(file_path, 'r') as file:
        word_list = [line.strip() for line in file]
    return word_list
