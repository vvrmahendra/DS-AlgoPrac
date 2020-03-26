"""N integers containing only 1,2 and 3
Given an integer A. Find and Return first positive A integers in ascending order containing only digits 1,2 and 3. NOTE: all the A integers will fit in 32 bit integer. 
Input Format
The only argument given is integer A.
Output Format
Find and Return first positive A integers in ascending order containing only digits 1,2 and 3.
Constraints
1 <= A <= 29500
For Example
Input 1:
    A = 3
Output 1:
    [1, 2, 3]

Input 2:
    A = 7
Output 2:
    [1, 2, 3, 11, 12, 13, 21]"""


def solve(A):
    if A <= 3:
        return [i+1 for i in range(A)]
    from collections import deque
    Q = deque()
    ans = []
    Q.append(1)
    Q.append(2)
    Q.append(3)
    n = 3
    while n < A:
        temp = Q.popleft()
        ans.append(temp)
        Q.append(10*temp+1)
        n += 1
        if n < A:
            Q.append(10*temp+2)
            n += 1
        if n < A:
            Q.append(10*temp+3)
            n += 1
            
    while Q:
        ans.append(Q.popleft())
        
    return ans