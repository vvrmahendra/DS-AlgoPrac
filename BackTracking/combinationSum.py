"""Problem Description
Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.  Each number in A may only be used once in the combination. Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
 Warning: DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS. Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.    



 Example Input
Input 1:
A = [10, 1, 2, 7, 6, 1, 5]
B = 8
    


Example Output
Output 1:
[ [1 1 6 ]
  [1 2 5 ]
  [1 7 ] 
  [2 6 ] ]"""





ans = []
def combinationSum(A, target, sum_, path):
    if sum_ == target:
        global ans
        temp = []
        for i in path:
            temp.append(i)
        if temp not in ans:
            ans.append(temp)
        return
    
    if sum_ > target:
        return
    
    if len(A) <= 0:
        return
    
    sum_ = sum_+A[0]
    path.append(A[0])
    combinationSum(A[1:],target, sum_, path)
    path.pop()
    sum_ = sum_ - A[0]
    
    combinationSum(A[1:],target, sum_, path)
    return


if __name__ == "__main__":
    A = [10, 1, 2, 7, 6, 1, 5]
    A.sort()
    B = 8
    combinationSum(A,B,0,[])
    print(ans)
    
    