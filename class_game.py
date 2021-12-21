import random as rdm
from domino_modules import *
from class_player import *


class Game:
    def __init__(self) -> None:
        print("\n###################################### Début de la partie de domino ######################################\n")

        self.player_count = int(valid_input(list(range(2, 7)), "Quel est le nombre de joueurs ?: "))
        self.initial_draw = int(self.initial_draw_finder(self.player_count))
        self.players = self.players_generation(self.player_count, Player)
        self.round_count = int(valid_input(list(range(1,11)), "Combien de manches dans cette partie ?: "))

    def player_order(self, players):
        previous_biggest_domino_value = 0

        for player in players:
            biggest_domino_value = 0
            
            for domino in player.hand:
                current_domino_value = domino.total_value()
                if current_domino_value > biggest_domino_value:
                    biggest_domino_value = current_domino_value

            if biggest_domino_value > previous_biggest_domino_value:
                previous_biggest_domino_value = biggest_domino_value
                first_player = player

        players.insert(0, players.pop(players.index(first_player)))

        return players

    def players_generation(self, nb_player, Class):
        list_players = []

        for i in range(nb_player):
            list_players.append(Class(i+1))

        return list_players

    def pile_generation(self, Class):
        pile = []
        pile_str = []

        for i in range(7):
            for j in range(i, 7):
                pile.append(Class(i, j))

        return pile
        
    def initial_draw_finder(self, nb_player):
        if nb_player == 2:
            initial_draw = 7
        elif nb_player <= 4:
            initial_draw = 6
        elif nb_player <= 6:
            initial_draw = 4
        
        return initial_draw

    def score_addition(self, players):
        smallest_score = 0
        for player in players:
            player_round_score = 0
            
            for domino in player.hand:
                player_round_score += domino.total_value()

            player.score += player_round_score
            
            if player_round_score < smallest_score:
                smallest_score = player_round_score
                current_winner = player

            print(f"Score de {player.name}: {player.score}")

        return players, current_winner

    def play(self, chain, player):
        """
        chain: liste de classe Domino
        player: classe Player
        """
        
        print(f"Voici la chaîne: {chain}")
        print(f"voici votre main: {player.hand}, quel pièce voulez vous jouer ?")

        choosed_domino = player.hand[int(valid_input(list(range(1, len(player.hand)+1))))-1]
        print(choosed_domino)

        if choosed_domino.double != True:
            if valid_input(['G', 'D'], "Quel face ? ({}): ") == 'G':
                face = 'G'
                choosed_domino_face = choosed_domino.left_face
            else:
                face = 'D'
                choosed_domino_face = choosed_domino.right_face
            print(choosed_domino_face)
        else:
            choosed_domino_face = choosed_domino.left_face
            face = 'G'

        if valid_input(['Q', 'T'], "Le placer à quel fin ? {} Queue/Tête: ") == "Q":
            end = 0
            choosed_chain_face = chain[end].left_face
        else:
            end = -1
            choosed_chain_face = chain[end].right_face
        print(choosed_chain_face)
            
        if choosed_domino_face == choosed_chain_face or choosed_domino_face == 0 or choosed_chain_face == 0:
            player.hand.remove(choosed_domino)

            if (end == 0 and face == 'G') or (end == -1 and face == 'D'):
                choosed_domino = choosed_domino.swap_faces()

            if end == 0:
                chain.insert(end, choosed_domino)
            else:
                chain.append(choosed_domino)

            return chain, player
        else:
            print("Mouvement invalide!")
            self.play(chain, player)
