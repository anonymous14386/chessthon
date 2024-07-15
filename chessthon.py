import numpy as np

#board
print("Default layout no pieces:")
print("8 ■ □ ■ □ ■ □ ■ □")
print("7 □ ■ □ ■ □ ■ □ ■")
print("6 ■ □ ■ □ ■ □ ■ □")
print("5 □ ■ □ ■ □ ■ □ ■")
print("4 ■ □ ■ □ ■ □ ■ □")
print("3 □ ■ □ ■ □ ■ □ ■")
print("2 ■ □ ■ □ ■ □ ■ □")
print("1 □ ■ □ ■ □ ■ □ ■")
print("  a b c d e f g h")
print()

#Define black pieces
bKing = "♔"
bQueen = "♕"
bRook1 = "♖"
bRook2 = "♖"
bBishop1 = "♗"
bBishop2 = "♗"
bKnight1 = "♘"
bKnight2 = "♘"
bPawn1 = "♙"
bPawn2 = "♙"
bPawn3 = "♙"
bPawn4 = "♙"
bPawn5 = "♙"
bPawn6 = "♙"
bPawn7 = "♙"
bPawn8 = "♙"
bSquare = "□"

#Define white pieces
wKing = "♚"
wQueen = "♛"
wRook1 = "♜"
wRook2 = "♜"
wBishop1 = "♝"
wBishop2 = "♝"
wKnight1 = "♞"
wKnight2 = "♞"
wPawn1 = "♟︎"
wPawn2 = "♟︎"
wPawn3 = "♟︎"
wPawn4 = "♟︎"
wPawn5 = "♟︎"
wPawn6 = "♟︎"
wPawn7 = "♟︎"
wPawn8 = "♟︎"
wSquare = "■"

a8 = bRook1
b8 = bKnight1
c8 = bBishop1
d8 = bQueen
e8 = bKing
f8 = bBishop2
g8 = bKnight2
h8 = bRook2

a7 = bPawn1
b7 = bPawn2
c7 = bPawn3
d7 = bPawn4
e7 = bPawn5
f7 = bPawn6
g7 = bPawn7
h7 = bPawn8

a6 = wSquare
b6 = bSquare
c6 = wSquare
d6 = bSquare
e6 = wSquare
f6 = bSquare
g6 = wSquare
h6 = bSquare

a5 = bSquare
b5 = wSquare
c5 = bSquare
d5 = wSquare
e5 = bSquare
f5 = wSquare
g5 = bSquare
h5 = wSquare

a4 = wSquare
b4 = bSquare
c4 = wSquare
d4 = bSquare
e4 = wSquare
f4 = bSquare
g4 = wSquare
h4 = bSquare

a3 = bSquare
b3 = wSquare
c3 = bSquare
d3 = wSquare
e3 = bSquare
f3 = wSquare
g3 = bSquare
h3 = wSquare

a2 = wPawn1
b2 = wPawn2
c2 = wPawn3
d2 = wPawn4
e2 = wPawn5
f2 = wPawn6
g2 = wPawn7
h2 = wPawn8

a1 = wRook1
b1 = wKnight1
c1 = wBishop1
d1 = bQueen
e1 = bKing
f1 = wBishop2
g1 = wKnight2
h1 = wRook2


board = np.array([[a8, b8, c8, d8, e8, f8, g8, h8],[a7, b7, c7, d7, e7, f7, g7, h7],[a6, b6, c6, d6, e6, f6, g6, h6],[a5, b5, c5, d5, e5, f5, g5, h5],[a4, b4, c4, d4, e4, f4, g4, h4],[a3, b3, c3, d3, e3, f3, g3, h3],[a2, b2, c2, d2, e2, f2, g2, h2],[a1, b1, c1, d1, e1, f1, g1, h1]])

print("Board with pieces:")
print("8", board[0,0],board[0,1],board[0,2],board[0,3],board[0,4],board[0,5],board[0,6],board[0,7])
print("7", board[1,0],board[1,1],board[1,2],board[1,3],board[1,4],board[1,5],board[1,6],board[1,7])
print("6", board[2,0],board[2,1],board[2,2],board[2,3],board[2,4],board[2,5],board[2,6],board[2,7])
print("5", board[3,0],board[3,1],board[3,2],board[3,3],board[3,4],board[3,5],board[3,6],board[3,7])
print("4", board[4,0],board[4,1],board[4,2],board[4,3],board[4,4],board[4,5],board[4,6],board[4,7])
print("3", board[5,0],board[5,1],board[5,2],board[5,3],board[5,4],board[5,5],board[5,6],board[5,7])
print("2", board[6,0],board[6,1],board[6,2],board[6,3],board[6,4],board[6,5],board[6,6],board[6,7])
print("1", board[7,0],board[7,1],board[7,2],board[7,3],board[7,4],board[7,5],board[7,6],board[7,7])
print("  a b c d e f g h")

pieceSel = input("Select a piece position (xy): ")
pieceDest = input("Where go? (xy): ")
