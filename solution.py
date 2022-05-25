class Field:
    def __init__(self, x, y):
        self.field = [[Empty for i in range(x)] for i in range(y)]

    def get_field(self):
        return self.field

    def create_cell(self, x, y):
        self.field[y][x] = Cell()

    def near(self, x, y):
        counter = 0
        for ypos in range(y - 1, y + 2):
            for xpos in range(x - 1, x + 2):
                try:
                    # print(self.field[ypos][xpos].char(), xpos+1, ypos+1)
                    if self.field[ypos][xpos].char() == 'R':
                        counter += 1
                except:
                    pass
        return counter - 1


class Cell:
    def __init__(self):
        self.alive = True

    def is_alive(self):
        return self.alive

    def char(self):
        if self.is_alive():
            return "R"
        return "X"


class Empty:
    @staticmethod
    def char():
        return 'O'