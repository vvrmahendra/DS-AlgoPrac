"""MODIFIED SEARCH
Problem Description
Given two arrays of strings A of size N and B of size M. Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using exactly one modification in B[i], Else C[i] = '0'. NOTE: modification is defined as converting a character into another character.     


Problem Constraints
1 <= N, M <= 1000 1 <= Sum of length of all strings in A <=1000 1 <= Sum of length of all strings in B <=1000 strings contains only lowercase alphabets


Input Format
First argument is the string arrray A. Second argument is the string array B.  


Output Format
Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using one modification in B[i], Else C[i] = '0'.


Example Input
Input 1:
 A = [data, circle, cricket]
 B = [date, circel, crikket, data, circl]
Input 2:
 A = [hello, world]
 B = [hella, pello, pella]
    


Example Output
Output 1:
 "10100"
Output 2:
 "110"
    


Example Explanation
Explanation 1:
 1. date = dat*(can be found in A)
 2. circel =(cannot be found in A using only one modification)
 3. crikket = cri*ket(can be found in A)
 4. data = (cannot be found in A using only one modification)
 5. circl = (cannot be found in A using only one modification)
Explanation 2:
 Only pella cannot be found in A using only one modification.
"""


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, A, B):
        from collections import defaultdict
        words = defaultdict(int)
        ASet = set(A)
        for word in A:
            for i in range(len(word)):
                words[word[:i]+'*'+word[i+1:]] += 1
        
        ans = []
        for word in B:
            search = 0
            flag = True
            if word in ASet:
                search += 1
                
            for i in range(len(word)):
                if words[word[:i]+'*'+word[i+1:]] > search:
                    ans.append(1)
                    flag = False
                    break
                
            if flag: ans.append(0)
            
        return "".join([str(i) for i in ans])
        