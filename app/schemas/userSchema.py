from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nombre: str
    apellido: str
    email: str
    password: str
    rol: str
   
   
