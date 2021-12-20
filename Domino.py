import random as rdm
from domino_modules import *

class Game:
    def __init__(self) -> None:
        pass

class Player:
    def __init__(self, player_number) -> None:
        self.name = f"Joueur {player_number}"
        self.score = 0
        self.hand = []
        self.can_play = True

    def clear_hand(self):
        self.hand = []

    def draw(self, pile, n_time=1):
        if len(pile) > 0:
            for i in range(n_time):
                ajout = pile.pop(rdm.randint(0, len(pile)-1))
                print(ajout)
                self.hand.add(ajout)
        else:
            self.can_play = False
        
        return pile

    def __repr__(self) -> str:
        return f"{self.name}; score actuel: {self.score}; main: {self.hand}"

class Domino:
    def __init__(self, left_face=rdm.randint(0,6), right_face=rdm.randint(0,6)):
        self.left_face = left_face
        self.right_face = right_face

        if left_face == right_face:
            self.double = True
        else:
            self.double = False

    def total_value(self):
        return self.left_face + self.right_face

    def swap_faces(self):
        # return f"{self.right_face}:{self.left_face}"
        return Domino(self.right_face, self.left_face)

    def __repr__(self):
        return f"{self.left_face}:{self.right_face}"



while True:
    print("Début de la partie de domino\nQuel est le nombre de joueurs ?")
    player_count = valid_input(range(2, 7))
    initial_draw = initial_draw_finder(player_count)
    players = players_generation(player_count, Player)

    print("Combien de manches dans cette partie ?")
    round_count = input_int(1, 10)

    for round in range(1, round_count+1): #loop for rounds
        pile = pile_generation(Domino)
        chain = []
        
        for player in players:
            player.draw(initial_draw)

        players_round = player_order(players)
        chain.append(get_biggest_domino(players_round[0].hand))

        cant_play = [False for i in range(player_count)]
        turn = 1 #on commence au deuxième joueur car le premier a déjà placé son domino
        while not all(cant_play): #loop for turns in round
            current_player = players_round[turn % player_count]
            if can_play(chain, current_player.hand):
                cant_play[turn%player_count] = False

            else:
                current_player.draw()
                if can_play(chain, current_player.hand):
                    continue
                else:
                    cant_play[turn%player_count] = True

            play(chain, current_player)

            if len(current_player.hand) == 0:
                print(f"{current_player.name} n'a plus de dominos, fin de la manche!")
                break
            print(f"Fin du tour de {current_player.name}")

        players = score_addition(players)
    break

print(range(7))