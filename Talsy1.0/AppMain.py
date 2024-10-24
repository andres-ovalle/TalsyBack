from fastapi import FastAPI
from .back_Talsy.app.routers.candidates import candidates
from .back_Talsy.app.routers.candidates import list_candidates, upload

app = FastAPI()

# Registrar las rutas
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
    return {"message": "Welcome to Talsy Backend"}
