"""Kth Smallest Element in a Sorted Matrix
Given a sorted matrix of integers A of size N x M and an integer B. Each of the rows and columns of matrix A are sorted in ascending order, find the Bth smallest element in the matrix. Note: Return The Bth smallest element in the sorted order, not the Bth distinct element. 
Input Format
The first argument given is the integer matrix A.
The second argument given is an integer B.
Output Format
Return the Bth smallest element in the matrix.
Constraints
1 <= N, M <= 500
1 <= A[i] <= 10^9
1 <= B <= N*M
For Example
Input 1:
    A = [   [9, 11, 15]
            [10, 15, 17]    ]
    B = 6
Output 1:
    17

Input 2:
    A = [    [5, 9, 11]
            [9, 11, 13]
            [10, 12, 15]
            [13, 14, 16]
            [16, 20, 21] ]
    B = 12
Output 2:
    16
"""


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        import heapq as hq
        set_ = set()
        n, m = len(A), len(A[0])
        count = 0
        heap = [(A[0][0],0,0)]
        set_.add((0,0))
        hq.heapify(heap)
        while count < B:
            a, i, j = hq.heappop(heap)
            # print(i,j, A[i][j])
            count += 1
            if i+1 < n and (i+1,j) not in set_:
                hq.heappush(heap, (A[i+1][j],i+1,j))
                set_.add((i+1,j))
            if j+1 < m and (i,j+1) not in set_:
                hq.heappush(heap, (A[i][j+1],i, j+1))
                set_.add((i,j+1))
                
        return A[i][j]