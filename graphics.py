import tkinter as tk


class Board(object):

    def __init__(self, filename):
        self.filename = filename
        self.board = self.boardify_file(self.get_file(filename))
        self.h = len(self.board)
        self.w = len(self.board[0])

    @staticmethod
    def get_file(filename):
        f = open(filename)
        return f

    @staticmethod
    def boardify_file(file):
        lines = file.read().splitlines()
        return lines


b = Board('/Users/martin/PycharmProjects/intro_ai/A* Pathfinder/boards/board-1-1.txt')
print(b.h)
print(b.w)


class Grid(object):

    def __init__(self, board):
        self.h = board.h
        self.w = board.w

        root = tk.Tk()
        self.c =


    def create_grid(self):
        c.delete
        for i in range(0, self.w, 100):
            c.create('grid_line')

"""
def create_grid(event=None):
    w = c.winfo_width()  # Get current width of canvas
    h = c.winfo_height()  # Get current height of canvas
    c.delete('grid_line')  # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line')



root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)

root.mainloop()
"""
