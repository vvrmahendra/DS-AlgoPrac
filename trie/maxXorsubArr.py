"""Maximum XOR Subarray
Problem Description
Given an array A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N which has maximum XOR value. NOTE: If there are multiple subarrays with same maximum value, return the subarray with minimum length. If length is same, return the subarray with minimum starting index.   


Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 109


Input Format
First and only argument is an integer array A.


Output Format
Return an integer array B of size 2. B[0] is the starting index(1-based) of the subarray and B[1] is the ending index(1-based) of the subarray.


Example Input
Input 1:
A = [1, 4, 3]
Input 2:
A = [8]
  


Example Output
Output 1:
[2, 3]
Output 2:
[1, 1]
  


Example Explanation
Explanation 1:
There are 6 possible subarrays of A:
subarray            XOR value
[1]                     1
[4]                     4
[3]                     3
[1, 4]                  5 (1^4)
[4, 3]                  7 (4^3)
[1, 4, 3]               6 (1^4^3)

[4, 3] subarray has maximum XOR value. So, return [1, 2].
Explanation 2:
There is only one element in the array. So, the maximum XOR value is equal to 8 and the only possible subarray is [1, 1]. 
"""

class Node:
    def __init__(self):
        self.kids = [None, None]
        self.ind = None
class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.trie = Node()
        
    def create(self, A):
        for i, arr in enumerate(A):
            cur = self.trie
            for bit in arr:
                if not cur.kids[bit]:
                    cur.kids[bit] = Node()
                cur = cur.kids[bit]
            cur.ind = i
        
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
        pre = [0]*len(A)
        pre[0] = A[0]
        for i in range(1,len(A)):
            pre[i] = pre[i-1]^A[i]
        pre = [0]+pre
        del A
        import math
        n = max([int(math.log2(i)) if i else 0 for i in pre])+1
        arr = [self.decBin(i,n) for i in pre]
        del pre
        self.create(arr)
        ans = float('-inf')
        first, second = -1, -1
        for i, num in enumerate(arr):
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
            secondTemp = cur.ind
            # print(temp, num)        
            if ans <= temp :
                if ans < temp:
                    ans = temp
                    first, second = i, secondTemp
                else:
                    if abs(secondTemp-i) < abs(second-first):
                        first, second = i, secondTemp
                
            if first > second:
                first, second = second, first
        return [first+1, second]


            
        
