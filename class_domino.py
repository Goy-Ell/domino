import random as rdm
from domino_modules import *

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
