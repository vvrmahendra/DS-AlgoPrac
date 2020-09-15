"""
You are given two strings A & B. You need to check if B is a sub-sequence of A or not.
Ex: A: 'abcdef' B:'acdf -> True
A:'abcdef' B:'acbe' -> False
"""

def nextAlphabet(s):
    if not s: return []
    n = len(s)
    ans = [[None]*26 for i in range(n)]
    print(s)
    for i in range(n-2,-1,-1):
        ans[i] = ans[i+1][:]
        ordN = ord(s[i+1])-ord('a')
        print(ordN, s[i])
        ans[i][ordN] = i+1
    
    return ans


def isSubSequence(master, student):
    dp = nextAlphabet(master)
    if student[0] == master[0]:
        student = student[1:]
    print(dp)
        
    cur = 0
    for i in student:
        ordN = ord(i)-ord('a')
        if not dp[cur][ordN]: return False
        cur = dp[cur][ordN]
        
    return True
