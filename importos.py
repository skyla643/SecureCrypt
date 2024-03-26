import os
import sys
from cryptography.fernet import Fernet

if 'cryptography' not in sys.modules:
    print("Module 'cryptography' is not installed. Please run 'pip install cryptography' to install it.")
    sys.exit(1)

# Rest of the code