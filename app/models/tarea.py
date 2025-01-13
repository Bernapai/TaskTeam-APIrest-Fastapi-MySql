from sqlalchemy import Table, Column, Integer, String,  ForeignKey
from database import meta, engine


Tarea = Table('tareas', meta, 
    Column('id', Integer, primary_key=True),
    Column('nombre', String(50)),
    Column('descripcion', String(200)),
    Column('proyecto', Integer, ForeignKey('proyectos.id')),
    Column('estado', String(50)),
    Column('fecha_inicio', String(50)),
    Column('responsable', String(50)),
)

meta.create_all(engine)



