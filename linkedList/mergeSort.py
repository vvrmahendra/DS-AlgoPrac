# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    @staticmethod
    def merge(A, B):
        if not A:
            return B
        if not B:
            return A
        
        if A.val < B.val:
            new = A
            A = A.next
        else:
            new = B
            B = B.next
            
        temp = new
        while A and B:
            if A.val < B.val:
                temp.next = A
                A = A.next
                temp = temp.next
            else:
                temp.next = B
                B = B.next
                temp = temp.next
                
        if A:
            temp.next = A
        if B:
            temp.next = B
            
        return new
    @staticmethod
    def divide(A):
        
        if not A:
            return (None, None)
        
        if not A.next:
            return (A, None)
        
        slow = A
        fast = A
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None
        # print(second.val)
        return (A, second)
                
    
    def sortList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        first, second = self.divide(head)
        firstSort = self.sortList(first)
        secondSort = self.sortList(second)
        return self.merge(firstSort, secondSort)
        
        
        