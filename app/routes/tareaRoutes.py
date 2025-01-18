from fastapi import APIRouter,Depends
from app.models.tarea import Tarea
from database import conn
from app.routes.authJwtRoute import verify_token

tarea = APIRouter()

@tarea.get('/tareas')
def get_tareas ():
    return conn.execute(tareas.select()).fetchall()

@tarea.get('/tareas/{tarea_id}')
def get_tarea (tarea_id: int):
    return conn.execute(tareas.select().where(tareas.c.id == tarea_id)).fetchall()

@tarea.get('/tareas/{nombre : str}')
def get_tarea (nombre: str):
    return conn.execute(tareas.select().where(tareas.c.nombre == nombre)).fetchall()

@tarea.get('/tareas/{estado : str}')
def get_tarea (estado: str):
    return conn.execute(tareas.select().where(tareas.c.estado == estado)).fetchall()

@tarea.get('/tareas/{proyecto : int}')
def get_tarea (proyecto: int):
    return conn.execute(tareas.select().where(tareas.c.proyecto == proyecto)).fetchall()

@tarea.get ('/tareas/{responsable : str}')
def get_tarea (responsable: str):
    return conn.execute(tareas.select().where(tareas.c.responsable == responsable)).fetchall()

@tarea.post('/tareas')
def create_tarea (tarea: Tarea, token: dict = Depends(verify_token)):
    conn.execute(tareas.insert().values(
        nombre = tarea.nombre,
        descripcion = tarea.descripcion,
        proyecto = tarea.proyecto,
        estado = tarea.estado,
        fecha_inicio = tarea.fecha_inicio,
        responsable = tarea.responsable
    ))
    return conn.execute(tareas.select()).fetchall()

@tarea.put('/tareas/{tarea_id}')
def update_tarea (tarea_id: int, tarea: Tarea , token: dict = Depends(verify_token)):
    conn.execute(tareas.update().values(
        nombre = tarea.nombre,
        descripcion = tarea.descripcion,
        proyecto = tarea.proyecto,
        estado = tarea.estado,
        fecha_inicio = tarea.fecha_inicio,
        responsable = tarea.responsable
    ).where(tareas.c.id == tarea_id))
    return conn.execute(tareas.select()).fetchall()

@tarea.delete('/tareas/{tarea_id}')
def delete_tarea (tarea_id: int, token: dict = Depends(verify_token)):
    conn.execute(tareas.delete().where(tareas.c.id == tarea_id))
    return conn.execute(tareas.select()).fetchall()

