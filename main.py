from fastapi import FastAPI
from fastapi.params import Body
from models import Post

app = FastAPI() 

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
    return {
        "data": posts,
        "status": "success"
    }

@app.post("/posts")
def create_post(post: Post):
    # post.model_dump() will convert a BaseModel instance to a dictionary .
    dumped_post = post.model_dump()
    dumped_post['id'] = posts[-1]['id'] + 1
    posts.append(dumped_post)
    return {
        "data": dumped_post,
        "status": "success"
    }
