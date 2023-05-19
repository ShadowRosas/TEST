from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return HTMLResponse(content="<html><body><h1>Ruta de ejemplo</h1><p>¡Hola, mundo!</p></body></html>")
