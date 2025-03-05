from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Monter le dossier static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route pour favicon.ico
@app.get('/favicon.ico')
async def favicon():
    return FileResponse('static/favicon.ico')

@app.get("/")
async def root():
    return {"message": "Hello World"}
