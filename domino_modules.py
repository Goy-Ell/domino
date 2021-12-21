def test_domino(Class, random=True, l_f=None, r_f=None):
    if random == True:
        domino = Class()
    else:
        domino = Class(l_f, r_f)

    print("Domino: " + str(domino))
    print("Faces Swapped: " + str(domino.swap_faces()))
    print("Total Value: " + str(domino.total_value()))

    return "End"

# def get_biggest_domino(hand):
#     biggest_domino_value = 0
#     for domino in hand:
#         current_domino_value = domino.total_value()
#         if current_domino_value > biggest_domino_value:
#             biggest_domino_value = current_domino_value
#             biggest_domino = domino

#     return biggest_domino

# def can_play(hand, chain):
#     chain_ends = [chain[0].left_face, chain[-1].right_face]
#     # print(chain_ends)
#     for domino in hand:
#         if (str(domino.left_face) in str(chain_ends)) or (str(domino.right_face) in str(chain_ends)) or ("0" in str([domino.left_face,domino.right_face] + chain_ends)):
#             return True
#     return False
        
def valid_input(accepted_inputs, ask_sentence="Veuillez choisir une des réponses suivantes: {}: "):    
    user_input = input(ask_sentence.format(accepted_inputs))
    if (len(user_input) > 0) and (type(user_input) != None) and (user_input in str(accepted_inputs)):
        return user_input
    else:
        print("Réponse invalide")
        valid_input(accepted_inputs, ask_sentence)

