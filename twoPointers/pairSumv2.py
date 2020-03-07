"""Count of pairs with the given sum II
Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B. Since the number of such pairs can be very large, return number of such pairs modulo (109+7). 
Input Format
The first argument given is the integer array A.
The second argument given is integer B.
Output Format
Return the number of pairs for which sum is equal to B modulo (10^9+7).
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
1 <= B <= 10^9
For Example
Input 1:
    A = [1, 1, 1, 2, 3]
    B = 4
Output 1:
    3

Input 2:
    A = [1, 2, 2, 3, 4]
    B = 5
Output 2:
    3"""



def solve(A, B):
    n = len(A)
    i = 0
    j = n-1
    ans = 0
    while i < j:
        temp_A = A[i]
        temp_B = A[j]
        if A[i]+A[j] < B:
            i = i+1
        elif A[i]+A[j] > B:
            j = j-1
        else:
            left = 1
            while i < n-1  :
                if A[i+1] == A[i]:
                    left += 1
                    i = i+1
                else:
                    i = i+1
                    break
            right = 1
            while j >0 :
                if A[j-1] == A[j]:
                    right += 1
                    j -= 1
                else:
                    j -= 1
                    break
            if temp_A == temp_B:
                ans = ans + left*(left-1)//2
            else:
                ans = ans+left*right
    return ans%(10**9+7)
                