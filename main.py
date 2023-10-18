from fastapi import FastAPI
from find_payment_user import get_payment_info_from_csv

app = FastAPI()


@app.get('/')
async def root():
    return {'example' : 'This is an example', 'Data' : 10}


@app.get('/find_user/{amount}')
async def find_user(amount : int):
    return get_payment_info_from_csv(amount)
