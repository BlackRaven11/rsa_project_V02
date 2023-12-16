import rsa

# Load the private key from file
with open('private_key.pem', 'rb') as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())

# Read the encrypted message from a file
with open('encrypted_message.bin', 'rb') as file:
    encrypted_message = file.read()

# Decrypt the message
decrypted_message = rsa.decrypt(encrypted_message, private_key)

# Print the decrypted message
print(decrypted_message.decode())