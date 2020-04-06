"""Next Pointer Binary Tree
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.
 Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example : Given the following perfect binary tree,
         1
       /  \
      2    5
     / \  / \
    3  4  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL
Note that using recursion has memory overhead and does not qualify for constant space."""





class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        from collections import deque
        q = deque()
        q.append(root)
        q.append(None)
        while q:
            if not q[0]:
                q.popleft()
            else:
                while q[0]:
                    current = q.popleft()
                    current.next = q[0]
                    if current.left:
                        q.append(current.left)
                        
                    if current.right:
                        q.append(current.right)
                        
                q.append(None)
                
        return
            
