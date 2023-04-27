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
    flag=1
    movy = 0
    movx = 0
    while(flag):
        move=int(input("Enter your move: "))
        move-=1
        movy=move%3
        movx=move//3
        if board[movx][movy] != "-":
            print("Oops! This place is already occupied")
        else:
            flag = 0
    mark(board,movx,movy,human) 
    return

def ai_move(board,ai):
    best = -99
    ij=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = ai
                score= minimax(board)
                board[i][j] = "-"
                if score>best:
                    best= score
                    ij.append(i)
                    ij.append(j)
    final = []
    final.append(ij[-2])
    final.append(ij[-1])
    return final

def minimax(board):
    return 1

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
        move = ai_move(board,ai) #this will give the computer move
        board[move[0]][move[1]] = ai
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