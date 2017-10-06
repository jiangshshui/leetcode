class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(" ")
        res=[]
        for word in s:
            newword=word[::-1]
            res.append(newword)
        return " ".join(res)

s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))