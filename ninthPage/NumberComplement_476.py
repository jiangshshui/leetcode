class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans=0
        count=0
        while num:
            rightmost=num&1
            newValue=rightmost^1
            ans+=newValue*(2**count)
            count+=1
            num//=2
        return ans
s=Solution()
print(s.findComplement(1))

