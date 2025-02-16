def format_string(input_str):
    lines = input_str.strip().split('\n')
    formatted_lines = []
    all_vars = []

    for line in lines:
        parts = line.split(' - ')
        if len(parts) == 2:
            var_name = parts[0].strip()
            formatted_lines.append(f"{var_name} = '{var_name}'")
            all_vars.append(var_name)

    # Adding ALL array at the bottom
    all_vars_str = f"ALL = [{', '.join(all_vars)}]"
    print('\n'.join(formatted_lines) + '\n' + all_vars_str)

format_string("""
OverviewPage - String
Tournament - String
Team1 - String
Team2 - String
WinTeam - String
LossTeam - String
DateTime_UTC - Datetime
DST - String
Team1Score - Integer
Team2Score - Integer
Winner - Integer
Gamelength - String
Gamelength_Number - Float
Team1Bans - List of String, delimiter: ,
Team2Bans - List of String, delimiter: ,
Team1Picks - List of String, delimiter: ,
Team2Picks - List of String, delimiter: ,
Team1Players - List of String, delimiter: ,
Team2Players - List of String, delimiter: ,
Team1Dragons - Integer
Team2Dragons - Integer
Team1Barons - Integer
Team2Barons - Integer
Team1Towers - Integer
Team2Towers - Integer
Team1Gold - Float
Team2Gold - Float
Team1Kills - Integer
Team2Kills - Integer
Team1RiftHeralds - Integer
Team2RiftHeralds - Integer
Team1VoidGrubs - Integer
Team2VoidGrubs - Integer
Team1Atakhans - Integer
Team2Atakhans - Integer
Team1Inhibitors - Integer
Team2Inhibitors - Integer
Patch - String
LegacyPatch - String
PatchSort - String
MatchHistory - String
VOD - Wikitext
N_Page - Integer
N_MatchInTab - Integer
N_MatchInPage - Integer
N_GameInMatch - Integer
Gamename - String
UniqueLine - String
GameId - String
MatchId - String
RiotPlatformGameId - String
RiotPlatformId - String
RiotGameId - String
RiotHash - String
RiotVersion - Integer
              """)