"""Sorted Array To Balanced BST
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Example :
Given A : [1, 2, 3]
A height balanced BST  : 

      2
    /   \
   1     3"""

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return None
        n = len(A)
        mid = n//2
        new = TreeNode(A[mid])
        new.left = self.sortedArrayToBST(A[:mid])
        new.right = self.sortedArrayToBST(A[mid+1:])
        return new