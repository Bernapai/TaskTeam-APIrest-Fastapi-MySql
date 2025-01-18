from fastapi import APIRouter,Depends
from app.models.proyecto import Proyecto
from database import conn
from app.routes.authJwtRoute import verify_token

proyecto = APIRouter()

@proyecto.get('/proyectos')
def get_proyectos ():
    return conn.execute(proyectos.select()).fetchall()

@proyecto.get('/proyectos/{proyecto_id}')
def get_proyecto (proyecto_id: int):
    return conn.execute(proyectos.select().where(proyectos.c.id == proyecto_id)).fetchall()

@proyecto.get('/proyectos/{nombre : str}')
def get_proyecto (nombre: str):
    return conn.execute(proyectos.select().where(proyectos.c.nombre == nombre)).fetchall()

@proyecto.get('/proyectos/{estado : str}')
def get_proyecto (estado: str):
    return conn.execute(proyectos.select().where(proyectos.c.estado == estado)).fetchall()

@proyecto.get('/proyectos/{lider : int}')
def get_proyecto (lider: int):
    return conn.execute(proyectos.select().where(proyectos.c.lider == lider)).fetchall()

@proyecto.post('/proyectos')
def create_proyecto (proyecto: Proyecto, token: dict = Depends(verify_token)):
    conn.execute(proyectos.insert().values(
        nombre = proyecto.nombre,
        descripcion = proyecto.descripcion,
        lider = proyecto.lider,
        sublider = proyecto.sublider,
        fecha_inicio = proyecto.fecha_inicio,
        estado = proyecto.estado
    ))
    return conn.execute(proyectos.select()).fetchall()

@proyecto.put('/proyectos/{proyecto_id}')
def update_proyecto (proyecto_id: int, proyecto: Proyecto , token: dict = Depends(verify_token)):
    conn.execute(proyectos.update().values(
        nombre = proyecto.nombre,
        descripcion = proyecto.descripcion,
        lider = proyecto.lider,
        sublider = proyecto.sublider,
        fecha_inicio = proyecto.fecha_inicio,
        estado = proyecto.estado
    ).where(proyectos.c.id == proyecto_id))
    return conn.execute(proyectos.select()).fetchall()

@proyecto.delete('/proyectos/{proyecto_id}')
def delete_proyecto (proyecto_id: int, token: dict = Depends(verify_token)):
    conn.execute(proyectos.delete().where(proyectos.c.id == proyecto_id))
    return conn.execute(proyectos.select()).fetchall()

