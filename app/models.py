from app.database import Base
from sqlalchemy.orm import relationship
from app.routers.post.models import Post
from app.routers.user.models import User

class Post(Post):
    pass

class User(User):
    pass
    