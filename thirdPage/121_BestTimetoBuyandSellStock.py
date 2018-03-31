class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        stack=[]
        stack.append(prices[0])
        i=0
        res=0
        i+=1
        while len(stack)!=0 and i<len(prices):
            if  stack[-1]<prices[i]:
                stack.append(prices[i])
            else:
                res=max(res,stack[-1]-stack[0])
                while len(stack)!=0 and stack[-1]>prices[i]:
                    stack.pop()
                stack.append(prices[i])
            i+=1
        if len(stack)!=0:
            res=max(res,stack[-1]-stack[0])
        return res
s=Solution()
print(s.maxProfit([2,4,1]))
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))