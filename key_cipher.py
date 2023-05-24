from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import requests
import json
# Load the RSA private key from a file
def token():
    URL='http://external.phuocthienpharma.net/v1/get-key'
    resp=requests.get(URL)
    with open('private_key.pem', 'r') as f:
        private_key_data = f.read()

    private_key = RSA.import_key(private_key_data)

    # Read the ciphertext from a file or receive it from Go
    # with open('ciphertext.txt', 'rb') as f:
    #     ciphertext = f.read()
    ciphertext=json.loads(resp.text)['data']
    byte_cipher=base64.b64decode(ciphertext)
    # Create a cipher object using the private key
    cipher = PKCS1_v1_5.new(private_key)

    # Decrypt the ciphertext
    decrypted = cipher.decrypt(byte_cipher, None)

    # Print the decrypted plaintext
    return decrypted.decode()
