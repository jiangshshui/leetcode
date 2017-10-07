class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0:
            s,t=t,s
        res=ord(s[0])
        for ch in s[1:]+t:
            res^=ord(ch)
        return chr(res)