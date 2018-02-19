class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        res=""
        sign=""
        if num<0:
            sign="-"
            num=abs(num)
        while num:
            res=str(num%7)+res
            num//=7
        return sign+res


s=Solution()
print(s.convertToBase7(-10))