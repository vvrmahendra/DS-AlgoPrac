"""Merge K Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Example :
1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in
1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Node:
    def __init__(self, A):
        self.A  = A
    
    def __eq__(self, A):
        return self.A.val == other.A.val
    def __ne__(self, A):
        return self.A.val != other.A.val
    def __lt__(self, other):
        return self.A.val < other.A.val
    def __gt__(self, other):
        return self.A.val > other.A.val
    def __le__(self, other):
        return self.A.val <= other.A.val
    def __ge__(self, other):
        return self.A.val >= other.A.val

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        import heapq as hq
        heap = [Node(i) for i in A if i]
        hq.heapify(heap)
        ans = hq.heappop(heap)
        
        ans = ans.A
        if ans.next:
            hq.heappush(heap,Node(ans.next))
        cur = ans
        while heap:
            temp = hq.heappop(heap)
            temp = temp.A
            cur.next = temp
            cur = cur.next
            if temp.next:
                hq.heappush(heap, Node(temp.next))
                
        return ans
        