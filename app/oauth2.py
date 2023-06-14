from jose import JWTError, jwt
from datetime import datetime, timedelta

# secret_key: handles data integrity of the token
# algorithm: hs256
# expiration time of the token, user cannot be logged in forever

SECRET_KEY = "c15f7086ccb71f8fbdbf558d928b22462d7f9cf7241029453e7e0ac24d891e01"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

