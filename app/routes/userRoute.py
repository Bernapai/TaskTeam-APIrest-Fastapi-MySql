from fastapi import APIRouter,Depends
from app.models.user import User
from database import conn
from app.routes.authJwtRoute import verify_token

user = APIRouter()

@user.get('/users')
def get_users ():
    return conn.execute(users.select()).fetchall()

@user.get('/users/{user_id}')
def get_user (user_id: int):
    return conn.execute(users.select().where(users.c.id == user_id)).fetchall()

@user.get('/users/{nombre : str}')
def get_user (nombre: str):
    return conn.execute(users.select().where(users.c.nombre == nombre)).fetchall()

@user.get('/users/{apellido : str}')
def get_user (apellido: str):
    return conn.execute(users.select().where(users.c.apellido == apellido)).fetchall()

@user.get('/users/{email : str}')
def get_user (email: str):
    return conn.execute(users.select().where(users.c.email == email)).fetchall()

@user.get('/users/{password : str}')
def get_user (password: str):
    return conn.execute(users.select().where(users.c.password == password)).fetchall()

@user.post('/users/create')
def create_user (user: User, token: dict = Depends(verify_token)):
    conn.execute(users.insert().values(
        nombre = user.nombre,
        apellido = user.apellido,
        email = user.email,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()

@user.put('/users/{user_id}')
def update_user (user_id: int, user: User, token: dict = Depends(verify_token)):
    conn.execute(users.update().values(
        nombre = user.nombre,
        apellido = user.apellido,
        email = user.email,
        password = user.password
    ).where(users.c.id == user_id))
    return conn.execute(users.select()).fetchall()

@user.delete('/users/{user_id}')
def delete_user (user_id: int, token: dict = Depends(verify_token)):
    conn.execute(users.delete().where(users.c.id == user_id))
    return conn.execute(users.select()).fetchall()


    