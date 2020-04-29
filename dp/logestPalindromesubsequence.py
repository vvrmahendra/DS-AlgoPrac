"""Longest Pallindromic Subsequence
Given a strings A. Find the common pallindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself You need to return the length of such longest common subsequence. NOTE:
Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.
CONSTRAINTS
1 <= Length of A, B <= 10^3 + 5
EXAMPLE INPUT
A : "bebeeed"
EXAMPLE OUTPUT
4
EXPLANATION
The longest common pallindromic subsequence is "eeee", which has a length of 4"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        B = "".join(list(A)[::-1])
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]