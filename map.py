
class Map(object):

    """
    Map object. Fetches the map from .txt file. Renders it to a listed list.
    """

    def __init__(self, filename):
        """
        Initialization. Stores filename. Makes the listed list (board) out of the .txt file.
        Stores height and width of the map in terms of cells, as well as the cells height and width in px.
        :param filename: Path to file (string).
        """
        self.filename = filename
        self.board = self.boardify_file(self.get_file(filename))
        self.h = len(self.board)
        self.w = len(self.board[0])
        self.cell_size = 30

    @staticmethod
    def get_file(filename):
        """
        Opens map .txt file.
        :param filename:
        :return: opened file.
        """
        f = open(filename)
        return f

    @staticmethod
    def boardify_file(file):
        """
        Takes file and split its lines in a list.
        :param file: map file
        :return: listed list
        """
        lines = file.read().splitlines()
        file.close()
        return lines
