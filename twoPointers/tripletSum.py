
"""Triplets with Sum between given range
Given an array of real numbers greater than zero in form of strings. Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 . Return 1 for true or 0 for false. 
Example: Given [0.6, 0.7, 0.8, 1.2, 0.4] , You should return 1 as 0.6+0.7+0.4=1.7 1<1.7<2 Hence, the output is 1.
O(n) solution is expected. Note: You can assume the numbers in strings don't overflow the primitive data type and there are no leading zeroes in numbers. Extra memory usage is allowed.

"""

"""
Refer this link
https://stackoverflow.com/questions/19557505/triplet-whose-sum-in-range-1-2

"""



def inscribe(A, target, number_till, minOrmax):
    if minOrmax == 1:
        if len(A) == 1:
            if A[0] != None:
                A[0] = max(A[0],target)
            else:
                A[0] = target
                
        elif len(A) == 2:
            if number_till == 0:
                A[0] = target
            elif number_till == 1:
                if A[0] <= target:
                    A[1] = A[0]
                    A[0] = target
                else:
                    A[1] = target
            
            else:
                if A[0] <= target:
                    A[1] = A[0]
                    A[0] = target
                elif target >= A[1]:
                    A[1] = target
        elif len(A) == 3:
            if number_till == 0:
                A[0] = target
            elif number_till == 1:
                if target >= A[0]:
                    A[1] = A[0]
                    A[0] = target
                else:
                    A[1] = target
                    
            elif number_till == 2:
                if target >= A[0]:
                    A[2] = A[1]
                    A[1] = A[0]
                    A[0] = target
                elif target >= A[1]:
                    A[2] = A[1]
                    A[1] = target
                else:
                    A[2] = target
            
            else:
                if target >= A[0]:
                    A[2] = A[1]
                    A[1] = A[0]
                    A[0] = target
                elif target >= A[1]:
                    A[2] = A[1]
                    A[1] = target
                elif target >= A[2]:
                    A[2] = target
                    
    elif minOrmax == 0:
        if len(A) == 1:
            if A[0] != None:
                A[0] = min(A[0],target)
            else:
                A[0] = target
        elif len(A) == 2:
            if number_till == 0:
                A[0] = target
            elif number_till == 1:
                if target <= A[0]:
                    A[1] = A[0]
                    A[0] = target
                    
                else:
                    A[1] = target
            else:
                if target <= A[0]:
                    A[1] = A[0]
                    A[0] = target
                    
                elif target <= A[1]:
                    A[1] = target
    return
                    
            
def tripletSUm(Arr):
    high_A = [None, None, None]
    high_A_ = [None, None]
    high_B = [None]
    
    low_A = [None, None]
    low_B = [None, None]
    low_C = [None]
    low_B_ = [None, None]
    low_A_ = [None]
    
    
    A = (0,2/3)
    B = (2/3,1)
    C = (1,2)
    A_ = (0,1/2)
    B_ = (1/2, 2/3)
    dict_ = {A:0, B:0, C:0, A_:0, B_:0}
    for ele in Arr:
        i = float(ele)
        if i < 2/3:
            inscribe(high_A, i, dict_[A],1)
            inscribe(low_A, i, dict_[A],0)
            dict_[A] += 1
        elif i <= 1:
            inscribe(low_B, i, dict_[B],0)
            inscribe(high_B, i, dict_[B],1)
            dict_[B] += 1
        else:
            inscribe(low_C, i, dict_[C],0)
            dict_[C] += 1
            
        if i < 1/2:
            inscribe(high_A_, i, dict_[A_],1)
            inscribe(low_A_, i, dict_[A_],0)
            dict_[A_] += 1
        elif i < 2/3:
            inscribe(low_B_, i, dict_[B_],0)
            dict_[B_] += 1
    for ele in dict_:
        print(ele, dict_[ele])        
    print ("high_A",high_A)
    print ("high_A_",high_A_)
    print ("high_B",high_B)
    print ("low_A",low_A)
    print("low_B",low_B)
    print("low_C",low_C)
    print("low_B_",low_B_)
    print("low_A_",low_A_)
    
    if dict_[A] >= 3:
        if high_A[0]+high_A[1]+high_A[2] > 1:
            return 1
    if dict_[A] >=2 and dict_[C] >= 1:
        if low_A[0]+low_A[1]+low_C[0] < 2:
            return 1
    if dict_[B] >= 2 and dict_[A] >= 1:
        if low_B[0]+low_B[1]+low_A[0] < 2:
            return 1
    if dict_[A] >= 1 and dict_[B] >= 1 and dict_[C] >= 1:
        if low_A[0]+low_B[0]+low_C[0] < 2:
            return 1
    
    if dict_[A] >= 2 and dict_[B] >= 1:
        if dict_[A_] >= 2:
            if high_A_[0]+high_A_[1]+high_B[0] > 1:
                return 1
        if dict_[A_] >= 1 and dict_[B_] >= 1:
            if low_A_[0]+low_B_[0]+low_B[0] < 2:
                return 1
        if dict_[B_] >= 2:
            if low_B_[0]+low_B_[1]+low_B[0] < 2:
                return 1
            
    return 0



if __name__ == "__main__"
    A = [ "0.297657", "0.420048", "0.053365", "0.437979", "0.375614", "0.264731", "0.060393", "0.197118", "0.203301", "0.128168" ]
    tripletSUm(A)


            