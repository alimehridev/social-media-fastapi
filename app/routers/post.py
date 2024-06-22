# General imports
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
# Database imports
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/posts",
    tags=['Posts'] # To grouping in API Swagger UI Documentation
)

# Get All Posts Function
@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# Create New Post Function
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get Latest Post Function
@router.get("/latest", response_model=schemas.PostResponse)
def post(db: Session = Depends(get_db)):
    post = db.query(models.Post).order_by(models.Post.id.desc()).first()
    return post

# Get One Post Function
@router.get("/{id}", response_model=schemas.PostResponse)
def post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "status": f"Post with id={id} not found ."
        })
    return post

# Delete A Post Function
@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exit to be deleted .")
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

# Update a Post Function
@router.put("/{id}")
def update_post(id: int, body: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exist .")
    
    post_query.update(body.model_dump(), synchronize_session=False)
    db.commit()
    return {
        "data": post_query.first(),
        "status": "success"
    }
