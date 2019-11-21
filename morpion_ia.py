from random import randint

class Morpion_ia():
    def __init__(self, field, tokken, u_tokken):
        self.field = field  #  self.field is the field that is in the ai memory
        self.tokken = tokken
        self.u_tokken = u_tokken  # the user's tokken

    def update_field(self, field):  # update the ai's field
        self.field = field

    def next_move(self):    # return the next move the ai will do
        move = 0            # move is the next move the ai will do
        available_spots = []  # a list of the availables spots

        i = 0
        for s in self.field:
            if s == "-":
                available_spots.append(i)
            i+= 1



        move = available_spots[randint(0, len(available_spots) - 1)]  # chose a random available spot

        # if the ai can take a corner, it will
        availables_corners = []
        if self.field[0] == "-":
            availables_corners.append(0)
        if self.field[2] == "-":
            availables_corners.append(2)
        if self.field[6] == "-":
            availables_corners.append(6)
        if self.field[8] == "-":
            availables_corners.append(8)

        if not len(availables_corners) == 0:
            move = availables_corners[randint(0, len(availables_corners) - 1)]

        # if the ai can take the center, it will
        if self.field[4] == "-":
            move = 4


        # ----------------------------------------
        # counter check -- can the ai prevent the user's win by placing a tokken in the field?
        """horizontal check"""
        i = 0
        while i < 3:
            if self.field[i * 3] == "-" and self.field[i*3 + 1] == self.field[i*3 + 2] == self.u_tokken:
                move = i * 3

            if self.field[i * 3 + 1] == "-" and self.field[i*3] == self.field[i*3 + 2] == self.u_tokken:
                move = i * 3 + 1

            if self.field[i * 3 + 2] == "-" and self.field[i*3] == self.field[i*3 + 1] == self.u_tokken:
                move = i * 3 + 2
            i+=1

        """vertical check"""
        i = 0
        while i < 3:
            if self.field[i] == "-" and self.field[i + 3] == self.field[i + 6] == self.u_tokken:
                move = i
            if self.field[i + 3] == "-" and self.field[i] == self.field[i + 6] == self.u_tokken:
                move = i + 3
            if self.field[i + 6] == "-" and self.field[i] == self.field[i + 3] == self.u_tokken:
                move = i + 6
            i +=1

        """horizontal check "\" """
        if self.field[0] == "-" and self.field[4] == self.field[8] == self.u_tokken:
            move = 0
        if self.field[4] == "-" and self.field[0] == self.field[8] == self.u_tokken:
            move = 4
        if self.field[8] == "-" and self.field[0] == self.field[4] == self.u_tokken:
            move = 8

        """horizontal check "/" """
        if self.field[2] == "-" and self.field[4] == self.field[6] == self.u_tokken:
            move = 2
        if self.field[4] == "-" and self.field[2] == self.field[6] == self.u_tokken:
            move = 4
        if self.field[6] == "-" and self.field[2] == self.field[4] == self.u_tokken:
            move = 6

        # ----------------------------------------
        # win check -- can the ai win with one move?
        """horizontal check"""
        i = 0
        while i < 3:
            if self.field[i * 3] == "-" and self.field[i*3 + 1] == self.field[i*3 + 2] == self.tokken:
                move = i * 3

            if self.field[i * 3 + 1] == "-" and self.field[i*3] == self.field[i*3 + 2] == self.tokken:
                move = i * 3 + 1

            if self.field[i * 3 + 2] == "-" and self.field[i*3] == self.field[i*3 + 1] == self.tokken:
                move = i * 3 + 2
            i+=1

        """vertical check"""
        i = 0
        while i < 3:
            if self.field[i] == "-" and self.field[i + 3] == self.field[i + 6] == self.tokken:
                move = i
            if self.field[i + 3] == "-" and self.field[i] == self.field[i + 6] == self.tokken:
                move = i + 3
            if self.field[i + 6] == "-" and self.field[i] == self.field[i + 3] == self.tokken:
                move = i + 6
            i +=1

        """horizontal check "\" """
        if self.field[0] == "-" and self.field[4] == self.field[8] == self.tokken:
            move = 0
        if self.field[4] == "-" and self.field[0] == self.field[8] == self.tokken:
            move = 4
        if self.field[8] == "-" and self.field[0] == self.field[4] == self.tokken:
            move = 8

        """horizontal check "/" """
        if self.field[2] == "-" and self.field[4] == self.field[6] == self.tokken:
            move = 2
        if self.field[4] == "-" and self.field[2] == self.field[6] == self.tokken:
            move = 4
        if self.field[6] == "-" and self.field[2] == self.field[4] == self.tokken:
            move = 6


        # ----------------------------------------
        return move  # move = position (0-8)
