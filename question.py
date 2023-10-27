import random

class Question:
    def __init__(self, question, options, correct_reponse):
        self.question = question
        self.options = options
        self.correct_reponse = correct_reponse

    def shuffle_options(self):
        shuffled_options = random.sample(self.options, len(self.options))
        return [(chr(96 + i), option) for i, option in enumerate(shuffled_options, 1)]

    def check_reponse(self, user_reponse):
        return user_reponse.lower() == self.correct_reponse.lower()
