from pydantic import BaseModel
from typing import Optional

class TareaSchema(BaseModel):
    nombre : str
    descripcion: Optional[str] = None
    proyecto: int
    estado: str
    fecha_inicio: str
    responsable: str


