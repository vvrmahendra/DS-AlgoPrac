Given a non-empty binary tree, find the maximum path sum.

"""For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_ = float('-inf')
        def helper(head):
            nonlocal max_
            left, right = 0, 0
            if head.left:
                left = max(helper(head.left), 0)
            if head.right:
                right = max(helper(head.right), 0)
                
            max_ = max(max_, head.val+left+right)
            return head.val+max(left,right)
        
        helper(root)
        return max_

# other Solution
class SolutionV2:
	# @param A : root node of tree
	# @return an integer
	def maxPathSum(self, A):
        if not A: return 0
        ans = [float('-inf')]
        
        def helper(head):
            if not head:
                return 0
                
            left = helper(head.left)
            right = helper(head.right)
            ans[0] = max(ans[0], left+right+head.val, left+head.val, right+head.val, head.val)
            
            return max(left,right)+head.val
            
        helper(A)
        return ans[0]