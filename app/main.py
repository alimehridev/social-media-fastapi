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
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    new_post = cursor.fetchone() #Fetch the result of "RETURNING *" command at the end of query .
    conn.commit()
    return {
        "data": new_post,
        "status": "success"
    }


@app.get("/posts/latest")
def post():
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC LIMIT 1")
    post = cursor.fetchone()
    return {
        "post_details": post,
        "status": "success"
    }

@app.get("/posts/{id}")
def post(id: int):
    cursor.execute("SELECT * FROM posts WHERE id=%s", (str(id), ))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "status": f"Post with id={id} not found ."
        })
    return {
        "post_details": post,
        "status": "success"
    }


@app.delete("/posts/{id}")
def delete_post(id: int):
    cursor.execute("DELETE FROM posts WHERE id=%s RETURNING *", (str(id), ))
    if cursor.fetchone() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exit to be deleted .")
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    


@app.put("/posts/{id}")
def update_post(id: int, body: Post):
    for i, p in enumerate(posts):
        if id == p['id']:
            body = body.model_dump()
            body['id'] = id
            posts[i] = body
            return {"status": "success"}
        
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id={id} does not exist .")