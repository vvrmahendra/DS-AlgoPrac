"""Check for BST with exactly one child of each internal nodes
Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a BST, where each internal node (non -leaf nodes) have exactly one child. CONSTRAINTS
1 <= N <= 100
INPUT
    A : [ 4, 10, 5 ,8 ]
OUTPUT
    YES
EXPLANATION
    The possible BST is:

            4
             \
             10
             /
             5
              \
              8"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        if not A:
            return 'YES'
        if len(A) == 1:
            return 'YES'
            
        range_ = [float('-inf'), float('inf')]
        for i in range(1,len(A)):
            # print(range_, A[i], A[i-1])
            if not range_[0] <= A[i] <= range_[1]:
                return 'NO'
                
            if A[i] < A[i-1]:
                # print('first')
                range_[1] = min(range_[1], A[i-1])
                
            else:
                range_[0] = max(range_[0], A[i-1])
                
        return 'YES'              