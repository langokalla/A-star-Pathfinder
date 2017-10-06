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

    def visualize_board(self):
        root = tk.Tk()

        for r in range(self.h):
            for c in range(self.w):
                tk.Canvas(root, bg='grey', height=40, width=40, bd=7, highlightthickness=1).grid(row=r, column=c)

        root.mainloop()


b = Board('boards/board-1-1.txt')
b.visualize_board()
