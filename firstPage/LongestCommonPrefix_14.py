class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        res=strs[0]
        i=0
        for str in strs[1:]:
            for i,ch in enumerate(res):
                if i<len(str) and ch!=str[i]:
                    res = res[:i]
                    break
                if i>=len(str):
                    res = res[:i]
                    break
        return res

s=Solution()
res=s.longestCommonPrefix(["aa","a"])
print(res)