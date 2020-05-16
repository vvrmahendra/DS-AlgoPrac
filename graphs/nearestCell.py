"""Distance of nearest cell
Problem Description
Given a matrix of integers A of size N x M consisting of 0 or 1. For each cell of the matrix find the distance of nearest 1 in the matrix. Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - y1| + |x2 - y2|. Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A. NOTE: There is atleast one 1 is present in the matrix. 


Problem Constraints
1 <= N, M <= 1000 0 <= A[i] <= 1 


Input Format
The first argument given is the integer matrix A.


Output Format
Return the matrix B.


Example Input
Input 1:
 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]
Input 2:
 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]


Example Output
Output 1:
 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]
Output 2:
 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]


Example Explanation
Explanation 1:
 A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
 A[1][0], A[1][1] will be nearest to A[1][2].
 A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].
Explanation 2:
 There is only a single 1. Fill the distance from that 1."""


 from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n, m = len(A),len(A[0])
        ans = [[-1]*m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i,j))
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            i, j = q.popleft()
            for l, r in dir_:
                x,y = i+l, r+j
                if 0 <= x < n and 0<=y<m and ans[x][y] == -1:
                    ans[x][y] = ans[i][j]+1
                    
                    q.append((x,y))
                    
        return ans