ans = []
def prune_sudoku(row, col, block, current_position,value):
    x = current_position[0]
    y = current_position[1]
    if row[x][value] != 0:
        return False
    if col[y][value] != 0:
        return False
    if block[3*(x//3)+(y//3)][value] != 0:
        return False
    
    return True


    
def next_position(i,j):
    if i == 8 and j == 8:
        return (-1,-1)
    
    if j == 8:
        i = i+1
        j = 0
    else:
        j = j+1
    return (i,j)

def check_sudoku(row, col, block):
    for i in range(9):
        for j_int in range(1,10):
            j = str(j_int)
            if row[i][j] > 1:
                return False
            if col[i][j] > 1:
                return False
            if block[i][j] > 1:
                return False
    return True
    
def sudoku_solver(A,row,col,block,countStar, current_position):
    
    i = current_position[0]
    j = current_position[1]
    is_sudoku = check_sudoku(row,col,block)

    if not is_sudoku:
        return
    
    if countStar == 0:
        global ans
        for i in A:
            temp = [j for j in i]
            ans.append(temp)
        return 
    if current_position == (-1,-1):
        return
    
    if A[i][j] == ".":
        for value_int in range(1,10):
            value = str(value_int)
            check = prune_sudoku(row,col,block,current_position,value)
            if check:
                next_pos = next_position(i,j)
                
                
                    
                A[i][j] = value
                countStar -= 1
                row[i][value] += 1
                col[j][value] += 1
                block[3*(i//3)+(j//3)][value] += 1
                sudoku_solver(A,row,col,block,countStar,next_pos)
                block[3*(i//3)+(j//3)][value] -= 1
                col[j][value] -= 1
                row[i][value] -= 1  
                countStar += 1
                A[i][j] = "."
                
    else:
        next_pos = next_position(i,j)
        if next_pos:
            sudoku_solver(A,row,col,block,countStar,next_pos)
                    
    return
    
    

    
from collections import defaultdict
    
if __name__ == "__main__":
    row = [None]*9
    col = [None]*9
    block = [None]*9
    for i in range(9):
        row[i] = defaultdict(int)
        col[i] = defaultdict(int)
        block[i] = defaultdict(int)
        
    A = [["53......."], ["6..195..."], [".98....6."], ["8...6...3"], ["4..8.3..1"], ["7...2...6"], [".6....28."], ["...419..5"], ["....8..7."]]
    
    Arr = []
    countStar = 0
    for i in A:
        temp = []
        for j in i[0]:
            temp.append(j)
            if j == ".":
                countStar += 1
        Arr.append(temp)
        
    for i in range(9):
        for j in range(9):
            value = Arr[i][j]
            row[i][value] += 1
            col[j][value] += 1
            block[3*(i//3)+(j//3)][value] += 1
        
    sudoku_solver(Arr,row,col,block,countStar, (0,0))