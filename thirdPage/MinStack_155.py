import heapq
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store=[]
        self.topIndex=-1
        #self.minimum=float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        #last=self.top()
        if self.topIndex <0:
            curMin=float('inf')
        else:
            curMin=self.store[self.topIndex][1]
        if x<curMin:
            curMin=x
        self.topIndex+=1
        self.store.append((x,curMin))

        # if x<self.minimum:
        #     self.minimum=x


    def pop(self):
        """
        :rtype: void
        """
        del (self.store[self.topIndex])
        self.topIndex-=1


    def top(self):
        """
        :rtype: int
        """
        if self.topIndex<0:
            return None
        return self.store[self.topIndex][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.store[self.topIndex][1]


minStack = MinStack()
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
#minStack.push(0)
print(minStack.top())
print(minStack.top())
print(minStack.getMin())

