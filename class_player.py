import random as rdm
from domino_modules import *

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
                self.hand.append(ajout)
        else:
            self.can_play = False

        if n_time == 1:
            print(ajout)

        return pile
    
    def get_biggest_domino(self):
        biggest_domino_value = 0
        for domino in self.hand:
            current_domino_value = domino.total_value()
            if current_domino_value > biggest_domino_value:
                biggest_domino_value = current_domino_value
                biggest_domino = domino

        return biggest_domino

    def can_play(self, chain):
        chain_ends = [chain[0].left_face, chain[-1].right_face]
        # print(chain_ends)
        for domino in self.hand:
            if (str(domino.left_face) in str(chain_ends)) or (str(domino.right_face) in str(chain_ends)) or ("0" in str([domino.left_face,domino.right_face] + chain_ends)):
                return True
        return False
            

    def __repr__(self) -> str:
        return f"{self.name}; score actuel: {self.score}; main: {self.hand}"
