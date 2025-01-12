from sqlalchemy import Table, Column, Integer, String,  ForeignKey
from db import meta, engine

Proyecto = Table('proyectos', meta, 
    Column('id', Integer, primary_key=True),
    Column('nombre', String(50)),
    Column('descripcion', String(200)),
    Column('lider', Integer, ForeignKey('usuarios.id')),
    Column('Sublider', Integer, ForeignKey('usuarios.id')),
    Column('fecha_inicio', String(50)),
    Column('estado', String(50)),
)

meta.create_all(engine)