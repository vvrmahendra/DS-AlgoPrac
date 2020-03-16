"""
There are N people attending to a party. There are A nuber of chacolates of first kind and B number of chacolates of second kind.
We have to distribute these chacolates to N peaople according to the following contraints.
A+B >= N
A person cannot get two varieties of chacolates.
Each person should get atleast one chacolate.

Our goal is to maximise the minimum amount of the chacolates given to all peaople. 
For example N = 4, B = 4, C = 5
we can distribute  1B, 3B, 1C, 4C here minimum chacolate is min(1,3,1,4) = 1
so our answer is 2B, 2B, 2C, 3C here min is 2 we cannot go furthur.
"""

def chacolates(N, A, B):
    ans = 0
    left = 1
    right = max(A,B)
    while left <= right:
        mid = (left+right)//2
        
        temp = 0
        temp = A//mid
        if (N-temp)*mid <= B:
            left = mid+1
            ans = mid
        else:
            right = mid - 1
            
    return ans


chacolates(4, 4, 5)