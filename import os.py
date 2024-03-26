import os
import secrets
from cryptography.fernet import Fernet

# Generate a secure encryption key
key = Fernet.generate_key()

# Create a file to store the encryption key
key_file = "encryption_key.txt"
if not os.path.exists(key_file):
    with open(key_file, "wb") as f:
        f.write(key)
        
# Encrypt a sensitive message
message = b"This is a secret message"
fernet = Fernet(key)
encrypted_message = fernet.encrypt(message)

# Save the encrypted message to a file
encrypted_file = "encrypted_message.txt"
if os.path.exists(encrypted_file):
    os.remove(encrypted_file)

with open(encrypted_file, "wb") as f:
    f.write(encrypted_message)

# At this point, the encrypted message is saved in the encrypted_file
# and can be securely transmitted over the network.

# To decrypt the message, read the key file and use the Fernet object to decrypt it
with open(key_file, "rb") as f:
    key = f.read()

fernet = Fernet(key)

with open(encrypted_file, "rb") as f:
    encrypted_message = f.read()

decrypted_message = fernet.decrypt(encrypted_message)
decrypted_message = decrypted_message.decode()

# The decrypted message is now available as a string
print(decrypted_message)