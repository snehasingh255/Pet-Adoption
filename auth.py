import hashlib

users = {"sneha": hashlib.sha256("sneha123".encode()).hexdigest()}

def login(username, password):
    passwd= hashlib.sha256(password.encode()).hexdigest()
    return users.get(username) == passwd