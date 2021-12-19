import random
from v_ball.models import Player

# Freshly calculate top and other players
# Return both lists in list like this: [top_players, other_players]
def prep_players():
    lst= Player.objects.values('player_name', 'skill_level')
    players1 = []

    for ele in lst:
        for key, value in ele.items():
            p = value
            players1.append(p)

    players = {players1[i]: players1[i + 1] for i in range(0, len(players1), 2)}

    # filter through players.items() instead of players.keys() so that we have direct access to the player's skill level
    # in the filter method (e.g., _top_players), then map it back (see the lambda) to just the player's name (key)
    # so that it works with the existing code in make_teams.py
    other_players = list(map(lambda p: p[0], filter(_other_players, players.items())))
    random.shuffle(other_players)
    top_players1 = list(map(lambda p: p[0], filter(_top_players, players.items())))

    return [top_players1, other_players]

def _top_players(player):
    # this and the other method below were returning 'players' before but a filter method (a predicate)
    # only needs to return True or False - it was working before because
    # the players list technically evaluates to True.
    # this one liner here will do the comparison and immediately return True or False
    return player[1] == 4
        
def _other_players(player):
    return player[1] != 4




        

         
  

            

