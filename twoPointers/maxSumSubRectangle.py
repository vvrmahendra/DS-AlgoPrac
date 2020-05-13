"""RECTANGLE SUM
Problem Description
Given a matrix of integers A of size N x M. Calculate the sum of all submatrices and return the maximum among all those sums. NOTE: Empty submatrix also need to be considered. 


Problem Constraints
1 <= N, M <= 100
-10000 <= A[i] <= 10000


Input Format
The first and only argument given is the integer matrix A.


Output Format
Return the maximum sum among all those sums of all possible submatrices.


Example Input
Input 1:
 A = [
       [1, 3, -2]
       [1, 4, 6]
       [-4, -2, 1] 
     ]
Input 2:
 
A = [  
      [-1, -1]
      [-1, -1] 
    ]


Example Output
Output 1:
 13
Output 2:
 0


Example Explanation
Explanation 1:
 Submatrix giving maximum sum is : 
    [ 
       [1, 3, -2]
       [1, 4, 6]
    ]
Explanation 2:
 Sum of empty submatrix will be 0."""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    @staticmethod
    def maxSum(A):
        ans = 0
        max_till = 0
        for i in A:
            max_till += i
            if max_till < 0:
                max_till = 0
            else:
                ans = max(ans, max_till)
        return ans
    
    def solve(self, A):
        n, m = len(A), len(A[0])
        
        ans = 0
        for f in range(m):
            arr = [0]*n
            for e in range(f, m):
                for j in range(n):
                    arr[j] += A[j][e]
                    
                ans = max(ans, self.maxSum(arr))
                
        return ans
        