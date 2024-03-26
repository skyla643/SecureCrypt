import os
from cryptography.fernet import Fernet

# Generate a key and save it to a file
key = Fernet.generate_key()
with open("C:/Users/Future5/OneDrive/Documents/GitHub/programer-rizz/encryption_key.txt", "wb") as file:
    file.write(key)

# Encrypt a message
message = "This is a secret message".encode()
fernet = Fernet(key)
encrypted_message = fernet.encrypt(message)

# Save the encrypted message to a file
with open("C:/Users/Future5/OneDrive/Documents/GitHub/programer-rizz/encrypted_message.txt", "wb") as file:
    file.write(encrypted_message)

# Decrypt the message
encrypted_message = open("C:/Users/Future5/OneDrive/Documents/GitHub/programer-rizz/encrypted_message.txt", "rb").read()
decrypted_message = fernet.decrypt(encrypted_message)
decrypted_message = decrypted_message.decode()

# Print the decrypted message
print(decrypted_message)