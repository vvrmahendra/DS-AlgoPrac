"""Length of longest palindromic list
Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list. Note: A palindrome list is a list that reads the same backward and forward. Expected memory complexity : O(1) 
Input Format
The only argument given is head pointer of the linked list.
Output Format
Return the length of the longest palindrome list.
Constraints
1 <= length of the linked list <= 2000
1 <= Node value <= 100 
For Example
Input 1:
    2 -> 3 -> 3 -> 3
Output 1:
   3 

Input 2:
    A = 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2
Output 2:
    5"""

def solve(A):
    if not A.next:
        return 1
        
    ans = 0
    ite = 0
    cur = A
    pre = None
    while cur:
        if ite%2 == 0:
            num = 1
            t1 = pre
            t2 = cur.next
            while t1 and t2:
                if t1.val == t2.val:
                    t1 = t1.next
                    t2 = t2.next
                    num += 2
                else:
                    break
            ans = max(num, ans)
            
            ite += 1
            temp = pre
            pre = cur
            
            cur = cur.next
            pre.next = temp
            
        else:
            num = 0
            t1 = cur
            t2 = pre
            while t1 and t2:
                if t1.val == t2.val:
                    t1 = t1.next
                    t2 = t2.next
                    num += 2
                else:
                    break
                
            ans = max(ans, num)
            ite += 1
            
    return ans
            
            
            