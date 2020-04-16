class segmentTree:
    def __init__(self, A):
        self.n = len(A)
        self.A = A
        self.tree = [0]*(4*self.n)
        self.createTree(0, self.n-1, 0)
        #self.rangeSum = partial(self.rangeSum, te = self.n-1)
    
    def createTree(self, s, e, index):
        if s == e: 
            self.tree[index] = self.A[s]
            return
        
        mid = (s+e)//2
        self.createTree(s,mid, 2*index+1)
        self.createTree(mid+1, e, 2*index+2)
        self.tree[index] = self.tree[2*index+1]+self.tree[2*index+2]
        return
    
    def rangeSum(self, s, e, ts=0, te=None, ind = 0):
        if te == None: te = self.n-1
        if s <= ts and e >= te:
            return self.tree[ind]
        elif s > te or e < ts:
            return 0
        
        mid = (ts+te)//2
        if qe <= mid:
            return self.rangeSum(s,mid,ts,mid,2*ind+1)
        elif qs > mid:
            return self.rangeSum(mid+1,e,mid+1,te,2*ind+2)

        first = self.rangeSum(s,mid,ts,mid,2*ind+1)
        second = self.rangeSum(mid+1,e,mid+1,te,2*ind+2)
        return first+second
            
        
    def updateAt(self, ind, val, s = 0, e = None, sind = 0):
        if e == None: e = self.n-1
        if s==e==ind:
            self.tree[sind] += val-self.A[ind]
            return
        
        if s <= ind <= e:
            self.tree[sind] += val-self.A[ind]
            mid = (s+e)//2
            if ind <= mid:
                self.updateAt(ind, val,s,mid,sind*2+1 )
            else:
                self.updateAt(ind,val, mid+1, e, sind*2+2)
        return
    
