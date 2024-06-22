## Social Media written in Python Fastapi Framework

Endpoints:
 1. Posts
	 1. GET /posts Get Posts
	 2. POST /posts Create Posts
	 3. GET /posts/{id} Get POST
	 4. PUT /posts/{id} Update Post
	 5. DELETE /posts/{id} Delete Post
	 6. GET /posts/latest Getting latest post
 2. Vote
	 1. POST /vote/ Vote to specific post
 3. Users
	 1. POST /users/ Create User
	 2. GET /users/{id} Get User
 4. Authentication
	 1. POST /login/ Login
	 2. POST /logout/ Logout
 5. Default
	 1. / Root
##
## How to run it ?
At first you need to install all requirements which are in requirements.txt file by command bellow :

    pip install -r requirements.txt
This command will install fastapi[all] for your that will include of all the fastapi dependencies like **uvicorn** and ..., so you can run the project by command bellow:

    uvicorn app.main:app
Now the application is running on 127.0.0.1 port 8000 . You can use it :)


> If I learnt anything in this project, I have written it in api-implementation-notes.md file . You can read those notes if you want .