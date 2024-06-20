from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from models import Post
import psycopg2
from psycopg2.extras import RealDictCursor
import time

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


posts = [
    {
        "id": 1,
        "title": "This is first post",
        "content": "Hello, this is first post and I wish you like it ."
    },
    {
        "id": 2,
        "title": "Second post title",
        "content": "In second post, I wanna talk about some thing ..."
    }
]


@app.get("/")
async def root():
    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {
        "data": posts,
        "status": "success"
    }

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    # post.model_dump() will convert a BaseModel instance to a dictionary .
    dumped_post = post.model_dump()
    dumped_post['id'] = posts[-1]['id'] + 1
    posts.append(dumped_post)
    return {
        "data": dumped_post,
        "status": "success"
    }


@app.get("/posts/{id}")
def post(id: int):
    cursor.execute("SELECT * FROM posts WHERE id=" + str(id))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "status": "failed"
        })
    return {
        "post_details": post,
        "status": "success"
    }


@app.delete("/posts/{id}")
def delete_post(id: int):
    for i, p in enumerate(posts):
        if id == p['id']:
            posts.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exits to be deleted .")


@app.put("/posts/{id}")
def update_post(id: int, body: Post):
    for i, p in enumerate(posts):
        if id == p['id']:
            body = body.model_dump()
            body['id'] = id
            posts[i] = body
            return {"status": "success"}
        
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exist .")