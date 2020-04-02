"""InorderTraversal without using recursion using stack"""

def inorderTraversal(A):
    if not A:
        return []
    from collections import deque
    s = deque.()
    ans = []
    current = A
    while True:
        if current:
            s.append(current)
            current = current.left
        elif s:
            current = s.pop()
            ans.append(current.val)
            current = current.right
            
        else:
            break
                
    return ans
