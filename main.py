import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

conn = psycopg2.connect(
    user='postgres',
    password='5918', # change to your password
    host='127.0.0.1',
    port='5432',
    database='store_db' # change to your db
)
cursor = conn.cursor()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def homePage():
    return FileResponse('templates/home.html')

@app.get('/reg')
def registerPage():
    return FileResponse('templates/reg.html')

@app.get('/check')
def check(login):
    cursor.execute("SELECT login FROM users WHERE login='" + login + "';")
    if cursor.fetchall():
        return JSONResponse({'isAvailable': False})
    else:
        return JSONResponse({'isAvailable': True})
# если логин занят return JSONResponse({'isAvailable': False})
# иначе return JSONResponse({'isAvailable': True})
