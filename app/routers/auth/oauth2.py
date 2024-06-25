from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from time import time
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# JWT utils
SECRET_KEY = "445da94dbdd9866f9e7e981546d9a999199f5cfcf272a105719a4b78bd155a73"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def create_jwt_token(data: dict):
    payload = data.copy()
    payload.update({
        "exp": ACCESS_TOKEN_EXPIRE_MINUTES * 60 + int(time())
    })
    
    return jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)


def verify_jwt_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except:
        raise credentials_exception

    id: str = payload.get("id")
    if id == None:
        raise credentials_exception
    return id

def is_auth(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not valid .")

    return verify_jwt_token(token=token, credentials_exception=credentials_exception)
    