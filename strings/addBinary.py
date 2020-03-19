"""Add Binary Strings
Given two binary strings, return their sum (also a binary string). Example:
a = "100"

b = "11"
Return a + b = "111"."""

def addBinary(A, B):
    n, m = len(A), len(B)
    i , j = n-1, m-1
    carry = 0
    ans = []
    while i >= 0 and j >= 0:
        temp_sum = int(A[i])+int(B[j])+carry
        if temp_sum in [0,1]:
            ans.append(str(temp_sum))
            carry = 0
        else:
            carry = 1
            ans.append(str(temp_sum%2))
            
        i -= 1
        j -= 1
            
    while i >= 0:
        temp_sum = int(A[i])+carry
        if temp_sum in [0,1]:
            ans.append(str(temp_sum))
            carry = 0
        else:
            carry = 1
            ans.append(str(temp_sum%2))
            
        i -= 1
    
    while j >= 0:
        temp_sum = int(B[j])+carry
        if temp_sum in [0,1]:
            ans.append(str(temp_sum))
            carry = 0
        else:
            carry = 1
            ans.append(str(temp_sum%2))
        j -= 1
        
    if carry:
        ans.append(str(carry))
        
    return "".join(ans[::-1])