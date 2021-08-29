import io
import os
import sys
import tempfile

BLACK, WHITE = ('BLACK', 'WHITE')

# コンソール
if sys.platform.startswith('win'):
    def console(char, background):
        return char or ""
    sys.stdout = io.StringIO()
else:
    def console(char, background):
        return "\x1B{}m{}\x1B[0m".format(
            43 if background == BLACK else 47, char or "")


# ピースの基底クラス
class Piece(str):
    __slots__ = ()


# BlackDraught
class BlackDraught(Piece):
    __slots__ = ()
    
    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "black draught man")
        self = "●"
        return self

# WhiteDraught
class WhiteDraught(Piece):
    __slots__ = ()
    
    def __new__(cls):
        self =  super().__new__(cls)
        # print('__new__', "white draught man")
        self = "○"
        return self

# BlackChessKing
class BlackChessKing(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "BlackChessKing")
        self = "(BK)"
        return self

# WhiteChessKing
class WhiteChessKing(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "WhiteChessKing")
        self = "(WK)"
        return self

# BlackChessQueen
class BlackChessQueen(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "BlackChessQueen")
        self = "(BQ)"
        return self

# WhiteChessQueen
class WhiteChessQueen(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "WhiteChessQueen")
        self = "(WQ)"
        return self

# BlackChessRook
class BlackChessRook(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "BlackChessRook")
        self = "(BR)"
        return self

# WhiteChessRook
class WhiteChessRook(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "WhiteChessRook")
        self = "(WR)"
        return self

# BlackChessBishop
class BlackChessBishop(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "BlackChessBishop")
        self = "(BB)"
        return self

# WhiteChessBishop
class WhiteChessBishop(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "WhiteChessBishop")
        self = "(WB)"
        return self

# BlackChessKnight
class BlackChessKnight(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "BlackChessKnight")
        self = "(BKN)"
        return self

# WhiteChessKnight
class WhiteChessKnight(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "WhiteChessKnight")
        self = "(WKN)"
        return self

# BlackChessPawn
class BlackChessPawn(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "BlackChessPawn")
        self = "(BP)"
        return self

# WhiteChessPawn
class WhiteChessPawn(Piece):

    __slots__ = ()

    def __new__(cls):
        self = super().__new__(cls)
        # print('__new__', "WhiteChessPawn")
        self = "(WP)"
        return self


# ボードの基底クラス
class AbstractBoard(object):

    def __init__(self, rows, columns):
        self.board = [ [None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()
        
    def populate_board(self):
        raise NotImplementedError
    
    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append('\n')
        return "".join(squares)


# チェッカーズボードのクラス
class CheckersBoard(AbstractBoard):

    def __init__(self):
        super().__init__(10, 10)

    def populate_board(self):
        for x in range(0, 9, 2):
            for row in range(4):
                column = x + ((row + 1) % 2)
                self.board[row][column] = BlackDraught()
                self.board[row + 6][column] = WhiteDraught()

# チェスボードのクラス
class ChessBoard(AbstractBoard):

    def __init__(self):
        super().__init__(8, 8)

    def populate_board(self):
        # black
        self.board[0][0] = BlackChessRook()
        self.board[0][1] = BlackChessKnight()
        self.board[0][2] = BlackChessBishop()
        self.board[0][3] = BlackChessQueen()
        self.board[0][4] = BlackChessKing()
        self.board[0][5] = BlackChessBishop()
        self.board[0][6] = BlackChessKnight()
        self.board[0][7] = BlackChessRook()

        # white
        self.board[7][0] = WhiteChessRook()
        self.board[7][1] = WhiteChessKnight()
        self.board[7][2] = WhiteChessBishop()
        self.board[7][3] = WhiteChessQueen()
        self.board[7][4] = WhiteChessKing()
        self.board[7][5] = WhiteChessBishop()
        self.board[7][6] = WhiteChessKnight()
        self.board[7][7] = WhiteChessRook()

        for column in range(8):
            self.board[1][column] = BlackChessPawn()
            self.board[6][column] = WhiteChessPawn()


# メインスレッド
def main():
    checkers = CheckersBoard()
    print(checkers)

    chess = ChessBoard()
    print(chess)

    if sys.platform.startswith('win'):
        filename = os.path.join(tempfile.gettempdir(), "gameboard.txt")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(sys.stdout.getvalue())
        print("wrote '{}'".format(filename), file=sys.__stdout__)



if __name__ == "__main__":
    main()