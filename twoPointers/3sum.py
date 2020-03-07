"""3 Sum
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
Assume that there will only be one solution 
Example: given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)"""



def threeSumClosest(A, B):
    A.sort()
    ans = float("inf")
    n = len(A)
    for i in range(n):
        left = i+1
        right = n-1
        while left < right:
            sum_temp = A[i]+A[left]+A[right]
            dif = abs(sum_temp-B)
            if dif < abs(ans-B):
                ans = sum_temp
            if sum_temp < B:
                left += 1
            else:
                right -= 1
    return ans