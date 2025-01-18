from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.sql import select
from database import conn
from app.models.user import User
import jwt
import datetime

# Clave secreta para JWT (cámbiala por una más segura en producción)
SECRET_KEY = "jmb28()"

# Router para las rutas de autenticación
auth = APIRouter()

# Esquema para login
class LoginSchema(BaseModel):
    nombre: str
    apellido: str

# Función para crear un token
def create_token(user):
    payload = {
        'id': user['id'],
        'nombre': user['nombre'],
        'apellido': user['apellido'],
        'rol': user['rol'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira en 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Función para verificar un token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Ruta para login
@auth.post('/login')
async def login(data: LoginSchema):
    query = select([User]).where(User.c.nombre == data.nombre).where(User.c.apellido == data.apellido)
    result = conn.execute(query).fetchone()

    if result:
        user = dict(result)
        token = create_token(user)
        return {"message": "Login exitoso", "token": token}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
