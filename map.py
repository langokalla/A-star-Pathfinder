
class Map(object):

    def __init__(self, filename):
        self.filename = filename
        self.board = self.boardify_file(self.get_file(filename))
        self.h = len(self.board)
        self.w = len(self.board[0])
        self.cellh = 20
        self.cellw = 20

    @staticmethod
    def get_file(filename):
        f = open(filename)
        return f

    @staticmethod
    def boardify_file(file):
        lines = file.read().splitlines()
        return lines