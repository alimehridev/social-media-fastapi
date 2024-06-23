from time import time
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError, JWTClaimsError

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


def verify_jwt_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return {
            "detail": decoded_token,
            "status": "success"
            }
    except ExpiredSignatureError:
        return {
            "detail": "Token has expired",
            "status": "failed"
        }
    except JWTClaimsError:
        return {
            "detail": "Invalid token claims",
            "status": "failed"
        }
    except JWTError:
        return {
            "detail": "Invalid Token",
            "status": "failed"
            }