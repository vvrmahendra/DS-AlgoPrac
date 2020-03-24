"""Remove Duplicate Letters
Given a string A consisting of lowercase English alphabets. 
Find and return lexicographically smallest string B after removing duplicate letters from A so that every letter appears once and only once. 
Input Format
The only argument given is string A.
Output Format
Return lexicographically smallest string B after removing duplicate letters from A.
Constraints
1 <= length of the string <= 200000
A consists of lowercase English alphabets only. 
For Example
Input 1:
    A = "cbacdcbc"
Output 1:
    B = "acdb"

Input 2:
    A = "bcabc"
Output 2:
    B = "abc""""

def solve(A):
    from collections import deque
    s = deque()
    dict_ = {}
    for i in A:
        if i in dict_:
            dict_[i][0] += 1
        else:
            dict_[i] = [1,False]
    for i in A:
        if not s:
            s.append(i)
            dict_[i][0] -= 1
            dict_[i][1] = True
        else:
            if dict_[i][1]:
                dict_[i] = [dict_[i][0]-1, True]
                continue
            while s and i <= s[-1]:
                if dict_[s[-1]][0] > 0:
                    temp = s.pop()
                    dict_[temp] = [dict_[temp][0], False]
                else:
                    break
            s.append(i)                    
            dict_[i] = [dict_[i][0]-1, True]
            
    ans = ""
    while s:
        ans = ans+s.pop()
        
    return ans[::-1]