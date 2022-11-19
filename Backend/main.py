from fastapi import FastAPI
from demo import findstring
from category import cat
from firebase import solve
app = FastAPI()

@app.get('/status')
async def status():
    x = findstring()
    return x


@app.get('/status/category')
async def statuscategory():
    x = cat()
    return x


@app.get('/firebase')
async def solutionfetch():
    x = solve()
    return x