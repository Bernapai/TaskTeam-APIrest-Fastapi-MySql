from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from database import conn
from app.models.user import User
from app.schemas.userSchema import UserSchema

user = APIRouter()

@user.get('/users')
def get_users():
    return conn.execute(select(User)).fetchall()

@user.get('/users/{user_id}')
def get_user_by_id(user_id: int):
    result = conn.execute(select(User).where(User.c.id == user_id)).fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.get('/users/nombre/{nombre}')
def get_user_by_nombre(nombre: str):
    result = conn.execute(select(User).where(User.c.nombre == nombre)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.get('/users/apellido/{apellido}')
def get_user_by_apellido(apellido: str):
    result = conn.execute(select(User).where(User.c.apellido == apellido)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.get('/users/email/{email}')
def get_user_by_email(email: str):
    result = conn.execute(select(User).where(User.c.email == email)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.get('/users/password/{password}')
def get_user_by_password(password: str):
    result = conn.execute(select(User).where(User.c.password == password)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.post('/users/create')
def create_user(user: UserSchema):
    conn.execute(User.insert().values(
        nombre=user.nombre,
        apellido=user.apellido,
        email=user.email,
        password=user.password
    ))
    return {"message": "Usuario creado exitosamente"}

@user.put('/users/{user_id}')
def update_user(user_id: int, user: UserSchema):
    conn.execute(User.update().values(
        nombre=user.nombre,
        apellido=user.apellido,
        email=user.email,
        password=user.password
    ).where(User.c.id == user_id))
    return {"message": "Usuario actualizado exitosamente"}

@user.delete('/users/{user_id}')
def delete_user(user_id: int):
    conn.execute(User.delete().where(User.c.id == user_id))
    return {"message": "Usuario eliminado exitosamente"}