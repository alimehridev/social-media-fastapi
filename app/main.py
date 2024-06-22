# General imports
from fastapi import FastAPI, Response, status, HTTPException, Depends
import time
# Database imports
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)
app = FastAPI() 


while True:
    try:
        conn = psycopg2.connect(host = "localhost", database = "social-media", user = "postgres", password = "mysecretpassword", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("[+] Connecting to database was successful .")
        break
    except Exception as err:
        print("[-] Connecting to database failed .")
        print("[-] Error:", err)
        time.sleep(5)



@app.get("/")
async def root():
    return {"message": "Welcome to my api"}


# Get All Posts Function
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts")
    # post = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {
        "data": posts,
        "status": "success"
    }

# Create New Post Function
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    # new_post = cursor.fetchone() #Fetch the result of "RETURNING *" command at the end of query .
    # conn.commit()

    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {
        "data": new_post,
        "status": "success"
    }

# Get Latest Post Function
@app.get("/posts/latest")
def post(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts ORDER BY created_at DESC LIMIT 1")
    # post = cursor.fetchone()
    post = db.query(models.Post).order_by(models.Post.id.desc()).first()
    print(post)
    return {
        "post_details": post,
        "status": "success"
    }

# Get One Post Function
@app.get("/posts/{id}")
def post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts WHERE id=%s", (str(id), ))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "status": f"Post with id={id} not found ."
        })
    return {
        "post_details": post,
        "status": "success"
    }

# Delete A Post Function
@app.delete("/posts/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("DELETE FROM posts WHERE id=%s RETURNING *", (str(id), ))
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exit to be deleted .")
    post.delete(synchronize_session=False)
    db.commit()

    # conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

# Update a Post Function
@app.put("/posts/{id}")
def update_post(id: int, body: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *", (
    #     body.title,
    #     body.content,
    #     body.published,
    #     str(id),
    # ))
    # updated_post = cursor.fetchone()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exist .")
    
    post_query.update(body.model_dump(), synchronize_session=False)
    db.commit()
    # conn.commit()
    return {
        "details": post_query.first(),
        "status": "success"
    }