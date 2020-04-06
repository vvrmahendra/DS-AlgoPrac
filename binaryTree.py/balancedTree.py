"""Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem Example :
Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. """

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
	    def helper(A):
            if not A:
                return (-1, True)
                
            left = helper(A.left)
            right = helper(A.right)
            temp = left[1] and right[1]
            height = max(left[0],right[0])+1
            
            return (height, temp and True if abs(left[0]-right[0]) < 2 else False)
            
        return 1 if helper(A)[1] else 0