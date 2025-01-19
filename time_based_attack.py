import string
import statistics
import time

from check_string_methods import *

nombre_essai = 500
nombre_echantillon = 500


def perform_attack(securised=False):
    extracted = ""
    amplification_factor = 1e6

    while True:
        max_median_time = 0
        next_char = ''

        """On verifie que le prochain caractere testé n'est pas le dernier"""
        for char in string.ascii_letters + string.digits:

            if securised:
                if check_string_hashed(extracted + char):
                    print(f"Password: {extracted + char}")
                    return {extracted + char}
            else:
                if check_string(extracted + char):
                    print(f"Password: {extracted + char}")
                    return {extracted + char}

            """On ajoute un caractere suplémentaire a la string afin de forcer une boucle de plus"""
            test_input = extracted + char + "a"
            times = []
            for _ in range(
                    nombre_echantillon):  # Nombre d'echantillon pour la medianne (la moyenne aurait pu être utilisée)
                start = time.perf_counter()
                for _ in range(nombre_essai):  # Nombre d'essai pour obtenir une valeur du calcul de la médianne
                    if securised:
                        check_string_hashed(test_input)
                    else:
                        check_string(test_input)
                elapsed = time.perf_counter() - start
                times.append(elapsed * amplification_factor)

            median_time = statistics.median(times)  # Calcul de la médiane

            if median_time > max_median_time:
                max_median_time = median_time
                next_char = char

        extracted += next_char
        print(f"Valeur actuelle: {extracted}")


if __name__ == "__main__":
    print("Starting the attack...")
    print("MDP a trouver: ", SECRET, " Version Hashée: ", hashlib.sha256(SECRET.encode()).hexdigest())
    print(perform_attack())  # Pour executer la fonction sécurisée print(perform_attack(True))
