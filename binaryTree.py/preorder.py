"""PreOrder traversal without using recursion."""



class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        from collections import deque
        if not A:
            return []
        s = deque()    
        ans = []
        s.append(A)
        while s:
            current = s.pop()
            
            ans.append(current.val)
            
            if current.right:
                s.append(current.right)
            if current.left:
                s.append(current.left)
                    
        return ans