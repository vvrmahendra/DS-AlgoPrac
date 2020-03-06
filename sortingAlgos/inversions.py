"""INVERSIONS
Given an array A, count the number of inversions in the array. Formally speaking, two elements A[i] and A[j] form an inversion if A[i] > A[j] and i < j Example:
A : [2, 4, 1, 3, 5]
Output : 3
as the 3 inversions are (2, 1), (4, 1), (4, 3)."""


def merge(A,B,ans):
    out = []
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    while i < n and j < m:
        if B[j] < A[i]:
            ans += n-i
            out.append(B[j])
            j += 1
        else:
            out.append(A[i])
            i += 1
            
    while i < n:
        out.append(A[i])
        i += 1
    while j < m:
        out.append(B[j])
        j += 1
        
    return (out,ans)


def mergeSort(A):
    n = len(A)
    if n <= 1:
        return (A,0)
    ans = 0
    mid = n//2
    left = A[:mid]
    right = A[mid:]
    
    left_sort = mergeSort(left)
    ans += left_sort[1]
    left_sort = left_sort[0]
    right_sort = mergeSort(right)
    ans += right_sort[1]
    right_sort = right_sort[0]
    return merge(left_sort,right_sort, ans)

if __name__ == "__main__":
    A = [2, 4, 1, 3, 5]
    out = mergeSort(A)
    print(out)