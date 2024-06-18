from fastapi import FastAPI
from fastapi.params import Body

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
def createpost(body: dict = Body(...)):
    try:
        id = 1
        title = body['title']
        content = body['content']
        return {
            "data": {
                "id": id,
                "title": title,
                "content": content
            },
            "status": "success"
        }
    except:
        return {
            "data": {},
            "status": "failed"
        }
