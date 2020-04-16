"""
K DISTANCE
Problem Description
Given a balanced binary tree of integers and an integer B, count the number of pairs (a, b) where:
a is ancestor of b.
Absolute difference between value of node a and value of node b <= B
     


Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= node values <= 105
1 <= B <= 105


Input Format
First argument is the root of the binary tree.
Second argument is an integer B.


Output Format
Return an integer denoting the number of pairs satisfying the condition.


Example Input
Input 1:
        1
      /   \
     2    3
    / \  / \
   4   5 6  7
  /
 8
 B = 1
Input 2:
    1
  /   \
 2     3
  \
   4
 B = 2
  


Example Output
Output 1:
 1
Output 2:
 3
     


Example Explanation
Explanation 1:
 Only possible pair is (1, 2).
Explanation 2:
 3 possible pair exists: {(1, 2), (2, 4), (1, 3)}."""



# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.nodes = {}
        
    def solve(self, A, B):
        if not A: return 0
        def helper(A):
            if A.left:
                self.nodes[A.left] = self.nodes[A]+[A.val]
                helper(A.left)
            if A.right:
                self.nodes[A.right] = self.nodes[A]+[A.val]
                helper(A.right)
        
        
        self.nodes[A] = []
        helper(A)
        ans = 0
        # print(type(self.nodes))
        for node in self.nodes:
            vals = self.nodes[node]
            ans += sum([1 if abs(node.val-i)<= B else 0 for i in vals])
        return ans