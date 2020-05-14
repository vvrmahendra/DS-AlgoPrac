"""1102. Path With Maximum Minimum Value
Medium

398

47

Add to List

Share
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 

Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9"""



import heapq as hq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        visited = [[0]*m for _ in range(n)]
        dir_ = [(-1,0),(0,-1),(1,0),(0,1)]
        q = [(-A[0][0], 0, 0)]
        while q:
            val, i,j = hq.heappop(q)
            visited[i][j] = 1
            if i == n-1 and j == m-1:
                return -val
            
            for l, r in dir_:
                if 0 <= i+l < n and 0 <= j+r < m and visited[i+l][r+j] == 0:
                    hq.heappush(q,(max(-A[i+l][j+r],val),i+l,j+r))
                    visited[i+l][r+j] = 1
            
        
            