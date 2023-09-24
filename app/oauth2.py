from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')  # retrieved from auth.py, remove the '/'
# secret_key: handles data integrity of the token
# algorithm: hs256
# expiration time of the token, user cannot be logged in forever

SECRET_KEY = "c15f7086ccb71f8fbdbf558d928b22462d7f9cf7241029453e7e0ac24d891e01"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")  #  extract the user_id
        
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)  #  validate the user_id
    except JWTError:
        raise credentials_exception
    
    return token_data  # return to whoever calls it, in the future also return additional fields other than id
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"Couldn't validate credentials", headers={"WWW-Authenticate: ", "Bearer"})

    return verify_access_token(token, credentials_exception)