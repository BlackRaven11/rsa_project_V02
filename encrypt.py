import rsa

# Load the public key from file
with open('public_key.pem', 'rb') as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())

# Read the message from a text file
with open('message.txt', 'r') as file:
    message = file.read()

# Encrypt the message
encrypted_message = rsa.encrypt(message.encode(), public_key)

# Save the encrypted message to a file
with open('encrypted_message.bin', 'wb') as file:
    file.write(encrypted_message)