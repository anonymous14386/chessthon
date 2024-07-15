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

#Black life vals
bKingAlive = 1
bQueenAlive = 1
bRook1Alive = 1
bRook2Alive = 1
bBishop1Alive = 1
bBishop2Alive = 1
bKnight1Alive = 1
bKnight2Alive = 1
bPawn1Alive = 1
bPawn2Alive = 1
bPawn3Alive = 1
bPawn4Alive = 1
bPawn5Alive = 1
bPawn6Alive = 1
bPawn7Alive = 1
bPawn8Alive = 1

#White life vals
wKingAlive = 1
wQueenAlive = 1
wRook1Alive = 1
wRook2Alive = 1
wBishop1Alive = 1
wBishop2Alive = 1
wKnight1Alive = 1
wKnight2Alive = 1
wPawn1Alive = 1
wPawn2Alive = 1
wPawn3Alive = 1
wPawn4Alive = 1
wPawn5Alive = 1
wPawn6Alive = 1
wPawn7Alive = 1
wPawn8Alive = 1

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
d1 = wQueen
e1 = wKing
f1 = wBishop2
g1 = wKnight2
h1 = wRook2


board = np.array([
    [a8, b8, c8, d8, e8, f8, g8, h8],
    [a7, b7, c7, d7, e7, f7, g7, h7],
    [a6, b6, c6, d6, e6, f6, g6, h6],
    [a5, b5, c5, d5, e5, f5, g5, h5],
    [a4, b4, c4, d4, e4, f4, g4, h4],
    [a3, b3, c3, d3, e3, f3, g3, h3],
    [a2, b2, c2, d2, e2, f2, g2, h2],
    [a1, b1, c1, d1, e1, f1, g1, h1]])

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

#Basically your grid looks like this:
# | 0,0 = 8,a | 0,1 = 8,b | 0,2 = 8,c | 0,3 = 8,d | 0,4 = 8,e | 0,5 = 8,f | 0,6 = 8,g | 0,7 = 8,h | 
# | 1,0 = 7,a | 1,1 = 7,b | 1,2 = 7,c | 1,3 = 7,d | 1,4 = 7,e | 1,5 = 7,f | 1,6 = 7,g | 1,7 = 7,h | 
# | 2,0 = 6,a | 2,1 = 6,b | 2,2 = 6,c | 2,3 = 6,d | 2,4 = 6,e | 2,5 = 6,f | 2,6 = 6,g | 2,7 = 6,h | 
# | 3,0 = 5,a | 3,1 = 5,b | 3,2 = 5,c | 3,3 = 5,d | 3,4 = 5,e | 3,5 = 5,f | 3,6 = 5,g | 3,7 = 5,h | 
# | 4,0 = 4,a | 4,1 = 4,b | 4,2 = 4,c | 4,3 = 4,d | 4,4 = 4,e | 4,5 = 4,f | 4,6 = 4,g | 4,7 = 4,h | 
# | 5,0 = 3,a | 5,1 = 3,b | 5,2 = 3,c | 5,3 = 3,d | 5,4 = 3,e | 5,5 = 3,f | 5,6 = 3,g | 5,7 = 3,h | 
# | 6,0 = 2,a | 6,1 = 2,b | 6,2 = 2,c | 6,3 = 2,d | 6,4 = 2,e | 6,5 = 2,f | 6,6 = 2,g | 6,7 = 2,h | 
# | 7,0 = 1,a | 7,1 = 1,b | 7,2 = 1,c | 7,3 = 1,d | 7,4 = 1,e | 7,5 = 1,f | 7,6 = 1,g | 7,7 = 1,h | 

pieceSel = input("Select a piece position (xy): ")

pieceSelY = pieceSel[1]
if pieceSelY == "1":
    selCordY = 7
elif pieceSelY == "2":
    selCordY = 6
elif pieceSelY == "3":
    selCordY = 5
elif pieceSelY == "4":
    selCordY = 4
elif pieceSelY == "5":
    selCordY = 3
elif pieceSelY == "6":
    selCordY = 2
elif pieceSelY == "7":
    selCordY = 1
elif pieceSelY == "8":
    selCordY = 0

pieceSelX = pieceSel[0]
if pieceSelX == "a":
    selCordX = 0
elif pieceSelX == "b":
    selCordX = 1
elif pieceSelX == "c":
    selCordX = 2
elif pieceSelX == "d":
    selCordX = 3
elif pieceSelX == "e":
    selCordX = 4
elif pieceSelX == "f":
    selCordX = 5
elif pieceSelX == "g":
    selCordX = 6
elif pieceSelX == "h":
    selCordX = 7


pieceDest = input("Where go? (xy): ")
pieceDestX = pieceDest[0]
pieceDestY = pieceDest[1]

print ("Selection: ", pieceSelX, ",", pieceSelY)
print("Destination: ", pieceDestX, ",", pieceDestY)

#DEFINE EVERY FUCKING CHESS MOVE IN EXISTANCE HERE THERE HAS TO BE A BETTER WAY BUT HERE WE ARE

#Starting withhhhh white pawns!
#We're looking at 6,0-7 here or 2,a-h

print("You selected: ", board[selCordY, selCordX] )
