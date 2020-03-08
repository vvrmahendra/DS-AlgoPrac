"""Max Continuous Series of 1s
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed. Find the position of zeros which when flipped will produce maximum continuous series of 1s. For this problem, return the indices of maximum continuous series of 1s in order. Example:
Input : 
Array = {1 1 0 1 1 0 0 1 1 1 } 
M = 1

Output : 
[0, 1, 2, 3, 4] """


def maxone(A, B):
        n = len(A)
        i = -1
        j = 0
        zeroes = 0
        ans = [0, 0]
        while j < n:
            if A[j] == 0:
                zeroes += 1
            
            if zeroes == B+1:
                # print(i,j)
                # print(j-i-1, ans[1]-ans[0]-1)
                if j-i-1 > ans[1]-ans[0]-1:
                    ans = [i,j]
                i = i+1
                while i < n:
                    if A[i] != 0:
                        i += 1
                    else:
                        break
                zeroes -= 1
            j += 1
            
        # print("--------end--------")
        # print(zeroes, i,j)
        if j-i-1 > ans[1]-ans[0]-1:
            ans = [i,j]
            
        # for i in range(ans[0]+1,ans[1])
            
        return [i for i in range(ans[0]+1,ans[1])]
                        