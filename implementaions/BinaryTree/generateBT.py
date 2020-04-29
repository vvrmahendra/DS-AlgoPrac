from .binaryNode import BinaryNode as Node
from collections import deque
class BT:
    def __init__(self):
        self.head = None

    @staticmethod
    def _getNode(val):
        return Node(val) 

    #inserting using level order traversal. Time Complexity O(number of nodes). Optimal solution than this exists! 
    def insertNode(self, val):
        newNode = self._getNode(val)
        if not self.head:
            self.head = newNode
            return
        
        q = deque()
        q.append(self.head)
        while True:
            curNode = q.popleft()
            if curNode.left:
                q.append(curNode.left)
            elif curNode.val != None:
                curNode.left = newNode
                break

            if curNode.right:
                q.append(curNode.right)
            elif curNode.val != None:
                curNode.right = newNode
                break
    
    """While Inteserting to represent nodes with no left child or right child we have initiated a node with val None. 
    We are removing them after creating the node"""
    def _cleanTree(self, head):
        if head == None:
            return
        
        if head.left:
            if head.left.val == None:
                head.left = None
        if head.right:
            if head.right.val == None:
                head.right = None

        self._cleanTree(head.left)
        self._cleanTree(head.right)


    @classmethod
    def BTFromList(cls, nums):
        Tree = cls()
        for i in nums:
            Tree.insertNode(i)
        Tree._cleanTree(Tree.head)
        return Tree

    def getLevelOrderTravarsal(self):
        ans = []
        q = deque()
        q.append(self.head)
        while q:
            curNode = q.popleft()
            if curNode:
                ans.append(curNode.val)
                q.append(curNode.left)
                q.append(curNode.right)
            else:
                ans.append(None)

        return ans

        

        

        



