"""Reverse the stack in place"""


def InsertBottom(stack, ele):
    if len(stack) == 0:
        stack.append(ele)
        return
    
    temp = stack.pop()
    InsertBottom(stack, ele)
    stack.append(temp)
    return
    

def revrse(stack):
    helper = []
    while len(stack) != 0:
        helper.append(stack.pop())
        
    while  helper:
        InsertBottom(stack, helper.pop())
        
    return

if __name__ == "__main__":
    A = [ 1,2,3,4 ]
    revrse(A)