"""Palindrome List
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively. Notes:
Expected solution is linear in time and constant in space.
For example,
List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
×"""
def lPalin(A):
    n, temp = 0, A
    while temp:
        n, temp = n+1, temp.next
        
    if n <= 1:
        return 1
    if n == 2:
        if A.val == A.next.val:
            return 1
        else:
            return 0

    iter, middle = n//2, A

    for _ in range(iter):
        middle = middle.next
        
    prev, temp = middle, middle.next
    while temp:
        next = temp.next
        if not next:
            second_head = temp
        temp.next = prev
        prev = temp
        temp = next

    if A.val != second_head.val:
        return 0

    for _ in range((n-1)//2):
        A, second_head = A.next, second_head.next
        if A.val != second_head.val:
            return 0
            
    return 1
        