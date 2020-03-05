"""The set [1,2,3,…,n] contains a total of n! unique permutations. By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3 ) :
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence. For example, given n = 3, k = 4, ans = "231""""



"""
Awesome problem. Used "Factorial Number System" like "Decimal Number Systam"
refer this link https://qr.ae/pIC2ER

"""

def getPermutation(A, B):
    def kthPerm(A,k):
        reverse_fact = [0]*len(A)
        temp = k
        i = 1
        j = len(A)-1
        while temp > 0:
            rem = temp%i
            reverse_fact[j] = rem
            j -= 1
            temp = temp//i
            i += 1
        
        ans = []
        for i in range(len(reverse_fact)):
            index_A = reverse_fact[i]
            ans.append(A[index_A])
            A = A[:index_A]+A[index_A+1:]
            
        return ans

        
    Arr = [i+1 for i in range(A)]
    ans = kthPerm(Arr,B-1)
    temp = ''
    for i in ans:
        temp += str(i)
    return temp
        