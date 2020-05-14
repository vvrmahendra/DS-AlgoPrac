"""Number of islands
Problem Description
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.  More formally, from any cell (i, j) if A[i][j] = 1 you can visit:  
(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
 Return the number of islands. NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.  


Problem Constraints
1 <= N, M <= 100 0 <= A[i] <= 1  


Input Format
The only argument given is the integer matrix A.


Output Format
Return the number of islands.


Example Input
Input 1:
 A = [ 
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]
Input 2:
 A = [   
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]    
     ]
 


Example Output
Output 1:
 2
Output 2:
 5
 


Example Explanation
Explanation 1:
 The 1's at position A[0][1] and A[1][2] forms one island.
 Other is formed by A[2][0].
Explanation 2:
 There 5 island in total."""


from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    @staticmethod
    def _clearit(A, cur):
        n,m = len(A), len(A[0])
        dir = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1)]
        q = deque()
        q.append(cur)
        while q:
            i,j = q.popleft()
            A[i][j] = 0
            for l,r in dir:
                if 0<=l+i< n and 0 <= r+j < m and A[l+i][r+j]:
                    q.append((l+i, r+j))
                    A[l+i][r+j] = 0
                    
        return
                    
    def solve(self, A):
        n, m = len(A), len(A[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if A[i][j]:
                    ans += 1
                    self._clearit(A, (i,j))
                    
        return ans