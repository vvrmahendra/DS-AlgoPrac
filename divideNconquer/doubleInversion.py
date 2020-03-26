class doubleInversion:
    def __init__(self):
        self.ans = None
    def merge(self, A,B):
        ans = 0
        out = []
        n, m = len(A), len(B)
        i, j, k = 0, 0, 0
        while i < n and j < m:
            if B[j] < A[i]:
                while k < n and A[k] < 2*B[j]:
                    k += 1
                
                ans += n-k
                out.append(B[j])
                j += 1
                
            else:
                out.append(A[i])
                i += 1
                
        while i < n:
            out.append(A[i])
            i += 1
            
        while j < m:
            out.append(B[j])
            j += 1
                
        return (out, ans)
    
    def doubleinversion(self,A):
        if len(A) <= 1:
            return A
        n = len(A)
        mid = n//2
        left = A[:mid]
        right = A[mid:]
        self.ans = 0
        first = self.doubleinversion(left)
        second = self.doubleinversion(right)
        inte = self.merge(first, second)
        self.ans = self.ans+inte[1]
        return inte[0]
    
    
A = [1,3,4,7,1,2,3,9]
temp = doubleInversion()
temp.doubleinversion(A)
temp.ans