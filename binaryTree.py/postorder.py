"""Postorder traversal without using recursion"""

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
	    from collections import deque
        if not A:
            return []
            
        ans = []
        s1 = deque()
        s2 = deque()
        s1.append(A)
        while s1:
            current = s1.pop()
            s2.append(current)
            if current.left:
                s1.append(current.left)
            if current.right:
                s1.append(current.right)
            
        
        while s2:
            ans.append(s2.pop().val)
            
        return ans

                