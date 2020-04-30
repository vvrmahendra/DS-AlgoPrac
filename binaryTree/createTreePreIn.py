"""Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

Return :
            1
           / \
          2   3
"""



class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        if not A:
            return None
            
        new = TreeNode(A[0])
        n = len(A)
        for i in range(n):
            if B[i] == A[0]:
                break
            
        new.left = self.buildTree(A[1:i+1], B[:i])
        new.right = self.buildTree(A[i+1:], B[i+1:])
        return new