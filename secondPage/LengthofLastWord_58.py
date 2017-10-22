class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        isFirst=True
        index=len(s)-1
        # for index in range(len(s)-1,-1,-1):
        while index>=0:
            if s[index]==' ':
                if not isFirst:
                    break
                index-=1
            else:
                isFirst=False
                count+=1
                index-=1
        return count

s=Solution()
res=s.lengthOfLastWord("a ")
print(res)