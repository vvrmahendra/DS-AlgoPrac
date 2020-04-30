"""Duplicates in binary tree
Given a binary tree of integers. Return whether it contains a duplicate sub-tree of size 2 or more. All node values lie between 0 and 9 inclusive. Return 1 if it contains a duplicate sub-tree of size 2 or more else return 0. Note: Two same leaf nodes are not considered as a subtree, As the size of a leaf node is one. Constraints
1 <= Number of nodes in binary tree <= 10000
0 <= node values <= 9
For Example
Input 1:
            1
          /   \
         2     6
        / \     \
       4   5     2
                / \
               4   5

Output 1:
    1

    Duplicate Subtree     2
                         / \
                        4   5

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5
Output 2:
    0"""


class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.inorder = {}
        self.ans = None
    def solve(self, A):
        def helper(A):
            if not A: return "()"
            
            str_ = "("
            left = helper(A.left)
            str_ = str_+left
            str_ = str_+str(A.val)
            right = helper(A.right)
            str_ = str_+right+')'
            
            if A.left or A.right:
                if str_ in self.inorder:
                    self.ans = True
                else:
                    self.inorder[str_] = 1
                
            return str_
        helper(A)
        return 1 if self.ans else 0
