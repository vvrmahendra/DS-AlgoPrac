class SegementTree:
    def __init__(self, A):
        self.n = len(A)
        self.A = A
        self.ST = [0]*(self.n*4)
        self.HST = [0]*(self.n*4)
        self.createHST(0,self.n-1,0)
        self.createST(0,self.n-1,0)
        
        
    def createHST(self, s,e, sind):
        if s == e:
            self.HST[sind] = self.A[s]
            return
            
        mid = (s+e)//2
        self.createHST(s,mid,2*sind+1)
        self.createHST(mid+1,e,2*sind+2)
        self.HST[sind] = self.HST[2*sind+1]+self.HST[2*sind+2]
        return
    
    def updateHST(self, s,e, sind, ind,val):
        if s == e == ind:
            self.HST[sind] = val
            return
            
        mid = (s+e)//2
        if ind <= mid:
            self.updateHST(s,mid,2*sind+1,ind,val)
        else:
            self.updateHST(mid+1,e,2*sind+2,ind,val)
        
        self.HST[sind] = self.HST[2*sind+1]+self.HST[2*sind+2]
    
    
    def createST(self, s, e, sind):
        if s == e:
            self.ST[sind] = self.A[s]
            return
        
        mid = (s+e)//2
        self.createST(s,mid,2*sind+1)
        self.createST(mid+1, e, 2*sind+2)
        self.ST[sind] = self.ST[2*sind+1]+self.ST[2*sind+2]+(mid-s+1)*self.HST[2*sind+2]
        
    def updateST(self, s,e, sind, ind,val):
        if s ==e== ind:
            self.ST[sind] = val
            return
            
        mid = (s+e)//2
        if ind <= mid:
            self.updateST(s,mid,2*sind+1,ind,val)
        else:
            self.updateST(mid+1,e,2*sind+2,ind,val)
        
        self.ST[sind] = self.ST[2*sind+1]+self.ST[2*sind+2]+(mid-s+1)*self.HST[2*sind+2]
        
    
    def querySum(self,s,e,qs,qe,sind):
        if qs > e or qe < s:
            return [0, 0]
        
        if qs <=s and qe >= e:
            return [self.ST[sind], self.HST[sind]]
        
        mid = (s+e)//2
        if qe <= mid:
            return self.querySum(s,mid,qs,qe,2*sind+1)
        elif qs > mid:
            return self.querySum(mid+1, e, qs,qe, 2*sind+2)
        
        left = self.querySum(s,mid,qs,qe,2*sind+1)  
        right = self.querySum(mid+1,e,qs,qe,2*sind+2)
            
        
        
        return [left[0]+right[0]+(mid+1-qs)*right[1], left[1]+right[1]]


if __name__ == "__main__":
    t = int(input())
    for test in range(1,t+1):
        n,q = input().split()
        n,q = map(int,(n,q))
        A = input().split()
        A = list(map(int, A))
        for i in range(n):
            if i%2 == 1:A[i] = -1*A[i]
            
        ans = 0
        tree = SegementTree(A)
        for query in range(q):
            qt, f, s = input().split()
            f,s = map(int,(f,s))
            if qt == 'Q':
                f,s = f-1,s-1
                out = tree.querySum(0,n-1,f,s,0)[0]
                if f%2 == 1:
                    out = -1*out
                    
                ans += out
                # print(out)    
            elif qt == 'U':
                f,s = f-1, s
                
                if f%2 == 1:
                    s = -1*s
                tree.A[f] = s
                # print(tree.ST)
                tree.updateHST(0,n-1, 0, f,s)
                tree.updateST(0,n-1, 0, f,s)
                # print(tree.ST)
                
        print("Case #{}: {}".format(test, ans))



