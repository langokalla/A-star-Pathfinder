import tkinter as tk
from tile import Tile
from time import sleep
from map import Map
import os


class Board(object):

    def __init__(self, canvas, map):

        self.map = map

        self.canvas = canvas

        self.tiles = {}

        self.populate_tiles()

        self.draw_board()


    def populate_tiles(self):
        for r in range(self.map.h):
            for c in range(self.map.w):
                self.tiles[r, c] = Tile(self.map.board[r][c], r, c)

    def draw_board(self):
        for row in range(self.map.h):
            for col in range(self.map.w):
                self.draw_tile(self.tiles[row, col])
        self.canvas.pack()
        # self.canvas.update()

    def draw_tile(self, tile):
        self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill=tile.color, outline="white")

    def redraw(self, tile):
        self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill=tile.color, outline="white")
        self.canvas.update()

    def run_algorithm(self):
        while True:
            for cord, tile in self.tiles.items():
                tile.visit()
                if tile.is_end:
                    return
                self.canvas.after(50, self.redraw(tile))


if __name__ == '__main__':
    path = os.getcwd()

    root = tk.Tk()

    m = Map(path + '/boards/board-2-4.txt')
    c = tk.Canvas(root, width=m.w*m.cellw, height=m.h*m.cellh, bd=0, highlightthickness=0)
    b = Board(c, m)

    b.run_algorithm()

    root.mainloop()