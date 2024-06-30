# General imports
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
# Database imports
from app.models import Post, User, Vote
from app.routers.post import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.routers.auth import oauth2
from sqlalchemy import or_, func, desc

router = APIRouter(
    prefix="/posts",
    tags=['Posts'] # To grouping in API Swagger UI Documentation
)

# Get All Posts Function
@router.get("", response_model=List[schemas.PostToResponseWithVotes])
def get_posts(db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user), page_number: int = 1, posts_count: int = 10):
    if page_number == 0:
        page_number = 1
    posts = db.query(Post, func.count(Vote.post_id).label("votes_count")).join(Vote, Post.id == Vote.post_id, isouter=True).group_by(Post.id).order_by(desc(Post.created_at)).limit(posts_count).offset((page_number - 1) * posts_count).all()
    return posts

# Search in posts title and content
@router.get("/search", response_model=List[schemas.PostToResponseWithVotes])
def search(db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user), q: str = "", page_number: int = 1, posts_count: int = 10):
    if page_number == 0:
        page_number = 1
    posts = db.query(Post, func.count(Vote.post_id).label("votes_count")).filter(or_(Post.content.ilike(f"%{q}%"), Post.title.ilike(f"%{q}%"))).join(Vote, Vote.post_id == Post.id, isouter=True).group_by(Post.id).limit(posts_count).offset((page_number - 1) * posts_count).all()
    return posts

# Create New Post Function
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.PostToResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    post = post.model_dump()
    post.update({
        "owner_id": current_user.id
    })
    new_post = Post(**post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get Latest Post Function
@router.get("/latest", response_model=schemas.PostToResponseWithVotes)
def post(db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    post = db.query(Post, func.count(Vote.post_id).label("votes_count")).order_by(Post.id.desc()).join(Vote, Vote.post_id == Post.id, isouter=True).group_by(Post.id).first()
    return post

# Get One Post Function
@router.get("/{id}", response_model=schemas.PostToResponseWithVotes)
def post(id: int, db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    post = db.query(Post, func.count(Vote.post_id).label("votes_count")).filter(Post.id == id).join(Vote, Vote.post_id == Post.id, isouter=True).group_by(Post.id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "status": f"Post with id={id} not found ."
        })
    return post

# Delete A Post Function
@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    post = db.query(Post).filter(Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exit to be deleted .")
    if post.first().owner_id == current_user.id:
        post.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to delete this post .")

    

# Update a Post Function
@router.put("/{id}")
def update_post(id: int, body: schemas.PostCreate, db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    post_query = db.query(Post).filter(Post.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exist .")
    if post_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to update this post .")
    post_query.update(body.model_dump(), synchronize_session=False)
    db.commit()
    return {
        "data": post_query.first(),
        "status": "success"
    }
