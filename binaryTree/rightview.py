"""Right view of Binary tree
Given a binary tree of integers. Return an array of integers representing the right view of the Binary tree. Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side. Constraints
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
    [1, 3, 7, 8]

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5
Output 2:
    [1, 3, 4, 5]
"""





class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        from collections import deque
        if not A:
            return []
            
        q = deque()
        q.append(A)
        ans = [A.val]
        q.append(None)
        while q:
            # print([i.val if i else None for i in list(q)])
            if not q[0]:
                q.popleft()
                if  q :
                    ans.append(q[0].val)
                    
            else:
                while q[0]:
                    current = q.popleft()
                    if current.right:
                        q.append(current.right)
                    if current.left:
                        q.append(current.left)
                        
                    
                if q[-1]:    
                    q.append(None)    
        return ans