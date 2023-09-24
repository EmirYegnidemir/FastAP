from typing import List
from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
from psycopg2.extras import RealDictCursor
import models, schemas, utils
from database import engine, get_db
from routers import post, user, auth
from sqlalchemy.orm import Session

import psycopg2
import time


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:

    try:
        # bad practice, will be improved later
        conn = psycopg2.connect(host='localhost', database='fastapi', 
                            user='postgres', password='123456',
                            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break

    except Exception as error:
        print("Connection to database is failed")
        print("Error:", error)
        time.sleep(2)

app.include_router(post.router)   # when we get a HTTP request, it will check whether there will be a match with router objects
app.include_router(user.router)   # the same for the "user" router
app.include_router(auth.router)
