import os
from cryptography.fernet import Fernet

# Generate a key and save it to a file
key = Fernet.generate_key()
with open("your file", "wb") as file:
    file.write(key)

# Encrypt a message
message = "This is a secret message".encode()
fernet = Fernet(key)
encrypted_message = fernet.encrypt(message)

# Save the encrypted message to a file
with open("your file", "wb") as file:
    file.write(encrypted_message)

# Decrypt the message
encrypted_message = open("your file", "rb").read()
decrypted_message = fernet.decrypt(encrypted_message)
decrypted_message = decrypted_message.decode()

# Print the decrypted message
print(decrypted_message)
