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
 10. One the most important thing about APIs is documentation . **FastAPI** will generate documentation about our API automatically and we can access to it with /docs and /redoc . /docs will give us a Swagger UI based documentation and /redoc will give us some UI else . 
 11. Do not forget to Parameterize your SQL query to be not in danger of SQL Injection . 
 13. If you wanna use Postgres DB in your project, you can use it from docker and in python you should import psycopg2 library .
 14. Schema/Pydantic Model can define the requests and responses model . For example, if you expect title, content, published in user's request and nothing more in a specific path like /post, You should define a Pydantic Model to check . By Pydantic models you can define every items structure you received . For example you expect user to send you a string title and not to send you an integer one, You should defined it in you Pydantic Models . So Pydantic Models will be used between users and server to defined the structure of transmitted data . But what about ORM Models ? They are between servers and databases and has nothing to do with users . Another thing you should know is that, Your Pydantic Models should be based on your ORM Models .
 15. Technically you do not need Pydantic Models in your API services, but you have to as strict as possible about the data you receive and send to the users and Pydantic Models will ensure that they are what we expect . 
 16. For each of requests our API service receives, We should define a different Pydantic/Model . It is one of the best practices we should know . 
 17. Never send user's password back to the users in your API, There is no reason to do this . 
 18. Never put all your paths in one file and you must separate them in different routers .
 19. I think it is better to separate your paths according to their usages in different directories . For example auth functions and routes should be in a file with the name of auth.py and auth functions have their own models, schemas, utils and etc . It is better to separate them from other routes in a directory like apps in Django .
 20. If you want to have a table with a combination of more than one column be unique, You have to use **Composite Keys** in your DBMS . In our project, Voting table should have a unique combination between post_id and user_id because a user cannot vote for a post twice . There are some other ways that you can implement something like this but best practices told us to use **Composite Keys** . **Composite Keys** are **Primary Key** that is spanned multiple columns .
 