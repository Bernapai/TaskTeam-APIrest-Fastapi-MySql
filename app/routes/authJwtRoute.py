from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from app.models.user import User
from sqlalchemy import and_, select
from database import conn
import datetime

auth = APIRouter()

SECRET_KEY = "jm2057bb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 50
security = HTTPBearer()

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@auth.post('/login')
def login(user: User):
    db_user = conn.execute(
        select(User).where(and_(User.c.nombre == user.nombre, User.c.apellido == user.apellido))
    ).fetchone()

    if db_user is None:
        raise HTTPException(status_code=401, detail="Nombre o apellido incorrectos")
    
    token_data = {
        "user_id": db_user.id,
        "nombre": db_user.nombre,
        "apellido": db_user.apellido,
    }
    token = create_token(token_data)
    return {"token": token}
