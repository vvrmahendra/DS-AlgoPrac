"""Christmas Trees
Problem Description
You are given an aray A consisting of heights of Christmas trees, and an array B of same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br. You are to choose 3 such trees such that they have the minimum cost, find the minimum cost. If not possible to choose 3 such trees, return -1.  


Problem Constraints
1 <= A[i], B[i] <= 109
3 <= size(A) = size(B) <= 3000


Input Format
First argument is an integer array A.
Second argument is an integer array B.


Output Format
Return an integer denoting the minimum cost of choosing 3 trees whose heights are strictly in increasing order, if not possible, -1.


Example Input
A = [1,3,5]
B = [1,2,3]


Example Output
6


Example Explanation
We can choose the trees with indices 1, 2 and 3, and the cost is 1+2+3 = 6
"""


def solve(A, B):
    n = len(A)
    ans = float('inf')
    for j in range(1,n-1):
        min_first = float('inf')
        for k in range(j):
            if A[k] < A[j]:
                min_first = min(min_first, B[k])
                
        min_third =  float('inf')
        for k in range(j+1,n):
            if A[j] < A[k]:
                min_third = min(min_third, B[k])
                
        ans = min(ans, min_first+B[j]+min_third)
        
    return ans if ans != float('inf') else -1