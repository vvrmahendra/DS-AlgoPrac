"""BST nodes in a range
Given a binary search tree of integers. You are given a range [B, C]. Return the count of the number of nodes that lies in this range. Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= B < = C <= 10^9 
For Example
Input 1:
            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20
Output 1:
    5

Input 2:
             8
            / \
           6  21
          / \
         1   4

        B = 2
        C = 20
Output 2:
    3"""

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def __init__(self):
        self.c = 0
        self.f = None
        self.s = None
    def solve(self, A, B, C):
        def helper(A):
            if not A: return
            
            helper(A.left)
            self.c += 1
            if not self.f and A.val >= B:
                self.f = self.c
                
            if self.f and A.val <= C:
                self.s = self.c
                
            helper(A.right)
            
        helper(A)
        # print(self.s, self.f)
        return abs(self.s-self.f+1) if self.s and self.f else 0