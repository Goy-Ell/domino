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
    while valid_input != None:
        initial_input = input()
        if isinstance(initial_input, int) and min <= initial_input <= max:
            valid_input = initial_input
        else:
            print(f"Entrée non valide, ré-entrer un chiffre supérieur ou égal à 2 svp")

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