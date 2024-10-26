from fastapi import FastAPI
from back_Talsy.app.routers.user_router import router as User

app = FastAPI()

# Registrar rutas
app.include_router(User, prefix="/api/v1")

# Punto de inicio para verificar que la app está corriendo
app.get('/')
def index():
    return {'Message': 'This is only a message!'}