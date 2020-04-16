"""Maximum XOR of Two Numbers in an Array
Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array. 
Input Format
The only argument given is the integer array A.
Output Format
Return the maximum result of A[i] XOR A[j].
Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    7

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    117
"""


class Node:
    def __init__(self):
        self.kids = [None, None]
class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.trie = Node()
        
    def create(self, A):
        for arr in A:
            cur = self.trie
            for bit in arr:
                if not cur.kids[bit]:
                    cur.kids[bit] = Node()
                cur = cur.kids[bit]
        
    @staticmethod
    def decBin(A, n):
        ans = [0]*n
        i = n-1
        while A:
            if A%2 == 1:
                ans[i] = 1
            A = A>>1
            
            i = i-1
        return ans
    def solve(self, A):
        import math
        n = max([int(math.log2(i)) if i else 0 for i in A])+1
        arr = [self.decBin(i,n) for i in A]
        self.create(arr)
        ans = float('-inf')
        for num in arr:
            temp = 0
            cur = self.trie
            
            for bit in num:
                nb = not bit
                if cur.kids[nb]:
                    temp = (temp <<1)+ 1
                    cur = cur.kids[nb]
                else:
                    temp = (temp << 1)
                    cur = cur.kids[bit]
            # print(temp, num)        
            ans = max(ans, temp)
            
        return ans

        
