"""
Time Complexity:- O(n**2)
Spcae Complexity:- O(1) InSpace
InStability (We can make it stable if we append to the unsoterd portion instead swaping with the left most element of unsorted portion)
Swaps O(n)

Intuation:- For every loop we are finding min value from unsorted portion and swaping it with left most element of the unsorted portion.
At every point the array is divided into two portions, left which is "absolutely" sorted and right which is not sorted.
By absolute here I mean new element cannot be inserted in between the sorted portion

"""



def selection(A):
    n = len(A)
    for i in range(n-1):
        min_value = A[i]
        min_index = i
        for j in range(i+1,n):
            if min_value > A[j]:
                min_value = A[j]
                min_index = j
                
        A[i],A[min_index] = A[min_index],A[i]
        
    return

if __name__ == "__main__":
    A = [5, 2, 6, 7, 2, 1, 0, 3]  
    selection(A)