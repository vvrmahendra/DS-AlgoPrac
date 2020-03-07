ans = []

def solveNQueens(self, A):
    global ans
    ans = []
    
    def validBoard(Qs):
                    
        if len(Qs) <= 1:
            return True
        QsNum = len(Qs)
        for first in range(QsNum-1):
            for second in range(first+1,QsNum):
                if Qs[first][0] == Qs[second][0]:
                    return False
                elif Qs[first][1] == Qs[second][1]:
                    return False
                elif abs(Qs[first][0]-Qs[second][0]) == abs(Qs[first][1]-Qs[second][1]):
                    return False
        return True
    
    
    def feasibility(current_pos,Qs):
        n = len(Qs)
        for i in range(n):
            if Qs[i][0] == current_pos[0]:
                return False
            if Qs[i][1] == current_pos[1]:
                return False
            if abs(Qs[i][1]-current_pos[1]) == abs(Qs[i][0]-current_pos[0]):
                return False
            
        return True
    
    def nQueens(A,countQ,current_pos,Qs):
        i = current_pos[0]
        j = current_pos[1]
        n = len(A)
        #print(current_pos)
        
        if countQ == n:
            check = validBoard(Qs)
            if not check:
                return
            # print("Yayyy Got a solution")
            
            global ans
            temp = []
            for i in A:
                temp_char = ""
                for j in i:
                    temp_char += j
                temp.append(temp_char)
            ans.append(temp)
            return
        
        if current_pos == (-1,-1):
            return
        if current_pos == (n,0):
            return
        
        for x in range(n):

            feasibility_check = feasibility((i, x),Qs)

            if feasibility_check:

                A[i][x] = 'Q'

                countQ += 1

                Qs.append((i,x))

                nQueens(A,countQ, (i+1,0),Qs)

                Qs.pop()

                countQ -= 1



                A[i][x] = '.'
        
        return

    
    
    
    Arr = []
    for i in range(A):
        Arr.append(['.'for j in range(A)])
        
    nQueens(Arr,0,(0,0),[])
    return ans