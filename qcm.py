import random
from question import Question

class QCM:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def questionnaire(self):
        self.shuffle_questions()
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question.question}")
            while True:
                options = question.shuffle_options()
                for option in options:
                    print(f"{option[0]}. {option[1]}")

                user_reponse = input("Votre réponse (a. b. c.) : ")
                if user_reponse.lower() in ('a', 'b', 'c'):
                    user_reponse_text = next(opt[1] for opt in options if opt[0] == user_reponse.lower())
                    if question.check_reponse(user_reponse_text):
                        print("Bonne réponse!\n")
                        self.score += 1
                    else:
                        correct_option = next(opt[1] for opt in options if question.check_reponse(opt[1].lower()))
                        print(f"Mauvaise réponse. La réponse correcte est {correct_option}.\n")
                    break
                else:
                    print("Caractère incorrect. Réessayez.\n")

    def show_resultat(self):
        print(f"Score final: {self.score}/{len(self.questions)}")
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question.question}")
            print(f"Réponse correcte: {question.correct_reponse}")

if __name__ == "__main__":
    q1 = Question("1 + 1", ["2", "3", "4"], "2")
    q2 = Question("2 + 2", ["4", "5", "6"], "4")
    q3 = Question("3 + 3", ["4", "5", "6"], "6")
    q4 = Question("4 + 4", ["8", "5", "6"], "8")
    q5 = Question("5 + 5", ["10", "5", "6"], "10")
    q6 = Question("6 + 6", ["12", "5", "6"], "12")
    q7 = Question("7 + 7", ["4", "14", "6"], "14")
    q8 = Question("8 + 8", ["4", "5", "16"], "16")
    q9 = Question("9 + 9", ["18", "5", "6"], "18")
    q10 = Question("10 + 10", ["4", "20", "6"], "20")

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    qcm = QCM(questions)
    qcm.questionnaire()
    qcm.show_resultat()
