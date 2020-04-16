class minHeap:
    def __init__(self, A):
        self.A = A
        
    def heapify(self, i):
        n = len(self.A)
        while True:
            small = i
            left = 2*small+1
            right = 2*small+2
            if left < n and self.A[small] > self.A[left]:
                small = left
            if right < n and self.A[small] > self.A[right]:
                small = right
                
            if small == i:
                break
            else:
                self.A[i], self.A[small] = self.A[small], self.A[i]
                i = small
                
    def insert(self, val):
        print(len(self.A))
        self.A.append(val)
        print(len(self.A))
        i = len(self.A)-1
        while True:
            print('here')
            par = (i-1)//2
            print(par, i)
            if self.A[par] > self.A[i] and par >= 0:
                self.A[par], self.A[i] = self.A[i], self.A[par]
                i = par
            else:
                break
            
    def deleteHead(self):
        self.A[0] = self.A[-1]
        self.A.pop()
        self.heapify(0)
                
                
            
    def buildHeap(self):
        n = len(self.A)
        leaf = (n+1)//2
        lastNL = n-leaf-1
        for i in range(lastNL, -1, -1):
            self.heapify(i)
            
            
if __name__ == "__main__":
    a = minHeap([3,2,1,5,6,7])
    a.buildHeap()
    print(a.A)
    a.insert(-1)
    print(a.A)
    a.deleteHead()
    print(a.A)