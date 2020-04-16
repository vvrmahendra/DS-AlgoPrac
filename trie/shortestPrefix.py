"""Shortest Unique Prefix
Find shortest unique prefix to represent each word in the list. Example:
Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov"""



class Node:
    def __init__(self):
        self.kids = [None]*26
        self.fre = 0
        self.end = False

class Solution:
	# @param A : list of strings
	# @return a list of strings
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
                
    def prefix(self, A):
        self.create(A)
        # self.parse( self.trie)
        ans = []
        for word in A:
            cur = self.trie
            n = len(word)
            temp = []
            for i in range(n):
                c = word[i]
                # print(c)
                ind = ord(c)-ord('a')
                temp.append(c)
                if i == n-1:
                    if cur.kids[ind].fre > 1:
                        temp = []
                if cur.kids[ind].fre == 1:
                    break
                
                cur = cur.kids[ind]
                
            ans.append("".join(temp))
            
        return ans
        	    