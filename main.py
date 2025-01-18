from fastapi import FastAPI
from app.routes.userRoute import user
from app.routes.proyectoRoutes import proyecto
from app.routes.tareaRoutes import tarea
from app.routes.authJwtRoute import auth

app = FastAPI()

app.include_router(user)
app.include_router(proyecto)
app.include_router(tarea)
app.include_router(auth)


