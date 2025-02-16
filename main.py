from lolfandom import lolfandom_api
from typing import Union
from fastapi import FastAPI

LolFandomAPI = lolfandom_api.LolFandomAPI()

LolFandomAPI.getCurrentTournaments()
app = FastAPI()


# kill 
# CMD+R: taskkill /f /im python.exe

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/currentTournaments")
def readCurrentTournaments():
    return LolFandomAPI.getCurrentTournaments()
