class Solution:

    def delNotCharacter(self,s):
        target=[' ']
        for i in range(26):
            target.append(chr(97+i))
        res=""
        for ch in s:
            if ch in target:
                res+=ch
        return res



    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph=paragraph.lower()
        words=self.delNotCharacter(paragraph).split()
        m={}
        for word in words:
            if word not in banned:
                if word not in m:
                    m[word]=1
                else:
                    m[word]+=1
        maximum=0
        res=""
        for key,value in m.items():
            if value>maximum:
                maximum=value
                res=key
        return res


s=Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
print(s.mostCommonWord("Bob!",["hit"]))