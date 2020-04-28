"""Min Sum Path in Matrix
Problem Description
Given a M x N grid A filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. Return the minimum sum of the path. NOTE: You can only move either down or right at any point in time.  


Problem Constraints
1 <= M, N <= 1000 -1000 <= A[i][j] <= 1000  


Input Format
First and only argument is a 2-D grid A.


Output Format
Return an integer denoting the minimum sum of the path.


Example Input
Input 1:
 A = [
       [1, 3, 2]
       [4, 3, 1]
       [5, 6, 1]
     ]
Input 2:
 A = [
       [1, -3, 2]
       [2, 5, 10]
       [5, -5, 1]
     ]
 


Example Output
Output 1:
 8
Output 2:
 -1
 


Example Explanation
Explanation 1:
 The path will be: 1 -> 3 -> 2 -> 1 -> 1.
Input 2:
 The path will be: 1 -> -3 -> 5 -> -5 -> 1."""

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
        n, m = len(A), len(A[0])
        for i in range(1,m):
            A[0][i] += A[0][i-1]
        for i in range(1,n):
            A[i][0] += A[i-1][0]
            
        for i in range(1,n):
            for j in range(1,m):
                A[i][j] += min(A[i][j-1], A[i-1][j])
                
        return A[-1][-1]