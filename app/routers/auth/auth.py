from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.routers.auth import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import User
from app.routers.auth.utils import hash, verify_hash
import app.routers.auth.oauth2 as oauth2

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    body.email = body.username
    user = db.query(User).filter(User.email == body.email).first()
    if (not user) or verify_hash(user.password, body.password) == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email or password is wrong .")
    
    elif verify_hash(user.password, body.password):
        payload = {
            "id": user.id
        }
        token = oauth2.create_jwt_token(payload)
        return {
            "status": "success",
            "token": token,
            "token_type": "bearer"
        }
    
@router.post("/register", response_model=schemas.UserResponse)
def register(body: schemas.UserSchema, db: Session = Depends(get_db)):
    body = body.model_dump()
    body['password'] = hash(body['password'])
    user = User(**body)
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{body['email']} email address is not available .")
    db.refresh(user)
    return user