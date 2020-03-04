"""
Time Complexity:- O(nlogn)
Space Complexity:- O(nlogn) [this is the crazy one google it for proof] Not InPlace
Stability:- yes

intuation:- Divide and Conquer
"""


def merge(A,B):
    n = len(A)
    m = len(B)
    out = []
    
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
            
    while i < n:
        out.append(A[i])
        i += 1
    
    while j < m:
        out.append(B[j])
        j += 1
        
    return out

def mergeSort(A):

    if len(A) <= 1:
        return A
    
    n = len(A)
    mid = n//2
    left = A[:mid]
    right = A[mid:]
    

    
    update_left = mergeSort(left)
    update_right = mergeSort(right)
    return merge(update_left,update_right)

if __name__ == "__main__":
    A = []
    B = []
    Arr = [-1,10,6,5,12,10,9,1]
    out = mergeSort(Arr)