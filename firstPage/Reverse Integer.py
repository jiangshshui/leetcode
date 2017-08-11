class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        isneg=True if x<0 else False
        x=abs(x)
        while x != 0:
            a=x%10
            res=res*10+a
            x=x//10
        if res>pow(2,31)-1:
            res=0
        return -res if isneg else res

s=Solution()
print(s.reverse(123456745646464647657657667))

