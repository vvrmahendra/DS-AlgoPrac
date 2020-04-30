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




#Optimised Solution
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        dict_ = {inorder[i]:i for i in range(len(inorder))}
        print(dict_)
        def helper(inorder, postorder, l1, l2, r1, r2):
            if not inorder[l1: r1]:
                return None
           
            new  = TreeNode(postorder[r2-1])
            i = dict_[postorder[r2-1]]
            buffer = i-l1
            new.left = helper(inorder, postorder, l1, l2, l1+buffer, l2+buffer)
            new.right = helper(inorder, postorder, l1+buffer+1, l2+buffer, r1, r2-1)
            return new
        
        return helper(inorder, postorder, 0, 0, len(inorder), len(postorder))