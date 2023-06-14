import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse

conn = psycopg2.connect(
    user='postgres',
    password='5918',
    host='127.0.0.1',
    port='5432',
    database=''
)
cursor = conn.cursor()

app = FastAPI()

@app.get('/')
def homePage():
    return FileResponse('templates/home.html')

@app.get('/reg')
def registerPage():
    return FileResponse('templates/home.html')

@app.get('/check')
def check(login):
    pass
