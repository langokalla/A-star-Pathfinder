import tkinter as tk
from tile import Tile
from map import Map
import os


class Board(object):

    """
    Board object.
    Has a tkinter.canvas to draw cells on.
    This is where we'll run our algorithms.
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

        self.populate_tiles()
        self.draw_board()

    def populate_tiles(self):
        """
        Runs throug all possible cell coordinates of the board and makes a Tile and puts it in the tile dictionary.
        :return: None
        """
        for r in range(self.map.h):
            for c in range(self.map.w):
                self.tiles[r, c] = Tile(self.map.board[r][c], r, c)
        return

    def draw_board(self):
        """
        Draws the first board setup. Iterates through the board grid, and draws the corresponding
        tiles to the right location.
        :return: None
        """
        for row in range(self.map.h):
            for col in range(self.map.w):
                self.draw_tile(self.tiles[row, col])
        self.canvas.pack()
        # self.canvas.update()
        return

    def draw_tile(self, tile):
        """
        Draws the tile in its location on the board.
        :param tile: Tile object
        :return: None
        """
        self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill=tile.color, outline="white")
        return

    def redraw(self, tile):
        """
        The update function. Re-draws a tile. Only called if a tile may be visited, and changed color.
        :param tile: Tile object.
        :return: None
        """
        self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill=tile.color, outline="white")
        self.canvas.update()
        return

    def run_algorithm(self, start_tile, end_tile):
        """
        The algorithm we are gonna run. BFS, Dijkstra, DFS etc.
        :param start_tile: Start node. Tile object.
        :param end_tile: Goal node. Tile object.
        :return: None
        """
        start_tile = self.tiles[start_tile]
        end_tile = self.tiles[end_tile]

        while True:
            for cord, tile in self.tiles.items():
                tile.visit()
                print(end_tile)
                self.canvas.after(50, self.redraw(tile))
                if end_tile.visited:
                    return


if __name__ == '__main__':
    path = os.getcwd()

    root = tk.Tk()

    m = Map(path + '/boards/board-2-4.txt')

    c = tk.Canvas(root, width=m.w*m.cellw, height=m.h*m.cellh, bd=0, highlightthickness=0)

    b = Board(c, m)

    b.run_algorithm(m.start, m.end)

    root.mainloop()
