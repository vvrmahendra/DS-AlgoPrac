"""Given an Array of numbers You have to find all possible non-empty subsets of the array of numbers and then, for each subset, find the difference between the largest and smallest numbers in that subset Then add up all the differences to get the number. As the number may be large, output the number modulo 1e9 + 7 (1000000007).
Example:

A = [1, 2]

All subsets
[1]    largest-smallest = 1 - 1 = 0
[2]    largest-smallest = 2 - 2 = 0
[1 2]  largest-smallest = 2 - 1 = 1

Sum of the differences = 0 + 0 + 1 = 1

So resultant number is 1"""




def solve(self, A):
    A.sort()
    mod = 10**9+7
    
    ans = 0
    n = len(A)
    for i in range(n):
        value = (A[i]*(2**(i)-2**(n-i-1)))%mod
        ans = (ans+value)%mod
        
    return ans