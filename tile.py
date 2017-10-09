import math


class Tile(object):

    def __init__(self, char, r, c):

        self.visited = False
        self.is_end = False
        self.char = char
        self.r = r
        self.c = c

        self.x1 = self.c * 20
        self.x2 = self.x1 + 20
        self.y1 = self.r * 20
        self.y2 = self.y1 + 20

        if char in ['r', 'g', 'f', 'm', 'w', '.', '#', 'A', 'B']:
            self.weight = {'r': 1,
                           'g': 5,
                           'f': 10,
                           'm': 50,
                           'w': 100,
                           '.': 0,
                           '#': math.inf,
                           'A': 0,
                           'B': 0}[char]

            self.color = {'r': '#fdd692',
                          'g': '#cbe079',
                          'f': '#69c13f',
                          'm': '#754f44',
                          'w': '#5bc0eb',
                          '.': '#cbe079',
                          '#': '#754f44',
                          'A': 'red',
                          'B': 'blue'}[char]

            if char == 'B':
                self.is_end = True

    def visit(self):
        if self.char != 'A':
            self.color = "grey"
        self.visited = True

    def __str__(self):
        return 'Color=' + self.color + '\t' + 'Weight=' + str(self.weight) + '\t' + str(self.visited)
