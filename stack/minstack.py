"""Implementing min stack by using constant extra space.. though it works for only positive integers."""


class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.S = []
        self.min_ = float("inf")
    def push(self, x):
        if self.S:
            if self.min_ > x:
                self.S.append(x-self.min_)
                self.min_ = x
            else:
                self.S.append(x)
                
        else:
            self.S.append(x)
            self.min_ = x

    # @return nothing
    def pop(self):
        if self.S:
            temp = self.S.pop()
            if temp < 0:
                self.min_ = self.min_-temp

        if not self.S:
            self.min_ = float("inf")

    # @return an integer
    def top(self):
        if self.S:
            temp = self.S[-1]
            if temp < 0:
                return self.min_
            else:
                return temp
        else:
            return -1

    # @return an integer
    def getMin(self):
        if self.S:
            return self.min_
        else:
            return -1
          