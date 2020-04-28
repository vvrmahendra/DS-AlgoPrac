"""Longest Common Subsequence
Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings. You need to return the length of such longest common subsequence. NOTE:
Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.
CONSTRAINTS
1 <= Length of A, B <= 10^3 + 5
EXAMPLE INPUT
A : "abbcdgf"
B : "bbadcgf"
EXAMPLE OUTPUT
5
EXPLANATION
The longest common subsequence is "bbcgf", which has a length of 5"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n, m = len(A), len(B)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]