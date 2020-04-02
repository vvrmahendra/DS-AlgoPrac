"""ZigZag Level Order Traversal BT
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between). Example : Given binary tree
    3
   / \
  9  20
    /  \
   15   7
return
[
         [3],
         [20, 9],
         [15, 7]
]"""


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if not A:
            return [[]]
            
        from collections import deque
        q = deque()
        q.append(A)
        q.append(None)
        ans = []
        flag = True
        while q:
            level = []
            if not q[0]:
                q.popleft()
            else:
                while q[0]:
                    temp = q.popleft()
                    level.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                        
                q.append(None)        
                if flag:
                    ans.append(level)
                else:
                    ans.append(level[::-1])
                    
                flag = not flag
                
        return ans