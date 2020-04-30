"""Identical Binary Trees
Given two binary trees, write a function to check if they are equal or not. Two binary trees are considered equal if they are structurally identical and the nodes have the same value. Return 0 / 1 ( 0 for false, 1 for true ) for this problem Example :
Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 or True"""

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):
        if not A:
            return 1 if not B else 0
        if not B:
            return 1 if not A else 0
                
                
        if A.val == B.val:
            f1 = self.isSameTree(A.left, B.left)
            f2 = self.isSameTree(A.right, B.right)
            
            return 1 if f1 and f2 else 0
        else:
            return 0