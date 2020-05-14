""""Make Circle
Problem Description
Given an array of strings A of size N, find if the given strings can be chained to form a circle. A string X can be put before another string Y in circle if the last character of X is same as first character of Y. NOTE: All strings consist of lower case characters.    


Problem Constraints
1 <= N <= 105 Sum of length of all strings <= 106    


Input Format
First and only argument is a string array A of size N.


Output Format
Return an integer 1 if it is possible to chain the strings to form a circle else return 0.


Example Input
Input 1:
 A = ["aab", "bac", "aaa", "cda"]
Input 2:
 A = ["abc", "cbc"]
   


Example Output
Output 1:
 1
Output 2:
 0
   


Example Explanation
Explanation 1:
 We can chain the strings aab -> bac -> cda -> aaa -> aab. So this forms a circle. So, output will be 1. 
Explanation 2:
 There is no way to chain the given strings such that they forms a circle.""""


from collections import defaultdict, deque
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        rays = defaultdict(list)
        inword = defaultdict(int)
        outword = defaultdict(int)
        let = set()
        for word in A:
            rays[word[0]].append(word[-1])
            inword[word[-1]] += 1
            outword[word[0]] += 1
            let.add(word[0])
            let.add(word[-1])
            
        for n in let:
            if inword[n] != outword[n]:
                return 0
                
        s = deque()
        s.append(A[0][0])
        visited = set()
        while s:
            cur = s.pop()
            visited.add(cur)
            for nei in rays[cur]:
                if nei not in visited:
                    s.append(nei)
                    visited.add(nei)
                    
        return int(let == visited)
            
            