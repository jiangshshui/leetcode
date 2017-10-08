class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=s.split()
        return " ".join(reversed(ls))

s=Solution()
print(s.reverseWords("I am a chinese!"))
