import pygame
from pygame.locals import *
from interface import *
from morpion import *
from morpion_ia import *

#initialisation des variables
""""dimentions"""
dim_fenetre = [800, 650]  #0 --> x / 1 --> y
"""couleurs"""
gris = (161, 161, 161)
"""Strings"""
equality = "Egalité!"
red_win = "Rouge a gagné!"
yellow_win = "Jaune a gagné!"
"""TIMER"""
STEP = 1
"""other"""
first_turn = True
winner = "-"
check = False

# initialisation de pygame
pygame.init()

# initialisation de la fenetre
fenetre = pygame.display.set_mode((dim_fenetre[0], dim_fenetre[1]))
pygame.display.set_caption("fenetre type")  # nom de la fenetre

# morpion initialisation
mor = Morpion()

# ia initialisation
ia_second = Morpion_ia(mor.field, "O", "X")

# interface initialisation
gui = Interface(fenetre, dim_fenetre[0], dim_fenetre[1], mor.get_field())
gui.show()

# timer initialisation
pygame.time.set_timer(STEP, 1250)

"""font initialisation"""
font = pygame.font.Font(None, 100)

# rafraichissement de la fenetre
pygame.display.flip()

# boucle infinie
continuer = True  # si continuer vaut False, alors la boucle (et le programme) s'arrete(nt)
while continuer:

    # parcourir les evenements
    for event in pygame.event.get():

        # quitte l'app si on appuie sur la croix
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False

        if event.type == MOUSEBUTTONDOWN and event.button == 1 :# or event.type == KEYDOWN and event.key == K_SPACE:
            # update ia's fields
            ia_second.update_field(mor.get_field())

            slots = 0
            winner = mor.is_won()

            for s in mor.field:
                if s == "-":
                    slots +=1

            if not slots == 0 and winner == "-":
                if first_turn:
                    co = gui.which_pos(event.pos)  # co of the spot
                    if mor.get_field()[co[0] + co[1] * 3] == "-":
                        mor.add("X", co[0], co[1])
                        first_turn = not first_turn





            if not winner == "-" or winner == "-" and slots == 0:
                check = True



    if not first_turn:
        # update ia's fields
        ia_second.update_field(mor.get_field())

        slots = 0
        winner = mor.is_won()

        for s in mor.field:
            if s == "-":
                slots +=1
        if not slots == 0:
            mor.add_pos("O", ia_second.next_move())
            first_turn = not first_turn
        if not winner == "-" or winner == "-" and slots == 0:
            check = True

    if check:

        mor.reset_field()


        fenetre.fill((255, 0, 0))

        if winner == "O":
            text_win = font.render(yellow_win,1,(255,255,255))
            fenetre.fill(gui.colors[2])
        elif winner == "X":
            text_win = font.render(red_win,1,(255,255,255))
            fenetre.fill(gui.colors[3])
        else :
            text_win = font.render(equality,1,(255,255,255))
            fenetre.fill(gui.colors[0])

        fenetre.blit(text_win, (int(dim_fenetre[0]/2 - text_win.get_width()/2), 200))

        pygame.display.flip()
        # -------------------------------
        # mettre en pause lecran
        br = True
        while br :
            for e in pygame.event.get():
                if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE :
                    br = False
                    continuer = False
                if e.type == KEYDOWN or (e.type == MOUSEBUTTONDOWN) and (e.button == 1 or e.button == 3):
                    br = False
        check = False

    gui.update_field(mor.field)
    gui.show()
    #rafraichissement de la fenetre
    pygame.display.flip()
