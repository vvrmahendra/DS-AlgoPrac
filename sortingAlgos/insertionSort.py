"""
Time Complexity:- O(n**2)
Space Complexity:- O(1) InSpace
Stablity
Swaps are O(n**2)


Intuition:- This is how we arrange playing cards while we play. At a given point left few cards are relatively sorted.
By relative here I mean cards in right side might contain even less values than least of the sorted portion.
"""





def insertion(A):
    if len(A) <= 1:
        return A
    
    
    n = len(A)
    for ele in range(1,n):
        cur_val = A[ele]
        
        prev_ind = ele-1
        while prev_ind >= 0 and A[prev_ind] > cur_val:
            A[prev_ind+1] = A[prev_ind]
            prev_ind -= 1    
        A[prev_ind+1] = cur_val

                
    return

if __name__ == "__main__":
    A = [4,5,-1]
    insertion(A)