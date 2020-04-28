"""Unique Paths in a Grid
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y). Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid. Example : There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
 Note: m and n will be at most 100."""

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
	    if A[0][0] == 1:
	        return 0
        n , m = len(A), len(A[0])
        dp = [[0]*m for i in range(n)]
        
        dp[0][0] = 1
        for i in range(1,m):
            if A[0][i] == 0:
                dp[0][i] = dp[0][i-1]
                
        for i in range(1,n):
            if A[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if A[i][j] == 0:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
                    
        return dp[-1][-1]