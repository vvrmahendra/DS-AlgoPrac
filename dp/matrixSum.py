"""Max Sum Without Adjacent Elements
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it. Note: You can choose more than 2 numbers. Input Format:
The first and the only argument of input contains a 2d matrix, A.
Output Format:
Return an integer, representing the maximum possible sum.
Constraints:
1 <= N <= 20000
1 <= A[i] <= 2000
Example:
Input 1:
    A = [   [1]
            [2]    ]

Output 1:
    2

Explanation 1:
    We will choose 2.

Input 2:
    A = [   [1, 2, 3, 4]
            [2, 3, 4, 5]    ]

Output 2:
    We will choose 3 and 5."""

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def adjacent(self, A):
        A = [max(A[0][i], A[1][i]) for i in range(len(A[0]))]
        n = len(A)
        if n <= 2: return max(A)
        dp = [0]*(n)
        dp[0] = A[0]
        dp[1] = max(A[0],A[1])
        
        for i in range(2, n):
            dp[i] = max(A[i]+dp[i-2], dp[i-1])

        return dp[n-1]
        