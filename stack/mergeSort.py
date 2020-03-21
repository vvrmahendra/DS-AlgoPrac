"""Sorting an array using merge sort using stack data structure"""


def mergesort(S1, S2):
    print(S1, S2)
    if not S1:
        return S2
    if not S2:
        return S1
    
    S3 = []
    while S1 and S2:
        if S1[-1] >= S2[-1]:
            S3.append(S1.pop())
        else:
            S3.append(S2.pop())
            
    while S1:
        S3.append(S1.pop())
    while S2:
        S3.append(S2.pop())
        
    merged = []
    while S3:
        merged.append(S3.pop())
        
    return merged

def divide(A):
    if len(A) <= 1:
        return A
    B = []
    while len(A) - len(B) > 1:
        B.append(A.pop())
        
    B1 = []
    while B:
        B1.append(B.pop())
        
    first = divide(A)
    second = divide(B1)
    return mergesort(first, second)


if __name__ == "__main__":
    out = divide([2,1,3,1])