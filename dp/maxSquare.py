# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

from functools import lru_cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        ans = 0
        @lru_cache(maxsize = None)
        def helper(i,j):
            nonlocal ans
            if i < 0 or j < 0:
                return 0
            
            temp = min(helper(i,j-1),helper(i-1, j),helper(i-1,j-1))+1
            if matrix[i][j] == '0':
                return 0
            ans = max(ans,temp)
            return temp
        
        n, m = len(matrix), len(matrix[0])
        helper(n-1,m-1)
        return ans**2