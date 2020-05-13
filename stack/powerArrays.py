"""POWER ARRAYS
Given an array of integers A of size N. An array is called POWER ARRAY if floor((maximum of array)/2) >= all other elements of array Example:- A = [5, 3, 6, 13] is a POWER ARRAY because floor((13/2)) >= all other elements of the array. Calculate how many subarrays of A are POWER ARRAYS. NOTE : Single element can never be a power array.
Input Format
The first argument given is the integer array A.
Output Format
Calculate how many subarrays of A are POWER ARRAYS.
Constraints
1 <= N <= 100000
1 <= A[i] <= 100000
For Example
Input 1:
    A = [1, 2, 3, 4, 5 ]
Output 1:
    1
Explaination 1:
    Only subarray which is also a POWER ARRAY is [1, 2]

Input 2:
    A = [64, 32, 16, 8, 4]
Output 2:
    10
Explanation 1:
    All subarrays of size greater than 1 are POWER ARRAYs. 
"""

from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        pre = [n]*n
        post = [-1]*n
        s = deque()
        for i in range(n):
            while s and A[s[-1]] < 2*A[i]:
                pre[s.pop()] = i
                
            s.append(i)
            
        s = deque()
        for i in range(n-1,-1,-1):
            while s and A[s[-1]] < 2*A[i]:
                post[s.pop()] = i
                
            s.append(i)
            
        ans = 0
        for i in range(n):
            ans += (pre[i]-i)*(i-post[i])-1
            
        return ans