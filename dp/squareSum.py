"""Minimum Number of Squares
Given an integer N. Return count of minimum numbers, sum of whose squares is equal to N. Example: N=6 Possible combinations are :
(12 + 12 + 12 + 12 + 12 + 12)
(12 + 12 + 22)
So, minimum count of numbers is 3 (i.e. 1,1,2). Note: 1 ≤ N ≤ 105"""

class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, A):
        if A <= 2: return A
        dp = [float("inf")]*(A+1)
        dp[1] = 1
        dp[2] = 2
        dp[0] = 0
        coins = [i**2 for i in range(1,int(A**0.5+1))]
        for i in range(2,A+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # print(coins)            
        return dp[A]