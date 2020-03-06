"""Largest Number
Given a list of non negative integers, arrange them such that they form the largest number. 
For example: Given [3, 30, 34, 5, 9], the largest formed number is 9534330. 
Note: The result may be very large, so you need to return a string instead of an integer."""





def largestNumber(A):
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


if __name__ == "__main__":
    a = [0,0,0,0]
    print(largestNumber(a))
