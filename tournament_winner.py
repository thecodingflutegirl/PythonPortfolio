
HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    current_best_team = ""
    teams = {current_best_team: 0}

    for i, pairing in enumerate(competitions):
        result = results[i]
        home_team, away_team = pairing

        if result == HOME_TEAM_WON:
            winning_team = home_team
        else:
            winning_team = away_team

        updateScores(winning_team, 3, teams)

        if teams[winning_team] > teams[current_best_team]:
            current_best_team = winning_team

    print(teams)

    return current_best_team


def updateScores(winning_team, points, teams):
    if winning_team not in teams:
        teams[winning_team] = 0

    teams[winning_team] += points
