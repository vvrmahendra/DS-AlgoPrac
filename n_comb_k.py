# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:31:23 2020

@author: mahi
"""

ans = []
def nck(A,len_,path):
    if len_ == 0:
        temp = []
        for i in path:
            temp.append(i)
            
        global ans
        ans.append(temp)
        return
    if len(A) == 0:
        return
    
    #for i in range(len(A)):
    path.append(A[0])
    len_ -= 1
    nck(A[1:],len_,path)
    len_ += 1
    path.pop()
    nck(A[1:],len_,path)
        
    return


nck([1,2,4],2,[])