"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level). Example : Given binary tree
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level order traversal of the tree when depth of the tree is much greater than number of nodes on a level."""


def levelOrder(A):
    if not A:
        return [[]]
    from collections import deque
    q = deque()
    q.append(A)
    q.append(None)
    ans = []
    while q:
        level = []
        if not q[0]:
            q.popleft()
            
        else:
            while q[0]:
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                    
                level.append(temp.val)
            
            ans.append(level)
            q.append(None)
        
    return ans