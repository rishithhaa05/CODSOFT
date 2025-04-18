import math 
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)
def check_winner(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)) or all(board[j][i]==player for j in range(3)):
            return True
    if all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(board[i][j]!=''for i in range(3)for j  in range(3))
def minimax(board,depth,is_maximizing):
    if check_winner(board,'O'):
        return 1
    if check_winner(board,'X'):
        return -1
    if is_full(board):
        return 0
    if is_maximizing:
        best_score=-math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='O'
                    score=minimax(board,depth+1,False)
                    board[i][j]=''
                    best_score=max(score,best_score)
        return best_score
    else:
        best_score=math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='X'
                    score=minimax(board,depth+1,False)
                    board[i][j]=''
                    best_score=min(score,best_score)
        return best_score
def best_move(board):
    best_score= -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                board[i][j]='O'
                score=minimax(board,0,False)
                board[i][j]=''
                if score>best_score:
                    move=(i,j)
    return move
def tic_tac_toe():
    board=[[''for _ in range(3)]for _ in range(3)]
    players=['X','O']
    
    for turn in range(9):
        print_board(board)
        player=players[turn%2]
        
        if player=='X':#Human player
            row,col=map(int,input("Enter row and col(0-2):").split())
            while board[row][col]!='':
                print("INVALID MOVE!Try again.")
                row,col=map(int,input("Enter row and col(0-2):").split())
        else:#AI Player(O)
            row,col=best_move(board)
            print(f"AI chooses:{row},{col}")
        board[row][col]=player
        if check_winner(board,player):
            print_board(board)
            print(f"player {player} wins!")
            return
    print_board(board)
    print("It's a draw!")
tic_tac_toe()
