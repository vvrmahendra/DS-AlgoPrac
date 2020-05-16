"""Rotten Oranges
Problem Description
Given a matrix of integers A of size N x M consisting of 0, 1 or 2. Each cell can have three values: The value 0 representing an empty cell. The value 1 representing a fresh orange. The value 2 representing a rotten orange. Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead. Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.  


Problem Constraints
1 <= N, M <= 1000 0 <= A[i] <= 2  


Input Format
The first argument given is the integer matrix A.


Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.If this is impossible, return -1 instead.


Example Input
Input 1:
A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
  Input 2:      
 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]
    


Example Output
Output 1:
 4
  Output 2:      
 -1
    


Example Explanation
Explanation 1:
 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
  Explanation 2:      
 Task is impossible"""

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        q, n, m = deque(), len(A), len(A[0])
        fresh = set()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 2:
                    q.append((i,j,0))
                elif A[i][j] == 1:
                    fresh.add((i,j))
                    
        dir_ = [(-1,0),(0,-1),(0,1),(1,0)]
        ite = 0            
        while True:
            i,j,d = q.popleft()
            for l,r in dir_:
                x,y = l+i, r+j
                if (x,y) in fresh:
                    q.append((x,y,d+1))
                    fresh.remove((x,y))
                    
                    
            if not fresh:
                return d+1
                
            if not q:
                return -1
            