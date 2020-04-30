"""Valid Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST). Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example :
Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem SOLUTION APPROACH : VIDEO : https://www.youtube.com/watch?v=yEwSGhSsT0U Complete solution in the hints."""



class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
	    isBinary = True
        def helper(head):
            if not head:
                return (float('-inf'), float('inf'))
                
            left = helper(head.left)
            right = helper(head.right)
            print(left[0],right[1])
            if head.val <= left[0] or head.val >= right[1]:
                nonlocal isBinary
                isBinary = False
                
            return (max(head.val,right[0]), min(head.val,left[1]))

        helper(A)
        return 1 if isBinary else 0