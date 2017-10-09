import tkinter as tk
import os

from board import Board
from map import Map


class App:

    def __init__(self):
        pass

    def run(self):
        level = '1-2'
        path = os.getcwd()

        # Make a root tkinter object and title it.
        root = tk.Tk()
        root.title('ALGIRITHMIS N SHITE: ' + level)
        # Make a map object to read the map file from level path.
        m = Map(path + '/boards/board-' + level + '.txt')

        # Make a canvas with correct width and height.
        # Make the board on the canvas with the current map.
        c = tk.Canvas(root, width=m.w * m.cell_size, height=m.h * m.cell_size, bd=0, highlightthickness=0)
        b = Board(c, m)

        # Run whichever algoritm is gonna run.
        b.run_algorithm("a")

        # tkinter mainloop
        root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()

