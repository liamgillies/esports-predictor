from lolfandom.cargo_request import makeCargoRequest
from .constants import TABLES, FIELDS, getFields, getTables

class LolFandomAPI:
    
    def setTournament():
         return

    def setPlayer(self):
        print(TABLES.Tournaments)
        tables=getTables([TABLES.Tournaments, TABLES.ScoreboardGames])
        response = makeCargoRequest(
                tables=tables,
                join_on="SG.OverviewPage=T.OverviewPage",
                fields="T.Name,T.Region,T.TournamentLevel,T.IsOfficial,T.Date",
                where="""T.TournamentLevel='Primary' AND 
                         T.isOfficial='1' AND
                         T.Date >= '2025-01-01'""",
                limit=2000
            )


        print(response)