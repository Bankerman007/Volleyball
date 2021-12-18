import random
from v_ball.models import Player



lst= Player.objects.values('player_name', 'skill_level')
players1 = []

for ele in lst:
    for key, value in ele.items():
        p = value
        players1.append(p)

players = {players1[i]: players1[i + 1] for i in range(0, len(players1), 2)}


def top_players(player):
    if players[player] == 4:
        return players
        
top_players1 = list(filter(top_players, players.keys()))

def other_players(player):
    if players[player] != 4:
        return players
        
other_players = list(filter(other_players, players.keys()))
random.shuffle(other_players)



        

         
  

            

