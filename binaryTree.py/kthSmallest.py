"""
Kth Smallest Element In Tree
Given a binary search tree, write a function to find the kth smallest element in the tree. Example :
Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree."""


class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def __init__(self):
	    self.ind = 0
	    self.ans = None
        
	def kthsmallest(self, A, B):
        def helper(A,B):
            if not A: return
            if self.ans: return
            
            helper(A.left, B)
            self.ind += 1
            if self.ind == B:
                self.ans = A.val
            helper(A.right, B)
            
        helper(A,B)
        return self.ans