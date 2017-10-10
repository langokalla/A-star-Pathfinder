import tkinter as tk
import os

from board import Board
from map import Map


class App:

    """
    The main app. Makes tkinter objects and runs an algorithm.
    """

    def __init__(self):
        pass

    def run(self, algo, level):
        """
        Runs the algorithm algo on the level level.
        :param algo: String ("bfs", "d" or "d").
        :param level: String ("1-1", "1-2", "1-3" etc.)
        :return: None
        """

        root = tk.Tk()

        if algo == "bfs":
            title = 'Breadth First Search: ' + level + '.'
            root.title('Breadth First Search: ' + level + '.')
        elif algo == "d":
            title = 'Dijkstra: ' + level + '.'
            root.title(title)
        elif algo == "a":
            title = 'A* Pathfinder: ' + level + '.'
            root.title(title)

        # Make a map object to read the map file from level path.
        path = os.getcwd()
        m = Map(path + '/boards/board-' + level + '.txt')

        # Make a canvas with correct width and height.
        # Make the board on the canvas with the current map.
        c = tk.Canvas(root, width=m.w * m.cell_size, height=m.h * m.cell_size, bd=0, highlightthickness=0)
        b = Board(c, m)

        # Run whichever algoritm is gonna run, set window on top.
        root.attributes("-topmost", True)
        cost = b.run_algorithm(algo)
        root.title(self.change_title(root, cost, algo, title))
        root.attributes('-topmost', False)

        # tkinter mainloop
        root.mainloop()
        return

    @staticmethod
    def change_title(root, cost, algo, temp_title):
        """
        Changes the title of the root window.
        :param root: Root tkinter
        :param cost: Path cost, int.
        :param algo: Algorithm, String.
        :param temp_title: The current title, String.
        :return: new title String
        """
        title = temp_title + " Cost: " + str(cost) + "."
        return title


if __name__ == '__main__':
    app = App()
    app.run("d", "2-4")

