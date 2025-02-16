from lolfandom.cargo_request import makeCargoRequest
from .helpers.constants import (
    TABLES, 
    FIELDS,
    getJoinOn,
    getFormattedDate,
    getFields
)


class LolFandomAPI:

    def __init__(self):
        self.date = getFormattedDate(1, 1, 2025)
        print(self.date)
        self.Tournaments = FIELDS.Tournaments

    def setDate(self, day, month, year):
        self.date = getFormattedDate(year, month, day)

    def getCurrentTournaments(self):
        tables = [f'{TABLES.Tournaments}=T', f'{TABLES.ScoreboardGames}=SG']
        T = self.Tournaments
        fields = getFields('T', T.Name, T.EventType, T.Split, T.Tags)
        join_on = getJoinOn('T', 'SG', T.OverviewPage)
        where = f"""
            T.{T.TournamentLevel}='Primary' AND
            T.{T.IsOfficial}='1' AND
            T.{T.Date}>={self.date}
         """
        order_by=f'T.{T.Date} DESC'
        print(makeCargoRequest(tables, fields, where, join_on, order_by=order_by, limit=50))
        

    # def setPlayer(self):
    #     tables=getTables([TABLES.Tournaments, TABLES.ScoreboardGames])
    #     response = makeCargoRequest(
    #             tables=tables,
    #             join_on="SG.OverviewPage=T.OverviewPage",
    #             fields="T.Name,T.Region,T.TournamentLevel,T.IsOfficial,T.Date",
    #             where="""T.TournamentLevel='Primary' AND 
    #                      T.isOfficial='1' AND
    #                      T.Date >= '2025-01-01'""",
    #             limit=2000
    #        