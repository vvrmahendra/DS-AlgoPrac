"""First negative integer in window size B
Given an array of integers A of size N and an integer B. Find the first negative integer for each and every window(contiguous subarray) of size B. If a window does not contain a negative integer, then return 0 for that window. 
Input Format
The arguments given are integer array A and integer B.
Output Format
Return an integer array of size N+1-B representing answer of the ith window.
Constraints
1 <= length of the array <= 200000
-10^9 <= A[i] <= 10^9 
For Example
Input 1:
    A = [-1, 2, 3, -4, 5]
    B = 2
Output 1:
    [-1, 0, -4, -4] 

Input 2:
    A = [-8, 2, 3, -6, 10]
    B = 2
Output 2:
    [-8, 0, -6, -6]
"""


def solve(A, k):
    n = len(A)
    ans = [None]*(n-k+1)
    from collections import deque
    Q = deque()
    for i in range(k):
        if A[i] < 0:
            Q.append(i)
    ans[0] = A[Q[0]] if Q else 0   
    
    
    for i in range(0,n-k):
        if Q and Q[0] == i:
            Q.popleft()
        if A[i+k] < 0:
            Q.append(i+k)
        ans[i+1] = A[Q[0]] if Q else 0
                
    return ans