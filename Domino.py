import random as rdm
from domino_modules import *
from class_domino import *
from class_player import *
from class_game import *

playing = True
while playing == True:
    game = Game()
    for round in range(1, game.round_count+1): #loop for rounds
        print(f"\n################## Manche {round} ##################\n")
        pile = game.pile_generation(Domino)
        # print(pile)
        chain = []
        
        for player in game.players:
            pile = player.draw(pile, game.initial_draw)

        players_round = game.player_order(game.players)
        print(f"Ordre: {[player.name for player in players_round]}\n")
        chain.append(players_round[0].get_biggest_domino())

        cant_play = [False for i in range(game.player_count)]
        turn = 1 #on commence au deuxième joueur car le premier a déjà placé son domino
        while not all(cant_play): #loop for turns in round
            num_joueur = turn % game.player_count
            current_player = players_round[num_joueur]
            print(f"Début du tour de {current_player.name}")

            if current_player.can_play(chain):
                cant_play[num_joueur] = False
            else:
                print(f"Ne peut pas jouer! Pioche d'un domino:")
                pile = current_player.draw(pile)
                if current_player.can_play(chain) != True:
                    print(f"Ne peut toujours pas jouer, tour passé!")
                    cant_play[num_joueur] = True
                    turn += 1
                    continue
            
            game.play(chain, current_player)

            if len(current_player.hand) == 0:
                print(f"\n{current_player.name} n'a plus de dominos, fin de la manche!")
                break

            print(cant_play)
            print(f"\nFin du tour de {current_player.name}\n")
            turn += 1

        game.players, current_winner = game.score_addition(game.players)
    
    print(f"\n\n########################################### {current_winner.name} remporte la partie avec {current_winner.score} points! ###########################################\n\n")

    if valid_input(["y", "n"], "Rejouer ? {}: ") == "n":
        playing == False

