"""Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.
 Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution? 
Example :
Input : 
         1
        / \
       2   3

Output : 
       [1, 2]

Explanation : Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST          """

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):
	    root = A
        from collections import deque
        s = deque()
        first = None
        second = None
        ansFirst = None
        ansSecond =None
        while True:
            if A:
                s.append(A)
                A = A.left
            elif s:
                temp = s.pop()
                A = temp.right
                # s.append(temp.right)
                
                if not first and not second:
                    first = temp
                else:
                    second = first
                    first = temp
                    
                if first and second:
                    if  second.val > first.val and not ansFirst:
                        ansFirst = second
                        ansSecond = first
                    elif second.val > first.val:
                        ansSecond = first
                        
            else:
                break
            
        # ansFirst.val, ansSecond.val = ansSecond.val, ansFirst.val
        
        return [ansSecond.val, ansFirst.val]