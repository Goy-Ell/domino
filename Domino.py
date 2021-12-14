import random as rdm
from domino_modules import *

class Game:
    def __init__(self) -> None:
        pass

class Player:
    def __init__(self, number, score=0, hand=[], can_play=True) -> None:
        self.number = number
        self.score = score
        self.hand = hand
        self.can_play = can_play

    def clear_hand(self):
        self.hand = []

    def draw(self, n_time=1):
        if len(pile) > 0:
            for i in range(n_time):
                self.hand.append(pile.pop(rdm.randint(0, len(pile)-1)))
        else:
            self.can_play = False

    def __repr__(self) -> str:
        return f"Joueur {self.number}; score actuel: {self.score}; main: {self.hand}"

class Domino:
    def __init__(self, left_face=rdm.randint(0,6), right_face=rdm.randint(0,6)):
        self.left_face = left_face
        self.right_face = right_face

    def total_value(self):
        return self.left_face + self.right_face

    def swap_faces(self):
        return f"{self.right_face}:{self.left_face}"

    def __repr__(self):
        return f"{self.left_face}:{self.right_face}"



while True:
    print("Début de la partie de domino\nQuel est le nombre de joueurs ?")
    player_count = input_int(2, 6)
    initial_draw = initial_draw_finder()
    players = players_generation(player_count, Player)

    print("Combien de manches dans cette partie ?")
    round_count = input_int(1, 10)

    for round in range(1, round_count+1):
        pile = pile_generation(Domino)
        
        for player in players:
            player.draw(initial_draw)


        # while all players can play AND no player has an empty hand
        new_turn = True
        while new_turn == True:
            for player in players:
                if player.can_play != True or len(player.hand) == 0:
                    new_turn = False
            
    break




players = players_generation(2, Player)
all(players.can_play)