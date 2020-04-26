"""Maximum Sum
You are given an array A of N integers and three integers X, Y, and Z. You have to find the maximum value of A[i]*X + A[j]*Y + A[k]*Z, where 1 <= i <= j <= k <= N. Input Format
1st argument is an array A
2nd argument is an integer X
3rd argument is an integer Y
4th argument is an integer Z
Output Format
Return an Integer S, i.e maximum value of (A[i]*X + A[j]*Y + A[k]*Z), where  1 <= i <= j <= k <= N.
Constraints
1 <= N <= 1e5
-1e4 <= A[i], X, Y, Z <= 1e4
For Example
Input:
    A = [1, 5, -3, 4, -2]
    X = 2
    Y = 1
    Z = -1
Output:
    18

Explanation:
    if you choose i = 2, j = 2, and k = 3 then we will get
    A[2]*X + A[2]*Y + A[3]*Z = 5*2 + 5*1 + (-3)*(-1) = 10 + 5 + 3 = 18"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        if B < 0:
            pre = [0]*n
            pre[0] = A[0]
            for i in range(1,n):
                pre[i] =min(pre[i-1], A[i]) 
            
        else:
            pre = [0]*n
            pre[0] = A[0]
            for i in range(1,n):
                pre[i] =max(pre[i-1], A[i]) 
            
        if D < 0:
            post = [0]*n
            post[~0] = A[~0]
            for i in range(1,n):
                post[~i] = min(post[~(i-1)], A[~i])
        else:
            post = [0]*n
            post[~0] = A[~0]
            for i in range(1,n):
                post[~i] = max(post[~(i-1)], A[~i])
            
        ans = float("-inf")
        for i, val in enumerate(A):
            ans = max(ans, pre[i]*B+A[i]*C+post[i]*D)
        return ans