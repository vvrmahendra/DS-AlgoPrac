"""
Implement StrStr
Implement strStr().
 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question. 
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""




#Using KMP Algorithm
def strStrKMP(A, B):
    def lpsTable(A):
        i, j, n = 1, 0, len(A)
        lps = [None]*n
        lps[0] = 0
        while i < n:
            if A[i] == A[j]:
                lps[i] = j+1
                i, j = i+1, j+1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
        
    i = 0
    target = 0
    lps = lpsTable(B)
    
    n, m = len(A), len(B)
    while i < n:
        if A[i] == B[target]:
            i, target = i+1, target+1
        
        if target == m:
            return i-m
            
        elif i < n and A[i]!=B[target]:
            if target != 0:
                target = lps[target-1]
            else:
                i += 1
                
                
    return -1

#Using Rolling Hash algorithm
def strStrRolling(A, B):
    if len(A) == 0 or len(B) == 0 or len(A) < len(B):
        return -1
    n, m = len(A), len(B)
    target = 0
    index = 0
    for i in B:
        temp = (37**index)
        target += ord(i)*temp
        target = target
        index += 1
    
    roll_hash = 0
    index = 0
    for i in range(m):
        temp = (37**index)
        roll_hash += ord(A[i])*temp
        roll_hash = roll_hash
        index += 1
        
    if roll_hash == target:
        return 0
        
    for i in range(1,n-m+1):
        roll_hash -= ord(A[i-1])
        roll_hash = roll_hash//37
        roll_hash += ord(A[m+i-1])*(37**(m-1))
        if roll_hash == target:
            return i
            
    return -1