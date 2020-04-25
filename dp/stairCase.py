"""Stairs
You are climbing a stair case and it takes A steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
 Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.
Constrains:
1 <= A <= 36
Example : Input 1:
A = 2
Output 1:
2"""

class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
	    if A <= 2: return A
        dp = [0]*(A+1)
        dp[2] = 2
        dp[1] = 1
        def helper(n):
            if dp[n] or n <= 0:
                return
            helper(n-1)
            helper(n-2)
            dp[n] = dp[n-1]+dp[n-2]
        helper(A)    
        return dp[A]