from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/addtional")
def opration(a, b):
    execute = int(a) + int(b)
    return execute

#  for substraction some numbers


@app.get("/substraction")
def opration(a, b):
    execute = int(a) - int(b)
    return execute

#  for multiplication some numbers


@app.get("/multiplication")
def opration(a, b):
    execute = int(a) * int(b)
    return execute

# for divison some numbers


@app.get("/division")
def opration(a, b):
    execute = int(a) / int(b)
    return execute

# for get averege of two numbers


@app.get("/avg")
def opration(a, b):
    execute = (int(a)+int(b))/2
    return execute


aboutuser = {
    1: {
        "id": 1,
        "Firstname": "vrushabh gohil",
        "Email": "vsgohil@gmail.com",
        "password": 123,
    },
    2: {
        "id": 2,
        "Firstname": "Vrushabh Gohil",
        "Email": "vsgohil@gmail.com",
        "password": 456,
    }
}


@app.get("/userdata")
async def user(user_id: int):
    return aboutuser[user_id]
# for get data from str..
note = "this is available stock"
products = {
    "sports": {
        "basket ball",
        "football",
        "tennis ball and racket",
        "suttlecoke"
    },
    "clothes": {
        "t-shirts",
        "shirts",
        "jeanse",
    },
    "snacks": {
        "meggie",
        "kurkure",
        "chips"
    }
}

stock = "there is no available"


@app.get("/store")
async def store_data(store_item: str):
    return note, products[store_item]

class user_data(BaseModel):
    id: int
    name: str
    Email_id: str
    password: str


@app.post("/name")
def get_full_name(user_detail: user_data):
    response = user_detail.dict()
    id = response.get("id")
    name = response.get("name")
    email = response.get("Email")
    password = response.get("password")
    return {id, name, email, password}

