import hashlib

def hash(password: str):
    return hashlib.sha256(bytes(password.encode())).hexdigest()

def verify_hash(password: str, plain_text_password: str):
    return password == hash(plain_text_password)