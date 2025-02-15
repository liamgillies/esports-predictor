from typing import List, Union
from mwrogue.esports_client import EsportsClient

site = EsportsClient('lol')

def makeCargoRequest(
    tables: Union[str, List[str]] = '',
    fields: Union[str, List[str]] = '',
    where: Union[str, None] = None,
    join_on: Union[str, List[str], None] = None,
    group_by: Union[str, None] = None,
    having: Union[str, List[str], None] = None,
    order_by: Union[str, None] = None,
    offset: Union[int, None] = None,
    limit: Union[int, None] = None,
    auto_continue: bool = True
) -> list:
    inputDict = {
        'tables': tables,
        'fields': fields,
        'where': where,
        'join_on': join_on,
        'group_by': group_by,
        'having': having,
        'order_by': order_by,
        'offset': offset,
        'limit': limit,
        'auto_continue': auto_continue
    }

    print(inputDict)

    for key, value in inputDict.items():
        if isinstance(value, list):
            inputDict[key] = ', '.join(value)

    return site.cargo_client.query(**inputDict)
