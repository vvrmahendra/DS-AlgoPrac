"""Difference between odd and even levels
Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level. Note: Consider the level of root node as 1. Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9 
For Example
Input 1:
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Output 1:
    10
    Sum of nodes at odd level = 23
    Sum of ndoes at even level = 13

Input 2:
            1
           /  \
          2    10
           \
            4
Output 2:
    -7
    Sum of nodes at odd level = 5
    Sum of ndoes at even level = 12
"""


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        from collections import deque
        q = deque()
        q.append(A)
        q.append(None)
        ans = 0
        level = 0
        while q:
            if not q[0]:
                q.popleft()
            else:
                level = level+1
                level_sum = 0
                
                while q[0]:
                    current = q.popleft()
                    level_sum += current.val
                    if current.left:
                        q.append(current.left)
                        
                    if current.right:
                        q.append(current.right)
                        
                q.append(None)
                if level%2 == 1:
                    ans = ans+level_sum
                else:
                    ans = ans-level_sum
                    
        return ans