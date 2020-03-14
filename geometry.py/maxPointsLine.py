"""Maximum Points on the same line
Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2-D plane. A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane. Find and return the maximum number of points which lie on the same line. 
Input Format
The arguments given are integer arrays A and B.
Output Format
Return the maximum number of points which lie on the same line.
Constraints
1 <= (length of the array A = length of array B) <= 1000
-10^5 <= A[i], B[i] <= 10^5 
For Example
Input 1:
    A = [-1, 0, 1, 2, 3, 3]
    B = [1, 0, 1, 2, 3, 4]
Output 1:
    4
    The maximum number of point which lie on same line are 4, those points are {0, 0}, {1, 1}, {2, 2}, {3, 3}

Input 2:
    A = [3, 1, 4, 5, 7, -9, -8, 6]
    B = [4, -8, -3, -2, -1, 5, 7, -4]
Output 2:
    2"""


from collections import defaultdict
def solve(self, A, B):
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    
    
    n, ans = len(A), 0

    points = [(A[i],B[i]) for i in range(n)]
    points_dict = defaultdict(int)
    for i in points:
        points_dict[i] += 1
        
    for i in range(n-1):
        dict_ = {}
        for j in range(i+1,n):
            if (A[i],B[i]) == (A[j],B[j]):
                continue
            else:
                num_m = B[j]-B[i]
                den_m = A[j]-A[i]
                if den_m != 0 and num_m != 0:
                    flag = 1
                    if num_m < 0:
                        flag = flag*(-1)
                        num_m = num_m*(-1)
                    if den_m < 0:
                        flag = flag*(-1)
                        den_m = den_m*(-1)
                    gcd_m = gcd(num_m,den_m)
                    num_m = (num_m//gcd_m)*flag
                    den_m = den_m//gcd_m
                    
                elif den_m == 0:
                    num_m = float('inf')
                    den_m = 0
                elif num_m == 0:
                    num_m = 0
                    den_m = float('inf')

                temp = (num_m, den_m)
                if temp in dict_:
                    dict_[temp].add(i)
                    dict_[temp].add(j)
                else:
                    dict_[temp] = {i,j}

        repe = points_dict[(A[i],B[i])]-1
        for ele in dict_:
            ans = max(ans, len(dict_[ele])+repe)
            
        
    return ans