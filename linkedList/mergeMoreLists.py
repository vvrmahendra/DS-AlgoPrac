"""Flatten a linked list
Given a linked list where every node represents a linked list and contains two pointers of its type:
Pointer to next node in the main list (right pointer)
Pointer to a linked list where this node is head (down pointer). All linked lists are sorted.
You are asked to flatten the linked list into a single list. Use down pointer to link nodes of the flattened list. The flattened linked list should also be sorted. 
Input Format
The only argument given is head pointer of the doubly linked list.
Output Format
Return the head pointer of the Flattened list. 
Constraints
1 <= Total nodes in the list <= 100000
1 <= Value of node <= 10^9
For Example
Input 1:
       3 -> 4 -> 20 -> 20 ->30
       |    |    |     |    |
       7    11   22    20   31
       |               |    |
       7               28   39
       |               |
       8               39

Output 1:
3 -> 4 -> 7 -> 7 -> 8 -> 11 -> 20 -> 20 -> 20 -> 22 -> 28 -> 30 -> 31 -> 39 -> 39 """

def flatten(root):
    if not root:
        return root
        
    heads = []
    node = root
    while node:
        heads.append(node)
        node = node.right
    
    n = len(heads)
    index_ = -1
    min_ = float('inf')
    for i in range(n):
        if heads[i].val < min_:
            index_ = i
            min_ = heads[i].val
            
    ans = heads[index_]
    heads[index_] = heads[index_].down
    temp = ans
    while True:
        index_ = -1
        min_ = float('inf')
        for i in range(n):
            if heads[i] and heads[i].val < min_:
                index_ = i
                min_ = heads[i].val
                
        if min_ == float('inf'):
            break
        
        temp.down = heads[index_]
        heads[index_] = heads[index_].down
        temp = temp.down
    return ans