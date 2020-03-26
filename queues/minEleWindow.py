""" Finding the minimum value of each window in O(n) time
Example:- [2, 5, -1, 7, -3, -1, -2], window size is 4
output:- [-1,-3,-3,-3]
"""

def minEleWindow(A,k):
    n = len(A)
    ans = [None]*(n-k+1)
    from collections import deque
    Q = deque()
    for i in range(k):
        if not Q:
            Q.append(i)
        else:
            while Q and A[Q[-1]] > A[i]:
                Q.pop()
                
            Q.append(i)
    ans[0] = A[Q[0]]        
    for i in range(0,n-k):
        if Q[0] == i:
            Q.popleft()
            
        if not Q:
            Q.append(i+k)
            ans[i+1] = A[i+k]    
        else:
            while Q and A[Q[-1]] > A[i+k]:
                Q.pop()
                
            Q.append(i+k)
            ans[i+1] = A[Q[0]]
                
    return ans
            