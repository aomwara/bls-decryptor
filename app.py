from utils.keystore import (
    Keystore,
)
from flask import Flask, json, request
api = Flask(__name__)

@api.route('/', methods=['GET'])
def welcome():
    return json.dumps({"message":"Welcome to the validator key decryptor"})

@api.route('/decrypt', methods=['POST'])
def decrypt_api():
    req = request.get_json()
    validator_key = req['validator_key']
    password = req['password']
    try:
        saved_keystore = Keystore.from_json(validator_key)
        secret_bytes = saved_keystore.decrypt(password)
        return json.dumps(hex(int.from_bytes(secret_bytes, 'big')))
    except:
        return json.dumps('Validator key or password is incorrect')  

if __name__ == '__main__':
    api.run()