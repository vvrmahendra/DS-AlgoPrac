"for [1,2,3] next permutaion is [1,3,2]"


def nextPerm(A):
    n = len(A)
    left = n-1
    while(A[left] <= A[left-1]):
        left -= 1
    
    pivot = left-1
    i = pivot+1
    j = n-1
    while i<=j:
        A[i],A[j] = A[j],A[i]
        i += 1
        j -=1
    
    for i in range(pivot+1,n):
        if A[i] > A[pivot]:
            A[i],A[pivot] = A[pivot],A[i]
            break
    return A