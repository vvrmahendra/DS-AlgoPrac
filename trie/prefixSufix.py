"""Prefix and Suffix
Problem Description
Given a list of N words denoted by string array A of size N. You have to answer Q queries denoted by string array B, for each query you have a string S of size M, find the number of words in the list A which have string S as a prefix and suffix. NOTE: The size M for all strings in the queries remains same.    


Problem Constraints
1 <= N <= 105 1 <= |A[i]| <= 1000 1 <= Q, M <= 1000 Sum of length of all N words <= 106    


Input Format
First argument is a string array A of size N denoting the list of words. Second argument is a string array B of size Q denoting the queries.    


Output Format
Return an integer array of size Q denoting the answer of each query.


Example Input
Input 1:
 A = ["abaaba", "aaveaa", "aecdsacea", "abaaxbqaba"]
 B = ["aba", "aec", "aav", "aab"]
Input 2:
 A = ["cazqzqzac", "cadssac", "parrot"]
 B = ["caz", "cad"]
   


Example Output
Output 1:
 [2, 1, 0, 0]
Output 2:
 [1, 0]
   


Example Explanation
Explanation 1:
 2 word "abaaba" and "abaaxbqaba" has both prefix and suffix "aba".
 1 word "aecdsacea" has both prefix and suffix "aec".
 No word has both prefix and suffix "aav".
 No word has both prefix and suffix "aab".
Explanation 2:
 1 word "cazqzqzac" has both prefix and suffix "caz".
 No word has both prefix and suffix "cad"."""


class Node:
    def __init__(self):
        self.kids = [None]*26
        self.fre = 0
        self.end = False

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
	def __init__(self):
        self.trie = Node()
        
    def parse(self, head):
        if not head: return 
        for i in range(len(head.kids)):
            if  head.kids[i]:
                print(chr(i+ord('a')))
            self.parse(head.kids[i])
	    
	def create(self, A):
        for word in A:
            cur = self.trie
            n = len(word)
            for i in range(n):
                c = word[i]
                ind = ord(c)-ord('a')
                if not cur.kids[ind]:
                    cur.kids[ind] = Node()
                    cur.kids[ind].fre += 1
                else:
                    cur.kids[ind].fre += 1
                if i == n-1:
                    cur.kids[ind].end = True
                cur = cur.kids[ind]
                
    def solve(self, A, B):
        if not B: return B
        m = len(B[0])
        arr = []
        for i in A:
            if len(i) >= m and i[:m] == i[::-1][:m][::-1]:
                arr.append(i)
                
        self.create(arr)
        ans = []
        for word in B:
            cur = self.trie
            for i in range(m):
                c = word[i]
                ind = ord(c)-ord('a')
                if i == m-1:
                    if cur.kids[ind]:
                        ans.append(cur.kids[ind].fre)
                    else:
                        ans.append(0)
                        
                else:
                    if not cur.kids[ind]:
                        ans.append(0)
                        break
                    else:
                        cur = cur.kids[ind]
                        
        return ans
