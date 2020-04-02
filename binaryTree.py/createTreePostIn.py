"""Binary Tree From Inorder And Postorder
Given inorder and postorder traversal of a tree, construct the binary tree.
 Note: You may assume that duplicates do not exist in the tree. 
Example :
Input : 
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return : 
            1
           / \
          2   3"""


class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        if not A:
            return None
        
        head = TreeNode(B[-1])
        n = len(A)
        for i in range(n):
            if A[i] == B[-1]:
                break
            
        head.left = self.buildTree(A[:i], B[:i])
        head.right = self.buildTree(A[i+1:], B[i:-1])
        
        return head