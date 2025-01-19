# Le mot de passe cherché
import hashlib
import time

SECRET = "aligotSo6"


def check_string(input_string, input_string_2=SECRET):
    for i, char in enumerate(input_string):
        if i >= len(input_string_2) or char != input_string_2[i]:
            return False
        #time.sleep(0.0001) permet d'emplifier le temps qui indique que le char est bon
    return input_string == input_string_2


def check_string_hashed(input_string, input_string_2=SECRET):
    input_hash = hashlib.sha256(input_string.encode()).hexdigest()
    input_string_2_hash = hashlib.sha256(input_string_2.encode()).hexdigest()
    for i, char in enumerate(input_hash):
        if i >= len(input_string_2_hash) or char != input_string_2_hash[i]:
            return False
        # time.sleep(0.0001) permet d'emplifier le temps qui indique que le char est bon
    return input_hash == input_string_2_hash
