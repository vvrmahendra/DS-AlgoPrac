"""
Time Complexity:- O(range+n)
Space Complexity:- O(range+n)
Swaps = 0
Not InSpace
Stability


Cons:- It works only when we sort only integers. Range should be low on compare with n
"""



def counting(A):
    high = max(A)
    helper = [0]*(high+1)
    for i in A:
        helper[i] += 1
        
    pre_helper = [0]*(high+1)
    pre_helper[0] = helper[0]
    for i in range(1,high+1):
        pre_helper[i] = pre_helper[i-1]+helper[i]
        
    out_A = [None]*len(A)
    
    for i in range(len(A)-1,-1,-1):
        #helper_index = A[i]
        out_A[pre_helper[A[i]]-1] = A[i]
        pre_helper[A[i]] -= 1
        print(pre_helper)
    return out_A

if __name__ == "__main__":
    A = [4, 2, 2, 8, 3, 3, 1]
    out = counting(A)