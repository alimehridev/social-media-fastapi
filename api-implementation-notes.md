## Notes and Best Practices
Here I will write all the notes I learnt in this project . 

 1. All the routes should be plural . For example 
	 - If you have routes for doing CRUD on posts in your project, These routes should be like /posts, /posts/{id} and ... . 
	 - If you have route for doing CRUD on users, These routes should be like /users, /users/{id}, ...
	 - You can not use single names in your routes
 2. Creating an entity must be a POST request and the path for this case should be something like /posts if your entity is a post .
	> app.post("/posts")
 3. Reading an entity or a bunch of them must be through a GET request . Reading an entity like a post should be done through /posts/{id} path and reading all of the entities like all of the post should be done through /posts path .
	> app.get("/posts")
	> app.get("/posts/{id}")
 4. Updating a pre-existed entity should be done by PUT/PATCH request . 
	- If you have some entities like posts and you want to create a path to update one of them you have to act like below:
		> app.put("/posts/{id}")
		> app.patch("/posts/{id}")
	- The difference between PUT and PATCH is that, In a PATCH request you just need to send updated fields and not all of them but in a PUT request you should pass all the fields including updated and not updated ones, in other words, PATCH focused on changed fields but PUT does not care about changed and unchanged fields .
 5. Deleting an entity like a post should be done through a DELETE HTTP Request . For example, If you want to delete a Post with id=5 you should send a DELETE request to /posts/5 path . To define a DELETE path in FastAPI you can do like below :
	> app.delete("/posts/{id}")
 6. When you create a new entity of anything, In return you should return new created and saved in database entity to the user . 
 7. Validating user inputs is very important and in **FastAPI** we use **pydantic** library to do this . 
