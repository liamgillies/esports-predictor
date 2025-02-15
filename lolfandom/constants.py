from enum import Enum

class TABLES(Enum):
    Tournaments = 'Tournaments=T'
    ScoreboardGames = 'ScoreboardGames=SG'

class FIELDS(Enum):
    Name = 'Name'
    Date = 'Date'
    Region = 'Region'
    
class JOIN_ON(Enum):
    OverviewPage = 'OverviewPage'

    def __str__(self):
        return self.value
    
def getTableVar(tableName):
    return '='.split(tableName)[1]

def getTables(tables):
    print(tables)
    print(",".join([t.value for t in tables]))
    return ",".join([t.value for t in tables])

def getFields(table, *fields):
    outputStr = ''
    tableVar = getTableVar(table)
    for f in fields:
        outputStr += f'{tableVar}.{f},'
    return outputStr

# only for two tables
def getJoinOn(tables, field):
    return f'{getTableVar(tables[0])}.{field}={getTableVar(tables[1])}.{field}'