import time
import string
import statistics

# Le mot de passe secret que l'on cherche à deviner
SECRET = "supersecret"

# Fonction simulant la validation côté serveur
def simulate_server(input_string):
    """
    Simule une validation avec une boucle qui compare chaque caractère.
    Un délai artificiel est ajouté pour chaque caractère correct.
    """
    for i, char in enumerate(input_string):
        if i >= len(SECRET) or char != SECRET[i]:
            return False  # Échec si un caractère est incorrect
        #time.sleep(0.0001)  # Délai pour chaque caractère correct
    return len(input_string) == len(SECRET)  # Réussite si tout correspond

# Fonction principale de l'attaque
def perform_attack():
    extracted = ""
    num_attempts = 500  # Nombre de tentatives pour chaque caractère

    while True:  # Continue jusqu'à ce que le secret soit découvert
        max_avg_time = 0
        next_char = ''

        for char in string.ascii_letters + string.digits:  # Tester les caractères alphanumériques
            test_input = extracted + char + "a"  # Ajouter un caractère supplémentaire
            total_time = 0

            # Effectuer plusieurs requêtes pour calculer la moyenne
            for _ in range(num_attempts):
                start = time.perf_counter()
                simulate_server(test_input)  # Appel à la simulation du serveur
                elapsed = time.perf_counter() - start
                total_time += elapsed

            avg_time = total_time / num_attempts  # Calcul de la moyenne
            print(f"{char} (with 'a'): {avg_time}")

            if avg_time > max_avg_time:
                max_avg_time = avg_time
                next_char = char

        # Ajouter le caractère avec le temps le plus long
        extracted += next_char
        print(f"Extracted so far: {extracted}")

        # Vérifier si la chaîne complète est correcte
        if simulate_server(extracted):
            print(f"Secret fully discovered: {extracted}")
            break

if __name__ == "__main__":
    print("Starting the attack...")
    perform_attack()
