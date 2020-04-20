"""Subarrays Xor less Than B
Problem Description
Given an array of integers A. Find and return the number of subarrays whose xor values is less than B. NOTE: As the answer can be very large, return the answer modulo (109+7).   


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 105
1 <= B <= 106


Input Format
The argument given is the integer array A
Second argument is an integer B.


Output Format
Return an integer denoting the number of subarrays whose xor values is less than B.


Example Input
Input 1:
 A = [8, 3, 10, 2, 6, 7, 6, 9, 3]
 B = 3
Input 2:
 A = [9, 4, 3, 11]
 B = 7
       


Example Output
Output 1:
 5
Output 2:
 3
       


Example Explanation
Explanation 1:
 Generate all the subarrays and their corresponding xor and there are only 5 such subaraays which have xor less than 3.
Explanation 2:
 Subarrays with xor < 7 are : [9, 4, 3, 11], [4] and [3].
 So, the answer is 3.
"""


import math
class Node:
    def __init__(self):
        self.val = {}
        self.ind = [0, 0]
        
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.trie = self.getNode()
        
    def getNode(self):
        return Node()
        
    @staticmethod
    def decToBin(a,n):
        temp = bin(a)[2:]
        if len(temp) < n:
            temp = "0"*(n-len(temp))+temp
        return [int(i) for i in temp]
        # ans = [0]*n
        # i = n-1
        # while a:
        #     if a%2 == 1:
        #         ans[i] = 1
        #     i, a = i-1, a//2
        # return ans
        
    def insert(self, ele):
        cur = self.trie
        for bit in ele:
            if bit not in cur.val:
                cur.val[bit] = self.getNode()
                
            cur.ind[bit] += 1
            cur = cur.val[bit]

        
    def subsolution(self, head, ele, B,ans,n):
        # ans = 0
        # n = 0
        while head and n < len(B):
            if B[n] == 0 and ele[n] == 1:
                if 1 in head.val:
                    head = head.val[1]
                    n = n+1
                else:
                    head = None
            
            elif B[n] == 0 and ele[n] == 0:
                if 0 in head.val:
                    head = head.val[0]
                    n = n+1
                else:
                    head = None
            elif B[n] == 1 and ele[n] == 1:
                ans[0] += head.ind[1]
                if 0 in head.val:
                    head = head.val[0]
                    n = n+1
                else:
                    head = None
                    
            elif B[n] == 1 and ele[n] == 0:
                ans[0] += head.ind[0]
                if 1 in head.val:
                    head = head.val[1]
                    n = n+1
                else:
                    head = None
            
        
    def solve(self, A, B):
        pre = [0]*len(A)
        pre[0] = A[0]
        for i in range(1,len(A)):
            pre[i] = pre[i-1]^A[i]
        pre = [0]+pre
        n = max([int(math.log2(i)) if i else 0 for i in pre]+[int(math.log2(B)) if i else 0])+1
        arr = [self.decToBin(i,n) for i in pre]
        b = self.decToBin(B,n)
        self.insert(arr[0])
        total = 0
        for i in range(1, len(arr)):
            ans = [0]
            self.subsolution(self.trie, arr[i], b, ans,0)
            total += ans[0]
            self.insert(arr[i])
        mod = 10**9+7    
        return total%mod