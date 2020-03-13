"""Window String
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N. Example :
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC""""



def minWindow(A, B):
    from collections import defaultdict
    
    ans, n, len_ = A, len(A), len(B)
    map_A, map_B = defaultdict(int), defaultdict(int)
    
    for i in B:
        map_B[i] += 1
        
    i, j, ans_po = 0, 0, 0
    while j < n:
        temp = A[j]
        temp_i = A[i]
        while map_A[temp_i] > map_B[temp_i]:
            map_A[temp_i] -= 1
            i += 1
            temp_i = A[i]
        
        if ans_po >= len_:
            if len(A[i:j]) < len(ans):
                ans = A[i:j]

        
        if map_A[temp] < map_B[temp] :
            ans_po += 1
        map_A[temp] += 1
        
        j += 1
        
    temp_i = A[i]    
    while  map_A[temp_i] > map_B[temp_i]:
        map_A[temp_i] -= 1
        i += 1
        if i < n:
            temp_i =A[i]
            
        else:
            break
        
    
    if len(ans) > len(A[i:j]):
        ans = A[i:j]

    if ans_po < len_:
        return ""
        
    return ans