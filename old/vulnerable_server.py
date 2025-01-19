from flask import Flask, request
import hashlib
import time

app = Flask(__name__)

SECRET = "supersecret"


@app.route('/validate', methods=['GET'])
def validate():
    provided = request.args.get('input', '')
    for i, char in enumerate(provided):
        if i >= len(SECRET) or char != SECRET[i]:
            return "Invalid", 403
        time.sleep(0.0001)

    if provided == SECRET:
        return "Valid", 200
    else:
        return "Invalid", 403


@app.route('/validate_hash', methods=['GET'])
def validate_hash():
    provided = request.args.get('input', '')

    provided_hash = hashlib.sha256(provided.encode()).hexdigest()
    secret_hash = hashlib.sha256(SECRET.encode()).hexdigest()

    for i, char in enumerate(provided_hash):
        if i >= len(secret_hash) or char != secret_hash[i]:
            print(provided_hash, "    :    ", secret_hash)
            return "Invalid", 403
        time.sleep(0.0001)

    if provided_hash == secret_hash:
        return "Valid", 200
    return "Invalid", 403


if __name__ == "__main__":
    app.run(debug=False, port=5000)
