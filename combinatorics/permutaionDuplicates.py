def permutationWithDuplicates(A):
    if not A: return []
    ans = []
    def helper(A, l, r):
        if l == r:
            ans.append([i for i in A])
            return
        
        for i in range(l,r+1):
            if A[i] not in A[l:i]: #Swaping with first unique value
                A[i],A[l] = A[l],A[i]
                helper(A, l+1, r)
                A[i],A[l] = A[l],A[i]
            
        return
    
    helper(A,0,len(A)-1)
    return ans
    
permutationWithDuplicates([1,1,3])
        