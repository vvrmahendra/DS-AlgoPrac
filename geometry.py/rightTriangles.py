"""Count Right Triangles
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane. Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis. Note: The answer may be large so return the answer modulo (10^9 + 7). 
Input Format
The first argument given is an integer array A.
The second argument given is the integer array B.
Output Format
Return the number of unordered triplets that form a right angled triangle modulo (10^9 + 7).
Constraints
1 <= N <= 100000
0 <= A[i], B[i] <= 10^9 
For Example
Input 1:
    A = [1, 1, 2]
    B = [1, 2, 1]
Output 1:
    1

Input 2:
    A = [1, 1, 2, 3, 3]
    B = [1, 2, 1, 2, 1]
Output 2:
    6"""



def solve(A, B):
    n = len(A)
    dict_x = {}
    dict_y = {}
    for i in range(n):
        if A[i] in dict_x:
            dict_x[A[i]] += 1
        else:
            dict_x[A[i]] = 1
            
        if B[i] in dict_y:
            dict_y[B[i]] += 1
        else:
            dict_y[B[i]] = 1
        
    ans = 0
    for i in range(n):
        ans = ans + (dict_x[A[i]]-1)*(dict_y[B[i]]-1)
        
    return ans