"""Largest Number
Given a list of non negative integers, arrange them such that they form the largest number. 
For example: Given [3, 30, 34, 5, 9], the largest formed number is 9534330. 
Note: The result may be very large, so you need to return a string instead of an integer."""


"""

Here I have done in 2 approaches.
1) Modifying cmp key functionality using functools
2) For every element getting the signicance of the digit among rest of digits having same size. (This solution is Insane)

"""


def largestNumberCmp(A):
    def cmp(a,b):
        a = str(a)
        b = str(b)
        if int(a+b) < int(b+a):
            return 1
        elif int(a+b) > int(b+a):
            return -1
        else:
            return 0

    from functools import cmp_to_key
    sort_ = sorted(A,key = cmp_to_key(cmp))
    ans = ""
    if sort_[0] == 0:
        return 0
    for i in sort_:
        ans += str(i)
    return ans



def largestNumber( A):
    def cmp(a):
        len_ = len(str(a))
        return a/((10**len_)-1)
    
    Arr = sorted(A,key = cmp, reverse = True)
    if Arr[0] == 0:
        return 0
    ans = ""
    for i in Arr:
        ans += str(i)
        
    return ans


if __name__ == "__main__":
    a = [0,0,0,0]
    b = [3,30,9,10]
    print(largestNumberCmp(a))
    print(largestNumber(b))
