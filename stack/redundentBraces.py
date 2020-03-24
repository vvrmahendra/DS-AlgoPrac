"""Redundant Braces
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'. Chech whether A has redundant braces or not. Return 1 if A has redundant braces, else return 0. Note: A will be always a valid expression. 
Input Format
The only argument given is string A.
Output Format
Return 1 if string has redundant braces, else return 0.
For Example
Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.

Input 2:
    A = "(a + (a + b))"
Output 2:
    0
    Explanation 2:
        (a + (a + b)) doesn't have have any redundant braces so answer will be 0.
"""


def braces(A):
    s, ans = [], 0
    ope, braces = 0, 0
    
    for i in A:
        # print(i, ans)
        if i == "(":
            braces += 1
            s.append(i)
            
        elif s and i in ['+', '-', '*', '/']:
            ope += 1
            
        elif i == ")":
            s.pop()
            if not s:
                ans += braces-ope
                braces, ope = 0, 0
                
    return 1 if ans else 0