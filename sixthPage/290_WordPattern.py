class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m={}
        str=str.split()
        if len(str)!=len(pattern):
            return False
        for index,ch in enumerate(pattern):
            if ch not in m:
                if index<len(str):
                    if str[index] not in m.values():
                        m[ch]=str[index]
                    else:
                        return False
                else:
                    return False
            else:
                if str[index]!=m[ch]:
                    return False
        return True

s=Solution()
#print(s.wordPattern("abba","dog cat cat dog dog"))
#print(s.wordPattern("jquery","jquery"))
#print(s.wordPattern("abba","dog dog dog dog"))
print(s.wordPattern("aaa","aa aa aa aa"))