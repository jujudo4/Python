# main.py

from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator, load_word_list_from_file

while True:
    choice = input(
        "Choisissez une option : 1 (testeur de mot de passe), 2 (générateur de mot de passe), 3 (générateur de passphrase), 4 (terminer le programme): ")

    if choice == "1":
        password = input("Entrez le mot de passe à tester : ")
        tester = PasswordStrengthTester(password)
        strength = tester.check_strength()
        print(f"Force du mot de passe : {strength}")
        print("")
    elif choice == "2":
        length = int(input("Longueur du mot de passe : "))
        num_lower = int(input("Nombre de minuscules : "))
        num_upper = int(input("Nombre de majuscules : "))
        num_digits = int(input("Nombre de chiffres : "))
        num_special = int(input("Nombre de caractères spéciaux : "))

        generator = PasswordGenerator()
        password = generator.generate_password(length, num_lower, num_upper, num_digits, num_special)
        print("Mot de passe généré :", password)
        print("")
    elif choice == "3":
        word_list = load_word_list_from_file("eff_large_wordlist.txt")
        word_list = [line.split('\t')[1] for line in word_list]
        num_words = int(input("Nombre de mots dans la passphrase : "))
        generator = PassphraseGenerator(word_list)
        passphrase = generator.generate_passphrase(num_words)
        print("Passphrase générée :", passphrase)
        print("")
    elif choice == "4":
        print("Programme terminé.")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")


