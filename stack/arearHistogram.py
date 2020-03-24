"""Largest Rectangle in Histogram
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of the ith histogram's bar. 
Width of each bar is 1. Largest Rectangle in Histogram: 
Example 1 Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]. 
Largest Rectangle in Histogram: 
Example 2 The largest rectangle is shown in the shaded area, which has area = 10 unit. 
Find the area of largest rectangle in the histogram. 
Input Format
The only argument given is the integer array A.
Output Format
Return the area of largest rectangle in the histogram.
For Example
Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
    Explanation 1:
        The largest rectangle is shown in the shaded area, which has area = 10 unit."""

def largestRectangleArea(A):
    n = len(A)
    min_right = [n]*n
    min_left = [-1]*n
    s = []
    i = 0
    while i < n:
        if not s:
            s.append(i)
            i += 1
            continue
        
        while s and A[i] < A[s[-1]]:
            min_right[s.pop()] = i
        
        s.append(i)
        i += 1
        
    i = n-1
    while i > -1:
        if not s:
            s.append(i)
            i -= 1
            continue
        
        while s and A[i] < A[s[-1]]:
            min_left[s.pop()] = i
        
        s.append(i)
        i -= 1
        
    ans = 0
    for i in range(n):
        area = A[i]*(min_right[i]-min_left[i]-1)
        ans = max(ans,area)
    return ans