from bfs import bfs
from dijkstra import dijkstra
from a_star import *
from tile import Tile

from time import sleep


class Board(object):

    """
    Board object.
    Has a tkinter.canvas to draw tiles (cells) on.
    This is where the algorithm runs.
    """

    def __init__(self, canvas, map):
        """
        Initalizes the Board object. Takes a tk.canvas and a  Map object.
        Stores the tiles in a tiles dictionary where the (row, col) is the key to the tile.
        Populates the board with tiles and draws the board.
        :param canvas: tkinter.canvas
        :param map: Map
        """
        self.map = map
        self.canvas = canvas

        self.tiles = {}
        self.tiles_list = []

        self.start = None
        self.end = None

        self.populate_tiles()
        self.map_neighbours()
        self.draw_board()

    def map_neighbours(self):
        """
        Each tile receives its adjecent neighbours.
        A bit of redundent code here.
        These neighbour lists is the "graph" we traverse in the algorithms.
        :return: None
        """
        for key, tile in self.tiles.items():
            r, c = key

            # Top left corner.
            if r == 0 and c == 0:
                self.add_neighbours(tile, self.tiles[r+1, c])       # Under
                self.add_neighbours(tile, self.tiles[r, c+1])       # Right

            # Top right corner.
            elif r == 0 and c == self.map.w-1:
                self.add_neighbours(tile, self.tiles[r, c-1])       # Left
                self.add_neighbours(tile, self.tiles[r+1, c])       # Under

            # Bottom left corner.
            elif r == self.map.h-1 and c == 0:
                self.add_neighbours(tile, self.tiles[r - 1, c])     # Over
                self.add_neighbours(tile, self.tiles[r, c + 1])     # Right

            # Bottom right corner.
            elif r == self.map.h-1 and c == self.map.w-1:
                self.add_neighbours(tile, self.tiles[r - 1, c])     # Over
                self.add_neighbours(tile, self.tiles[r, c - 1])     # Left

            # Top border.
            elif r == 0:
                self.add_neighbours(tile, self.tiles[r + 1, c])     # Under
                self.add_neighbours(tile, self.tiles[r, c + 1])     # Right

            # Right border.
            elif c == self.map.w-1:
                self.add_neighbours(tile, self.tiles[r + 1, c])     # Under
                self.add_neighbours(tile, self.tiles[r - 1, c])     # Over
                self.add_neighbours(tile, self.tiles[r, c - 1])     # Left

            # Bottom border.
            elif r == self.map.h-1:
                self.add_neighbours(tile, self.tiles[r - 1, c])     # Over
                self.add_neighbours(tile, self.tiles[r, c - 1])     # Left
                self.add_neighbours(tile, self.tiles[r, c + 1])     # Right

            # Left border.
            elif c == 0:
                self.add_neighbours(tile, self.tiles[r - 1, c])     # Over
                self.add_neighbours(tile, self.tiles[r + 1, c])     # Under
                self.add_neighbours(tile, self.tiles[r, c + 1])     # Right

            # Elsewhere in the map.
            else:
                self.add_neighbours(tile, self.tiles[r - 1, c])     # Over
                self.add_neighbours(tile, self.tiles[r + 1, c])     # Under
                self.add_neighbours(tile, self.tiles[r, c + 1])     # Right
                self.add_neighbours(tile, self.tiles[r, c - 1])     # Left
        return

    def add_neighbours(self, tile1, tile2):
        """
        Helper method for the map_neighbours. Adds a tile2 to tile1's neighbours and vica versa.
        :param tile1: Tile
        :param tile2: Tile
        :return: None
        """
        if tile2.char != '#':
            if tile2 not in tile1.neighbours:
                tile1.neighbours.append(tile2)
        if tile1.char != '#':
            if tile1 not in tile2.neighbours:
                tile2.neighbours.append(tile1)
        return

    def populate_tiles(self):
        """
        Runs throug all possible cell coordinates of the board and makes a Tile and puts it in the tile dictionary.
        :return: None
        """
        size = self.map.cell_size
        for r in range(self.map.h):                         # Iterates through the whole map.
            for c in range(self.map.w):
                t = Tile(self.map.board[r][c], r, c, size)  # Makes a tile.
                if t.char == 'A':                           # If the tile is a start tile or
                    self.start = t                          # a end tile, set it accordingly.
                elif t.char == 'B':
                    self.end = t

                self.tiles[r, c] = t                        # Put the tile in a dictionary with
                self.tiles_list.append(t)                   # coord as keys. Also append in list.
        return

    def draw_board(self):
        """
        Draws the first board setup. Iterates through the board grid, and draws the corresponding
        tiles to the right location.
        :return: None
        """
        for row in range(self.map.h):                           # Iterate through the whole map.
            for col in range(self.map.w):
                t = self.tiles[row, col]
                self.draw_tile(t, t.color, "white")             # Draw the tile.
        self.canvas.pack()                                      # Pack the canvas.
        # self.canvas.update()
        return

    def draw_tile(self, tile, color, outline):
        """
        Draws the tile in its location on the board.
        :param tile: Tile object
        :param color: String color.
        :param outline: String color.
        :return: None
        """
        self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill=color, outline=outline)
        self.canvas.update()
        return

    def redraw_oval(self, tile, color, outline):
        """
        The update function. Re-draws a tile. Only called if a tile may be visited, and changed color.
        :param tile: Tile object.
        :param color: String color.
        :param outline: String color.
        :return: None
        """                                                 # Px is pixel offset. Calculates a new
        px = 0.35*self.map.cell_size                        # centered oval to draw. Not draw on start/end.
        if tile != self.start and tile != self.end:
            self.canvas.create_oval(tile.x1 + px, tile.y1 + px, tile.x2 - px, tile.y2 - px, fill=color, outline=outline)
            self.canvas.update()
        return

    def run_algorithm(self, algo):
        """
        The algorithm we are gonna run. BFS, Dijkstra, DFS etc.
        :param start_tile: Start node. Tile object.
        :param end_tile: Goal node. Tile object.
        :return: int total cost
        """
        if algo == "bfs":
            (cf, suc, hbn) = bfs(self.start, self.end)                  # Sets all necessary lists and
            path = reconstruct_path(cf, self.start, self.end)           # and dictionaries for bfs,
            cost = 0                                                    # and sums the total cost of the
            for tile in path:                                           # calculated path.
                cost += tile.weight
            print("Total cost: ", cost)

        elif algo == "d":
            (cf, csf, suc, hbn) = dijkstra(self.start, self.end)        # Sets all necessary lists and
            path = reconstruct_path(cf, self.start, self.end)           # and dictionaries for dijkstra,
            cost = csf[self.end]                                        # and sums the total cost of the
            print("Total cost: ", cost)                                 # calculated path.
        elif algo == "a":
            (cf, csf, suc, hbn) = a_star(self.start, self.end)          # Sets all necessary lists and
            cost = csf[self.end]                                        # and dictionaries for a* pathinder,
            print("Total cost: ", cost)                                 # and sums the total cost of the
            path = reconstruct_path(cf, self.start, self.end)           # calculated path.

        if suc:                                                         # Only if the end was found (success).
            for tile, came_from in cf.items():                          # Iterate through visited tiles,
                if came_from is None:                                   # from end to start.
                    pass
                else:
                    if tile.char == 'B':
                        break
                    if tile.char != 'A' and tile.char != 'B' and not tile.visited:
                        pass
                    else:                                               # Draw the visited tile
                        self.canvas.after(25, self.draw_tile(tile, tile.color_visited, 'black'))

            for tile in hbn:                                            # Draw tiles that has been considered
                if tile.char != 'A' and tile.char != 'B' and not tile.visited:  # visited, but visited.
                    self.canvas.after(25, self.redraw_oval(tile, "#999", "black"))

            for tile in path:                                           # Draw the calculated path.
                self.canvas.after(25, self.redraw_oval(tile, "black", "black"))

            """
                                                                        # Draw the calculated path reversed.
            current = cf[self.end]
            while current != self.start:
                self.canvas.after(25, self.redraw_oval(current, "black", "black"))
                current = cf[current]
            """
            return cost
