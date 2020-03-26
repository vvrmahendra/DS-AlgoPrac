"""First non-repeating character in a stream of characters
Given a string A denoting a stream of lowercase alphabets. You have to make new string B. B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. if no non-repeating character is found then append '#' at the end of B. 
Input Format
The only argument given is string A.
Output Format
Return a string B after processing the stream of lowercase alphabets A.
Constraints
1 <= length of the string <= 100000
For Example
Input 1:
    A = "abadbc"
Output 1:
    "aabbdd"

    Explanation:
    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "aba"    -   first non repeating character 'b'
    "abad"   -   first non repeating character 'b'
    "abadb"  -   first non repeating character 'd'
    "abadbc" -   first non repeating character 'd'

Input 2:
    A = "abcabc"
Output 2:
    "aaabc#"

    Explanation
    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "abc"    -   first non repeating character 'a'
    "abca"   -   first non repeating character 'b'
    "abcab"  -   first non repeating character 'c'
    "abcabc" -   no non repeating character so '#'
"""


def solve(A):
    from collections import deque
    Q = deque()
    dict_ = {}
    n = len(A)
    ans = ["#"]*n
    for i in range(n):
        if not Q:
            if A[i] in dict_:
                ans[i] = "#"
                dict_[A[i]] += 1
            else:
                ans[i] = A[i]
                dict_[A[i]] = 1
                Q.append(A[i])
            
            
            
        else:
            if A[i] != Q[0]:
                ans[i] = Q[0]
                if A[i] in dict_:
                    dict_[A[i]] += 1
                else:
                    dict_[A[i]] = 1
                    Q.append(A[i])
                    
            else:
                Q.popleft()
                while Q and dict_[Q[0]] > 1:
                    Q.popleft()
                
                if not Q:
                    ans[i] = "#"
                    dict_[A[i]] += 1
                else:
                    ans[i] = Q[0]
                    dict_[A[i]] += 1

                    
    return "".join(ans)