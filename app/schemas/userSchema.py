from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nombre: str
    apellido: str
    email: str
    password: str
    rol: str
   
   
class UserOutSchema(BaseModel):
    nombre: str
    apellido: str
    email: str
    rol: str

class UserUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    rol: Optional[str] = None