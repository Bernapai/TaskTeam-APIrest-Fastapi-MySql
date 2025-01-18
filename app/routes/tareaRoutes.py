from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from database import conn
from app.models.tarea import Tarea

tarea = APIRouter()

@tarea.get('/tareas')
def get_tareas():
    return conn.execute(select(Tarea)).fetchall()

@tarea.get('/tareas/{tarea_id}')
def get_tarea_by_id(tarea_id: int):
    result = conn.execute(select(Tarea).where(Tarea.c.id == tarea_id)).fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@tarea.get('/tareas/nombre/{nombre}')
def get_tarea_by_name(nombre: str):
    result = conn.execute(select(Tarea).where(Tarea.c.nombre == nombre)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@tarea.get('/tareas/estado/{estado}')
def get_tarea_by_estado(estado: str):
    result = conn.execute(select(Tarea).where(Tarea.c.estado == estado)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@tarea.get('/tareas/proyecto/{proyecto}')
def get_tarea_by_proyecto(proyecto: int):
    result = conn.execute(select(Tarea).where(Tarea.c.proyecto == proyecto)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@tarea.get('/tareas/responsable/{responsable}')
def get_tarea_by_responsable(responsable: str):
    result = conn.execute(select(Tarea).where(Tarea.c.responsable == responsable)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@tarea.post('/tareas')
def create_tarea(tarea: Tarea):
    conn.execute(Tarea.insert().values(
        nombre=tarea.nombre,
        descripcion=tarea.descripcion,
        proyecto=tarea.proyecto,
        estado=tarea.estado,
        fecha_inicio=tarea.fecha_inicio,
        responsable=tarea.responsable
    ))
    return {"message": "Tarea creada exitosamente"}

@tarea.put('/tareas/{tarea_id}')
def update_tarea(tarea_id: int, tarea: Tarea):
    conn.execute(Tarea.update().values(
        nombre=tarea.nombre,
        descripcion=tarea.descripcion,
        proyecto=tarea.proyecto,
        estado=tarea.estado,
        fecha_inicio=tarea.fecha_inicio,
        responsable=tarea.responsable
    ).where(Tarea.c.id == tarea_id))
    return {"message": "Tarea actualizada exitosamente"}

@tarea.delete('/tareas/{tarea_id}')
def delete_tarea(tarea_id: int):
    conn.execute(Tarea.delete().where(Tarea.c.id == tarea_id))
    return {"message": "Tarea eliminada exitosamente"}
