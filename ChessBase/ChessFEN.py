figures = {'r': 5, 'n': 3, 'b': 3, 'k': 4, 'q': 9, 'p': 1, 'R': 5, 'N': 3, 'B': 3, 'K': 4, 'Q': 9, 'P': 1}


def get_neighbours(king_pos):
    neighbours = []
    left_figure = chr(ord(king_pos[0]) - 1) + king_pos[1]
    right_figure = chr(ord(king_pos[0]) + 1) + king_pos[1]
    up_figure = king_pos[0] + str(int(king_pos[1]) + 1)
    down_figure = king_pos[0] + str(int(king_pos[1]) - 1)
    up_left_figure = chr(ord(king_pos[0]) - 1) + str(int(king_pos[1]) + 1)
    up_right_figure = chr(ord(king_pos[0]) + 1) + str(int(king_pos[1]) + 1)
    down_left_figure = chr(ord(king_pos[0]) - 1) + str(int(king_pos[1]) - 1)
    down_right_figure = chr(ord(king_pos[0]) + 1) + str(int(king_pos[1]) - 1)
    if king_pos == 'A1':
        neighbours.extend([up_figure, up_right_figure, right_figure])
    elif king_pos == 'A8':
        neighbours.extend([right_figure, down_right_figure, down_figure])
    elif king_pos == 'H8':
        neighbours.extend([left_figure, down_left_figure, down_figure])
    elif king_pos == 'H1':
        neighbours.extend([up_figure, up_left_figure, left_figure])
    elif king_pos[1] == '1':
        neighbours.extend([up_figure, up_left_figure, left_figure, up_right_figure, right_figure])
    elif king_pos[1] == '8':
        neighbours.extend([down_figure, down_right_figure, down_left_figure, left_figure, right_figure])
    else:
        neighbours.extend(
            [down_figure, down_right_figure, down_left_figure, left_figure, right_figure, up_figure, up_left_figure,
             up_right_figure])
    return neighbours


class ChessException(Exception):
    pass


class ChessScore:
    def __init__(self, figure_list):
        self.figure_list = figure_list

    def __int__(self):
        points = 0
        for el in self.figure_list:
            if el in figures:
                points += figures[el]
        return points

    def __add__(self, other):
        return int(self.figure_list) + int(other.figure_list)

    def __sub__(self, other):
        return int(self.figure_list) - int(other.figure_list)

    def __lt__(self, other):
        return int(self.figure_list) < int(other.figure_list)

    def __le__(self, other):
        return int(self.figure_list) <= int(other.figure_list)

    def __eq__(self, other):
        return int(self.figure_list) == int(other.figure_list)

    def __ne__(self, other):
        return int(self.figure_list) != int(other.figure_list)

    def __gt__(self, other):
        return int(self.figure_list) > int(other.figure_list)

    def __ge__(self, other):
        return int(self.figure_list) >= int(other.figure_list)


class ChessPosition:

    def __init__(self, def_str):
        self.def_str = def_str
        self._rows = self.def_str.split('/')
        white_king = 0
        black_king = 0
        for row in self._rows:
            for char in row:
                if char == 'k':
                    white_king += 1
                    king_pos = chr(ord('@')+row.find(char) + 1) + str(self._rows.index(row) + 1)
                    neighbour_fig = get_neighbours(king_pos)
                    if white_king != 1 or white_king != 1:
                        raise ChessException("kings")
                    for fig in neighbour_fig:
                        if self.position(fig) == 'K':
                            raise ChessException("kings")
                elif char == 'K':
                    black_king += 1
                    king_pos = chr(ord('@') + row.find(char) + 1) + str(self._rows.index(row) + 1)
                    neighbour_figs = get_neighbours(king_pos)
                    for figure in neighbour_figs:
                        if self.position(figure) == 'k':
                            raise ChessException("kings")
                    if black_king != 1 or black_king != 1:
                        raise ChessException("kings")
                elif char == 'p' or char == 'P':
                    pawn_row = self._rows.index(row) + 1
                    if pawn_row == 1 or pawn_row == 8:
                        raise ChessException("pawns")

    def print(self):
        print(self.def_str)

    def get_white_score(self):
        all_whites = []
        for row in self._rows:
            for char in row:
                if char.isupper():
                    all_whites.append(char)
        return ChessScore.__int__(ChessScore(all_whites))

    def get_black_score(self):
        all_black = []
        for row in self._rows:
            for char in row:
                if char.islower():
                    all_black.append(char)
        return ChessScore.__int__(ChessScore(all_black))

    def white_is_winning(self):
        return self.get_white_score() > self.get_black_score()

    def black_is_winning(self):
        return self.get_white_score() < self.get_black_score()

    def is_equal(self):
        return self.get_white_score() == self.get_black_score()

    def position(self, pos_check):
        column = ord(pos_check[0]) - 65
        row = int(pos_check[1]) - 1
        if column < len(self._rows[row]):
            if self._rows[row][column].isdigit():
                return None
            else:
                return (self._rows[row])[column]
        else:
            return None

    def len(self):
        figure_count = 0
        for row in self._rows:
            for char in row:
                if char.isalpha():
                    figure_count += 1
        return figure_count
