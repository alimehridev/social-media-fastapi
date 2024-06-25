from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from time import time
import jwt
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers.user.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# JWT utils
SECRET_KEY = "445da94dbdd9866f9e7e981546d9a999199f5cfcf272a105719a4b78bd155a73"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

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

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not valid .")
    user_id = verify_jwt_token(token=token, credentials_exception=credentials_exception)

    user = db.query(User).filter(User.id == user_id).first()
    return user
    