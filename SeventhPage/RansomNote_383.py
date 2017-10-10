class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            index=magazine.find(i)
            if index==-1:
                return False
            if index+1<len(magazine):
                magazine=magazine[:index]+magazine[index+1:]
            else:
                magazine=magazine[:index]
        return True

s=Solution()
print(s.canConstruct("aa","ab"))

