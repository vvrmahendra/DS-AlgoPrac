"""Symmetric Binary Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center). Example :
    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric. But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""




class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
        if not A:
            return 1
            
        def helper(A, B):
            if not A:
                return True if not B else False
            if not B:
                return False if not A else False
                
            if A.val == B.val:
                f1 = helper(A.left, B.right)
                f2 = helper(A.right, B.left)
                return f1 and f2
                
            else:
                return False
                
        return 1 if helper(A,A) else 0