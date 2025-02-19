from collections import OrderedDict
from lolfandom.cargo_request import makeCargoRequest
from .helpers.constants import (
    TABLES, 
    FIELDS,
    getJoinOn,
    getFormattedDate,
    getFormattedToday,
    getFields
)


class LolFandomAPI:

    def __init__(self):
        self.date = getFormattedDate(1, 1, 2025)
        print(self.date)

    def setDate(self, day, month, year):
        self.date = getFormattedDate(year, month, day)

    def getDateToday(self):
        return getFormattedToday()

    def formatCargoResult(self, resultDict):
        return OrderedDict((key[0].lower() + key[1:], value) for key, value in resultDict.items())
    
    def formatCargoListResult(self, resultList):
        return [OrderedDict((key[0].lower() + key[1:], value) for key, value in resultDict.items()) for resultDict in resultList]

    def getCurrentTournaments(self):
        tables = [f'{TABLES.Tournaments}=T', f'{TABLES.ScoreboardGames}=SG']
        T = FIELDS.Tournaments
        fields = getFields('T', T.Name, T.DateStart)
        join_on = getJoinOn('T', 'SG', T.OverviewPage)
        where1 = f"T.{T.Country}='South Korea' AND T.{T.DateStart} <= '{self.getDateToday()}'"
        where2 = f"T.{T.DateStart} <= '{self.getDateToday()}'"
        order_by=f'T.{T.DateStart} DESC'
        korea_cargo_res = makeCargoRequest(tables, fields, where1, join_on, order_by=order_by, limit=10)
        cargo_res = makeCargoRequest(tables, fields, where2, join_on, order_by=order_by, limit=500)
        # trim
        list_of_names = set()
        res = []
        for tournament in cargo_res + korea_cargo_res:
            if(tournament["Name"] not in list_of_names):
                list_of_names.add(tournament["Name"])
                res.append(self.formatCargoResult(tournament))
        return res
        
    def getTournamentRosters(self, tournamentName):
        tables = [f'{TABLES.TournamentRosters}=T']
        T = FIELDS.TournamentRosters
        fields = getFields('T', T.Tournament, T.PageAndTeam, T.Team, T.RosterLinks, T.Roles, T.OverviewPage)
        where = f"T.Tournament = '{tournamentName}'"
        cargo_res = makeCargoRequest(tables, fields, where)
        return self.formatCargoListResult(cargo_res)

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