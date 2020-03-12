"""Colorful Number
For Given Number N find if its COLORFUL number or not Return 0/1 COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:
N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1"""


def colorful(A):
    Arr = []
    while A > 0:
        Arr.append(A%10)
        A = A//10
        
    i , j = 0, len(Arr)-1    
    while i < j:
        Arr[i], Arr[j] = Arr[j], Arr[i]
        i, j = i+1, j-1
        
    
    pre_Arr = [0]*len(Arr)
    pre_Arr[0] = Arr[0]
    
    for i in range(1,len(Arr)):
        pre_Arr[i] = pre_Arr[i-1]*Arr[i]
    
    set_ = set()
    n = len(pre_Arr)        
    for i in range(-1,n-1):
        for j in range(i+1,n):
            if i == -1:
                if pre_Arr[j] in set_:
                    return 0
                else:
                    set_.add(pre_Arr[j])
            else:
                if pre_Arr[j]//pre_Arr[i] in set_:
                    return 0
                else:
                    set_.add(pre_Arr[j]//pre_Arr[i])
                    
    return 1
        