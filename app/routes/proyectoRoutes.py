from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from database import conn
from app.models.proyecto import Proyecto
from app.schemas.proyectoSchema import ProyectoSchema

proyecto = APIRouter()

@proyecto.get('/proyectos')
def get_proyectos():
    return conn.execute(select(Proyecto)).fetchall()

@proyecto.get('/proyectos/{proyecto_id}')
def get_proyecto_by_id(proyecto_id: int):
    result = conn.execute(select(Proyecto).where(Proyecto.c.id == proyecto_id)).fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@proyecto.get('/proyectos/nombre/{nombre}')
def get_proyecto_by_nombre(nombre: str):
    result = conn.execute(select(Proyecto).where(Proyecto.c.nombre == nombre)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@proyecto.get('/proyectos/estado/{estado}')
def get_proyecto_by_estado(estado: str):
    result = conn.execute(select(Proyecto).where(Proyecto.c.estado == estado)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@proyecto.get('/proyectos/lider/{lider}')
def get_proyecto_by_lider(lider: int):
    result = conn.execute(select(Proyecto).where(Proyecto.c.lider == lider)).fetchall()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@proyecto.post('/proyectos')
def create_proyecto(proyecto: ProyectoSchema):
    conn.execute(Proyecto.insert().values(
        nombre=proyecto.nombre,
        descripcion=proyecto.descripcion,
        lider=proyecto.lider,
        sublider=proyecto.sublider,
        fecha_inicio=proyecto.fecha_inicio,
        estado=proyecto.estado
    ))
    return {"message": "Proyecto creado exitosamente"}

@proyecto.put('/proyectos/{proyecto_id}')
def update_proyecto(proyecto_id: int, proyecto: ProyectoSchema):
    conn.execute(Proyecto.update().values(
        nombre=proyecto.nombre,
        descripcion=proyecto.descripcion,
        lider=proyecto.lider,
        sublider=proyecto.sublider,
        fecha_inicio=proyecto.fecha_inicio,
        estado=proyecto.estado
    ).where(Proyecto.c.id == proyecto_id))
    return {"message": "Proyecto actualizado exitosamente"}

@proyecto.delete('/proyectos/{proyecto_id}')
def delete_proyecto(proyecto_id: int):
    conn.execute(Proyecto.delete().where(Proyecto.c.id == proyecto_id))
    return {"message": "Proyecto eliminado exitosamente"}
