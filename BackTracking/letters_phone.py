# https://www.interviewbit.com/problems/letter-phone/
ans = []
def phone_letter(A,path,hash_map):
    if len(A) == 0:
        global ans
        ans.append(path)
        return
    
    for i in hash_map[int(A[0])]:
        path = path+i
        phone_letter(A[1:],path,hash_map)
        path = path[:-1]
        
    return

hash_map = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

phone_letter("2","",hash_map)