from fastapi import FastAPI
from fastapi.params import Body
from models import Post

app = FastAPI() 

@app.get("/")
async def root():
    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    return {
        "data": [
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
        ],
        "status": "success"
    }

@app.post("/createpost")
def createpost(post: Post):
    # post.model_dump() will convert a BaseModel instance to a dictionary .
    return {
        "data": {
            "id": 1,
            "title": post.title,
            "content": post.content,
            "published": post.published,
            "rating": post.rating
        },
        "status": "success"
    }
