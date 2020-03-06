"""B Closest Points to Origin
Problem Description
We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0). Here, the distance between two points on a plane is the Euclidean distance. You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.) NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt( (x1-x2)^2 + (y1-y2)^2 ). 


Problem Constraints
1 <= B <= length of the list A <= 100000
-100000 <= A[i][0] <= 100000
-100000 <= A[i][1] <= 100000


Input Format
The argument given is list A and an integer B.


Output Format
Return the B closest points to the origin (0, 0) in any order.


Example Input
A = [ [1, 3],
      [-2, 2]  ]
B = 1


Example Output
[ [-2, 2] ]
"""






def solve(self, A, B):
    def customSort(ele):
        i = ele[0]
        j = ele[1]
        return (i**2+j**2)
    
    A.sort(key = customSort)
    return A[:B]