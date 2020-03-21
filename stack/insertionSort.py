"""Insertion Sort using merge"""


def InsertAtRightPlace(A,ele):
    if not A or A[-1] <= ele:
        A.append(ele)
        return
    
    temp = A.pop()
    InsertAtRightPlace(A, ele)
    A.append(temp)
    
def insertionSort(A):
    helper = []
    while A:
        helper.append(A.pop())
        
    while helper:
        InsertAtRightPlace(A, helper.pop())
        
    return

if __name__ == "__main__":
    A = [5,3,1,2]
    insertionSort(A)
        