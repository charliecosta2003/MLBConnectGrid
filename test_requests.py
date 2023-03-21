import requests
import statsapi


# Write a function that takes in a player id and return a function of all the teams they ever played for
def get_teams(playerName):
    if len(playerName.split(" ")) == 1 and playerName != "Ichiro":
        print("Put first and last bitch")
        return

    player_ids = set()
    for i in range(1961, 2024):
        for player in statsapi.lookup_player('David Ortiz', season=i):
            player_ids.add(player['id'])

    for player_id in player_ids:
        response = requests.get(f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats?stats=yearByYear&sportId=1")
        j = response.json()
        teams = set()
        for split in j['stats'][0]['splits']:
            try:
                teams.add(split['team']['name'])
            except KeyError:
                pass
        print(teams)


def main():
    #ids = [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 158]

    # response = requests.get("https://statsapi.mlb.com/api/v1/teams/117/roster?season=2000")
    # j = response.json()
    # for person in j['roster']:
    #     print(f"Person: {person['person']}")
    # print(j)
    # get_teams('Harper')

    # player_ids = set()
    # for i in range(1961, 2024):
    #     for player in statsapi.lookup_player('David Ortiz', season=i):
    #         player_ids.add(player['id'])
    #
    # for player_id in player_ids:
    #     print(player_id)

    print(played_for_both_efficient('David Ortiz', 111, 119))

# Player_name is the string of the fullName, while the teams are actually the team ids
def played_for_both(player_name, team1, team2):
    possible_ids = set()
    for i in range(1961, 2023):
        response = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{team1}/roster?season={i}")
        j = response.json()
        roster = j['roster']
        for player in roster:
            if player['person']['fullName'] == player_name:
                possible_ids.add(player['person']['id'])


    for player_id in possible_ids:
        response = requests.get(f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats?stats=yearByYear&sportId=1")
        j = response.json()
        for split in j['stats'][0]['splits']:
            try:
                team_id = split['team']['id']
            except KeyError:
                pass
            if team_id == team2:
                return True
    return False

def played_for_both_efficient(player_name, team1, team2):
    id = None
    found = False
    for i in range(2022, 1960, -1):
        response = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{team1}/roster?season={i}")
        j = response.json()
        roster = j['roster']
        for player in roster:
            if player['person']['fullName'] == player_name:
                id = player['person']['id']
                found = True
                break
        if found:
            break

    if not found:
        return False

    response = requests.get(f"https://statsapi.mlb.com/api/v1/people/{id}/stats?stats=yearByYear&sportId=1")
    j = response.json()
    for split in j['stats'][0]['splits']:
        try:
            team_id = split['team']['id']
        except KeyError:
            pass
        if team_id == team2:
            return True
    return False




if __name__ == '__main__':
    main()

#493316
#660271



