class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        res=0
        tempmax=prices[0]
        tempmin=prices[0]
        preprice=prices[0]
        for price in prices[1:]:
            if preprice<price:
                tempmax=price
            else:
                res+=(tempmax-tempmin)
                tempmin=tempmax=price
            preprice =price
        return res+tempmax-tempmin

s=Solution()
#print(s.maxProfit())
print(s.maxProfit([1,2]))
print(s.maxProfit([2,4,1]))
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))