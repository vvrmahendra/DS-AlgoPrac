"""Capture Regions on Board
Problem Description
Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.  


Problem Constraints
1 <= N, M <= 1000


Input Format
First and only argument is a N x M character matrix A.


Output Format
Make changes to the the input only as matrix is passed by reference.


Example Input
Input 1:
 A = [ 
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X] 
     ]
Input 2:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]
 


Example Output
Output 1:
 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2:
 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]
 


Example Explanation
Explanation 1:
 O in (4,2) is not surrounded by X from below.
Explanation 2:
 No O's are surrounded."""


from collections import defaultdict, deque
class Solution:
    # @param A : list of list of chars
    @staticmethod
    def cover(A, cur, n,m):
        q = deque()
        visited = {cur}
        flag = True
        q.append(cur)
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            i,j = q.popleft()
            if i == n-1 or j == m-1 or i == 0 or j == 0:
                flag = False
                
            for l,r in dir_:
                x,y = l+i,j+r
                if 0 <= x < n and 0 <= y< m and (x,y) not in visited and A[x][y] == 'O':
                    q.append((x,y))
                    visited.add((x,y))
                    
        ph = 'X' if flag else 'Y'
        for i,j in visited:
            A[i][j] = ph
            
        return
            
    def solve(self, A):
        # print(A)
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 'O':
                    self.cover(A, (i,j), n, m)
                    
        
        for i in range(n):
            for j in range(m):
                if A[i][j] == 'Y':
                    A[i][j] = 'O'
        
        # print(A)
                    
        