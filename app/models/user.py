from sqlalchemy import Table, Column, Integer, String,  ForeignKey
from database import meta, engine

User = Table('usuarios', meta,
    Column('id', Integer, primary_key=True),
    Column('nombre', String(50)),
    Column('apellido', String(50)),
    Column('email', String(50)),
    Column('password', String(50)),
    Column('rol', String(50)),
)

meta.create_all(engine)