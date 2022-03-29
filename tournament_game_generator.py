#GAME GENERATOR ALGORITH FROM PROGRAMMING EXPERT 

#THIS PROGRAM IS ASSUMING INPUTS ARE THE CORRECT DATA TYPE (INTS), THAT THE NUMBER OF TEAMS IS DIVISIBLE BY TWO, AND THAT EACH TEAM PLAYS THE SAME NUMBER OF GAMES. 


from time import sleep

def number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams < 2:
            print("The minimum number of teams is 2, try again.")
        else:
            return num_teams


def get_team_names(num_teams):
    list_of_team_names = []
    for num in range(num_teams):
        while True:
            team_name = input(f"Enter the name for team #{num +1}: ")
            if len(team_name) < 2:
                print("Team names must have at least 2 characters. Try again.")
            elif len(team_name.split(" ")) > 2:
                print("Team names may have at most 2 words, try again.")
            else:
                break
        list_of_team_names.append(team_name)

    return list_of_team_names


def number_of_games_played(num_teams):
    while True:
        games_played = int(
            input("Enter the number of games played by each team: "))
        if games_played < (num_teams - 1):
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        else:
            break
    return games_played


def team_wins(team_names, games_played):
    num_team_wins = []
    for team in team_names:
        while True:
            games_won = int(
                input(f"Enter the number of wins Team {team} had: "))
            if games_won < 0:
                print("The minimum number of wins is 0, try again.")
            elif games_won > games_played:
                print(
                    f"The maximum number of wins is {games_played}, try again.")

            num_team_wins.append((team, games_won))
            break

    return num_team_wins


def second_item(item):
    return item[1]


num_teams = number_of_teams()
team_names = get_team_names(num_teams)
games_played = number_of_games_played(num_teams)
num_team_wins = team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sleep(1)

sorted_teams = sorted(num_team_wins, key=second_item)
pairings = []

games_to_make = len(sorted_teams) // 2

for game_num in range(games_to_make):
    home_team = sorted_teams[game_num][0]
    away_team = sorted_teams[num_teams - 1 - game_num][0]
    pairings.append([home_team, away_team])

for pairing in pairings:
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")
