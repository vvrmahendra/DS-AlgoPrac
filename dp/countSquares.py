"""1277. Count Square Submatrices with All Ones
Medium

499

14

Add to List

Share
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7."""

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        ans = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1])+1
                    ans += dp[i][j]
                    
        return ans