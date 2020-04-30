"""2-Sum Binary Tree
Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K. Return 1 to denote that two such nodes exist. Return 0, otherwise. Notes
Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :
Input 1: 

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2: 

T:        10
         / \
        9   20

K = 40

Return: 0
"""


class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def t2Sum(self, A, B):
        if not A:
            return 0
        from collections import deque
        first = A
        second = A
        fs = deque()
        ss = deque()
        while True:
            if first:
                fs.append(first)
                first = first.left
                
            elif second:
                ss.append(second)
                second = second.right
                
            elif fs and ss and fs[-1].val+ss[-1].val == B:
                if fs[-1] != ss[-1]:
                    return 1
                else:
                    first = fs.pop().right
                    second = ss.pop().left
                
            elif fs and ss and fs[-1].val+ss[-1].val < B:
                first = fs.pop().right
            elif fs and ss:
                second = ss.pop().left
                
            else:
                break
            
        return 0