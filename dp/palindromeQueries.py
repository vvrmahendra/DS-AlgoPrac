"""Odd Palindrome
Problem Description
A palindrome string is a string which reads the same forward and backward. If a palindrome string is of odd length l, then (l+1)/2th character (1 index based) is said to be the centre of the palindrome. You are given a string A. Return an array X of integers where X[i] = (number of odd length palindrome subsequence of A with A[i] as the centre) modulo (109 + 7). A subsequence of A is a string which can be derived from A by deleting some of its character. 


Problem Constraints
1 <= length(A) <= 1000
Every character of A will be a lowercase English letter 'a' - 'z'.


Input Format
First and only argument is a string A.


Output Format
Return an integer array X as mentioned in the question.


Example Input
Input 1:
 A = "xyzx"
Input 2:
 A = "ababzz"


Example Output
Output 1:
 [1, 2, 2, 1]
Output 2:
 [1, 2, 2, 1, 1, 1]


Example Explanation
Explanation 1:
 
 Index(i)  |   Palindrome subsequences with centre i
   0       |   a        
   1       |   y, xyx
   2       |   z, xzx
   3       |   x
 So, output array is [1, 2, 2, 1]

Explanation 2:
 Index(i)  |  Palindrome subsequences with centre i
   0       |  a    
   1       |  b, aba
   2       |  a, bab
   3       |  b
   4       |  z
   5       |  z
 So, output array is [1, 2, 2, 1, 1, 1] """

class Solution:
    # @param A : string
    # @return a list of integers
    @staticmethod
    def NumberOfSubSequences(A,B):
        mod = 10**9+7
        n,m = len(A), len(B)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1] != B[j-1]:
                    dp[i][j] = (dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1])%mod
                else:
                    dp[i][j] = (dp[i][j-1]+dp[i-1][j]+1)%mod
                    
        return dp
    def solve(self, A):
        n = len(A)
        dp = self.NumberOfSubSequences(A,A[::-1])
        return [dp[i][n-i-1]+1 for i in range(n)]
        