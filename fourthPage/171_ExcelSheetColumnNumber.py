class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for index,ch in enumerate(s):
            res+=(ord(ch)-ord('A')+1)*26**(len(s)-1-index)
        return res


s=Solution()
print(s.titleToNumber("AB"))