class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        res=""
        #return "" if num == 0 else self.convertToTitle((num - 1) // 26) + chr((num - 1) % 26 + ord('A'))
        while num!=0:
            num-=1
            res+=chr((num)%26+ord('A'))
            num//=26
        result=""
        for item in reversed(res):
            result+=item
        return result
s=Solution()
print(s.convertToTitle(28))

#% 进制数  是保留后面的数
#// 进制数 是取前面的数
