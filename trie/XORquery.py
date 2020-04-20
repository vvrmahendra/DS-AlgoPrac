"""XOR Queries on Tree
Problem Description
Given a tree with A nodes and A-1 edges which is rooted at node 1. There are C queries and for each query you are given two integers d (the node number) and e and you have to find the maximum value when e is xor’ed with any of the ancestors of d or d itself. More formally, find the maximum value which can be obtained when e is XOR with any node in the path from d to the root. NOTE: XOR is the bitwise XOR operator for example, 1 XOR 1 = 0 and 1 XOR 0 = 1 etc. 


Problem Constraints
2 <= A <= 100000 |B| = A-1 and B[i] <= i for all i from 1 till A-1
1 <= C <= 300000
|D| = |E| = C
1 <= D[i] <= A
1 <= E[i] <= 300000


Input Format
The first argument given is the Integer A.
The second argument given is the parent array B, where B[i] denotes the parent of (i+1)'th node for all i from 1 to A-1.
Note: Size of the array B is A-1 and its indexing starts form 1.
The third argument given is the Integer C denoting the number of queries.
The fourth argument given is the array D, where D[i] denotes the value of d for the i'th query.
The fifth argument given is the array E, where E[i] denotes the value of e for the i'th query.


Output Format
Return the integer array where each index denotes the answer for every query in the same order as input.


Example Input
Input 1:
 A = 8
 B = [1, 1, 2, 2, 3, 3, 1]
 C = 5
 D = [2, 3, 5, 6, 8]
 E = [1, 1, 5, 4, 10]
Input 2:
 A = 3
 B = [1, 1]
 C = 2
 D = [2, 3]
 E = [3, 1]


Example Output
Output 1:
 [3, 2, 7, 7, 11]
Output 2:
 [2, 2]


Example Explanation
Explanation 1:
 For first query, d = 2 and e = 1, the path from 1 to 2 will be 1 -> 2, so the maximum value will be 3 i.e 1 ^ 2.
 Likewise we will get the result for all other queries.
Explanation 2:
 For first query, d = 2 and e = 3, the path from 1 to 2 will be 1 -> 2, so the maximum value will be 2 i.e 3 ^ 1.
 For second query, d = 3 and e = 1, the path from 1 to 3 will be 1 -> 3, so the maximum value will be 2 i.e 1 ^ 3."""

from math import log2
import sys
sys.setrecursionlimit(150000)
class node:
    def __init__(self):
        self.val = {}
        self.fre = {}
        
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : integer
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def __init__(self):
        self.trie = node()
        self.len_ = None
    def parseTree(self, head):
        if not head: return
        for i in head.val:
            print(i, head.fre[i], end = "|")
            self.parseTree(head.val[i])
    
    def decToBin(self, a):
        n = self.len_
        temp = bin(a)[2:]
        if len(temp) < n:
            temp = "0"*(n-len(temp))+temp
        return [int(i) for i in temp]
    def insert(self, arr):
        cur = self.trie
        for bit in arr:
            if bit not in cur.val:
                cur.val[bit] = node()
                cur.fre[bit] = 1
            else:
                cur.fre[bit] += 1
            cur = cur.val[bit]
            
    def delete(self, arr):
        cur = self.trie
        for bit in arr:
            if cur.fre[bit] > 1:
                cur.fre[bit] -= 1
                cur = cur.val[bit]
            else:
                cur.val.pop(bit)
                cur.fre.pop(bit)
                break
            
    def getMax(self, arr):
        ans = 0
        cur = self.trie
        for bit in arr:
            nb = int(not bit)
            if nb in cur.val:
                ans = (ans << 1)+1
                cur = cur.val[nb]
            else:
                ans = (ans << 1)
                cur = cur.val[bit]
                
        return ans
        
    def parse(self, i, dict_, q, ans):
        if i not in dict_:
            return
        for ele in dict_[i]:
            # print("----------------")
            # print(ele)
            # self.parseTree(self.trie)
            temparr = self.decToBin(ele)
            # self.parseTree(self.trie)
            self.insert(temparr)
            if ele in q:
                for e in q[ele]:
                    #print(e)
                    maxtemp = self.getMax(self.decToBin(e[0]))
                    ans[e[1]] = maxtemp
                    
                # ans[ele] = temp
                
            self.parse(ele, dict_, q, ans)
            self.delete(temparr)
            # self.parseTree(self.trie)
                    
                
    def solve(self, A, B, C, D, E):
        n = len(B)
        dict_ = {}
        for i in range(n):
            if B[i] in dict_:
                dict_[B[i]].append(i+2)
            else:
                dict_[B[i]] = [i+2]
                
        q = {}
        for i in range(len(D)):
            if D[i] in q:
                q[D[i]].append([E[i], i])
            else:
                q[D[i]] = [[E[i], i]]
        max_ele = max(A, max(E))
        self.len_ = int(log2(max_ele))+1
        ans = [None]*len(D)
        self.insert(self.decToBin(1))
        if 1 in q:
            for e in q[1]:
                #print(e)
                maxtemp = self.getMax(self.decToBin(e[0]))
                ans[e[1]] = maxtemp
        self.parse(1, dict_, q, ans)
        return ans