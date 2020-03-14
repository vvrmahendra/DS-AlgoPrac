"""Count Rectangles
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane. Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis. 
Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.
Output Format
Return the number of unordered quadruplet that form a rectangle.
Constraints
1 <= N <= 2000
0 <= A[i], B[i] <= 10^9 
For Example
Input 1:
    A = [1, 1, 2, 2]
    B = [1, 2, 1, 2]
Output 1:
    1

Input 2:
    A = [1, 1, 2, 2, 3, 3]
    B = [1, 2, 1, 2, 1, 2]
Output 2:
    3"""


def solve(A, B):
    n = len(A)
    set_ = set([(A[i],B[i]) for i in range(n)])
    
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (A[i],B[j]) in set_ and (A[j],B[i]) in set_ and A[j] != A[i] and B[j] != B[i]:
                ans += 1
                
    return ans//2