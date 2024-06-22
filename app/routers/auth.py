from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import User
from app.utils import hash
from app import utils


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(body: schemas.LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if (not user) or (user.password != hash(body.password)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email or password is wrong .")
    
    elif user.password == hash(body.password):
        payload = {
            "id": user.id
        }
        token = utils.create_jwt_token(payload)
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