"""Array 3 Pointers
You are given 3 arrays A, B and C. All 3 of the arrays are sorted. Find i, j, k such that : max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized. Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) **abs(x) is absolute value of x and is implemented in the following manner : **
      if (x < 0) return -x;
      else return x;
Example :
Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C. """

"""
Trick here is given expression can reduce to max(A[i],B[j],C[k])-min(A[i],B[j],C[k])
"""


def minimize(A, B, C):
    def helper(a,b,c):
        min_ = None
        max_ = None
        if a <= b and a <= c:
            min_ = 1
        elif b <= a and b <= c:
            min_ = 2
        else:
            min_ = 3
        if a >= b and a >= c:
            max_ = 1
        elif b >= a and b >= c:
            max_ = 2
        else:
            max_ = 3
        return (min_,max_)
    i = 0
    j = 0
    k = 0
    l = len(A)
    m = len(B)
    n = len(C)

    ans = float("inf")
    while i < l and j < m and k < n:
        min_ = min(A[i],B[j],C[k])
        max_ = max(A[i],B[j],C[k])
        temp = max_-min_
        ans = min(temp,ans)
        min_in,max_in = helper(A[i],B[j],C[k])
        if min_in == 1:
            i += 1
        elif min_in == 2:
            j += 1
        else:
            k += 1

    
    return ans
        