class Morpion(object):
    def __init__(self):

        self.field = [  # "-" = free, "O" = circle, "X" = cross
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
        ]
    # -------------------------------------------------------------------------
    
    def print_field(self):  # print the field in the terminal
        i = 0
        while i < 3:
            print(self.field[i * 3] +" "+  self.field[i * 3 + 1] +" "+ self.field[i * 3 + 2])
            i+=1
    
    def get_field(self):
        return self.field

    def add(self, c, x, y):  # the case at x, y is replace by c ("X" or "O")
        self.field[x + y * 3] = c
    
    def add_pos(self, c, pos):# the case at the index pos is replace by c ("X" or "O")
        self.field[pos] = c
    
    def reset_field(self):  
        self.field = []
        i = 0
        while i < 9:
            self.field.append("-")
            i +=1

    def is_won(self):
        # horizontal check
        i = 0
        while i < 3:
            if not self.field[i * 3] == "-" and self.field[i * 3] == self.field[i * 3 + 1] == self.field[i * 3 + 2]:
                return self.field[i * 3]
            i +=1
        
        # vertical check
        i = 0
        while i < 3:
            if not self.field[i] == "-" and self.field[i] == self.field[i + 3] == self.field[i + 6]:
                return self.field[i]
            i +=1
        
        # horizontal check \
        
        if not self.field[0] == "-" and self.field[0] == self.field[4] == self.field[8]:
            return self.field[0]
            
        # horizontal check /
        
        if not self.field[2] == "-" and self.field[2] == self.field[4] == self.field[6]:
            return self.field[2]
        
        return "-"
