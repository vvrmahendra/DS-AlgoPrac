"""
Time Complexity:- O(n**2)
Space Complexity:- O(1) InSpace
Stablity
Swaps:- O(n**2)

Intuition:- It is like bubble is growing from left to right. For each step we are comparing every adjacent eleents and moving bigger element
towards right side. So at every instance we have array with two parts left which is unsorted and the right which is absolutely sorted.
By absolute here I mean new element cannot be inserted in between the sorted portion


"""


def bubble(A):
    n = len(A)
    if n <= 1:
        return A
    
    last = n-1
    while last >= 0:
        flag = 1
        for i in range(last):
            
            if A[i+1] < A[i]:
                A[i+1],A[i] = A[i],A[i+1]
                flag = 0
                
        if flag == 1:
            
            break
                
        last -= 1
        
    return

if __name__ == "__main__":
    A = [-2, 45, 0, 11, -9]
    bubble(A)