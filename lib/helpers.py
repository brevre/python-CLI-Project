import random
import string
import re
from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

cipher = Fernet(load_key())

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

# Validation Functions
def validate_name(name):
    pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
    return bool(re.fullmatch(pattern, name))

def validate_url(url):
    pattern = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(\/\S*)?$"
    return bool(re.fullmatch(pattern, url))

def check_password_strength(password):
    if len(password) < 8:
        return "Weak (Password must be at least 8 characters)"
    if not re.search(r"[A-Z]", password):
        return "Weak (Include at least one uppercase letter)"
    if not re.search(r"[a-z]", password):
        return "Weak (Include at least one lowercase letter)"
    if not re.search(r"\d", password):
        return "Weak (Include at least one number)"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak (Include at least one special character)"
    return "Strong"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(length))
