import random 

def board_to_sudoku():
    row=[]
    col1=[]
    board=[]
    col2=[]

    for i in range(3):
        col1=[]
        for j in range(3):
            col1.append(0)
        row.append(col1)
    for g in range(3):
        col2=[]
        for h in range(3):
            col2.append(row)
        board.append(col2)

    print(board[0],'\n',board[1],'\n',board[2])
    return(board)


def sudoku(board):
    start_num_tab=[]
    start_num=random.randint(1,9)
    #start_num_tab.append(start_num)
    #start_num_tab.append(start_num+1)
    #start_num_tab.append(start_num+2)
    #board[0][0][0]=start_num_tab
    print(board[0][0][0][0])
    board[0][0][0][0] = start_num
    print(board[0][0][0][0])
    print(board[0][0][0])
    print(board[0][0])
    print(board[1][0])
    #print(board[0],'\n',board[1],'\n',board[2])

tab=board_to_sudoku()
sudoku(tab)