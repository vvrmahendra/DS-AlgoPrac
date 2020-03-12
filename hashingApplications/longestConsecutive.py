"""Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence. 
Example: Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1, 2, 3, 4]. 
Return its length: 4. Your algorithm should run in O(n) complexity."""


def longestConsecutive(A):
    set_, ans = set(A), 0
    left = []
    for i in A:
        if i-1 not in set_:
            left.append(i)
            
    for j in left:
        value = 1
        i = j
        while True:
            if i+1 in set_:
                value += 1
                i += 1
            else:
                break
            
        ans = max(ans,value)
        
    return ans