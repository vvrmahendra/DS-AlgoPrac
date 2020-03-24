"""Evaluate Expression
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. 
Input Format
The only argument given is character array A.
Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.
For Example
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9"""

def evalRPN(A):
    s = []
    evel = {'+': lambda a,b:a+b,
        '*': lambda a,b:a*b,
        '-': lambda a,b:a-b,
        '/': lambda a,b:a//b
    }
    for i in A:
        if i in ['+','-', '*', '/']:
            second = s.pop()
            first = s.pop()
            s.append(evel[i](first, second))
            
        else:
            s.append(int(i))
            
    return s.pop()