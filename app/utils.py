
from jose import JWTError, jwt
from time import time
import hashlib

def hash(password: str):
    return hashlib.sha256(bytes(password.encode())).hexdigest()


# JWT utils
SECRET_KEY = "445da94dbdd9866f9e7e981546d9a999199f5cfcf272a105719a4b78bd155a73"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt_token(data: dict):
    payload = data.copy()
    payload.update({
        "exp": ACCESS_TOKEN_EXPIRE_MINUTES * 60 + int(time())
    })

    return jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)