from lolfandom import lolfandom_api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

LolFandomAPI = lolfandom_api.LolFandomAPI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LolFandomAPI.getTeamCurrentPlayers('ESUG Ultimate Five Feeder')

# start: cd fullstack/esports-predictor && python -m uvicorn main:app --reload

# kill 
# CMD+R: taskkill /f /im python.exe

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/currentTournaments")
def readCurrentTournaments():
    return LolFandomAPI.getCurrentTournaments()

@app.get("/tournaments/{name}/rosters")
def getTournamentRosters(name: str):
    print(name)
    return LolFandomAPI.getTournamentRosters(name)

# @app.get("/teams/{name}/currentPlayers")
# def getTeamCurrentPlayers(name: str):
#     return LolFandomAPI.getTeamCurrentPlayers(name)