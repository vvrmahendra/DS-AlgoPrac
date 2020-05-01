"""Palindrome Partitioning II
Problem Description
Given a string A, partition A such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of A. 


Problem Constraints
1 <= length(A) <= 501


Input Format
The first and the only argument contains the string A.


Output Format
Return an integer, representing the minimum cuts needed.


Example Input
Input 1:
 A = "aba"
Input 2:
 A = "aab"


Example Output
Output 1:
 0
Output 2:
 1


Example Explanation
Explanation 1:
 "aba" is already a palindrome, so no cuts are needed.
Explanation 2:
 Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut."""


# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42212/Two-C%2B%2B-versions-given-(one-DP-28ms-one-Manancher-like-algorithm-10-ms)
# Refer the above link for algorithm
class Solution:
	# @param A : string
	# @return an integer
    def minCut(self, A):
        n = len(A)
        dp = [[False]*(n) for i in range(n)]
        cuts = [i for i in range(-1,n)]
        
        for j in range(n):
            for i in range(j, -1, -1):
                if (A[i] == A[j]) and (j-i < 2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    cuts[j+1] = min(cuts[j+1], cuts[i]+1)
                    
        return cuts[-1]