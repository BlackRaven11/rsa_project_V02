from rsa.key import newkeys
import pickle

# Generate RSA key pair
public_key, private_key = newkeys(2048)

# Save the keys to files
with open('public_key.pem', 'wb') as file:
    file.write(public_key.save_pkcs1())

with open('private_key.pem', 'wb') as file:
    file.write(private_key.save_pkcs1())