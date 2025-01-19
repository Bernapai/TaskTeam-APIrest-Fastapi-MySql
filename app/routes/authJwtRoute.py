
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.sql import select, and_
from database import conn
from app.models.user import User
from app.schemas.authSchema import LoginSchema
from app.utils.jwt import create_token



# Router para las rutas de autenticación
auth = APIRouter()

def verify_user_in_db(nombre: str, apellido: str):
        try:
            query = select(User).where(and_(User.c.nombre == nombre, User.c.apellido == apellido))
            result = conn.execute(query).first()

            if not result:
                return None
            return dict(result._mapping)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {e}")

@auth.post('/login')
def login(data: LoginSchema):
    # Verificamos si el usuario existe en la base de datos
    user_dict = verify_user_in_db(data.nombre, data.apellido)
    
    if not user_dict:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Si el usuario existe, generamos el token
    token = AuthService.create_token(user_dict)
    return {"message": "Login exitoso", "token": token}

    