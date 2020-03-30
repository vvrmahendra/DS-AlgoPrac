"""Implementing min stack by using constant extra space.. It works for all real numbers unlike minstackV1 appraock."""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.S = deque()
        self.M = None

    def push(self, x: int) -> None:
        if not self.S:
            self.S.append(x)
            self.M = x
            return
        else:
            if 2*x-self.M < x:
                self.S.append(2*x-self.M)
                self.M = x
            else:
                self.S.append(x)
                
            return

    def pop(self) -> None:
        if self.S:
            temp = self.S.pop()
            if temp < self.M:
                self.M = 2*self.M-temp
                return self.M
            if not S:
                self.M = None
                return temp

    def top(self) -> int:
        if self.S:
            temp = self.S[-1]
            if temp < self.M:
                return self.M
            else:
                return temp
        

    def getMin(self) -> int:
        if self.S:
            return self.M

