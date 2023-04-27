def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def isWin(board):
    for i in range(3):
        if(board[i][0]== board[i][1] and board[i][0]== board[i][2] and board[i][0]!="-"):
            return str(board[i][0])
        if(board[0][i]== board[1][i] and board[0][i]== board[2][i] and board[0][i]!="-"):
            return str(board[0][i])
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!="-"):
        return str(board[0][0])
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]!="-"):
        return str(board[0][2])
    return "None"
    
def mark(board, x,y,sign):
    board[x][y] = sign
    return

def userInput(board):
    move=int(input("Enter your move: "))
    move-=1
    movy=move%3
    movx=move//3
    mark(board,movx,movy,human) 
    return

def ai_move(board):
    pass

def minimax(board):
    pass

board= [ ["-","-","-"],["-","-","-"],["-","-","-"] ]


ai = "o"
human = "x"
spaceCount = 9
win=0
printBoard(board)
while(spaceCount!=0 and win ==0):
    if spaceCount%2==1:
        userInput(board)
    else:
        ai_move(board) #this will give the computer move
    spaceCount-=1
    if isWin(board) == "None":
        printBoard(board)
        continue
    else:
        printBoard(board)
        print(isWin(board), "WON!!")
        break



# printBoard(board)
# print(isWin(board))