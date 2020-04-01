import constants

teams_list = constants.TEAMS

experienced_players = []
inexperienced_players = []

for player in constants.PLAYERS:
    for key, value in player.items():
        if key == "experience":
            if value == "NO":
                inexperienced_players.append(player)
            else:
                experienced_players.append(player)





