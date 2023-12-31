import psycopg2
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

conn = psycopg2.connect(
    user='postgres',
    password='5918',  # change to your password
    host='127.0.0.1',
    port='5432',
    database='store_db'  # change to your db
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


@app.get('/good_detail')
def goodDetailPage():
    return FileResponse('templates/good_detail.html')


@app.post('/reg')
def registration(
        login: str = Form(),
        password: str = Form(),
        name: str = Form(),
        surname: str = Form(),
        tel: str = Form(),
        iin: str = Form()
):
    print(login, password, name, surname, tel, iin)


@app.get('/check')
def check(login):
    cursor.execute("SELECT login FROM users WHERE login='" + login + "';")
    if cursor.fetchall():
        return JSONResponse({'isAvailable': False})
    else:
        return JSONResponse({'isAvailable': True})


@app.get('/categories')
def getCategories():
    # Достает из БД имена и id всех категорий. Возвращает из в JSON формате
    cursor.execute("SELECT id, name FROM categories")
    categories = []
    for category in cursor.fetchall():
        categories.append({
            'id': category[0],
            'name': category[1]
        })
    return JSONResponse(categories)


@app.get('/goodsByCategory')
def goodsByCategory(category):
    cursor.execute('SELECT id, name FROM goods WHERE category_id=' + str(category))
    goods = []
    for good in cursor.fetchall():
        goods.append({
            'id': good[0],
            'name': good[1]
        })
    return JSONResponse(goods)


@app.get('/test')
def test():
    return FileResponse('media/Patrick.jpeg')


@app.get('/good')
def getGood(good_id):
    query = "SELECT * FROM goods WHERE id=" + str(good_id)
    cursor.execute(query)
    good = cursor.fetchone()
    print(good)
    if good:
        good = {
            'id': good[0],
            'name': good[1],
            'description': good[2],
            'price': good[3],
            'category': good[4]
        }
        return JSONResponse(good)
    else:
        return JSONResponse({'message': 'Good with ' + str(good_id) + ' id doesn`t exist'},
                            status_code=404)
