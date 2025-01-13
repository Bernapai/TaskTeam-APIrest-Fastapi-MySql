from pydantic import BaseModel
from typing import Optional

class ProyectoSchema(BaseModel):
    nombre: str
    descripcion: str
    lider: int
    sublider: int
    fecha_inicio: str
    estado: str
    

