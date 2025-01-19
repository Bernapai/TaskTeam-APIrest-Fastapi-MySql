from pydantic import BaseModel
from typing import Optional

class LoginSchema(BaseModel):
    nombre: str
    apellido: str

class LoginOutSchema(BaseModel):
    nombre: str
    apellido: str
    rol: str
    token: str