class Solution(object):
    def isScramble(self, s1, s2):
        if s1==s2:
            return True
        length=len(s1)
        count=[0]*26
        for i in range(length):
            count[ord(s1[i])-ord('a')]+=1
            count[ord(s2[i])-ord('a')]-=1
        for i in range(26):
            if count[i]!=0:
                return False

        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:length],s2[i:length]):
                return True
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False

s=Solution()
print(s.isScramble("abb","bba"))