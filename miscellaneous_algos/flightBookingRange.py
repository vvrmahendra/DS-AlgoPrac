#https://www.geeksforgeeks.org/constant-time-range-add-operation-array/

def solve(self, A, B):
    ans = [0]*A
    for item in B:
        i,j,value = item
        i,j = i-1,j-1
        ans[i] += value
        if j != A-1:
            ans[j+1] += -1*value
    
    pre_ans = [0]*A
    pre_ans[0] = ans[0]
    for i in range(1,A):
        pre_ans[i] = pre_ans[i-1]+ans[i]
        
    return pre_ans