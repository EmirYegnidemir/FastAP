from fastapi import FastAPI
import models
from database import engine
from routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)   # when we get a HTTP request, it will check whether there will be a match with router objects
app.include_router(user.router)   # the same for the "user" router
app.include_router(auth.router)
