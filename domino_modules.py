def test_domino(Class, random=True, l_f=None, r_f=None):
    if random == True:
        domino = Class()
    else:
        domino = Class(l_f, r_f)

    print("Domino: " + str(domino))
    print("Faces Swapped: " + str(domino.swap_faces()))
    print("Total Value: " + str(domino.total_value()))

    return "End"

def input_int(min, max):
    valid_input = None
    while valid_input != None:
        initial_input = input(f"Veuillez entrez un chiffre entre {min} et {max}")
        if isinstance(initial_input, int) and min <= initial_input <= max:
            valid_input = initial_input
        else:
            print(f"Entrée non valide, ré-entrer un chiffre entre {min} et {max} svp")

    return valid_input

def players_generation(nb_player, Class):
    list_players = []

    for i in range(nb_player):
        list_players.append(Class(i+1))

    return list_players

def pile_generation(Class):
    pile = []
    pile_str = []

    for i in range(7):
        for j in range(i, 7):
            pile.append(Class(i, j))

    return pile
    
def initial_draw_finder(nb_player):
    if nb_player == 2:
        initial_draw = 7
    elif nb_player <= 4:
        initial_draw = 6
    elif nb_player <= 6:
        initial_draw = 4
    
    return initial_draw

def score_addition(players):
    for player in players:
        round_score = 0
        for domino in player.hand:
            round_score += domino.total_value
        player.score += round_score

    return players

def player_order(players):
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

def get_biggest_domino(hand):
    for domino in hand:
        current_domino_value = domino.total_value()
        if current_domino_value > biggest_domino_value:
            biggest_domino_value = current_domino_value

    return biggest_domino_value

def can_play(hand, chain):
    for domino in hand:
        if (domino.left_face in str([chain[0], chain[-1]])) or (domino.right_face in str([chain[0], chain[-1]])) or (0 in [domino.left_face,domino.right_face]):
            return True
    print(f"Ne peut pas jouer! Pioche d'un domino:")
    return False
        
def valid_input(accepted_input, ask_sentence="Veuillez choisir une des réponses suivantes: {}: "):    
    user_input = input(ask_sentence.format(accepted_input))
    if user_input in accepted_input:
        return user_input
    else:
        print("Réponse invalide")
        valid_input(accepted_input, ask_sentence)

def play(chain, player):
    """
    chain: liste de classe Domino
    player: classe Player
    """
    
    print(f"Voici la chaîne: {chain}")
    print(f"voici votre main: {player.hand}, quel pièce voulez vous jouer ?")

    choosed_domino = player.hand[input_int(1, len(player.hand))]

    if valid_input(['G', 'D'], "Quel face ? ({})") == 'G':
        face = 'G'
        choosed_domino_face = choosed_domino.left_face
    else:
        face = 'D'
        choosed_domino_face = choosed_domino.right_face

    if valid_input(['Queue', 'Tête'], "Le placer à quel fin ? ({})") == "Queue":
        end = 0
        choosed_chain_face = chain[end].left_face
    else:
        end = -1
        choosed_chain_face = chain[end].right_face

    if choosed_domino_face == choosed_chain_face or choosed_domino_face == 0:
        if end == 0:
            chain.insert(end, choosed_domino)
        else:
            chain.append(choosed_domino)
        player.hand.remove(choosed_domino)
        return chain, player
    else:
        print("Mouvement invalide!")
        play(chain, player)

    