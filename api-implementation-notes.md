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
 8. Ordering is important in routes defining . **FastAPI** will choose the first path which match with user input . Let's have an example . If you have two routes like below:
	> app.get("/posts/{id}")
	> app.get("/posts/latest")
 If /posts/{id} is above of /posts/latest, users will never be able to send a request to /posts/latest because /posts/{id} will also match /posts/latest too . In other words, If you send a request to /posts/latest to get the latest post, this path is also match with /posts/{id} so **FastAPI** will choose it because it is defined sooner . To solving this problem you need to define /posts/latest at first then define /posts/{id} after that . 
 9. If you want to delete an entity, at the end in response you should send 204 No Content status code . You should know that a response with 204 No Content should not have any content and if you send any content back with this status code, You will see an error .
 So, When a DELETE HTTP Request is sent to our server to deleting an entity, We should response with status code of 204 No Content without any fucking content .