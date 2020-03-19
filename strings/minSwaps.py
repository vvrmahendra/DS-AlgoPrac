"""Regroup 0's and 1's using Minimum Swaps
Regroup 0's and 1's using Minimum Swaps
Given a string S, count minimum no. of swaps needed to regroup 0's and 1's. 
After all swaps final string will look like all 0's followed by all 1's or all 1's followed by all 0's. 
Swap operation swaps two adjacent characters (01 -> 10, 10 -> 01, 00 -> 00 and 11 -> 11). Note:
 Try to solve the problem using constant extra space. Expected time complexity is worst case O(length of S). 
Examples: S: 000111 Answer: 0 S: 1110101 Answer: 3 Explanation: 1110101 -> 1111001 -> 1111010 -> 1111100"""


def solve(A):
    n = len(A)
    ones = sum([1 for i in A if int(i)])
    sun_indexes = sum([i for i in range(n) if int(A[i])])
    ans1 = sun_indexes-(ones)*(ones-1)//2
    ones = sum([1 for i in A if not int(i)])
    sun_indexes = sum([i for i in range(n) if not int(A[i])])
    ans2 = sun_indexes-(ones)*(ones-1)//2
    return min(ans1, ans2)