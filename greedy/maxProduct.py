"""Max Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product. Return an integer corresponding to the maximum product possible. Example :
Input : [2, 3, -2, 4]
Return : 6 

Possible with [2, 3]"""


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProduct(self, A):
        ans = float('-inf')
        n = len(A)
        chunkJ = 0
        while chunkJ < n:
            while chunkJ < n and A[chunkJ] == 0:
                chunkJ += 1
                ans = max(ans, 0)
            
            chunkI = chunkJ
            p = 1
            while chunkJ < n and A[chunkJ] != 0:
                p *= A[chunkJ]
                ans = max(ans, p)
                chunkJ += 1
                
            while  chunkI < chunkJ-1:
                p = p//A[chunkI]
                ans = max(ans, p)
                chunkI += 1
                
        return ans