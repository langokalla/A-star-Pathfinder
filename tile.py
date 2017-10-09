import math


class Tile(object):

    """
    The Tile object. Can be interpreted as a node in the structure.
    Includes positional values and weighted values as colors.
    Can be visited and not visited (bool).
    Can be the end if the node is the goal tile (bool).
    """

    def __init__(self, char, r, c):
        """
        Initializes the tile node.
        :param char: Fetched from the .txt-map. Determines the weighted value.
        :param r: Row location.
        :param c: Column location

        Sets visited and is_end to False, except the end node B.
        """

        self.visited = False
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

            if char == 'B' or char == 'A':
                self.is_end = True
            else:
                self.is_end = False

    def visit(self):
        """
        Sets a tiles visit value to True. Start tile just keeps it's color.
        :return: None
        """
        if self.char != 'A':
            self.color = "grey"
        self.visited = True
        return

    def __str__(self):
        """
        toString method.
        :return: The tiles information as string.
        """
        return 'Color=' + self.color + '\t' + 'Weight=' + str(self.weight) + '\t' + str(self.visited)
