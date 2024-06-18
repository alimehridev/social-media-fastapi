from fastapi import FastAPI

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
                "body": "Hello, this is first post and I wish you like it ."
            },
            {
                "id": 2,
                "title": "Second post title",
                "body": "In second post, I wanna talk about some thing ..."
            }
        ],
        "status": "success"
    }