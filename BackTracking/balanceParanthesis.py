"""Remove Invalid Parentheses
Given a string A consisting of lowercase English alphabets and parentheses '(' and '). Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results. You can return the results in any order. 
 Input Format
The only argument given is string A.
Output Format
Return all possible strings after removing the minimum number of invalid parentheses.
Constraints
1 <= length of the string <= 20
For Example
Input 1:
    A = ""()())()"
Output 1:
     ["()()()", "(())()"]
     Explanation 1:
        By removing 1 parentheses we can make the string valid.
                1. Remove the parentheses at index 4 then string becomes : "()()()"
                2. Remove the parentheses at index 2 then string becomes : "(())()"



Input 2:
    A = "(a)())()"
Output 2:
    ["(a)()()", "(a())()"]
"""


def solve(A):
    global ans,sz
    ans = []
    sz = 0
    def paranthesis(A, idx, value, s):
        n = len(A)
        if value < 0:
            return
        
        if idx == n:
            if value == 0:
                global ans
                global sz
                if len(s) > sz:
                    sz = len(s)
                    ans = []
                    ans.append(s)
                elif len(s) < sz:
                    return
                
                else:
                    if s not in ans:
                        ans.append(s)
                    
            return
        
        if A[idx] not in ['(',')']:
            s = s+A[idx]
            paranthesis(A, idx+1, value, s)
            return
        paranthesis(A,idx+1,value,s)
        s = s+A[idx]
        if A[idx] == '(':
            paranthesis(A, idx+1, value+1, s)
        else:
            paranthesis(A, idx+1, value-1, s)
            
    paranthesis(A,0,0,'')
    return ans