import pygame

class Interface(pygame.Surface):
    """docstring for Interface."""

    def __init__(self, window, width, height, field):
        super().__init__((width, height))
        self.window = window
        self.field = field
        self.width = width
        self.height = height

        self.colors = [ # blue, grey, yellow, red
             (30, 98, 224), (220, 220, 220),
             (230, 255, 18), (183, 0, 0)
        ]

        self.marge = 40

    def update_field(self, field):
        self.field = field
    
    def which_pos(self, position):  # get the mouse x and y and return the column and the line coresponding
        return [int(position[0]/(self.width/3)), int(position[1]/(self.height/3))]

    def show(self):
        # TODO: mettre les composants graphique
        self.fill(self.colors[0])
        div_x = int(self.width / 3)
        div_y = int(self.height / 3)

        rad = int((div_x)/2 - self.marge)

        loc_x = int(div_x/2)
        loc_y = int(div_y/2)

        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if self.field[i*3 + j] == "-":
                    pygame.draw.circle(self, self.colors[1], (int(div_x * j + loc_x), int(div_y * i + loc_y)), rad)

                if self.field[i*3 + j] == "X":
                    pygame.draw.circle(self, self.colors[3], (int(div_x * j + loc_x), int(div_y * i + loc_y)), rad)

                if self.field[i*3 + j] == "O":
                    pygame.draw.circle(self, self.colors[2], (int(div_x * j + loc_x), int(div_y * i + loc_y)), rad)
                j+=1
            i+=1


        
        self.window.blit(self, (0, 0))
