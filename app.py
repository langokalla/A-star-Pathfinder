import tkinter as tk
from tkinter.ttk import Separator, Style
import os

from board import Board
from map import Map


class safe:  # the decorator

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        try:
            return self.function(*args)
        except Exception as e:
            # make a popup here with your exception information.
            # might want to use traceback module to parse the exception info
            print("Error: %s" % (e))


class App:

    """
    The main app. Makes tkinter objects and runs an algorithm.
    """

    def __init__(self):
        self.algo = None
        self.level = None

    def set_algo(self, algo):
        self.algo = algo

    def set_level(self, level):
        self.level = level

    def main_menu(self):
        root = tk.Tk()
        root.title("Pathfinding")

        left = tk.Frame(root, bg="#b3b3b6", width=200, height=200)
        left.pack_propagate(False)
        tk.Label(left, text="1: Choose algorthm.", fg="black", bg="#b3b3b6", anchor="center", justify="center").pack()
        left.grid(column=0, row=0, pady=5, padx=10, sticky="n")

        sepl = Separator(root, orient="vertical")
        sepl.grid(column=1, row=0, sticky="ns")

        sty = Style(root)
        sty.configure("TSeparator", background="#eaeaef")

        center = tk.Frame(root, bg="#b3b3b6", width=200, height=200)
        center.pack_propagate(False)
        tk.Label(center, text="2: Choose level.", fg="black", bg="#b3b3b6").pack()
        center.grid(column=2, row=0, pady=5, padx=10, sticky="n")

        sepr = Separator(root, orient="vertical")
        sepr.grid(column=3, row=0, sticky="ns")


        bfs_button = tk.Button(left, text="Breadth First Search", bg="#D6AA5B", command=lambda *args: self.set_algo("bfs"),
                               width=15)
        bfs_button.grid(row=0, column=0)

        d_button = tk.Button(left, text="Dijkstra", command=lambda *args: self.set_algo("d"), width=15)
        d_button.grid(row=1, column=0)

        a_button = tk.Button(left, text="A* Pathfinder", command=lambda *args: self.set_algo("a"), width=15)
        a_button.grid(row=2, column=0)



        level11_button = tk.Button(center, text="1-1", command=lambda *args: self.set_level("1-1"))
        level11_button.grid(row=0, column=0)

        level12_button = tk.Button(center, text="1-2", command=lambda *args: self.set_level("1-2"))
        level12_button.grid(row=1, column=0)

        level13_button = tk.Button(center, text="1-3", command=lambda *args: self.set_level("1-3"))
        level13_button.grid(row=2, column=0)

        level14_button = tk.Button(center, text="1-4", command=lambda *args: self.set_level("1-4"))
        level14_button.grid(row=3, column=0)

        level21_button = tk.Button(center, text="2-1", command=lambda *args: self.set_level("2-1"))
        level21_button.grid(row=0, column=1)

        level22_button = tk.Button(center, text="2-2", command=lambda *args: self.set_level("2-2"))
        level22_button.grid(row=1, column=1)

        level23_button = tk.Button(center, text="2-3", command=lambda *args: self.set_level("2-3"))
        level23_button.grid(row=2, column=1)

        level24_button = tk.Button(center, text="2-4", command=lambda *args: self.set_level("2-4"))
        level24_button.grid(row=3, column=1)

        execute_button = tk.Button(root, text="Run!", bg="green", command=lambda *args: self.run(self.algo, self.level))
        execute_button.grid(row=0, column=4, padx=5)

        root.mainloop()

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
    #app.run("d", "2-4")
    app.main_menu()

