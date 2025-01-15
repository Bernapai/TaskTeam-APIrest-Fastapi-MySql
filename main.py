from fastapi import FastAPI
from app.routes.userRoute import user
from app.routes.proyectoRoutes import proyecto
from app.routes.tareaRoutes import tarea


app = FastAPI()

app.include_router(user)
app.include_router(proyecto)
app.include_router(tarea)


