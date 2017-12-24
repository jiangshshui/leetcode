class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #for char in haystack:
        for index in range(len(haystack)-len(needle)+1):
            if haystack[index:index+len(needle)]==needle:
                return index
        return -1

s=Solution()
print(s.strStr("mississippi","sippia"))

