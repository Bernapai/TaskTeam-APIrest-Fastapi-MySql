from pydantic import BaseModel
from typing import Optional

class TareaSchema(BaseModel):
    nombre : str
    descripcion: Optional[str] = None
    proyecto: int
    estado: str
    fecha_inicio: str
    responsable: str


class TareaOutSchema(BaseModel):
    nombre : str
    descripcion: Optional[str] = None
    proyecto: int
    estado: str
    fecha_inicio: str
    responsable: str

class TareaUpdateSchema(BaseModel):
    nombre : Optional[str] = None
    descripcion: Optional[str] = None
    proyecto: Optional[int] = None
    estado: Optional[str] = None
    fecha_inicio: Optional[str] = None
    responsable: Optional[str] = None