"""Maximum Rectangle
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M. Find the largest rectangle containing only 1's and return its area. Note: Rows are numbered from top to bottom and columns are numbered from left to right. 
Input Format
The only argument given is the integer matrix A.
Output Format
Return the area of the largest rectangle containing only 1's.
Constraints
1 <= N, M <= 1000
0 <= A[i] <= 1
For Example
Input 1:
    A = [   [0, 0, 1]
            [0, 1, 1]
            [1, 1, 1]   ]
Output 1:
    4

Input 2:
    A = [   [0, 1, 0, 1]
            [1, 0, 1, 0]    ]
Output 2:
    1"""
from arearHistogram import largestRectangleArea
# Here we used the help of largestRectangleArea method
def solve(A): 
    n = len(A)
    m = len(A[0])
    hist_array = A[0]
    ans = largestRectangleArea(hist_array)
    for i in range(1,n):
        hist_array = [hist_array[j]+1 if A[i][j] else 0 for j in range(m)]
        ans = max(ans, largestRectangleArea(hist_array))
        
    return ans