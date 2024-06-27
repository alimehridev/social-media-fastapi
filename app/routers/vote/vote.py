from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers.vote import schemas
from app.routers.user.models import User
from app.routers.auth import oauth2
from app.models import Vote

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post("/up")
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    user_id = current_user.id
    post_id = vote.post_id

    # Check for vote to be not existed 
    last_vote = db.query(Vote).filter(and_(Vote.post_id == post_id, Vote.user_id == user_id)).first()
    if last_vote != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="vote has been done before .")
    vote = Vote()
    vote.post_id = post_id
    vote.user_id = user_id
    db.add(vote)
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id={post_id} not found .")
    db.refresh(vote)
    return vote

@router.post("/back")
def vote_back(vote: schemas.Vote, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    user_id = current_user.id
    post_id = vote.post_id

    vote = db.query(Vote).filter(and_(Vote.post_id == post_id, Vote.user_id == user_id)).first()
    if vote == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no vote for user {user_id} on post {post_id}")
    db.delete(vote)
    db.commit()
    
    return {
        "detail": "Vote deleted ."
    }