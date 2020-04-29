#This is the DP implementaion of maxSum. I have implemented Greedy in Greedy section
#refer there for problme statement

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        dp = [[0]*(n+1) for i in range(3)]
        for i in range(3):
            dp[i][0] = float('-inf')
            
        for i in range(1,n+1):
            dp[0][i] = max(dp[0][i-1], A[i-1]*B)
            dp[1][i] = max(dp[1][i-1], dp[0][i]+A[i-1]*C)
            dp[2][i] = max(dp[2][i-1], dp[1][i]+A[i-1]*D)
            
        return dp[2][n]
        