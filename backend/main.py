from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from katara import db1, db2, Movie

app = FastAPI()

# Adiciona o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens; ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.get('/')
async def index():
    return 'If you are seeing this page, the backend is working.'

@app.get('/add')
async def add(db: str, title: str):
    movie = Movie(title)
    if db == 'db1':
        return db1.add_movie(movie)
    elif db == 'db2':
        return db2.add_movie(movie)
    else:
        raise HTTPException(status_code=400, detail="Invalid database")

@app.get('/delete')
async def delete(db: str, title: str):
    if db == 'db1':
        return db1.delete_movie(title)
    elif db == 'db2':
        return db2.delete_movie(title)
    else:
        raise HTTPException(status_code=400, detail="Invalid database")

@app.get('/compare')
async def compare(title: str):
    return bool(db1.get_movie(title)) and bool(db2.get_movie(title))

@app.get('/movies')
async def movies(db: str = Query(..., description="Database name")) -> List[str]:
    if db == 'db1':
        return db1.get_all_movies()
    elif db == 'db2':
        return db2.get_all_movies()
    else:
        raise HTTPException(status_code=400, detail="Invalid database")
