# General imports
from fastapi import status, HTTPException, Depends, APIRouter
# Database imports
from app.models import User
from app.routers.user import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.routers.auth import oauth2

router = APIRouter(
    prefix="/users",
    tags=['User'], # To grouping the routes in API Swagger UI Documentation 
)

# Getting a user by it's id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    user = db.query(User).filter(User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id={id} not found .")
    return user