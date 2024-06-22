# General imports
from fastapi import status, HTTPException, Depends, APIRouter
# Database imports
from app import models, schemas, utils
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/users",
    tags=['User'] # To grouping the routes in API Swagger UI Documentation 
)

# Create new user
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(body: schemas.UserSchema, db: Session = Depends(get_db)):
    body.password = utils.hash(body.password)
    user = models.User(**body.model_dump())
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{body.email} email address is not available .")
    
    db.refresh(user)
    return user

# Getting a user by it's id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id={id} not found .")
    return user