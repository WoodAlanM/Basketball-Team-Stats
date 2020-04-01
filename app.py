import constants
import random
import sys


# Function for creating and returning player lists based on
# experience
def create_player_lists():
    experienced_players = []
    inexperienced_players = []
    for player in constants.PLAYERS:
        for key, value in player.items():
            if key == "experience":
                if value == "NO":
                    inexperienced_players.append(player)
                else:
                    experienced_players.append(player)
    return experienced_players, inexperienced_players


# Function for creating the teams given two list of players
def populate_teams(exp_players, inexp_players):
    team1_players = []
    team2_players = []
    team3_players = []
    still_have_players = True
    while still_have_players:
        # Add players to the team1
        exp_index = random.randint(0, len(exp_players) - 1)
        inexp_index = random.randint(0, len(inexp_players) - 1)
        team1_players.append(exp_players[exp_index])
        del exp_players[exp_index]
        team1_players.append(inexp_players[inexp_index])
        del inexp_players[inexp_index]
        # Add players to the team2
        exp_index = random.randint(0, len(exp_players) - 1)
        inexp_index = random.randint(0, len(inexp_players) - 1)
        team2_players.append(exp_players[exp_index])
        del exp_players[exp_index]
        team2_players.append(inexp_players[inexp_index])
        del inexp_players[inexp_index]
        print(len(exp_players))
        # Add players to the team3
        exp_index = random.randint(0, len(exp_players) - 1)
        inexp_index = random.randint(0, len(inexp_players) - 1)
        team3_players.append(exp_players[exp_index])
        del exp_players[exp_index]
        team3_players.append(inexp_players[inexp_index])
        del inexp_players[inexp_index]
        print(len(exp_players))
        if len(exp_players) > 0:
            continue
        else:
            still_have_players = False

    return team1_players, team2_players, team3_players

def display_teams():
    print("\n")
    print("1. Panthers")
    print("2. Bandits")
    print("3. Warriors")
    print("\n")

if __name__ == "__main__":
    exp, inexp = create_player_lists()
    panthers_players, bandits_players, warriors_players = populate_teams(exp, inexp)
    print("Basketball Teams Stats Tool")
    print("---------------------------")
    print("Main Menu:")
    print("\n")
    print("Please choose an option")
    print("\n")
    print("1. Display Team Stats")
    print("2. Quit")
    print("\n")
    not_quit = True
    in_teams = False

    # Loop for initial menu selection
    while not_quit:
        try:
            selection = int(input("Please make a selection: "))
        except:
            print("Please choose only 1 or 2")
            continue
        if selection > 2 or selection < 1:
            print("Please choose either 1 or 2")
            continue
        elif selection == 1:
            display_teams()
            in_teams = True
            while in_teams:
                try:
                    selection =int(input("Please make a selection: "))
                except:
                    print("Please choose only 1,2 or 3")
                    continue
                if selection < 1 or selection > 3:
                    print("Please choose one of the menu options.")


        elif selection == 2:
            not_quit = False












