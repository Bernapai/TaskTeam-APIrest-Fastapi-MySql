from pydantic import BaseModel
from typing import Optional

class ProyectoSchema(BaseModel):
    nombre: str
    descripcion: str
    lider: int
    sublider: int
    fecha_inicio: str
    estado: str
    
class ProyectoOutSchema(BaseModel):
    nombre: str
    descripcion: str
    lider: int
    sublider: int
    fecha_inicio: str
    estado: str


class ProyectoUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    lider: Optional[int] = None
    sublider: Optional[int] = None
    fecha_inicio: Optional[str] = None
    estado: Optional[str] = None

