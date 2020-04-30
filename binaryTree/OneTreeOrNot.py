"""Check if given Preorder, Inorder and Postorder traversals are of same tree
Given 3 array of integers A, B and C. A represents preorder traversal of a binary tree. B represents inorder traversal of a binary tree. C represents postorder traversal of a binary tree. Check whether these tree traversals are of the same tree or not. If they are of same tree return 1 else return 0. 
Input Format
The arguments given are integer arrays A, B, and C.
Output Format
Return 1 if they are of same tree else return 0.
Constraints
1 <= length of the array <= 1000
all arrays are of same length
1 <= A[i], B[i], C[i] <= 10^9 
For Example
Input 1:
    A = [1, 2, 4, 5, 3]
    B = [4, 2, 5, 1, 3]
    C = [4, 5, 2, 3, 1]
Output 1:
    1

Input 2:
    A = [1, 5, 4, 2, 3]
    B = [4, 2, 5, 1, 3]
    C = [4, 1, 2, 3, 5]

Output 2:
    0"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def __init__(self):
        self.pre = []
	def buildTree(self, A, B):
        if not A:
            return None
            
        if len(A) != len(B):
            return None
            
        head = TreeNode(B[-1])
        n = len(A)
        flag = False
        for i in range(n):
            if A[i] == B[-1]:
                flag = True
                break
            
        if not flag:
            return None
            
        head.left = self.buildTree(A[:i], B[:i])
        head.right = self.buildTree(A[i+1:], B[i:-1])
        return head
        
     
    def PreOrderTravarsal(self, head):
        if not head:
            return None
            
        
        self.pre.append(head.val)
        self.PreOrderTravarsal(head.left)
        self.PreOrderTravarsal(head.right)
        return None
        
    def solve(self, A, B, C):
        if not A:
            return 1
        
        head = self.buildTree(B,C)
        if not head:
            return 0
        self.PreOrderTravarsal(head)
        if self.pre == A:
            return 1
        else:
            return 0
