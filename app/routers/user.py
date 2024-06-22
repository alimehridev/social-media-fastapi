# General imports
from fastapi import status, HTTPException, Depends, APIRouter
# Database imports
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=['User'], # To grouping the routes in API Swagger UI Documentation 
)


# Getting a user by it's id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id={id} not found .")
    return user