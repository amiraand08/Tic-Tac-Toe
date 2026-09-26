
WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]


class TicTacToeGame:
    def __init__(self):
        self.board = []
        self.current_player = "X"
        self.winner = None
        self.reset()

    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None 

    def make_move(self, index):
        if self.winner is not None or self.board[index] != "":
            return False

        self.board[index] = self.current_player
        self.winner = self._check_winner()

        if self.winner is None:
            self.current_player = "O" if self.current_player == "X" else "X"

        return True

    def _check_winner(self):
        for a, b, c in WINNING_COMBOS:
            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if "" not in self.board:
            return "Tie"
        return None