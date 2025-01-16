from fastapi import APIRouter, Depends , HTTPException
import jwt  
from app.models.user import User
from sqlalchemy import and_
from database import conn
import datetime

auth = APIRouter()

SECRET_KEY = "jm2057bb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 50


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def  verify_token(token: str = Depends(create_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=400, detail="Could not validate credentials")



@auth.post('/login')
def login(user: User):
     # Consulta a la base de datos para verificar las credenciales
    db_user =  conn.execute(User.select().where(and_(User.nombre == user.nombre, User.apellido == user.apellido))).fetchone()

    # Validación del usuario
    if not db_user:
        raise HTTPException(status_code=401, detail="Nombre o apellido incorrectos")
    
    # Crear el token si las credenciales son correctas
    token_data = {
        "user_id": db_user.id,
        "nombre": db_user.nombre,
        "apellido": db_user.apellido,
    }
    token = create_token(token_data)

    return {"token": token}
   
    
    
