"""Simplify Directory Path
Given a string A representing an absolute path for a file (Unix-style). Return the string A after simplifying the absolute path. Note:
Absolute path always begin with '/' ( root directory ).
Path will not have whitespace characters.

Input Format
The only argument given is string A.
Output Format
Return a string denoting the simplified absolue path for a file (Unix-style).
For Example
Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"""

def simplifyPath(A):
    stack = []
    for i in A.split('/'):
        if i == ".":
            pass
        elif i == "..":
            if stack:
                stack.pop()
        elif i:
            stack.append(i)
    
    ans = ("/".join(stack))  
    return "/"+ans if ans else "/"